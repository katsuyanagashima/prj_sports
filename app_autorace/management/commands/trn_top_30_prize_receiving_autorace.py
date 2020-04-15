import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import time
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max
from app_autorace.models import *
from logging import getLogger
from pathlib import Path

#!/usr/bin/env
logger = getLogger(__name__)

# 監視対象ファイルのパターンマッチを指定する
# 選手取得賞金上位３０位レコード（mmddhhmmss00000003.dat）
scheduleID = 4
top30prizeData = "top30prizeData"
target_file_top30prize_record = '*00000003.dat'

# PatternMatchingEventHandler の継承クラスを作成
class FileChangeHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)
        self.watch_path = str()

        self.classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
        self.data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
        self.send_date	 = str()                    # ファイル名をキーとして送信日を記憶する
        self.Totaling_date	 = str()
        self.Ranking	 = str()
        self.Rider_code	 = int()
        self.Rider_full_name = str()
        self.Rider_shortened_3_name	 = str()
        self.Rider_shortened_4_name = str()
        self.LG_code	 = int()
        self.LG_name = str()
        self.Rider_class_code	 = int()
        self.By_period = str()
        self.Rider_birthplace	 = str()
        self.Rider_Age = str()
        self.Prize	 = str()

    # 正規表現で半角ブランク削除
    def chkBlank(self, top30prizeLineStr):
        if (not re.sub('\\s', '', top30prizeLineStr)):
            return False
        return True

    # datファイル設定する
    def setDatData(self, top30prizeLine):

        # 選手取得賞金上位３０位
        for s in range(self.top30prize):
            if s==0:
                if self.chkBlank(top30prizeLine[0:2]):
                    self.Ranking = top30prizeLine[0:2]
                if self.chkBlank(top30prizeLine[2:6]):
                    self.Rider_code	 = top30prizeLine[2:6]
                if self.chkBlank(top30prizeLine[6:22]):
                    self.Rider_full_name	 = top30prizeLine[6:22]
                if self.chkBlank(top30prizeLine[22:28]):
                    self.Rider_shortened_3_name	 = top30prizeLine[22:28]
                if self.chkBlank(top30prizeLine[28:36]):
                    self.Rider_shortened_4_name	 = top30prizeLine[28:36]
                if self.chkBlank(top30prizeLine[36:37]):
                    self.LG_code	 = top30prizeLine[36:37]
                if self.chkBlank(top30prizeLine[37:43]):
                    self.LG_name	 = top30prizeLine[37:43]
                if self.chkBlank(top30prizeLine[43:44]):
                    self.Rider_class_code	 = top30prizeLine[43:44]
                if self.chkBlank(top30prizeLine[44:46]):
                    self.By_period	 = top30prizeLine[44:46]
                if self.chkBlank(top30prizeLine[46:52]):
                    self.Rider_birthplace	 = top30prizeLine[46:52]
                if self.chkBlank(top30prizeLine[52:54]):
                    self.Rider_Age	 = top30prizeLine[52:54]
                if self.chkBlank(top30prizeLine[54:66]):
                    self.Prize	 = top30prizeLine[54:66]

    def update_Trn_Top_30_Prize(self, trn_Update):
        updateFields = list()
        if self.ranking:
            trn_Update.Ranking=self.ranking
            updateFields.append('Ranking')
        if self.rider_code:
            trn_Update.Rider_code=self.rider_code
            updateFields.append('Rider_code')
        if self.rider_full_name:
            trn_Update.Rider_full_name= self.rider_full_name
            updateFields.append('Rider_full_name')
        if self.rider_shortened_3_name:
            trn_Update.Rider_shortened_3_name= self.rider_shortened_3_name
            updateFields.append('Rider_shortened_3_name')
        if self.rider_shortened_4_name:
            trn_Update.Rider_shortened_4_name= self.rider_shortened_4_name
            updateFields.append('Rider_shortened_4_name')
        if self.lG_name:
            trn_Update.LG_name= self.lG_name
            updateFields.append('LG_name')
        if self.by_period:
            trn_Update.By_period= self.by_period
            updateFields.append('By_period')
        if self.rider_birthplace:
            trn_Update.Rider_birthplace= self.rider_birthplace
            updateFields.append('Rider_birthplace')
        if self.rider_Age:
            trn_Update.Rider_Age=self.rider_Age
            updateFields.append('Rider_Age')
        if self.prize:
            trn_Update.Prize=self.prize
            updateFields.append('Prize')

        #マスターに確認 エラー
        if self.lG_code:
            trn_Update.LG_code=self.lG_code
            updateFields.append('LG_code')
        if self.rider_class_code:
            trn_Update.Rider_class_code=self.rider_class_code
            updateFields.append('Rider_class_code')

        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)


    def insert_or_update_Trn_Top_30_Prize(self, name):
        try:
            file = open(name,'r')
            for line in file: # 1行しかない
                self.classification = line[0:1]
                self.data_type = line[1:2]
                self.send_date = line[2:10]
                self.totaling_date = line[10:18]

                top30prizeLine = line[18:]

                self.setDatData(top30prizeLine)
                break
            file.close()

            # DB　ファイル登録
            # 必須項目のみ
            #INSERTが実行される
            with transaction.atomic():
                Trn_Top_30_Prize(Cllasification=self.classification, Data_type=self.data_type, Send_date=self.send_date, Totaling_date=self.totaling_date).save()

                # 空白チェックして実体があるカラムは更新
                self.update_Trn_Top_30_Prize(Trn_Top_30_Prize.objects.get(id=Trn_Top_30_Prize.objects.all().aggregate(Max('id')).get('id__max')))

        except FileNotFoundError as e:
            print(e)
        except UnboundLocalError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)

    # ファイル作成時のイベント
    def on_created(self, event):
        filepath = event.src_path
        filename_top30prize_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,top30prizeData ,filename_top30prize_record))

        # 監視元のフォルダパスを生成

        print('%s created Start' % filename_top30prize_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Top_30_Prize(name)

        print('%s created End' % filename_top30prize_record)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename_top30prize_record = os.path.basename(filepath)
        print('%s changed' % filename_top30prize_record)

    # ファイル削除時のイベント
    def on_deleted(self, event):
        filepath = event.src_path
        filename_top30prize_record = os.path.basename(filepath)
        print('%s deleted' % filename_top30prize_record)

    # ファイル移動時のイベント
    def on_moved(self, event):
        filepath = event.src_path
        filename_top30prize_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,top30prizeData ,filename_top30prize_record))
        print('%s moved Start' % filename_top30prize_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Top_30_Prize(name)

        print('%s moved End' % filename_top30prize_record)

# コマンド実行の確認
class Command(BaseCommand):

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'ファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    def add_arguments(self, parser):
        # 今回はscheduleという名前で取得する。（引数は最低でも1個, int型）
        parser.add_argument('command_id', nargs='+', type=int)


    """受け取った引数を登録する"""
    def handle(self, *args, **options):
        # ファイル監視の開始
        # 選手取得賞金上位３０位レコード（mmddhhmmss00000003.dat） 1: 選手取得賞金上位３０位
        # 監視対象ディレクトリを指定する
        if scheduleID in options['command_id']:
            base_trn_Top_30_Prize = os.path.dirname(os.path.abspath(__file__))
            base = os.path.normpath(os.path.join(base_trn_Top_30_Prize,top30prizeData))
            target_dir = os.path.expanduser(base)

            event_handler = FileChangeHandler([target_file_top30prize_record])
            observer = Observer()
            observer.schedule(event_handler, target_dir, recursive=False)# recursive再帰的
            observer.start()
        else:
            raise ValueError("command_id エラー")

        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

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
# スケジュールレコード（mmddhhmmss00000000.dat）
scheduleID = 1
scheduleData = "scheduleData"
target_file_schedule_record = '*00000000.dat'

# PatternMatchingEventHandler の継承クラスを作成
class FileChangeHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)
        self.watch_path = str()
        
        self.classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
        self.data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
        self.send_date	 = str()                    # ファイル名をキーとして送信日を記憶する
        self.race_date_1	 = str()
        self.outside_1	 = str()
        self.track_code_1_1	 = str()
        self.races_1_1 = int()
        self.track_code_1_2	 = str()
        self.races_1_2 = int()
        self.track_code_1_3	 = str()
        self.races_1_3 = int() 
        self.track_code_1_4	 = str()
        self.races_1_4 = int() 
        self.track_code_1_5	 = str()
        self.races_1_5 = int() 
        self.track_code_1_6	 = str()
        self.races_1_6 = int() 
        self.race_date_2	 = str()
        self.outside_2	 = str()
        self.track_code_2_1	 = str()
        self.races_2_1 = int()	 
        self.track_code_2_2	 = str()
        self.races_2_2 = int()	 
        self.track_code_2_3	 = str()
        self.races_2_3 = int()	 
        self.track_code_2_4	 = str()
        self.races_2_4 = int() 
        self.track_code_2_5	 = str()
        self.races_2_5 = int() 
        self.track_code_2_6	 = str()
        self.races_2_6 = int()	 
        self.race_date_3	 = str()
        self.outside_3	 = str()
        self.track_code_3_1	 = str()
        self.races_3_1 = int()	 
        self.track_code_3_2	 = str()
        self.races_3_2 = int()	 
        self.track_code_3_3	 = str()
        self.races_3_3 = int()	 
        self.track_code_3_4	 = str()
        self.races_3_4 = int()	 
        self.track_code_3_5	 = str()
        self.races_3_5 = int()	 
        self.track_code_3_6	 = str()
        self.races_3_6 = int()	 
        self.top_30_prizes	 = str()            
        self.schedule = 3        

    # 正規表現で半角ブランク削除
    def chkBlank(self, scheduleLineStr):
        if (not re.sub('\\s', '', scheduleLineStr)):       
            return False    
        return True

    # datファイル設定する
    def setDatData(self, scheduleLine):

        # スケジュール 繰り返し ×3
        for s in range(self.schedule):
            if s==0:
                if self.chkBlank(scheduleLine[0:8]):
                    self.race_date_1 = scheduleLine[0:8]
                if self.chkBlank(scheduleLine[8:9]):    
                    self.outside_1 = scheduleLine[8:9]

                # 場スケジュール 繰り返し ×6
                if self.chkBlank(scheduleLine[9:10]):
                    self.track_code_1_1	 = scheduleLine[9:10]
                if self.chkBlank(scheduleLine[10:12]):
                    self.races_1_1	 = scheduleLine[10:12]
                if self.chkBlank(scheduleLine[12:13]):
                    self.track_code_1_2	 = scheduleLine[12:13]                        
                if self.chkBlank(scheduleLine[13:15]):
                    self.races_1_2	 = scheduleLine[13:15]   
                if self.chkBlank(scheduleLine[15:16]):
                    self.track_code_1_3	 = scheduleLine[15:16]
                if self.chkBlank(scheduleLine[16:18]):
                    self.races_1_3	 = scheduleLine[16:18]  
                if self.chkBlank(scheduleLine[18:19]):
                    self.track_code_1_4	 = scheduleLine[18:19]
                if self.chkBlank(scheduleLine[19:21]):
                    self.races_1_4	 = scheduleLine[19:21]
                if self.chkBlank(scheduleLine[21:22]):                           
                    self.track_code_1_5	 = scheduleLine[21:22]
                if self.chkBlank(scheduleLine[22:24]):
                    self.races_1_5	 = scheduleLine[22:24]                             
                if self.chkBlank(scheduleLine[24:25]):
                    self.track_code_1_6	 = scheduleLine[24:25]
                if self.chkBlank(scheduleLine[25:27]):
                    self.races_1_6	 = scheduleLine[25:27]
                
            elif s==1:
                if self.chkBlank(scheduleLine[27:35]):
                    self.race_date_2 = scheduleLine[27:35]
                if self.chkBlank(scheduleLine[35:36]):
                    self.outside_2 = scheduleLine[35:36]

                # 場スケジュール 繰り返し ×6
                if self.chkBlank(scheduleLine[36:37]):
                    self.track_code_2_1	 = scheduleLine[36:37]
                if self.chkBlank(scheduleLine[37:39]):
                    self.races_2_1	 = scheduleLine[37:39]
                if self.chkBlank(scheduleLine[39:40]):  
                    self.track_code_2_2	 = scheduleLine[39:40]
                if self.chkBlank(scheduleLine[40:42]):
                    self.races_2_2	 = scheduleLine[40:42]
                if self.chkBlank(scheduleLine[42:43]):
                    self.track_code_2_3	 = scheduleLine[42:43]
                if self.chkBlank(scheduleLine[43:45]):
                    self.races_2_3	 = scheduleLine[43:45]
                if self.chkBlank(scheduleLine[45:46]):
                    self.track_code_2_4	 = scheduleLine[45:46]
                if self.chkBlank(scheduleLine[46:48]):
                    self.races_2_4	 = scheduleLine[46:48]
                if self.chkBlank(scheduleLine[48:49]):
                    self.track_code_2_5	 = scheduleLine[48:49]
                if self.chkBlank(scheduleLine[49:51]):
                    self.races_2_5	 = scheduleLine[49:51]
                if self.chkBlank(scheduleLine[51:52]):
                    self.track_code_2_6	 = scheduleLine[51:52]
                if self.chkBlank(scheduleLine[52:54]):
                    self.races_2_6	 = scheduleLine[52:54]
            else:
                if self.chkBlank(scheduleLine[54:62]):
                    self.race_date_3 = scheduleLine[54:62]
                if self.chkBlank(scheduleLine[62:63]):  
                    self.outside_3 = scheduleLine[62:63]

                # 場スケジュール 繰り返し ×6
                if self.chkBlank(scheduleLine[63:64]):
                    self.track_code_3_1	 = scheduleLine[63:64]
                if self.chkBlank(scheduleLine[64:66]):  
                    self.races_3_1	 = scheduleLine[64:66]
                if self.chkBlank(scheduleLine[66:67]):
                    self.track_code_3_2	 = scheduleLine[66:67]
                if self.chkBlank(scheduleLine[67:69]):  
                    self.races_3_2	 = scheduleLine[67:69]
                if self.chkBlank(scheduleLine[69:70]):  
                    self.track_code_3_3	 = scheduleLine[69:70]
                if self.chkBlank(scheduleLine[70:72]):  
                    self.races_3_3	 = scheduleLine[70:72]
                if self.chkBlank(scheduleLine[72:73]):  
                    self.track_code_3_4	 = scheduleLine[72:73]
                if self.chkBlank(scheduleLine[73:75]):  
                    self.races_3_4	 = scheduleLine[73:75]
                if self.chkBlank(scheduleLine[75:76]):  
                    self.track_code_3_5	 = scheduleLine[75:76]
                if self.chkBlank(scheduleLine[76:78]):  
                    self.races_3_5	 = scheduleLine[76:78]
                if self.chkBlank(scheduleLine[78:79]):  
                    self.track_code_3_6	 = scheduleLine[78:79]
                if self.chkBlank(scheduleLine[79:81]):    
                    self.races_3_6	 = scheduleLine[79:81]
                if self.chkBlank(scheduleLine[-1]):
                    self.top_30_prizes = scheduleLine[-1]  
    
    def update_Trn_Schedule(self, trn_Update):
        updateFields = list()
        if self.race_date_1:
            trn_Update.Race_date_1=self.race_date_1
            updateFields.append('Race_date_1')
        if self.outside_1:
            trn_Update.Outside_1=self.outside_1
            updateFields.append('Outside_1')
        if self.races_1_1:
            trn_Update.races_1_1= self.races_1_1
            updateFields.append('races_1_1')
        if self.races_1_2:
            trn_Update.races_1_2= self.races_1_2
            updateFields.append('races_1_2')
        if self.races_1_3:
            trn_Update.races_1_3= self.races_1_3
            updateFields.append('races_1_3')
        if self.races_1_4:
            trn_Update.races_1_4= self.races_1_4
            updateFields.append('races_1_4')
        if self.races_1_5:
            trn_Update.races_1_5= self.races_1_5
            updateFields.append('races_1_5')
        if self.races_1_6:
            trn_Update.races_1_6= self.races_1_6
            updateFields.append('races_1_6')

        if self.race_date_2:
            trn_Update.Race_date_2=self.race_date_2
            updateFields.append('Race_date_2')
        if self.outside_2:
            trn_Update.Outside_2=self.outside_2
            updateFields.append('Outside_2')
        if self.races_2_1:
            trn_Update.races_2_1= self.races_2_1
            updateFields.append('races_2_1')
        if self.races_2_2:
            trn_Update.races_2_2= self.races_2_2
            updateFields.append('races_2_2')
        if self.races_2_3:
            trn_Update.races_2_3= self.races_2_3
            updateFields.append('races_2_3')
        if self.races_2_4:
            trn_Update.races_2_4= self.races_2_4
            updateFields.append('races_2_4')
        if self.races_2_5:
            trn_Update.races_2_5= self.races_2_5
            updateFields.append('races_2_5')
        if self.races_2_6:
            trn_Update.races_2_6= self.races_2_6
            updateFields.append('races_2_6')

        if self.race_date_3:
            trn_Update.Race_date_3=self.race_date_3
            updateFields.append('Race_date_3')
        if self.outside_3:
            trn_Update.Outside_3=self.outside_3
            updateFields.append('Outside_3')
        if self.races_3_1:
            trn_Update.races_3_1= self.races_3_1
            updateFields.append('races_3_1')
        if self.races_3_2:
            trn_Update.races_3_2= self.races_3_2
            updateFields.append('races_3_2')
        if self.races_3_3:
            trn_Update.races_3_3= self.races_3_3
            updateFields.append('races_3_3')
        if self.races_3_4:
            trn_Update.races_3_4= self.races_3_4
            updateFields.append('races_3_4')
        if self.races_3_5:
            trn_Update.races_3_5= self.races_3_5
            updateFields.append('races_3_5')
        if self.races_3_6:
            trn_Update.races_3_6= self.races_3_6
            updateFields.append('races_3_6')

        if self.top_30_prizes:
            trn_Update.Top_30_prizes = self.top_30_prizes
            updateFields.append('Top_30_prizes')

        if self.track_code_1_1:
            #マスターに確認 エラー
            trn_Update.Track_code1_1_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_1)
            updateFields.append('Track_code1_1_id')
        if self.track_code_1_2:
            trn_Update.Track_code1_2_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_2)
            updateFields.append('Track_code1_2_id')
        if self.track_code_1_3:
            trn_Update.Track_code1_3_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_3)
            updateFields.append('Track_code1_3_id')
        if self.track_code_1_4:
            trn_Update.Track_code1_4_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_4)
            updateFields.append('Track_code1_4_id')
        if self.track_code_1_5:
            trn_Update.Track_code1_5_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_5)
            updateFields.append('Track_code1_5_id')
        if self.track_code_1_6:
            trn_Update.Track_code1_6_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_6)
            updateFields.append('Track_code1_6_id')
        if self.track_code_2_1:
            trn_Update.Track_code2_1_id=Mst_Race_track.objects.get(Track_code=self.track_code_1_1)
            updateFields.append('Track_code2_1_id')
        if self.track_code_2_2:
            trn_Update.Track_code2_2_id=Mst_Race_track.objects.get(Track_code=self.track_code_2_2)
            updateFields.append('Track_code2_2_id')
        if self.track_code_2_3:
            trn_Update.Track_code2_3_id=Mst_Race_track.objects.get(Track_code=self.track_code_2_3)
            updateFields.append('Track_code2_3_id')
        if self.track_code_2_4:
            trn_Update.Track_code2_4_id=Mst_Race_track.objects.get(Track_code=self.track_code_2_4)
            updateFields.append('Track_code2_4_id')
        if self.track_code_2_5:
            trn_Update.Track_code2_5_id=Mst_Race_track.objects.get(Track_code=self.track_code_2_5)
            updateFields.append('Track_code2_5_id')
        if self.track_code_2_6:
            trn_Update.Track_code2_6_id=Mst_Race_track.objects.get(Track_code=self.track_code_2_6)
            updateFields.append('Track_code2_6_id')
        if self.track_code_3_1:
            trn_Update.Track_code3_1_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_1)
            updateFields.append('Track_code3_1_id')
        if self.track_code_3_2:
            trn_Update.Track_code3_2_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_2)
            updateFields.append('Track_code3_2_id')
        if self.track_code_3_3:
            trn_Update.Track_code3_3_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_3)
            updateFields.append('Track_code3_3_id')
        if self.track_code_3_4:
            trn_Update.Track_code3_4_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_4)
            updateFields.append('Track_code3_4_id')
        if self.track_code_3_5:
            trn_Update.Track_code3_5_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_5)
            updateFields.append('Track_code3_5_id')
        if self.track_code_3_6:
            trn_Update.Track_code3_6_id=Mst_Race_track.objects.get(Track_code=self.track_code_3_6)
            updateFields.append('Track_code3_6_id')
        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)            


    def insert_or_update_Trn_Schedule(self, name):
        try:
            file = open(name,'r')
            for line in file: # 1行しかない
                self.classification = line[0:1]
                self.data_type = line[1:2]
                self.send_date = line[2:10]
                              
                scheduleLine = line[10:]

                self.setDatData(scheduleLine)
                break            
            file.close()

            # DB　ファイル登録
            # 必須項目のみ
            #INSERTが実行される
            with transaction.atomic():
                Trn_Schedule(Cllasification=self.classification, Data_type=self.data_type, Send_date=self.send_date).save()

                # 空白チェックして実体があるカラムは更新
                self.update_Trn_Schedule(Trn_Schedule.objects.get(id=Trn_Schedule.objects.all().aggregate(Max('id')).get('id__max')))

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
        filename_schedule_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,scheduleData ,filename_schedule_record))

        # 監視元のフォルダパスを生成

        print('%s created Start' % filename_schedule_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Schedule(name)
        
        print('%s created End' % filename_schedule_record)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename_schedule_record = os.path.basename(filepath)
        print('%s changed' % filename_schedule_record)

    # ファイル削除時のイベント
    def on_deleted(self, event):
        filepath = event.src_path
        filename_schedule_record = os.path.basename(filepath)
        print('%s deleted' % filename_schedule_record)

    # ファイル移動時のイベント
    def on_moved(self, event):
        filepath = event.src_path
        filename_schedule_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,scheduleData ,filename_schedule_record))    
        print('%s moved Start' % filename_schedule_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Schedule(name)

        print('%s moved End' % filename_schedule_record)

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
        # スケジュールレコード（mmddhhmmss00000000.dat） 1: スケジュール
        # 監視対象ディレクトリを指定する
        if scheduleID in options['command_id']:
            base_trn_Schedule = os.path.dirname(os.path.abspath(__file__))
            base = os.path.normpath(os.path.join(base_trn_Schedule,scheduleData))
            target_dir = os.path.expanduser(base)

            event_handler = FileChangeHandler([target_file_schedule_record])
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
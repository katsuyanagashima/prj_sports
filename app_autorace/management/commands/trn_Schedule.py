import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import time
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from django.core.management.base import BaseCommand, CommandError
from app_autorace.models import *
from logging import getLogger

#!/usr/bin/env 
logger = getLogger(__name__)

# 監視対象ディレクトリを指定する
base = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.expanduser(base)
# 監視対象ファイルのパターンマッチを指定する
# スケジュールレコード（mmddhhmmss00000000.dat）
target_file_schedule_record = '*00000000.dat'

# PatternMatchingEventHandler の継承クラスを作成
class FileChangeHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)

    # ファイル作成時のイベント
    def on_created(self, event):
        filepath = event.src_path
        filename_schedule_record = os.path.basename(filepath)
        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base, filepath))
        print('%s created' % filename_schedule_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-

        try:

            classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
            data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
            send_date	 = str()                    # ファイル名をキーとして送信日を記憶する
            race_date_1	 = str()
            outside_1	 = str()
            track_code_1_1	 = str()
            races_1_1	 = int()
            track_code_1_2	 = str()
            races_1_2	 = int()
            track_code_1_3	 = str()
            races_1_3	 = int()
            track_code_1_4	 = str()
            races_1_4	 = int()
            track_code_1_5	 = str()
            races_1_5	 = int()
            track_code_1_6	 = str()
            races_1_6	 = int()
            race_date_2	 = str()
            outside_2	 = str()
            track_code_2_1	 = str()
            races_2_1	 = int()
            track_code_2_2	 = str()
            races_2_2	 = int()
            track_code_2_3	 = str()
            races_2_3	 = int()
            track_code_2_4	 = str()
            races_2_4	 = int()
            track_code_2_5	 = str()
            races_2_5	 = int()
            track_code_2_6	 = str()
            races_2_6	 = int()
            race_date_3	 = str()
            outside_3	 = str()
            track_code_3_1	 = str()
            races_3_1	 = int()
            track_code_3_2	 = str()
            races_3_2	 = int()
            track_code_3_3	 = str()
            races_3_3	 = int()
            track_code_3_4	 = str()
            races_3_4	 = int()
            track_code_3_5	 = str()
            races_3_5	 = int()
            track_code_3_6	 = str()
            races_3_6	 = int()
            top_30_prizes	 = str()
            schedule = 3

            file = open(name,'r')
            for line in file: # 1行しかない
                classification = line[0:1]
                data_type = line[1:2]
                send_date = line[2:10]
                top_30_prizes = line[-1]                
                scheduleLine = line[10:-1]

                def chkBlank(scheduleLineStr):
                    if (not re.sub('\s', '', scheduleLineStr)):                
                        return False
                    return True

                # スケジュール 繰り返し ×3
                for s in range(schedule):
                    if s==0:
                        if chkBlank(scheduleLine[0:8]):
                            race_date_1 = scheduleLine[0:8]
                        if chkBlank(scheduleLine[8:9]):    
                            outside_1 = scheduleLine[8:9]

                        # 場スケジュール 繰り返し ×6
                        if chkBlank(scheduleLine[9:10]):
                            track_code_1_1	 = scheduleLine[9:10]
                        if chkBlank(scheduleLine[10:12]):
                            races_1_1	 = scheduleLine[10:12]
                        if chkBlank(scheduleLine[12:13]):
                            track_code_1_2	 = scheduleLine[12:13]                        
                        if chkBlank(scheduleLine[13:15]):
                            races_1_2	 = scheduleLine[13:15]   
                        if chkBlank(scheduleLine[15:16]):
                            track_code_1_3	 = scheduleLine[15:16]
                        if chkBlank(scheduleLine[16:18]):
                            races_1_3	 = scheduleLine[16:18]  
                        if chkBlank(scheduleLine[18:19]):
                            track_code_1_4	 = scheduleLine[18:19]
                        if chkBlank(scheduleLine[19:21]):
                            races_1_4	 = scheduleLine[19:21]
                        if chkBlank(scheduleLine[21:22]):                           
                            track_code_1_5	 = scheduleLine[21:22]
                        if chkBlank(scheduleLine[22:24]):
                            races_1_5	 = scheduleLine[22:24]                             
                        if chkBlank(scheduleLine[24:25]):
                            track_code_1_6	 = scheduleLine[24:25]
                        if chkBlank(scheduleLine[25:27]):
                            races_1_6	 = scheduleLine[25:27]
                        
                    elif s==1:
                        if chkBlank(scheduleLine[27:35]):
                            race_date_2 = scheduleLine[27:35]
                        if chkBlank(scheduleLine[35:36]):
                            outside_2 = scheduleLine[35:36]

                        # 場スケジュール 繰り返し ×6
                        if chkBlank(scheduleLine[36:37]):
                            track_code_2_1	 = scheduleLine[36:37]
                        if chkBlank(scheduleLine[37:39]):
                            races_2_1	 = scheduleLine[37:39]
                        if chkBlank(scheduleLine[39:40]):  
                            track_code_2_2	 = scheduleLine[39:40]
                        if chkBlank(scheduleLine[40:42]):
                            races_2_2	 = scheduleLine[40:42]
                        if chkBlank(scheduleLine[42:43]):
                            track_code_2_3	 = scheduleLine[42:43]
                        if chkBlank(scheduleLine[43:45]):
                            races_2_3	 = scheduleLine[43:45]
                        if chkBlank(scheduleLine[45:46]):
                            track_code_2_4	 = scheduleLine[45:46]
                        if chkBlank(scheduleLine[46:48]):
                            races_2_4	 = scheduleLine[46:48]
                        if chkBlank(scheduleLine[48:49]):
                            track_code_2_5	 = scheduleLine[48:49]
                        if chkBlank(scheduleLine[49:51]):
                            races_2_5	 = scheduleLine[49:51]
                        if chkBlank(scheduleLine[51:52]):
                            track_code_2_6	 = scheduleLine[51:52]
                        if chkBlank(scheduleLine[52:54]):
                            races_2_6	 = scheduleLine[52:54]
                    else:
                        if chkBlank(scheduleLine[54:62]):
                            race_date_3 = scheduleLine[54:62]
                        if chkBlank(scheduleLine[62:63]):  
                            outside_3 = scheduleLine[62:63]

                        # 場スケジュール 繰り返し ×6
                        if chkBlank(scheduleLine[63:64]):
                            track_code_3_1	 = scheduleLine[63:64]
                        if chkBlank(scheduleLine[64:66]):  
                            races_3_1	 = scheduleLine[64:66]
                        if chkBlank(scheduleLine[66:67]):
                            track_code_3_2	 = scheduleLine[66:67]
                        if chkBlank(scheduleLine[67:69]):  
                            races_3_2	 = scheduleLine[67:69]
                        if chkBlank(scheduleLine[69:70]):  
                            track_code_3_3	 = scheduleLine[69:70]
                        if chkBlank(scheduleLine[70:72]):  
                            races_3_3	 = scheduleLine[70:72]
                        if chkBlank(scheduleLine[72:73]):  
                            track_code_3_4	 = scheduleLine[72:73]
                        if chkBlank(scheduleLine[73:75]):  
                            races_3_4	 = scheduleLine[73:75]
                        if chkBlank(scheduleLine[75:76]):  
                            track_code_3_5	 = scheduleLine[75:76]
                        if chkBlank(scheduleLine[76:78]):  
                            races_3_5	 = scheduleLine[76:78]
                        if chkBlank(scheduleLine[78:79]):  
                            track_code_3_6	 = scheduleLine[78:79]
                        if chkBlank(scheduleLine[79:81]):    
                            races_3_6	 = scheduleLine[79:81]
                    break            
            file.close()

            # DB　ファイル登録
            # 必須項目のみ
            #INSERTが実行される
            trn_S =Trn_Schedule(Cllasification=classification, Data_type=data_type, Send_date=send_date)
            trn_S.save()
            
            # 空白チェックして実体があるカラムは登録
            if not race_date_1:
                trn_S.Race_date_1=race_date_1
            if not outside_1:
                trn_S.Outside_1=outside_1
            if not races_1_1:
                trn_S.races_1_1=races_1_1
            if not races_1_2:
                trn_S.races_1_2=races_1_2
            if not races_1_3:
                trn_S.races_1_3=races_1_3
            if not races_1_4:
                trn_S.races_1_4=races_1_4
            if not races_1_5:
                trn_S.races_1_5=races_1_5
            if not races_1_6:
                trn_S.races_1_6=races_1_6

            if not race_date_2:
                trn_S.race_date_2=race_date_2
            if not outside_2:
                trn_S.Outside_2=outside_2
            if not races_2_1:
                trn_S.races_2_1=races_2_1
            if not races_2_2:
                trn_S.races_2_2=races_2_2
            if not races_2_3:
                trn_S.races_2_3=races_2_3
            if not races_2_4:
                trn_S.races_2_4=races_2_4
            if not races_2_5:
                trn_S.races_2_5=races_2_5
            if not races_2_6:
                trn_S.races_2_6=races_2_6

            if not race_date_3:
                trn_S.race_date_3=race_date_3
            if not outside_3:
                trn_S.Outside_3=outside_3
            if not races_3_1:
                trn_S.races_3_1=races_3_1
            if not races_3_2:
                trn_S.races_3_2=races_3_2
            if not races_3_3:
                trn_S.races_3_3=races_3_3
            if not races_3_4:
                trn_S.races_3_4=races_3_4
            if not races_3_5:
                trn_S.races_3_5=races_3_5
            if not races_3_6:
                trn_S.races_3_6=races_3_6

            if not top_30_prizes:
                trn_S.Top_30_prizes = top_30_prizes

            trn_S.save()
            if not track_code_1_1:
                trn_S.Track_code1_1=Mst_Race_track(Track_code=track_code_1_1)
            if not track_code_1_2:
                trn_S.Track_code1_2=Mst_Race_track(Track_code=track_code_1_2)
            if not track_code_1_3:
                trn_S.Track_code1_3=Mst_Race_track(Track_code=track_code_1_3)
            if not track_code_1_4:
                trn_S.Track_code1_4=Mst_Race_track(Track_code=track_code_1_4)
            if not track_code_1_5:
                trn_S.Track_code1_5=Mst_Race_track(Track_code=track_code_1_5)                
            if not track_code_1_6:
                trn_S.Track_code1_6=Mst_Race_track(Track_code=track_code_1_6)
            if not track_code_2_1:
                trn_S.Track_code2_1=Mst_Race_track(Track_code=track_code_2_1)
            if not track_code_2_2:
                trn_S.Track_code2_2=Mst_Race_track(Track_code=track_code_2_2)
            if not track_code_2_3:
                trn_S.Track_code2_3=Mst_Race_track(Track_code=track_code_2_3)
            if not track_code_2_4:
                trn_S.Track_code2_4=Mst_Race_track(Track_code=track_code_2_4)
            if not track_code_2_5:
                trn_S.Track_code2_5=Mst_Race_track(Track_code=track_code_2_5)                
            if not track_code_2_6:
                trn_S.Track_code2_6=Mst_Race_track(Track_code=track_code_2_6)
            if not track_code_3_1:
                trn_S.Track_code3_1=Mst_Race_track(Track_code=track_code_3_1)
            if not track_code_3_2:
                trn_S.Track_code3_2=Mst_Race_track(Track_code=track_code_3_2)
            if not track_code_3_3:
                trn_S.Track_code3_3=Mst_Race_track(Track_code=track_code_3_3)
            if not track_code_3_4:
                trn_S.Track_code3_4=Mst_Race_track(Track_code=track_code_3_4)
            if not track_code_3_5:
                trn_S.Track_code3_5=Mst_Race_track(Track_code=track_code_3_5)                
            if not track_code_3_6:
                trn_S.Track_code3_6=Mst_Race_track(Track_code=track_code_3_6)


        except FileNotFoundError as e:
            print(e)

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
        print('%s moved' % filename_schedule_record)

# コマンド実行の確認
class Command(BaseCommand):

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'スケジュールレコードのファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    # def add_arguments(self, parser):

    """受け取った引数を登録する"""
    def handle(self, *args, **options):
        # ファイル監視の開始
        # スケジュールレコード（mmddhhmmss00000000.dat）
        event_handler = FileChangeHandler([target_file_schedule_record])
        observer = Observer()
        observer.schedule(event_handler, target_dir, recursive=True)
        observer.start()
        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
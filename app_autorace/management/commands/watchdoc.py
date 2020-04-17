import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import pprint
import re
import sys
import time
from logging import getLogger
from pathlib import Path

# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver
sys.path.append("/code/app_autorace/management/commands/")
import trn_Schedule
from app_autorace.models import *
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max

# 監視対象ディレクトリを指定する
# target_dir = 'C:\\Users\\sports\\Desktop\\ttt\\test'
# target_dirSample = os.getcwd() # /code 取得する。

# print(sys.path)
#!/usr/bin/env 
logger = getLogger('command')

# 監視対象ファイルのパターンマッチを指定する
# スケジュールレコード（mmddhhmmss00000000.dat）
scheduleID = 1
scheduleData = "scheduleData"
target_file_schedule_record = '*00000000.dat'
base = os.path.dirname(os.path.abspath(__file__))

# PatternMatchingEventHandler の継承クラスを作成
class WatchDocHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(WatchDocHandler, self).__init__(patterns=patterns)

    # ファイル作成時のイベント
    def on_created(self, event):
        # ①～⑤　どれを呼び出すかパスから判断する。
        filepath = event.src_path

        if scheduleData in filepath:   
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base,scheduleData ,filename_schedule_record))

            logger.info( "created Start:" + filename_schedule_record)
            # ファイル読み込み
            schedule = trn_Schedule.Schedule()
            logger.info( "created End:")
                
            
            schedule.insert_or_update_Trn_Schedule(name)
        

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
        schedule = trn_Schedule.Schedule()
        schedule.insert_or_update_Trn_Schedule(name)

        print('%s moved End' % filename_schedule_record)

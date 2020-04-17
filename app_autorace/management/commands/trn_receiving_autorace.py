import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import pprint
import re
import sys
import time
from logging import getLogger
from pathlib import Path
sys.path.append("/code/app_autorace/management/commands/")
import trn_Schedule
import watchdoc
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver

from app_autorace.models import *
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max


# 監視対象ディレクトリを指定する
# target_dir = 'C:\\Users\\sports\\Desktop\\ttt\\test'
# target_dirSample = os.getcwd() # /code 取得する。

# print(sys.path)
#!/usr/bin/env 
logger = getLogger("command")

# 監視対象ファイルのパターンマッチを指定する
# スケジュールレコード（mmddhhmmss00000000.dat）
# scheduleID = 1
scheduleData = "scheduleData"
resultData = "resultData"
target_file_schedule_record = '*00000000.dat'
target_file_result_record = ['*0000[1-6]0[1-9]2.dat','*0000[1-6]1[0-2]2.dat']
go_recursively = False
trn_rider_result_list = 8
base_trn = os.path.dirname(os.path.abspath(__file__))

# コマンド実行の確認
class Command(BaseCommand):
    # コンストラクターの定義
    def __init__(self):
        self.observer_trn_schedule = PollingObserver()
        self.observer_trn_result = PollingObserver()

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'ファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    # def add_arguments(self, parser):
        # 今回はscheduleという名前で取得する。（引数は最低でも1個, int型）
        # parser.add_argument('command_id', nargs='+', type=int)

    """受け取った引数を登録する"""
    def handle(self, *args, **options):
        # ファイル監視の開始
        # スケジュールレコード（mmddhhmmss00000000.dat） 1: スケジュール
        # 監視対象ディレクトリを指定する
        try:
            baseScheduleData = os.path.normpath(os.path.join(base_trn,scheduleData))
            target_dir_scheduleData = os.path.expanduser(baseScheduleData)
            
            logger.info("scheduleData: スケジュール監視　Start")
            event_handler_schedule = watchdoc.WatchDocHandler([target_file_schedule_record])
            self.observer_trn_schedule.schedule(event_handler_schedule, target_dir_scheduleData, recursive=go_recursively)# recursive再帰的
            logger.info("scheduleData: スケジュール監視　End")
            self.observer_trn_schedule.start()
        except Exception:
            self.observer_trn_schedule.stop()

        # 監視対象ディレクトリを指定する
        # レース結果データレコード（mmddhhmmss0000JRR2.dat） 3: レース結果
        try:
            baseResultData = os.path.normpath(os.path.join(base_trn,resultData))
            target_dir_resultData = os.path.expanduser(baseResultData)

            logger.info("resultData: レース結果監視　Start")
            event_handler_result = watchdoc.WatchDocHandler([target_file_result_record])
            self.observer_trn_result.schedule(event_handler_result, target_dir_resultData, recursive=go_recursively)# recursive再帰的
            logger.info("resultData: レース結果監視　End")
            self.observer_trn_result.start()
        except Exception:
            self.observer_trn_result.stop()

        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)

                # エラーの処理を判断して止める


        except KeyboardInterrupt:
            self.observer_trn_schedule.stop()
            self.observer_trn_result.stop()
        self.observer_trn_schedule.join()
        self.observer_trn_result.join()

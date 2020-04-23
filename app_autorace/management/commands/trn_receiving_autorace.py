# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import pprint
import re
import sys
import time
from logging import getLogger
from pathlib import Path
sys.path.append("/code/app_autorace/management/commands/")

import watchdoc
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_autorace.models import *
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max
sys.path.append("/code/app_autorace/")
from consts import *

logger = getLogger('command')
# 監視対象ファイルのパターンマッチを指定する
target_file_schedule_record = ['*00000000.dat']
target_file_program_record = ['*0000[1-6]001.dat']
target_file_result_record = ['*0000[1-6]0[1-9]2.dat','*0000[1-6]1[0-2]2.dat']
target_file_top30prize_record = ['*00000003.dat']
target_file_outsidetrack_record = ['*00000004.dat']

base_trn = os.path.dirname(os.path.abspath(__file__))   
# コマンド実行の確認
class Command(BaseCommand):    
    # コンストラクターの定義
    def __init__(self):

        self.observer_trn_schedule = PollingObserver()
        self.observer_trn_program = PollingObserver()
        self.observer_trn_result = PollingObserver()
        self.observer_trn_top_30_prize = PollingObserver()
        self.observer_trn_outsidetrack = PollingObserver()

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'ファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    # def add_arguments(self, parser):
        # 今回はscheduleという名前で取得する。（引数は最低でも1個, int型）
        # parser.add_argument('command_id', nargs='+', type=int)

    """受け取った引数を登録する"""
    # ファイル監視の開始
    def handle(self, *args, **options):

        # 監視対象ディレクトリを指定する
        # スケジュールレコード（mmddhhmmss00000000.dat） 1: スケジュール
        try:
            baseScheduleData = os.path.normpath(os.path.join(base_trn, SCHEDULEDATA))
            target_dir_scheduleData = os.path.expanduser(baseScheduleData)
            
            event_handler_schedule = watchdoc.WatchDocHandler(target_file_schedule_record)
            logger.info("target_dir_scheduleData:" + target_dir_scheduleData )
            self.observer_trn_schedule.schedule(event_handler_schedule, target_dir_scheduleData, recursive=GO_RECURSIVELY)# recursive再帰的
            # 監視実行
            self.observer_trn_schedule.start()
            logger.info("scheduleData: スケジュール監視　Start" )
        except Exception as e:
            logger.error(e)

        # 監視対象ディレクトリを指定する
        # 番組編成データレコード（mmddhhmmss0000J001.dat） 2: 番組編成
        try:
            baseProgramData = os.path.normpath(os.path.join(base_trn, PROGRAMDATA))
            target_dir_programData = os.path.expanduser(baseProgramData)

            event_handler_result = watchdoc.WatchDocHandler(target_file_program_record)
            logger.info("target_dir_programData:" + target_dir_programData )
            self.observer_trn_program.schedule(event_handler_result, target_dir_programData, recursive=GO_RECURSIVELY)# recursive再帰的
            # 監視実行
            logger.info("programData: 番組編成監視　Start")
            self.observer_trn_program.start()
        except Exception as e:
            logger.error(e)

        # 監視対象ディレクトリを指定する
        # レース結果データレコード（mmddhhmmss0000JRR2.dat） 3: レース結果
        try:
            baseResultData = os.path.normpath(os.path.join(base_trn, RESULTDATA))
            target_dir_resultData = os.path.expanduser(baseResultData)

            event_handler_result = watchdoc.WatchDocHandler(target_file_result_record)
            logger.info("target_dir_resultData:" + target_dir_resultData )
            self.observer_trn_result.schedule(event_handler_result, target_dir_resultData, recursive=GO_RECURSIVELY)# recursive再帰的
            # 監視実行
            logger.info("resultData: レース結果監視　Start")
            self.observer_trn_result.start()
        except Exception as e:
            logger.error(e)

        # 監視対象ディレクトリを指定する
        # 選手取得賞金上位３０位レコード（mmddhhmmss00000003.dat） 4: 選手取得賞金上位３０位
        try:
            baseTop30prizeData = os.path.normpath(os.path.join(base_trn, TOP30PRIZEDATA))
            target_dir_top30prizeData = os.path.expanduser(baseTop30prizeData)

            event_handler_result = watchdoc.WatchDocHandler(target_file_top30prize_record)
            logger.info("target_dir_top30prizeData:" + target_dir_top30prizeData )
            self.observer_trn_top_30_prize.schedule(event_handler_result, target_dir_top30prizeData, recursive=GO_RECURSIVELY)# recursive再帰的
            # 監視実行
            logger.info("top30prizeData: 選手取得賞金上位３０位監視　Start")
            self.observer_trn_top_30_prize.start()
        except Exception as e:
            logger.error(e)    

        # 監視対象ディレクトリを指定する
        # 場外売場情報（mmddhhmmss00000004.dat） 5: 場外売場情報 
        try:
            baseOutsidetrackData = os.path.normpath(os.path.join(base_trn, OUTSIDETRACKDATA))
            target_dir_outsidetrackData = os.path.expanduser(baseOutsidetrackData)

            event_handler_result = watchdoc.WatchDocHandler(target_file_outsidetrack_record)
            logger.info("target_dir_outsidetrackData:" + target_dir_outsidetrackData )
            self.observer_trn_outsidetrack.schedule(event_handler_result, target_dir_outsidetrackData, recursive=GO_RECURSIVELY)# recursive再帰的
            # 監視実行
            logger.info("outsidetrackData: 場外売場情報監視　Start")
            self.observer_trn_outsidetrack.start()
        except Exception as e:
            logger.error(e)

        # 処理が終了しないようスリープを挟んで無限ループ
        try:

            while True:
                time.sleep(1)
                # システムステータスの処理
                # エラーの処理を判断して止める
                # systemstatus = Tran_Systemstatus.objects.select_related('Operationmode').get(id=1)
                # if (systemstatus.Operationmode.Operationmode_code==1):

                #    self.observer_trn_schedule.stop()
                #    logger.warning("scheduleData: スケジュール監視　End")
                #    self.observer_trn_program.stop()
                #    logger.warning("programData: 番組編成監視　End")
                #    self.observer_trn_result.stop()
                #    logger.warning("resultData: レース結果監視　End")
                #    self.observer_trn_top_30_prize.stop()
                #    logger.warning("top30prizeData: 選手取得賞金上位３０位監視　End")
                #    self.observer_trn_outsidetrack.stop()
                #    logger.warning("outsidetrackData: 場外売場情報監視　End")                    
                #    return False

        except KeyboardInterrupt:
            self.observer_trn_schedule.stop()
            self.observer_trn_program.stop()
            self.observer_trn_result.stop()
            self.observer_trn_top_30_prize.stop()
            self.observer_trn_outsidetrack.stop()
            
        finally:
            logger.info("scheduleData: スケジュール監視　End")
            logger.info("programData: 番組編成監視　End")
            logger.info("resultData: レース結果監視　End")
            logger.info("top30prizeData: 選手取得賞金上位３０位監視　End")
            logger.info("outsidetrackData: 場外売場情報監視　End")
 
            # .pid_lockfile消去
            # finaly = 例外の発生に関係なく最後に処理
            self.observer_trn_schedule.join()
            self.observer_trn_program.join()
            self.observer_trn_result.join()
            self.observer_trn_top_30_prize.join()
            self.observer_trn_outsidetrack.join()
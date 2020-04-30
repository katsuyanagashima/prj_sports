# pwd : /code
import os
import re
import sys
import time
from logging import getLogger
from pathlib import Path

# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_autorace.consts import *

logger = getLogger('command')
base_trn = os.path.dirname(os.path.abspath(__file__))
try:
    from app_autorace import trn_schedule, trn_program, trn_result, trn_top_30_prize, trn_outside_track
except Exception as e:
    logger.error("トランファイル読み込み失敗" + str(e))

class DatManage():
    # コンストラクターの定義
    def __init__(self):

        self.observer_trn_watchdoc = PollingObserver()

    def stop_trn_watchdoc(self):
        # システムステータスの処理
        # エラーの処理を判断して止める
        # モデル読み込みがここでしか読み込みできない
        try:
            from app_autorace.models import Tran_Systemstatus
            while True:
                time.sleep(1)
                systemstatus = Tran_Systemstatus.objects.select_related('Operationmode').get(id=1)
                if systemstatus and (systemstatus.Operationmode.Operationmode_code==1):

                    self.observer_trn_watchdoc.stop()
                    logger.warning("watchdoc監視　End")
                return False

        except Exception as e:
            logger.error("トランシステム該当レコードなし" + str(e))

    def run_trn_watchdoc(self):
        # watchdoc 呼び出し
        baseDatData = os.path.normpath(os.path.join(base_trn, DATDATA))
        targetDirDatData = os.path.expanduser(baseDatData)

        event_handler_schedule = WatchDocHandler(TARGET_FILE_DAT_RECORD)
        logger.info("targetDirDatData: " + targetDirDatData )
        self.observer_trn_watchdoc.schedule(event_handler_schedule, targetDirDatData, recursive=GO_RECURSIVELY)# recursive再帰的
        # 監視実行
        logger.info("watchdoc監視　Start" )
        self.observer_trn_watchdoc.start()

# PatternMatchingEventHandler の継承クラスを作成
class WatchDocHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(WatchDocHandler, self).__init__(patterns=patterns)

    def checkDatData(self, filepath):
        if re.search('00000000.dat', filepath):
            return SCHEDULE

        if re.search('0000[1-6]001.dat', filepath):
            return PROGRAM

        if re.search('0000[1-6]0[1-9]2.dat', filepath) or re.search('0000[1-6]1[0-2]2.dat', filepath):
            return RESULT

        if re.search('00000003.dat', filepath):
            return TOP30PRIZE

        if re.search('00000004.dat', filepath):
            return OUTSIDETRACK

        return None

    # ファイル作成時のイベント
    def on_created(self, event):

        filepath = event.src_path
        logger.info(filepath)
        # ①～⑤　どれを呼び出すか判断する。
        datDataFileFlg=self.checkDatData(filepath)
        logger.info("datDataFileFlg: " + str(datDataFileFlg))

        if datDataFileFlg == SCHEDULE:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_schedule_record))

            logger.info( "created Start:" + fileName)
            # ファイル読み込み
            schedule = trn_schedule.Schedule()

            logger.error("DB insert_or_update_Trn_Schedule: 失敗：ファイル名" + fileName) if not schedule.insert_or_update_Trn_Schedule(fileName) else logger.info( "created End:")

        if datDataFileFlg == PROGRAM:
            filename_program_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_program_record))

            logger.info( "created Start:" + fileName)
            # ファイル読み込み
            program = trn_program.Program()

            logger.error("DB insert_or_update_Trn_Program: 失敗：ファイル名" + fileName) if not program.insert_or_update_Trn_Program(fileName) else logger.info( "created End:")

        if datDataFileFlg == RESULT:
            filename_result_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_result_record))

            logger.info( "created Start:" + fileName)
            # ファイル読み込み
            result = trn_result.Result()

            logger.error("DB insert_or_update_Trn_Result: 失敗：ファイル名" + fileName) if not result.insert_or_update_Trn_Result(fileName) else logger.info( "created End:")

        if datDataFileFlg == TOP30PRIZE:
            filename_top30prize_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_top30prize_record))

            logger.info( "created Start:" + fileName)
            # ファイル読み込み
            top_30_prize = trn_top_30_prize.Top_30_prize()

            logger.error("DB insert_or_update_Trn_Top_30_Prize: 失敗：ファイル名" + fileName) if not top_30_prize.insert_or_update_Trn_Top_30_Prize(fileName) else logger.info( "created End:")

        if datDataFileFlg == OUTSIDETRACK:
            filename_outside_track_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_outside_track_record))

            logger.info( "created Start:" + fileName)
            # ファイル読み込み
            outside_track = trn_outside_track.Outside_track()

            logger.error("DB insert_or_update_Trn_Outside_track: 失敗：ファイル名" + fileName) if not outside_track.insert_or_update_Trn_Outside_track(fileName) else logger.info( "created End:")

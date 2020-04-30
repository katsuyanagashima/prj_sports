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

from app_ckeiba.consts import *

logger = getLogger('app_ckeiba')
base_trn = os.path.dirname(os.path.abspath(__file__))
try:
    from app_ckeiba import trn_BA7, trn_SEI
except Exception as e:
    logger.error(f'トランファイル読み込み失敗  {e}')

class CsvManage():
    # コンストラクターの定義
    def __init__(self):

        self.observer_trn_watchdoc = PollingObserver()

    def stop_trn_watchdoc(self):
        # システムステータスの処理
        # エラーの処理を判断して止める
        # モデル読み込みがここでしか読み込みできない
        try:
            from app_ckeiba.models import Tran_Systemstatus
            while True:
                time.sleep(1)
                systemstatus = Tran_Systemstatus.objects.select_related('Operationmode').get(id=1)
                if systemstatus and (systemstatus.Operationmode.Operationmode_code==1):

                    self.observer_trn_watchdoc.stop()
                    logger.warning("watchdoc監視　End")
                return False

        except Exception as e:
            logger.error(f'トランシステム該当レコードなし {e}')

    def run_trn_watchdoc(self):
        # watchdoc 呼び出し
        baseCsvData = os.path.normpath(os.path.join(base_trn, CSVDATA))
        targetDirCsvData = os.path.expanduser(baseCsvData)

        event_handler_schedule = WatchDocHandler(TARGET_FILE_DAT_RECORD)
        logger.info(f'targetDirCsvData:  {targetDirCsvData}' )
        self.observer_trn_watchdoc.schedule(event_handler_schedule, targetDirCsvData, recursive=GO_RECURSIVELY)# recursive再帰的
        # 監視実行
        logger.info("watchdoc監視　Start" )
        self.observer_trn_watchdoc.start()

# 監視対象ファイルのパターンマッチを指定する
# PatternMatchingEventHandler の継承クラスを作成
class WatchDocHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(WatchDocHandler, self).__init__(patterns=patterns)

    def checkCsvData(self, filepath):
        if re.search(EVENTDATEDATA, filepath):
            return EVENTDATEDATA

        if re.search(SIMPLERACERESULTSDATA, filepath):
            return SIMPLERACERESULTSDATA

        return None

    # ファイル作成時のイベント
    def on_created(self, event):

        filepath = event.src_path
        logger.info(filepath)
        # ①～⑤　どれを呼び出すか判断する。
        csvDataFileFlg=self.checkCsvData(filepath)
        logger.info(f'csvDataFileFlg :{csvDataFileFlg}')

        # 開催日割データ
        if EVENTDATEDATA == csvDataFileFlg:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, CSVDATA, filename_schedule_record))

            logger.info( f'created Start :{fileName}')
            # ファイル読み込み
            trn_Ba7 = trn_BA7.Ba7()

            logger.error(f'DB insert_or_update_Trn_XXXXXXX: 失敗：ファイル名  {fileName}') if not trn_Ba7.insert_or_update_Trn_Ba7(fileName) else logger.info( "created End:")

        # 簡易競走成績データ
        if SIMPLERACERESULTSDATA == csvDataFileFlg:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, CSVDATA, filename_schedule_record))

            logger.info( f'created Start :{fileName}')
            # ファイル読み込み
            trn_sei = trn_SEI.Sei()

            logger.error(f'DB insert_or_update_Trn_XXXXXXX: 失敗：ファイル名  {fileName}') if not trn_sei.insert_or_update_Trn_Sei(fileName) else logger.info( "created End:")

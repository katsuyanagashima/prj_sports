# pwd : /code
import os
import re
import shutil
import sys
import time
from logging import getLogger
from pathlib import Path

# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_autorace.consts import *

logger = getLogger('app_autorace')
base_trn = os.path.dirname(os.path.abspath(__file__))

try:
    from app_autorace import commons
except Exception as e:
    logger.error(f'commonsファイル読み込み失敗: {e}')

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
            logger.error(f'トランシステム該当レコードなし {e}')

    def run_trn_watchdoc(self):
        # watchdoc 呼び出し
        baseDatData = os.path.normpath(os.path.join(base_trn, DATDATA))
        targetDirDatData = os.path.expanduser(baseDatData)

        event_handler_schedule = WatchDocHandler(TARGET_FILE_DAT_RECORD)
        logger.info(f'targetDirDatData:  {targetDirDatData}' )
        self.observer_trn_watchdoc.schedule(event_handler_schedule, targetDirDatData, recursive=GO_RECURSIVELY)# recursive再帰的
        # 監視実行
        logger.info("watchdoc監視　Start" )
        self.observer_trn_watchdoc.start()

# PatternMatchingEventHandler の継承クラスを作成
class WatchDocHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(WatchDocHandler, self).__init__(patterns=patterns)

    # ファイル作成時のイベント
    def on_created(self, event):

        cmn = commons.Common()
        filepath = event.src_path
        logger.info(filepath)
        # ①～⑤　どれを呼び出すか判断する。
        datDataFileFlg=cmn.checkDatData(filepath)
        logger.info(f'datDataFileFlg:  {datDataFileFlg}')

        cmn.call_insert_or_update_Trn(datDataFileFlg, filepath)

        # 処理済みフォルダへ移動し、受信フォルダからは削除する機能
        try:
            cmn.call_check_isfile_move(datDataFileFlg, filepath)
        except Exception as e:
            logger.error(e)

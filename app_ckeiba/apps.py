# -*- coding: utf-8 -*-
import glob
import os
import pathlib
import shutil
import subprocess as sp
import sys
import threading
import time
from logging import getLogger
from pathlib import Path

from django.apps import AppConfig

from app_ckeiba import csv_start_manage as cm
from app_ckeiba.consts import *

logger = getLogger('app_ckeiba')
try:
    from app_ckeiba import commons
except Exception as e:
    logger.error(f'commonsファイル読み込み失敗 : {e}')

base =  os.path.dirname(os.path.abspath(__file__)) # app_ckeiba

class AppCkeibaConfig(AppConfig):
    name = 'app_ckeiba'

    run_already = False

    def make_csv_folder(self):
        """
        起動時にcsvフォルダが無ければ作成
        :return:
        """
        csv_dir = pathlib.Path(base) / pathlib.Path(CSVDATA)
        if not csv_dir.exists():
            os.makedirs(str(csv_dir))

        event_schedule_dir = pathlib.Path(base) / pathlib.Path(EVENTSCHEDULEDATDATA)
        if not event_schedule_dir.exists():
            os.makedirs(str(event_schedule_dir))

        processed_csv_dir = pathlib.Path(base) / pathlib.Path(PROCESSEDDATDATA)
        if not processed_csv_dir.exists():
            os.makedirs(str(processed_csv_dir))

    def make_lock_file(self):
        baseCsvData = os.path.normpath(os.path.join(base, CSVDATA))
        pidCsvData = os.path.normpath(os.path.join(baseCsvData, CSV_LOCK_FILE))

        # ロックファイルを削除する。
        if os.path.isfile(pidCsvData):
            os.remove(pidCsvData)

            return False

        with open(pidCsvData, mode='w') as f:
            logger.info(f'pid = [{str(os.getpid())}]')
            f.write(str(os.getpid()))

        return True

    def call_watch_doc(self):

        try:
            csvManage = cm.CsvManage()
            cmn = commons.Common()
            # 受信順に取り込む機能 次の登録処理で後ろからするため、更新日時の新しいものから取り込み。
            csvFileNameList = sorted(glob.glob('./app_ckeiba/CSVフォルダ/*'), key=lambda f: os.stat(f).st_mtime, reverse=True)

            logger.info(f'{CSVDATA}にある受信順{csvFileNameList}')

            for filepath in reversed(csvFileNameList):
                logger.info(filepath)
                # ①～⑤　どれを呼び出すか判断する。
                csvDataFileFlg=cmn.checkCsvData(filepath)
                logger.info(f'csvDataFileFlg:  {csvDataFileFlg}')

                cmn.call_insert_or_update_Trn(csvDataFileFlg, filepath)

                # 処理済みフォルダへ移動し、受信フォルダからは削除する機能
                try:
                    logger.info('ファイル移動処理開始')
                    shutil.move(filepath, './app_ckeiba/開催日割フォルダ/') if EVENTDATEDATA == csvDataFileFlg else shutil.move(filepath, './app_ckeiba/処理済みフォルダ/')
                    logger.info('ファイル移動処理終了')
                except Exception as e:
                    logger.error(e)
                    continue

            # watchdoc
            # 並列処理
            thread_start = threading.Thread(target=csvManage.run_trn_watchdoc())
            # thread_stop = threading.Thread(target=csvManage.stop_trn_watchdoc())
            thread_start.start()
            # thread_stop.start()

        except Exception as e:
            logger.error(e)

    # docker-compose up -d docker-compose stop 呼ばれる？
    def ready(self):
        try:
            logger.info('ready Start:')

            # 2回呼ばれる対策
            if AppCkeibaConfig.run_already:
                return
            AppCkeibaConfig.run_already = True

            # 固定長フォルダフォルダ作成
            self.make_csv_folder()

            # ロックファイル作成
            # if not self.make_lock_file():
            #     logger.info('ready End:')
            #     return

            self.call_watch_doc()
            logger.info('ready call_watch_doc End:')

        except Exception as e:
            logger.error(e)

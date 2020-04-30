# -*- coding: utf-8 -*-
import glob
import os
import pathlib
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
base =  os.path.dirname(os.path.abspath(__file__)) # app_ckeiba

class AppCkeibaConfig(AppConfig):
    name = 'app_ckeiba'

    run_already = False

    def make_csv_folder(self):
        """
        起動時にcsvフォルダが無ければ作成
        :return:
        """
        datdir = pathlib.Path(base) / pathlib.Path(CSVDATA)
        if not datdir.exists():
            os.makedirs(str(datdir))


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
        csvManage = cm.CsvManage()

        try:
            # 受信　/code
            #path = os.getcwd()
            #cmd = "ls"
            #proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
            #std_out, std_err = proc.communicate()
            # byte文字列で返るのでstrに
            #ls_file_name = std_out.decode('utf-8').rstrip().split('\n')
            #logger.info(ls_file_name)

            csvFileNameList = sorted(glob.glob('./app_ckeiba/CSVフォルダ/*'), key=lambda f: os.stat(f).st_mtime, reverse=False)

            logger.info(f'CSVDATA  {csvFileNameList}')

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
            if not self.make_lock_file():
                logger.info('ready End:')
                return

            self.call_watch_doc()
            logger.info('ready call_watch_doc End:')

        except Exception as e:
            logger.error(e)

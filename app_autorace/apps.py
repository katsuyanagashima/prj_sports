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

from app_autorace import dat_start_manage as dm
from app_autorace.consts import *

try:
    import codecs
except ImportError:
    codecs = None

logger = getLogger('command')
base =  os.path.dirname(os.path.abspath(__file__)) # app_autorace

class AppAutoraceConfig(AppConfig):
    name = 'app_autorace'

    run_already = False

    def make_dat_folder(self):
        """
        起動時に固定長フォルダフォルダが無ければ作成
        :return:
        """
        datdir = pathlib.Path(base) / pathlib.Path(DATDATA)
        if not datdir.exists():
            os.makedirs(str(datdir))

    def make_lock_file(self):
        baseDatData = os.path.normpath(os.path.join(base, DATDATA))
        pidDatData = os.path.normpath(os.path.join(baseDatData, DAD_LOCK_FILE))

        # ロックファイルを削除する。
        if os.path.isfile(pidDatData):
            os.remove(pidDatData)

            return False

        with open(pidDatData, mode='w') as f:
            logger.info(f'pid = [{str(os.getpid())}]')
            f.write(str(os.getpid()))

        return True

    def call_watch_doc(self):
        datManage = dm.DatManage()

        try:
            # 受信　/code
            #path = os.getcwd()
            #cmd = "ls"
            #proc= sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
            #std_out, std_err = proc.communicate()
            # byte文字列で返るのでstrに
            #ls_file_name = std_out.decode('utf-8').rstrip().split('\n')
            #logger.info(ls_file_name)

            datFileNameList = sorted(glob.glob('./app_autorace/固定長フォルダ/*.dat'), key=lambda f: os.stat(f).st_mtime, reverse=False)

            logger.info(DATDATA + str(datFileNameList))

            # watchdoc
            # 並列処理
            thread_start = threading.Thread(target=datManage.run_trn_watchdoc())
            # thread_stop = threading.Thread(target=datManage.stop_trn_watchdoc())
            thread_start.start()
            # thread_stop.start()

        except Exception as e:
            logger.error(e)

    # docker-compose up -d docker-compose stop 呼ばれる？
    def ready(self):
        try:
            logger.info('ready Start:')

            # 2回呼ばれる対策
            if AppAutoraceConfig.run_already:
                return
            AppAutoraceConfig.run_already = True

            # 固定長フォルダフォルダ作成
            self.make_dat_folder()

            # ロックファイル作成
            if not self.make_lock_file():
                logger.info('ready End:')
                return

            self.call_watch_doc()
            logger.info('ready call_watch_doc End:')

        except Exception as e:
            logger.error(e)

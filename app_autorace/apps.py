# -*- coding: utf-8 -*-
import datetime
import glob
import os
import pathlib
import shutil
import sys
import threading
import time
from logging import getLogger
from pathlib import Path

from django.apps import AppConfig

from app_autorace import dat_start_manage as dm
from app_autorace.consts import *

logger = getLogger('app_autorace')
try:
    from app_autorace import commons
except Exception as e:
    logger.error(f'commonsファイル読み込み失敗 : {e}')

base =  os.path.dirname(os.path.abspath(__file__)) # app_autorace

class AppAutoraceConfig(AppConfig):
    name = 'app_autorace'

    run_already = False

    def make_dat_folder(self):
        """
        起動時に固定長フォルダフォルダ,スケジュールフォルダ,処理済みフォルダが無ければ作成
        :return:
        """
        datdir = pathlib.Path(base) / pathlib.Path(DATDATA)
        if not datdir.exists():
            os.makedirs(str(datdir))

        schedule_dir = pathlib.Path(base) / pathlib.Path(SCHEDULEDATDATA)
        if not schedule_dir.exists():
            os.makedirs(str(schedule_dir))

        processed_dat_dir = pathlib.Path(base) / pathlib.Path(PROCESSEDDATDATA)
        if not processed_dat_dir.exists():
            os.makedirs(str(processed_dat_dir))

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

        try:
            datManage = dm.DatManage()
            cmn = commons.Common()
            # 受信順に取り込む機能 次の登録処理で後ろからするため、更新日時の新しいものから取り込み。
            datFileNameList = sorted(glob.glob('./app_autorace/固定長フォルダ/*.dat'), key=lambda f: os.stat(f).st_mtime, reverse=True)

            logger.info(f'{DATDATA}にある受信順{datFileNameList}')

            for filepath in reversed(datFileNameList):
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
                    continue

            # watchdoc
            # 並列処理
            thread_start = threading.Thread(target=datManage.run_trn_watchdoc())
            # thread_stop = threading.Thread(target=datManage.stop_trn_watchdoc())
            thread_start.start()
            # thread_stop.start()

        except Exception as e:
            logger.error(e)


    def call_db_conn(self):

        conn = False
        while not conn:
            time.sleep(10)
            try:
                from app_autorace.models import Tran_Systemstatus
                Tran_Systemstatus.objects.count()
                logger.info('DB接続可:')
                conn = True
            except Exception as e:
                logger.info(f'DB接続不可 prj_sports.dbコンテナを起動する必要があります。: {e}')


    # docker-compose up -d docker-compose stop 呼ばれる？
    def ready(self):
        try:
            logger.info('ready Start:')

            # 2回呼ばれる対策
            if AppAutoraceConfig.run_already:
                return
            AppAutoraceConfig.run_already = True

            # DB接続確認
            logger.info('DB接続確認 Start:')
            self.call_db_conn()
            logger.info('DB接続確認 End:')

            # 固定長フォルダフォルダ作成
            self.make_dat_folder()

            # ロックファイル作成
            # if not self.make_lock_file():
            #     logger.info('ready End:')
            #     return

            self.call_watch_doc()
            logger.info('ready call_watch_doc End:')

        except Exception as e:
            logger.error(e)

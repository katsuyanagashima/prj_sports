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
from watchdog.observers.polling import PollingObserver
sys.path.append("/code/app_autorace/management/commands/")
import trn_schedule, trn_program, trn_result, trn_top_30_prize, trn_outside_track
from app_autorace.models import *
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max
sys.path.append("/code/app_autorace/")
from consts import *

logger = getLogger('command')

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
        if SCHEDULEDATA in filepath:   
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base, SCHEDULEDATA, filename_schedule_record))
            
            logger.info( "created Start:" + name)
            # ファイル読み込み
            schedule = trn_schedule.Schedule()
                
            logger.error("DB insert_or_update_Trn_Schedule: 失敗：ファイル名" + name) if not schedule.insert_or_update_Trn_Schedule(name) else logger.info( "created End:")

        if RESULTDATA in filepath:   
            filename_result_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base, RESULTDATA, filename_result_record))

            logger.info( "created Start:" + name)
            # ファイル読み込み
            result = trn_result.Result()
                
            logger.error("DB insert_or_update_Trn_Result: 失敗：ファイル名" + name) if not result.insert_or_update_Trn_Result(name) else logger.info( "created End:")

        if PROGRAMDATA in filepath:   
            filename_program_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base, PROGRAMDATA, filename_program_record))

            logger.info( "created Start:" + name)
            # ファイル読み込み
            program = trn_program.Program()
                
            logger.error("DB insert_or_update_Trn_Program: 失敗：ファイル名" + name) if not program.insert_or_update_Trn_Program(name) else logger.info( "created End:")

        if TOP30PRIZEDATA in filepath:   
            filename_top30prize_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base, TOP30PRIZEDATA, filename_top30prize_record))

            logger.info( "created Start:" + name)
            # ファイル読み込み
            top_30_prize = trn_top_30_prize.Top_30_prize()
                
            logger.error("DB insert_or_update_Trn_Top_30_Prize: 失敗：ファイル名" + name) if not top_30_prize.insert_or_update_Trn_Top_30_Prize(name) else logger.info( "created End:")

        if OUTSIDETRACKDATA in filepath:   
            filename_outside_track_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            name = os.path.normpath(os.path.join(base, OUTSIDETRACKDATA, filename_outside_track_record))

            logger.info( "created Start:" + name)
            # ファイル読み込み
            outside_track = trn_outside_track.Outside_track()

            logger.error("DB insert_or_update_Trn_Outside_track: 失敗：ファイル名" + name) if not outside_track.insert_or_update_Trn_Outside_track(name) else logger.info( "created End:")

    # ファイル変更時のイベント
    def on_modified(self, event):
        logger.info( "changed:")

    # ファイル削除時のイベント
    def on_deleted(self, event):
        logger.info( "deleted:")

    # ファイル移動時のイベント
    def on_moved(self, event):
        logger.info( "moved:")

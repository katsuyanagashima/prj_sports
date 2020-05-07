# pwd : /code
import os
import re
import sys
import time
from logging import getLogger
from pathlib import Path

from app_autorace.consts import *

logger = getLogger('app_autorace')
try:
    from app_autorace import trn_schedule, trn_program, trn_result, trn_top_30_prize, trn_outside_track
except Exception as e:
    logger.error(f'トランファイル読み込み失敗: {e}')

base_trn = os.path.dirname(os.path.abspath(__file__))


class Common():
    # 正規表現で半角ブランク削除
    def chkBlank(self, chkline):

        if (not re.sub('\\s+', '', chkline)):
            return False
        return True

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

        logger.warning(f'該当しないファイル{filepath}')
        return None

    # 他からもcallできるようにする。
    def call_insert_or_update_Trn(self, datDataFileFlg, filepath):

        if SCHEDULE == datDataFileFlg:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_schedule_record))

            logger.info( f'created Start:  {fileName}')
            # ファイル読み込み
            schedule = trn_schedule.Schedule()

            logger.error(f'DB insert_or_update_Trn_Schedule: 失敗：ファイル名 {fileName}') if not schedule.insert_or_update_Trn_Schedule(fileName) else logger.info( "created End:")

        if PROGRAM == datDataFileFlg:
            filename_program_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_program_record))

            logger.info( f'created Start: {fileName}')
            # ファイル読み込み
            program = trn_program.Program()

            logger.error(f'DB insert_or_update_Trn_Program: 失敗：ファイル名 {fileName}') if not program.insert_or_update_Trn_Program(fileName) else logger.info( "created End:")

        if RESULT == datDataFileFlg:
            filename_result_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_result_record))

            logger.info( f'created Start:  {fileName}')
            # ファイル読み込み
            result = trn_result.Result()

            logger.error(f'DB insert_or_update_Trn_Result: 失敗：ファイル名 {fileName}') if not result.insert_or_update_Trn_Result(fileName) else logger.info( "created End:")

        if TOP30PRIZE == datDataFileFlg:
            filename_top30prize_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_top30prize_record))

            logger.info( f'created Start:  {fileName}')
            # ファイル読み込み
            top_30_prize = trn_top_30_prize.Top_30_prize()

            logger.error(f'DB insert_or_update_Trn_Top_30_Prize: 失敗：ファイル名 {fileName}') if not top_30_prize.insert_or_update_Trn_Top_30_Prize(fileName) else logger.info( "created End:")

        if OUTSIDETRACK == datDataFileFlg:
            filename_outside_track_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, DATDATA, filename_outside_track_record))

            logger.info( f'created Start:  {fileName}')
            # ファイル読み込み
            outside_track = trn_outside_track.Outside_track()

            logger.error(f'DB insert_or_update_Trn_Outside_track: 失敗：ファイル名 {fileName}') if not outside_track.insert_or_update_Trn_Outside_track(fileName) else logger.info( "created End:")

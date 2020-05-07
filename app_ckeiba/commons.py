# pwd : /code
import os
import re
import sys
import time
from logging import getLogger
from pathlib import Path

from app_ckeiba.consts import *

logger = getLogger('app_ckeiba')
try:
    from app_ckeiba import trn_BA7, trn_SEI
except Exception as e:
    logger.error(f'トランファイル読み込み失敗: {e}')

base_trn = os.path.dirname(os.path.abspath(__file__))


class Common():
    # 正規表現で半角ブランク削除
    def chkBlank(self, chkline):

        if (not re.sub('\\s+', '', chkline)):
            return False
        return True

    def checkCsvData(self, filepath):
        if re.search(EVENTDATEDATA, filepath):
            return EVENTDATEDATA

        if re.search(SIMPLERACERESULTSDATA, filepath):
            return SIMPLERACERESULTSDATA

        logger.warning(f'該当しないファイル{filepath}')
        return None

    # 他からもcallできるようにする。
    def call_insert_or_update_Trn(self, csvDataFileFlg, filepath):

        # 開催日割データ
        if EVENTDATEDATA == csvDataFileFlg:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, CSVDATA, filename_schedule_record))

            logger.info( f'created Start :{fileName}')
            # ファイル読み込み
            trn_Ba7 = trn_BA7.Ba7()

            logger.error(f'DB insert_or_update_Trn_Ba7: 失敗：ファイル名  {fileName}') if not trn_Ba7.insert_or_update_Trn_Ba7(fileName) else logger.info( "created End:")

        # 簡易競走成績データ
        if SIMPLERACERESULTSDATA == csvDataFileFlg:
            filename_schedule_record = os.path.basename(filepath)
            # 監視元のフォルダパスを生成
            fileName = os.path.normpath(os.path.join(base_trn, CSVDATA, filename_schedule_record))

            logger.info( f'created Start :{fileName}')
            # ファイル読み込み
            trn_sei = trn_SEI.Sei()

            logger.error(f'DB insert_or_update_Trn_Sei: 失敗：ファイル名  {fileName}') if not trn_sei.insert_or_update_Trn_Sei(fileName) else logger.info( "created End:")

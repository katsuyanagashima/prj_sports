import csv
import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import sys
import time
from logging import getLogger
from pathlib import Path

import chardet
from django.db import transaction
from django.db.models import Max
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_ckeiba.consts import *

#ダミーコメント

logger = getLogger('app_ckeiba')

class Su1():

    def chk_master(self, line, Mst_Jou, Mst_Accident_type, Mst_Accident_reason):

        if not Mst_Jou.objects.filter(Jou_code=line[2]):
            logger.info(f'競馬場マスタ にJou_code :{line[2]} ないので登録します。')
            jou = Mst_Jou(Jou_code=line[2],Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line[2]}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

        if not Mst_Accident_type.objects.filter(Accident_type_code=line[9]):
            logger.info(f'事故種類マスタ にAccident_type_code :{line[9]} ないので登録します。')
            accident_type = Mst_Accident_type(Accident_type_code=line[9], Accident_type_name=ACCIDENT_TYPE_NAME)
            accident_type.save()
            logger.warning(f'事故種類マスタ にAccident_type_code :{line[9]},Accident_type_name :{ACCIDENT_TYPE_NAME}を登録しました。')

        if not Mst_Accident_reason.objects.filter(Accident_reason_code=line[11]):
            logger.info(f'事故理由マスタ にAccident_reason_code :{line[11]} ないので登録します。')
            accident_reason = Mst_Accident_reason(Accident_reason_code=line[11], Accident_reason_name=ACCIDENT_REASON_NAME)
            accident_reason.save()
            logger.warning(f'事故理由マスタ にAccident_reason_code :{line[11]},Accident_reason_name :{ACCIDENT_REASON_NAME}を登録しました。')

    #取消除外_SU1
    def CSV_Trn_Cancellation_exclusion_SU1(self, fileName, Trn_Cancellation_exclusion_SU1, Mst_Jou, Mst_Accident_type, Mst_Accident_reason):

        with open(fileName, encoding='shift_jis') as f:

            reader = csv.reader(f, delimiter=',')

            # bulk createを使った場合
            '''
            Trn_Cancellation_exclusion_SU1.objects.bulk_create([Trn_Cancellation_exclusion_SU1(
                共通　カラム設定
            ) for line in reader])
            '''

            # forを使った場合
            for line in reader:

                # マスターチェック
                logger.info(f'マスターチェック: {Mst_Jou} {Mst_Accident_type} {Mst_Accident_reason}')
                self.chk_master(line, Mst_Jou, Mst_Night_race_class)

                trn_cancellation_exclusion_su1 = Trn_Cancellation_exclusion_SU1(
                    Data_ID = line[0],
                    Race_date = line[1],
                    Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
                    Held_times = line[3],
                    Race_No = line[4],
                    Horse_name = = line[5],
                    Horse_No = line[6],
                    Trainer_license_No = line[7],
                    Trainer_name = line[8],
                    Accident_code = Mst_Accident_type.objects.get(Accident_type_code=line[9]),
                    Accident_name = line[10],
                    Accident_reason_code = Mst_Accident_reason.objects.get(Accident_reason_code=line[11]),
                    Accident_reason_name = line[12],
                )
                trn_cancellation_exclusion_su1.save()

    def insert_or_update_Trn_Cancellation_exclusion_SU1(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_ckeiba.models import Trn_Cancellation_exclusion_SU1, Mst_Jou, Mst_Accident_type, Mst_Accident_reason

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Trn_Cancellation_exclusion_SU1 Start')
            self.CSV_Trn_Cancellation_exclusion_SU1(fileName, Trn_Cancellation_exclusion_SU1, Mst_Jou, Mst_Accident_type, Mst_Accident_reason)
            logger.info( "内容:insert_Trn_Cancellation_exclusion_SU1 Start End")

            return NORMAL

        except FileNotFoundError as e:
            logger.error(e)
            return ABNORMAL
        except UnboundLocalError as e:
            logger.error(e)
            return ABNORMAL
        except ValueError as e:
            logger.error(e)
            return ABNORMAL
        except Exception as e:
            logger.error(e)
            return ABNORMAL

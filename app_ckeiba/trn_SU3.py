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

logger = getLogger('app_ckeiba')

class Su3():

    def chk_master(self, line, Mst_Jou, Mst_Belonging, Mst_Jockey_changed_reason):

        if not Mst_Jou.objects.filter(Jou_code=line[2]):
            logger.info(f'競馬場マスタ にJou_code :{line[2]} ないので登録します。')
            jou = Mst_Jou(Jou_code=line[2],Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line[2]}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

        if not Mst_Belonging.objects.filter(Belonging_code=line[16]):
            logger.info(f'所属場マスタ にBelonging_code :{line[16]} ないので登録します。')
            belonging = Mst_Belonging(Belonging_code=line[16],Belonging=BELONGING,Belonging_1char=BELONGING_1CHAR)
            belonging.save()
            logger.warning(f'所属場マスタ にBelonging_code {line[16]}：Belonging {BELONGING}:Belonging_1char {BELONGING_1CHAR}を登録しました。')

        if not Mst_Jockey_changed_reason.objects.filter(Jockey_changed_reason_code=line[23]):
            logger.info(f'騎手変更理由マスタ にJockey_changed_reason_code :{line[23]} ないので登録します。')
            jockey_changed_reason = Mst_Jockey_changed_reason(Jockey_changed_reason_code=line[23], Jockey_changed_reason_name=JOCKEY_CHANGED_REASON_NAME)
            jockey_changed_reason.save()
            logger.warning(f'騎手変更理由マスタ にJockey_changed_reason_code :{line[23]},Jockey_changed_reason_name :{JOCKEY_CHANGED_REASON_NAME}を登録しました。')

        if not Mst_Belonging.objects.filter(Belonging_code=line[27]):
            logger.info(f'所属場マスタ にBelonging_code :{line[27]} ないので登録します。')
            belonging = Mst_Belonging(Belonging_code=line[27],Belonging=BELONGING,Belonging_1char=BELONGING_1CHAR)
            belonging.save()
            logger.warning(f'所属場マスタ にBelonging_code {line[27]}：Belonging {BELONGING}:Belonging_1char {BELONGING_1CHAR}を登録しました。')

        if not Mst_Jockey_changed_reason.objects.filter(Jockey_changed_reason_code=line[34]):
            logger.info(f'騎手変更理由マスタ にJockey_changed_reason_code :{line[34]} ないので登録します。')
            jockey_changed_reason = Mst_Jockey_changed_reason(Jockey_changed_reason_code=line[34], Jockey_changed_reason_name=JOCKEY_CHANGED_REASON_NAME)
            jockey_changed_reason.save()
            logger.warning(f'騎手変更理由マスタ にJockey_changed_reason_code :{line[34]},Jockey_changed_reason_name :{JOCKEY_CHANGED_REASON_NAME}を登録しました。')

        if not Mst_Belonging.objects.filter(Belonging_code=line[38]):
            logger.info(f'所属場マスタ にBelonging_code :{line[38]} ないので登録します。')
            belonging = Mst_Belonging(Belonging_code=line[38],Belonging=BELONGING,Belonging_1char=BELONGING_1CHAR)
            belonging.save()
            logger.warning(f'所属場マスタ にBelonging_code {line[38]}：Belonging {BELONGING}:Belonging_1char {BELONGING_1CHAR}を登録しました。')

    #騎乗変更_SU3
    def CSV_Trn_Change_riding_SU3(self, fileName, Trn_Change_riding_SU3, Mst_Belonging, Mst_Jockey_changed_reason):

        with open(fileName, encoding='shift_jis') as f:

            reader = csv.reader(f, delimiter=',')

            # bulk createを使った場合
            '''
            Trn_Change_riding_SU3.objects.bulk_create([Trn_Change_riding_SU3(
                共通　カラム設定
            ) for line in reader])
            '''

            # forを使った場合
            for line in reader:

                # マスターチェック
                logger.info(f'マスターチェック: {Mst_Jou} {Mst_Belonging} {Mst_Jockey_changed_reason}')
                self.chk_master(line, Mst_Jou, Mst_Belonging, Mst_Jockey_changed_reason)

                trn_change_riding_su3 = Trn_Change_riding_SU3(
                    Data_ID = line[0],
                    Race_date = line[1],
                    Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
                    Held_times = line[3],
                    Race_No = line[4],
                    Horse_name = line[5],
                    Horse_No = line[6],
                    Weight = line[7],
                    Carry_weight = line[8],
                    Jockey_license_No = line[9],
                    Jockey_name = line[10],
                    Jockey_shortened = line[11],
                    Weight_handicap = line[12],
                    Weight_handicap_symbol = line[13],
                    Jockey_belong_stable = line[14],
                    Jockey_invitation_code = line[15],
                    Jockey_belonging_code = Mst_Belonging.objects.get(Belonging_code=line[16]),
                    Jockey_location_code = line[17],
                    Jockey_license_No_1 = line[18],
                    Jockey_name_1 = line[19],
                    Jockey_shortened_1 = line[20],
                    Weight_handicap_1 = line[21],
                    Weight_handicap_symbol_1 = line[22],
                    Jockey_changed_reason_code_1 = Mst_Jockey_changed_reason.get(Jockey_changed_reason_code=line[23]),
                    Jockey_changed_reason_name_1 = line[24],
                    Jockey_belong_stable_1 = line[25],
                    Jockey_invitation_code_1 = line[26],
                    Jockey_belonging_code_1 = Mst_Belonging.objects.get(Belonging_code=line[27]),
                    Jockey_location_code_1 = line[28],
                    Jockey_license_No_2 = line[29],
                    Jockey_name_2 = line[30],
                    Jockey_shortened_2 = line[31],
                    Weight_handicap_2 = line[32],
                    Weight_handicap_symbol_2 = line[33],
                    Jockey_changed_reason_code_2 = Mst_Jockey_changed_reason.get(Jockey_changed_reason_code=line[34]),
                    Jockey_changed_reason_name_2 = line[35],
                    Jockey_belong_stable_2 = line[36],
                    Jockey_invitation_code_2 = line[37],
                    Jockey_belonging_code_2 = Mst_Belonging.objects.get(Belonging_code=line[38]),
                    Jockey_location_code_2 = line[39],
                )
                trn_change_riding_su3.save()

    def insert_or_update_Trn_Change_riding_SU3(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_ckeiba.models import Trn_Change_riding_SU3, Mst_Jou, Mst_Belonging, Mst_Jockey_changed_reason

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Trn_Change_riding_SU3 Start')
            self.CSV_Trn_Change_riding_SU3(fileName, Trn_Change_riding_SU3, Mst_Jou, Mst_Belonging, Mst_Jockey_changed_reason)
            logger.info( "内容:insert_Trn_Change_riding_SU3 End")

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

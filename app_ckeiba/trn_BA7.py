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

class Ba7():

    def chk_master(self, line, Mst_Jou, Mst_Night_race_class):

        if not Mst_Jou.objects.filter(Jou_code=line[5]):
            logger.info(f'競馬場マスタ にJou_code :{line[5]} ないので登録します。')
            jou = Mst_Jou(Jou_code=line[5],Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line[5]}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

        if not Mst_Night_race_class.objects.filter(Night_race_code=line[7]):
            logger.info(f'ナイター区分マスタ にNight_race_code :{line[7]} ないので登録します。')
            night_race_class = Mst_Night_race_class(Night_race_code=line[7], Night_race_name=NIGHT_RACE_NAME)
            night_race_class.save()
            logger.warning(f'ナイター区分マスタ にNight_race_code :{line[7]},Night_race_name :{NIGHT_RACE_NAME}を登録しました。')

    #開催日割_BA7
    def CSV_Schedule_BA7(self, fileName, Schedule_BA7, Mst_Jou, Mst_Night_race_class):

        with open(fileName, encoding='shift_jis') as f:

            reader = csv.reader(f, delimiter=',')

            # bulk createを使った場合
            '''
            Schedule_BA7.objects.bulk_create([Schedule_BA7(
                共通　カラム設定
            ) for line in reader])
            '''

            # forを使った場合
            for line in reader:

                # マスターチェック
                logger.info(f'マスターチェック: {Mst_Jou} {Mst_Night_race_class}')
                self.chk_master(line, Mst_Jou, Mst_Night_race_class)

                schedule_ba7 = Schedule_BA7(
                    Data_ID = line[0],
                    held_year = line[1],
                    Organizer_times = line[2],
                    Track_times = line[3],
                    Organizer_code = line[4],
                    Track_code = Mst_Jou.objects.get(Jou_code=line[5]),
                    Held_code = line[6],
                    Night_game_code = Mst_Night_race_class.objects.get(Night_race_code=line[7]),
                    Dates = line[8],
                    Date_1 = line[9],
                    Day_code_1 = line[10],
                    Races_1 = line[11],
                    Postpone_date_1_1 = line[12],
                    Postpone_day_code_1_1 = line[13],
                    Postpone_start_1_1 = line[14],
                    Postpone_date_1_2 = line[15],
                    Postpone_day_code_1_2 = line[16],
                    Postpone_start_1_2 = line[17],
                    Date_2 = line[18],
                    Day_code_2 = line[19],
                    Races_2 = line[20],
                    Postpone_date_2_1 = line[21],
                    Postpone_day_code_2_1 = line[22],
                    Postpone_start_2_1 = line[23],
                    Postpone_date_2_2 = line[24],
                    Postpone_day_code_2_2 = line[25],
                    Postpone_start_2_2 = line[26],
                    Date_3 = line[27],
                    Day_code_3 = line[28],
                    Races_3 = line[29],
                    Postpone_date_3_1 = line[30],
                    Postpone_day_code_3_1 = line[31],
                    Postpone_start_3_1 = line[32],
                    Postpone_date_3_2 = line[33],
                    Postpone_day_code_3_2 = line[34],
                    Postpone_start_3_2 = line[35],
                    Date_4 = line[36],
                    Day_code_4 = line[37],
                    Races_4 = line[38],
                    Postpone_date_4_1 = line[39],
                    Postpone_day_code_4_1 = line[40],
                    Postpone_start_4_1 = line[41],
                    Postpone_date_4_2 = line[42],
                    Postpone_day_code_4_2 = line[43],
                    Postpone_start_4_2 = line[44],
                    Date_5 = line[45],
                    Day_code_5 = line[46],
                    Races_5 = line[47],
                    Postpone_date_5_1 = line[48],
                    Postpone_day_code_5_1 = line[49],
                    Postpone_start_5_1 = line[50],
                    Postpone_date_5_2 = line[51],
                    Postpone_day_code_5_2 = line[52],
                    Postpone_start_5_2 = line[53],
                    Date_6 = line[54],
                    Day_code_6 = line[55],
                    Races_6 = line[56],
                    Postpone_date_6_1 = line[57],
                    Postpone_day_code_6_1 = line[58],
                    Postpone_start_6_1 = line[59],
                    Postpone_date_6_2 = line[60],
                    Postpone_day_code_6_2 = line[61],
                    Postpone_start_6_2 = line[62],
                )
                schedule_ba7.save()

    def insert_or_update_Trn_Ba7(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_ckeiba.models import Schedule_BA7, Mst_Jou, Mst_Night_race_class

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Schedule_BA7 Start')
            self.CSV_Schedule_BA7(fileName, Schedule_BA7, Mst_Jou, Mst_Night_race_class)
            logger.info( "内容:insert_Schedule_BA7 End")

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

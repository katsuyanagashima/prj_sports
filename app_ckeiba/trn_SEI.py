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

class Sei():

    def chk_master(self, line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list):

        if not Trn_Running_list_A_SUA_Mst_list[0].objects.filter(Jou_code=line[4]):
            logger.info(f'競馬場マスタ にJou_code :{line[4]} ないので登録します。')
            jou = Trn_Running_list_A_SUA_Mst_list[0](Jou_code=line[4],Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line[4]}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

        if not Trn_Running_list_A_SUA_Mst_list[6].objects.filter(Night_race_code=line[7]):
            logger.info(f'ナイター区分マスタ にNight_race_code :{line[7]} ないので登録します。')
            night_race_class = Trn_Running_list_A_SUA_Mst_list[6](Night_race_code=line[7], Night_race_name=NIGHT_RACE_NAME)
            night_race_class.save()
            logger.warning(f'ナイター区分マスタ にNight_race_code :{line[7]},Night_race_name :{NIGHT_RACE_NAME}を登録しました。')

    def run_sua(self, line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list):
        # マスターチェック-
        logger.info(f'マスターチェック : {Trn_Running_list_A_SUA_Mst_list}')
        self.chk_master(line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list)

        trn_running_list_a_sua = Trn_Running_list_A_SUA(
            Data_ID = line[0],
            Organizer_times = line[1],
            Track_times = line[2],
            Race_date = line[3],
            Track_code = Trn_Running_list_A_SUA_Mst_list[0].objects.get(Jou_code=line[4]),
            Track_name = line[5],
            Track_name_shortened = line[6],
            Organizer_code = line[7],
            Organizer_name = line[8],
            Held_day = line[9],
            Held_times = line[10],
            Race_No = line[11],
            Win_sale = line[12],
            Place_sale = line[13],
            Bracketquinella_sale = line[14],
            bracketexacta_sale = line[15],
            Quinella_sale = line[16],
            Exacta_sale = line[17],
            Race_type_code = line[18],
            Race_type_name = line[19],
            Breed_age_code = line[20],
            Breed_age_name = line[21],
            Weight_code = line[22],
            Weight_name = line[23],
            Male_weight = line[24],
            Female_weight = line[25],
            Race_times = line[26],
            Race_name = line[27],
            Additional_name = line[28],
            JRA_exchanges_code = line[29],
            Race_code = line[30],
            Certified_race_code = line[31],
            Grade_code = line[32],
            Grade_name = line[33],
            Night_race_code = line[34],
            Prize_money_1 = line[35],
            Prize_money_2 = line[36],
            Prize_money_3 = line[37],
            Prize_money_4 = line[38],
            Main_prize_5 = line[39],
            Additional_prize_1 = line[40],
            Additional_prize_2 = line[41],
            Additional_prize_3 = line[42],
            Additional_prize_4 = line[43],
            Additional_prize_5 = line[44],
            Supplementary_prize_1 = line[45],
            Supplementary_prize_2 = line[46],
            Supplementary_prize_3 = line[47],
            Supplementary_prize_4 = line[48],
            Supplementary_prize_5 = line[49],
            Supplementary_prize_6 = line[50],
            Supplementary_prize_7 = line[51],
            Supplementary_prize_8 = line[52],
            Supplementary_prize_9 = line[53],
            Supplementary_prize_10 = line[54],
            Supplementary_prize_11 = line[55],
            Supplementary_prize_12 = line[56],
            Supplementary_Award_13 = line[57],
            Supplementary_prize_14 = line[58],
            Supplementary_prize_15 = line[59],
            Organizer_total_races = line[60],
            Scheduled_participation = line[61],
            Race_qualification_1 = line[62],
            Race_qualification_2 = line[63],
            Race_qualification_3 = line[64],
            Race_rank_1 = line[65],
            Race_rank_2 = line[66],
            Race_group_1 = line[67],
            Race_group_2 = line[68],
            Prize_amount_1 = line[69],
            Under_1 = line[70],
            Prize_amount_2 = line[71],
            Under_2 = line[72],
            Saddling_enclosure_time = line[73],
            Start_time = line[74],
            Race_Distance = line[75],
            Turf_dirt_code = line[76],
            Turf_Dart_name = line[77],
            Inner_outer_code = line[78],
            Inner_outer_name = line[79],
            CW_or_CCW_code = line[80],
            Weather_code = line[81],
            Weather_name = line[82],
            Track_condition_code = line[83],
            Track_condition_name = line[84],
            Track_moisture = line[85],
            Night_lighting = line[86],
            Record_time = line[87],
            Record_era = line[88],
            Record_race_date_JP = line[89],
            Horse_name = line[90],
            Weight = line[91],
            Jockey_name = line[92],
        )
        trn_running_list_a_sua.save()


    def chk_ID(self, line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list):

        if RACECARD == line[0]:
            # self.run_sua(line, Trn_Running_list_A_SUA,Trn_Running_list_A_SUA_Mst_list)
            pass

        elif ARRIVALTIME == line[0]:
            pass

        elif BETTINGHANDLE == line[0]:
            pass

        elif BRACKETQUINELLA == line[0]:
            pass

        elif TIERCES == line[0]:
            pass

        elif TIERCE == line[0]:
            pass

        elif ADDITIONALDOCUMENT == line[0]:
            pass

        else:
            # 該当しない
            pass

    #簡易競走成績データ_SEI
    def CSV_Schedule_SEI(self, fileName, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list):

        with open(fileName, encoding='shift_jis') as f:

            reader = csv.reader(f, delimiter=',')

            # bulk createを使った場合
            '''
            Trn_Running_list_A_SUA.objects.bulk_create([Trn_Running_list_A_SUA(
                共通　カラム設定
            ) for line in reader])
            '''
            # forを使った場合
            for line in reader:

                # 振り分け
                self.chk_ID(line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list)

    def insert_or_update_Trn_Sei(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            # 出馬表Ａ_SUA:Trn_Running_list_A_SUA
            from app_ckeiba.models import Trn_Running_list_A_SUA, Mst_Jou, Mst_Race_type, Mst_Breed_age, Mst_Handicap, Mst_JRA_exchanges, Mst_Grade, Mst_Night_race_class, Mst_Turf_dirt_class, Mst_Course_class, Mst_Clockwise_class, Mst_Weather, Mst_Track_condition

            Trn_Running_list_A_SUA_Mst_list = [Mst_Jou, Mst_Race_type, Mst_Breed_age, Mst_Handicap, Mst_JRA_exchanges, Mst_Grade, Mst_Night_race_class, Mst_Turf_dirt_class, Mst_Course_class, Mst_Clockwise_class, Mst_Weather, Mst_Track_condition]

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Schedule_SEI Start')
            self.CSV_Schedule_SEI(fileName, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list)
            logger.info( "内容:insert_Schedule_SEI End")

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

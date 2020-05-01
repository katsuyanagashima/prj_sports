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

    def chk_master_Mst_Jou(self, line, Master):
        logger.info('競馬場マスタデータ有無確認処理')
        if not Master.objects.filter(Jou_code=line):
            logger.info(f'競馬場マスタ にJou_code :{line} ないので登録します。')
            mst_jou = Master(Jou_code=line,Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            mst_jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

    def chk_master_Mst_Race_type(self, line, Master):
        logger.info('競走種類マスタデータ有無確認処理')
        if not Master.objects.filter(Race_type_code=line):
            logger.info(f'競走種類マスタ Race_type_code :{line} ないので登録します。')
            mst_race_type = Master(Race_type_code=line, Race_type_name=RACE_TYPE_NAME, Race_type_deliverytype=RACE_TYPE_DELIVERYTYPE )
            mst_race_type.save()
            logger.warning(f'競走種類マスタ にRace_type_code: {line}, Race_type_name: {RACE_TYPE_NAME}, Race_type_deliverytype: {RACE_TYPE_DELIVERYTYPE}を登録しました。')

    def chk_master_Mst_Breed_age(self, line, Master):
        logger.info('品種年齢区分マスタデータ有無確認処理')
        if not Master.objects.filter(Breed_age_code=line):
            logger.info(f'品種年齢区分マスタ Breed_age_code :{line} ないので登録します。')
            mst_breed_age = Master(Breed_age_code=line, Name_for_race_type=NAME_FOR_RACE_TYPE )
            mst_breed_age.save()
            logger.warning(f'品種年齢区分マスタ にRaceBreed_age_code_type_code: {line}, Name_for_race_type: {NAME_FOR_RACE_TYPE} を登録しました。')

    def chk_master_Mst_Handicap(self, line, Master):
        logger.info('負担重量区分マスタデータ有無確認処理')
        if not Master.objects.filter(Handicap_code=line):
            logger.info(f'負担重量区分マスタ Race_type_code :{line} ないので登録します。')
            mst_handicap = Master(Handicap_code=line, Handicap_name=HANDICAP_NAME )
            mst_handicap.save()
            logger.warning(f'競走種類負担重量区分マスタ Handicap_code: {line}, Handicap_name: {HANDICAP_NAME}を登録しました。')

    def chk_master_Mst_JRA_exchanges(self, line, Master):
        logger.info('中央交流区分マスタデータ有無確認処理')
        if not Master.objects.filter(JRA_exchanges_code=line):
            logger.info(f'中央交流区分マスタ JRA_exchanges_code :{line} ないので登録します。')
            mst_jra_exchanges = Master(JRA_exchanges_code=line, JRA_exchanges=JRA_EXCHANGES )
            mst_jra_exchanges.save()
            logger.warning(f'中央交流区分マスタ JRA_exchanges_code: {line}, JRA_exchanges: {JRA_EXCHANGES}を登録しました。')

    def chk_master_Mst_Grade(self, line, Master):
        logger.info('グレードマスタデータ有無確認処理')
        if not Master.objects.filter(Grade_code=line):
            logger.info(f'競走種類マスタ Grade_code :{line} ないので登録します。')
            mst_grade = Master(Grade_code=line, Grade_name=GRADE_NAME )
            mst_grade.save()
            logger.warning(f'競走種類マスタ にGrade_code: {line}, Grade_name: {GRADE_NAME}を登録しました。')

    def chk_master_Mst_Night_race_class(self, line, Master):
        logger.info('ナイター区分マスタデータ有無確認処理')
        if not Master.objects.filter(Night_race_code=line):
            logger.info(f'ナイター区分マスタ にNight_race_code :{line} ないので登録します。')
            night_race_class = Master(Night_race_code=line, Night_race_name=NIGHT_RACE_NAME)
            night_race_class.save()
            logger.warning(f'ナイター区分マスタ にNight_race_code :{line},Night_race_name :{NIGHT_RACE_NAME}を登録しました。')

    def chk_master_Mst_Turf_dirt_class(self, line, Master):
        logger.info('芝・ダート区分マスタデータ有無確認処理')
        if not Master.objects.filter(Turf_dirt_code=line):
            logger.info(f'芝・ダート区分マスタ Turf_dirt_code :{line} ないので登録します。')
            mst_turf_dirt_class = Master(Turf_dirt_code=line, Turf_dirt_name=TURF_DIRT_NAME )
            mst_turf_dirt_class.save()
            logger.warning(f'芝・ダート区分マスタ にTurf_dirt_code: {line}, Turf_dirt_name: {TURF_DIRT_NAME}を登録しました。')

    def chk_master_Mst_Course_class(self, line, Master):
        logger.info('コース区分マスタデータ有無確認処理')
        if not Master.objects.filter(Course_class_code=line):
            logger.info(f'コース区分マスタ Course_class_code :{line} ないので登録します。')
            mst_course_class = Master(Course_class_code=line, Course_class_name=COURSE_CLASS_NAME )
            mst_course_class.save()
            logger.warning(f'コース区分マスタ にCourse_class_code: {line}, Course_class_name: {COURSE_CLASS_NAME}を登録しました。')

    def chk_master_Mst_Clockwise_class(self, line, Master):
        logger.info('回り区分マスタデータ有無確認処理')
        if not Master.objects.filter(CW_or_CCW_code=line):
            logger.info(f'回り区分マスタ CW_or_CCW_code :{line} ないので登録します。')
            mst_clockwise_class = Master(CW_or_CCW_code=line, CW_or_CCW=CW_OR_CCW )
            mst_clockwise_class.save()
            logger.warning(f'回り区分マスタ にCW_or_CCW_code: {line}, CW_or_CCW: {CW_OR_CCW}を登録しました。')

    def chk_master_Mst_Weather(self, line, Master):
        logger.info('天候マスタデータ有無確認処理')
        if not Master.objects.filter(Weather_code=line):
            logger.info(f'天候マスタ Weather_code :{line} ないので登録します。')
            mst_weather = Master(Weather_code=line, Weather_name=WEATHER_NAME )
            mst_weather.save()
            logger.warning(f'天候マスタ にWeather_code: {line}, Weather_name: {WEATHER_NAME}を登録しました。')

    def chk_master_Mst_Track_condition(self, line, Master):
        logger.info('馬場状態マスタデータ有無確認処理')
        if not Master.objects.filter(Track_condition_code=line):
            logger.info(f'馬場状態マスタ Track_condition_code :{line} ないので登録します。')
            mst_track_condition = Master(Track_condition_code=line, Track_condition_name=TRACK_CONDITION_NAME )
            mst_track_condition.save()
            logger.warning(f'馬場状態マスタ にTrack_condition_code: {line}, Track_condition_name: {TRACK_CONDITION_NAME}を登録しました。')

    def chk_master_Mst_Gender(self, line, Master):
        logger.info('性別マスタデータ有無確認処理')
        if not Master.objects.filter(Horse_gender_code=line):
            logger.info(f'性別マスタ Horse_gender_code :{line} ないので登録します。')
            mst_gender = Master(Horse_gender_code=line, Horse_gender=HORSE_GENDER )
            mst_gender.save()
            logger.warning(f'性別マスタ にHorse_gender_code: {line}, Horse_gender: {HORSE_GENDER}を登録しました。')

    def chk_master_Mst_Belonging(self, line, Master):
        logger.info('所属場マスタデータ有無確認処理')
        if not Master.objects.filter(Belonging_code=line):
            logger.info(f'所属場マスタ Belonging_code :{line} ないので登録します。')
            mst_belonging = Master(Belonging_code=line, Belonging=BELONGING)
            mst_belonging.save()
            logger.warning(f'所属場マスタ にBelonging_code: {line}, Belonging: {BELONGING}を登録しました。')

    def chk_master_Mst_Jockey_changed_reason(self, line, Master):
        logger.info('騎手変更理由マスタデータ有無確認処理')
        if not Master.objects.filter(Jockey_changed_reason_code=line):
            logger.info(f'騎手変更理由マスタ Jockey_changed_reason_code :{line} ないので登録します。')
            mst_jockey_changed_reason = Master(Jockey_changed_reason_code=line, Jockey_changed_reason_name=JOCKEY_CHANGED_REASON_NAME )
            mst_jockey_changed_reason.save()
            logger.warning(f'騎手変更理由マスタ にJockey_changed_reason_code: {line}, Jockey_changed_reason_name: {JOCKEY_CHANGED_REASON_NAME}を登録しました。')

    def chk_master_Mst_Margin(self, line, Master):
        logger.info('着差マスタデータ有無確認処理')
        if not Master.objects.filter(Margin_code=line):
            logger.info(f'着差マスタ Margin_code :{line} ないので登録します。')
            mst_margin = Master(Margin_code=line, Margin_name=MARGIN_NAME )
            mst_margin.save()
            logger.warning(f'着差マスタ にMargin_code: {line}, Margin_name: {MARGIN_NAME}を登録しました。')

    def chk_master_Mst_Accident_type(self, line, Master):
        logger.info('事故種類マスタデータ有無確認処理')
        if not Master.objects.filter(Accident_type_code=line):
            logger.info(f'事故種類マスタ Accident_type_code :{line} ないので登録します。')
            mst_accident_type = Master(Accident_type_code=line, Accident_type_name=ACCIDENT_TYPE_NAME )
            mst_accident_type.save()
            logger.warning(f'事故種類マスタ にAccident_type_code: {line}, Accident_type_name: {ACCIDENT_TYPE_NAME}を登録しました。')

    def chk_master_Mst_Accident_reason(self, line, Master):
        logger.info('事故理由マスタデータ有無確認処理')
        if not Master.objects.filter(Accident_reason_code=line):
            logger.info(f'事故理由マスタ Accident_reason_code :{line} ないので登録します。')
            mst_accident_reason = Master(Accident_reason_code=line, Accident_reason_name=ACCIDENT_REASON_NAME )
            mst_accident_reason.save()
            logger.warning(f'事故理由マスタ にAccident_reason_code: {line}, Accident_reason_name: {ACCIDENT_REASON_NAME}を登録しました。')

    def chk_master_Mst_Matter(self, line, Master):
        logger.info('事象マスタデータ有無確認処理')
        if not Master.objects.filter(Matter_code=line):
            logger.info(f'事象マスタ にMatter_code :{line} ないので登録します。')
            mst_matter = Master(Matter_code=line,Matter_name=MATTER_NAME)
            mst_matter.save()
            logger.warning(f'事象マスタ にMatter_code {line}：Matter_name{MATTER_NAME}を登録しました。')

    def chk_master_Mst_Target_person(self, line, Master):
        logger.info('対象者マスタデータ有無確認処理')
        if not Master.objects.filter(Target_person_code=line):
            logger.info(f'対象者マスタ Target_person_code :{line} ないので登録します。')
            mst_target_person = Master(Target_person_code=line,Target_person_name=TARGET_PERSON_NAME)
            mst_target_person.save()
            logger.warning(f'対象者マスタ にTarget_person_code: {line}, Target_person_name: {TARGET_PERSON_NAME}を登録しました。')

    def chk_master_sua(self, line, Trn_Running_list_A_SUA_Mst_list):
        self.chk_master_Mst_Jou(line[4], Trn_Running_list_A_SUA_Mst_list[0])
        self.chk_master_Mst_Race_type(line[18], Trn_Running_list_A_SUA_Mst_list[1])
        self.chk_master_Mst_Breed_age(line[20], Trn_Running_list_A_SUA_Mst_list[2])
        self.chk_master_Mst_Handicap(line[22], Trn_Running_list_A_SUA_Mst_list[3])
        self.chk_master_Mst_JRA_exchanges(line[29], Trn_Running_list_A_SUA_Mst_list[4])
        self.chk_master_Mst_Grade(line[32], Trn_Running_list_A_SUA_Mst_list[5])
        self.chk_master_Mst_Night_race_class(line[34], Trn_Running_list_A_SUA_Mst_list[6])
        self.chk_master_Mst_Turf_dirt_class(line[76], Trn_Running_list_A_SUA_Mst_list[7])
        self.chk_master_Mst_Course_class(line[78], Trn_Running_list_A_SUA_Mst_list[8])
        self.chk_master_Mst_Clockwise_class(line[80], Trn_Running_list_A_SUA_Mst_list[9])
        self.chk_master_Mst_Weather(line[81], Trn_Running_list_A_SUA_Mst_list[10])
        self.chk_master_Mst_Track_condition(line[83], Trn_Running_list_A_SUA_Mst_list[11])

    def chk_master_su6(self, line, Trn_Result_SU6_Mst_list):
        self.chk_master_Mst_Jou(line[2], Trn_Result_SU6_Mst_list[0])
        self.chk_master_Mst_Gender(line[6], Trn_Result_SU6_Mst_list[1])
        self.chk_master_Mst_Belonging(line[28], Trn_Result_SU6_Mst_list[2])
        self.chk_master_Mst_Jockey_changed_reason(line[35], Trn_Result_SU6_Mst_list[3])
        self.chk_master_Mst_Jockey_changed_reason(line[46], Trn_Result_SU6_Mst_list[3])
        self.chk_master_Mst_Belonging(line[50], Trn_Result_SU6_Mst_list[2])
        self.chk_master_Mst_Margin(line[54], Trn_Result_SU6_Mst_list[5])
        self.chk_master_Mst_Margin(line[56], Trn_Result_SU6_Mst_list[5])
        self.chk_master_Mst_Margin(line[58], Trn_Result_SU6_Mst_list[5])
        self.chk_master_Mst_Accident_type(line[63], Trn_Result_SU6_Mst_list[6])
        self.chk_master_Mst_Accident_reason(line[65], Trn_Result_SU6_Mst_list[7])

    def chk_master_bu1(self, line, Trn_Attached_document_BU1_Mst_list):
        self.chk_master_Mst_Jou(line[2], Trn_Attached_document_BU1_Mst_list[0])
        self.chk_master_Mst_Matter(line[6], Trn_Attached_document_BU1_Mst_list[1])
        self.chk_master_Mst_Target_person(line[8], Trn_Attached_document_BU1_Mst_list[2])

    def run_sua(self, line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list):
        # マスターチェック-
        logger.info(f'マスターチェック : {Trn_Running_list_A_SUA_Mst_list}')
        self.chk_master_sua(line, Trn_Running_list_A_SUA_Mst_list)

        logger.info(f'insert table : {Trn_Running_list_A_SUA}')
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
            Race_type_code = Trn_Running_list_A_SUA_Mst_list[1].objects.get(Race_type_code=line[18]),
            Race_type_name = line[19],
            Breed_age_code = Trn_Running_list_A_SUA_Mst_list[2].objects.get(Breed_age_code=line[20]),
            Breed_age_name = line[21],
            Weight_code = Trn_Running_list_A_SUA_Mst_list[3].objects.get(Handicap_code=line[22]),
            Weight_name = line[23],
            Male_weight = line[24],
            Female_weight = line[25],
            Race_times = line[26],
            Race_name = line[27],
            Additional_name = line[28],
            JRA_exchanges_code = Trn_Running_list_A_SUA_Mst_list[4].objects.get(JRA_exchanges_code=line[29]),
            Race_code = line[30],
            Certified_race_code = line[31],
            Grade_code = Trn_Running_list_A_SUA_Mst_list[5].objects.get(Grade_code=line[32]),
            Grade_name = line[33],
            Night_race_code = Trn_Running_list_A_SUA_Mst_list[6].objects.get(Night_race_code=line[34]),
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
            Turf_dirt_code = Trn_Running_list_A_SUA_Mst_list[7].objects.get(Turf_dirt_code=line[76]),
            Turf_Dart_name = line[77],
            Inner_outer_code = Trn_Running_list_A_SUA_Mst_list[8].objects.get(Course_class_code=line[78]),
            Inner_outer_name = line[79],
            CW_or_CCW_code = Trn_Running_list_A_SUA_Mst_list[9].objects.get(CW_or_CCW_code=line[80]),
            Weather_code = Trn_Running_list_A_SUA_Mst_list[10].objects.get(Weather_code=line[81]),
            Weather_name = line[82],
            Track_condition_code = Trn_Running_list_A_SUA_Mst_list[11].objects.get(Track_condition_code=line[83]),
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

    def run_su6(self, line, Trn_Result_SU6, Trn_Result_SU6_Mst_list):
        # マスターチェック-
        logger.info(f'マスターチェック : {Trn_Result_SU6_Mst_list}')
        self.chk_master_su6(line, Trn_Result_SU6_Mst_list)

        logger.info(f'insert table : {Trn_Result_SU6}')
        trn_result_su6 = Trn_Result_SU6(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Trn_Result_SU6_Mst_list[0].objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Horse_name = line[5],
            Horse_gender_code = Trn_Result_SU6_Mst_list[1].objects.get(Horse_gender_code=line[6]),
            Horse_birth_date = line[7],
            Horse_age = line[8],
            Bracket_No = line[9],
            Hat_color = line[10],
            Horse_No = line[11],
            Horse_weight = line[12],
            Previous_Horse_weight = line[13],
            Weight = line[14],
            Carry_weight = line[15],
            Owner_Registration_No = line[16],
            Horse_owner_name = line[17],
            Trainer_license_No = line[18],
            Trainer_name = line[19],
            Trainer_shortened = line[20],
            Jockey_license_No = line[21],
            Jockey_name = line[22],
            Jockey_shortened = line[23],
            Weight_handicap = line[24],
            Weight_handicap_symbol = line[25],
            Jockey_belong_stable = line[26],
            Jockey_invitation_code = line[27],
            Jockey_belonging_code = Trn_Result_SU6_Mst_list[2].objects.get(Belonging_code=line[28]),
            Jockey_location_code = line[29],
            Jockey_license_No_1 = line[30],
            Jockey_name_1 = line[31],
            Jockey_shortened_1 = line[32],
            Weight_handicap_1 = line[33],
            Weight_handicap_symbol_1 = line[34],
            Jockey_changed_reason_code_1 = Trn_Result_SU6_Mst_list[3].objects.get(Jockey_changed_reason_code=line[35]),
            Jockey_changed_reason_name_1 = line[36],
            Jockey_belong_stable_1 = line[37],
            Jockey_invitation_code_1 = line[38],
            Jockey_belonging_code_1 = Trn_Result_SU6_Mst_list[2].objects.get(Belonging_code=line[39]),
            Jockey_location_code_1 = line[40],
            Jockey_license_No_2 = line[41],
            Jockey_name_2 = line[42],
            Jockey_shortened_2 = line[43],
            Weight_handicap_2 = line[44],
            Weight_handicap_symbol_2 = line[45],
            Jockey_changed_reason_code_2 = Trn_Result_SU6_Mst_list[3].objects.get(Jockey_changed_reason_code=line[46]),
            Jockey_changed_reason_name_2 = line[47],
            Jockey_belong_stable_2 = line[48],
            Jockey_invitation_code_2 = line[49],
            Jockey_belonging_code_2 = Trn_Result_SU6_Mst_list[2].objects.get(Belonging_code=line[50]),
            Jockey_location_code_2 = line[51],
            Result = line[52],
            Result_input_order = line[53],
            Margin_code_1 = Trn_Result_SU6_Mst_list[5].objects.get(Margin_code=line[54]),
            Margin_1 = line[55],
            Margin_code_2 = Trn_Result_SU6_Mst_list[5].objects.get(Margin_code=line[56]),
            Margin_2 = line[57],
            Margin_code_3 = Trn_Result_SU6_Mst_list[5].objects.get(Margin_code=line[58]),
            Margin_3 = line[59],
            Deadheat_code = line[60],
            Finish_time = line[61],
            Finish_line_result = line[62],
            Accident_code = Trn_Result_SU6_Mst_list[6].objects.get(Accident_type_code=line[63]),
            Accident_name = line[64],
            Accident_reason_code = Trn_Result_SU6_Mst_list[7].objects.get(Accident_reason_code=line[65]),
            Accident_reason_name = line[66],
            Prize_money_1 = line[67],
            Program_prize_1 = line[68],
            Additional_prize_1 = line[69],
            Last_3furlong = line[70],
            Win_Pic = line[71],
        )
        trn_result_su6.save()

    def run_wi2(self, line, Trn_Win_place_dividend_WI2, Mst_Jou):
        # マスターチェック-
        logger.info(f'マスターチェック : {Mst_Jou}')
        self.chk_master_Mst_Jou(line[2], Mst_Jou)

        logger.info(f'insert table : {Trn_Win_place_dividend_WI2}')
        trn_win_place_dividend_wi2 = Trn_Win_place_dividend_WI2(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Win_No_1 = line[5],
            Win_1 = line[6],
            Win_pick_1 = line[7],
            Win_No_2 = line[8],
            Win_2 = line[9],
            Win_pick_2 = line[10],
            Win_No_3 = line[11],
            Win_3 = line[12],
            Win_pick_3 = line[13],
            Win_total = line[14],
            Place_Resutl_1 = line[15],
            Place_No_1 = line[16],
            Place_1 = line[17],
            Place_pick_1 = line[18],
            Place_Resutl_2 = line[19],
            Place_No_2 = line[20],
            Place_2 = line[21],
            Place_pick_2 = line[22],
            Place_Resutl_3 = line[23],
            Place_No_3 = line[24],
            Place_3 = line[25],
            Place_pick_3 = line[26],
            Place_Resutl_4 = line[27],
            Place_No_4 = line[28],
            Place_4 = line[29],
            Place_pick_4 = line[30],
            Place_Resutl_5 = line[31],
            Place_No_5 = line[32],
            Place_5 = line[33],
            Place_pick_5 = line[34],
            Place_Resutl_6 = line[35],
            Place_No_6 = line[36],
            Place_6 = line[37],
            Place_pick_6 = line[38],
            Place_total = line[39],
            Win_sales = line[40],
            Place_sales = line[41]
        )
        trn_win_place_dividend_wi2.save()

    def run_bl2(self, line, Trn_Bracket_quinella_exacta_dividend_BL2, Mst_Jou):
        # マスターチェック-
        logger.info(f'マスターチェック : {Mst_Jou}')
        self.chk_master_Mst_Jou(line[2], Mst_Jou)

        logger.info(f'insert table : {Trn_Bracket_quinella_exacta_dividend_BL2}')
        trn_bracket_quinella_exacta_dividend_bl2 = Trn_Bracket_quinella_exacta_dividend_BL2(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Data_Classification = line[5],
            Bracket_No_1_1 = line[6],
            Bracket_No_1_2 = line[7],
            Bracket_quinella_exacta_1 = line[8],
            Bracket_quinella_exacta_pic_1 = line[9],
            Bracket_No_2_1 = line[10],
            Bracket_No_2_2 = line[11],
            Bracket_quinella_exacta_2 = line[12],
            Bracket_quinella_exacta_pic_2 = line[13],
            Bracket_No_3_1 = line[14],
            Bracket_No_3_2 = line[15],
            Bracket_quinella_exacta_3 = line[16],
            Bracket_quinella_exacta_pic_3 = line[17],
            Bracket_No_4_1 = line[18],
            Bracket_No_4_2 = line[19],
            Bracket_quinella_exacta_4 = line[20],
            Bracket_quinella_exacta_pic_4 = line[21],
            Bracket_No_5_1 = line[22],
            Bracket_No_5_2 = line[23],
            Bracket_quinella_exacta_5 = line[24],
            Bracket_quinella_exacta_pic_5 = line[25],
            Bracket_No_6_1 = line[26],
            Bracket_No_6_2 = line[27],
            Bracket_quinella_exacta_6 = line[28],
            Bracket_quinella_exacta_pic_6 = line[29],
            Bracket_quinella_exacta_total = line[30],
            Bracket_quinella_exacta_sales = line[31],
        )
        trn_bracket_quinella_exacta_dividend_bl2.save()

    def run_qu2(self, line, Trn_Quinella_exacta_wide_dividend_QU2, Mst_Jou):
        # マスターチェック-
        logger.info(f'マスターチェック : {Mst_Jou}')
        self.chk_master_Mst_Jou(line[2], Mst_Jou)

        logger.info(f'insert table : {Trn_Quinella_exacta_wide_dividend_QU2}')
        trn_quinella_exacta_wide_dividend_qu2 = Trn_Quinella_exacta_wide_dividend_QU2(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Data_Classification = line[5],
            Horce_No_1_1 = line[6],
            Horce_No_1_2 = line[7],
            Quinella_exacta_wide_1 = line[8],
            Quinella_exacta_wide_pic_1 = line[9],
            Horce_No_2_1 = line[10],
            Horce_No_2_2 = line[11],
            Quinella_exacta_wide_2 = line[12],
            Quinella_exacta_wide_pic_2 = line[13],
            Horce_No_3_1 = line[14],
            Horce_No_3_2 = line[15],
            Quinella_exacta_wide_3 = line[16],
            Quinella_exacta_wide_pic_3 = line[17],
            Horce_No_4_1 = line[18],
            Horce_No_4_2 = line[19],
            Quinella_exacta_wide_4 = line[20],
            Quinella_exacta_wide_pic_4 = line[21],
            Horce_No_5_1 = line[22],
            Horce_No_5_2 = line[23],
            Quinella_exacta_wide_5 = line[24],
            Quinella_exacta_wide_pic_5 = line[25],
            Horce_No_6_1 = line[26],
            Horce_No_6_2 = line[27],
            Quinella_exacta_wide_6 = line[28],
            Quinella_exacta_wide_pic_6 = line[29],
            Horce_No_7_1 = line[30],
            Horce_No_7_2 = line[31],
            Quinella_exacta_wide_7 = line[32],
            Quinella_exacta_wide_pic_7 = line[33],
            Quinella_exacta_wide_total = line[34],
            Quinella_exacta_wide_sales = line[35]
        )
        trn_quinella_exacta_wide_dividend_qu2.save()

    def run_tb3(self, line, Trn_Trio_dividend_TB3, Mst_Jou):
        # マスターチェック-
        logger.info(f'マスターチェック : {Mst_Jou}')
        self.chk_master_Mst_Jou(line[2], Mst_Jou)

        logger.info(f'insert table : {Trn_Trio_dividend_TB3}')
        trn_trio_dividend_tb3 = Trn_Trio_dividend_TB3(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Horce_No_1_1 = line[5],
            Horce_No_1_2 = line[6],
            Horce_No_1_3 = line[7],
            Trio_1 = line[8],
            Trio_pic_1 = line[9],
            Horce_No_2_1 = line[10],
            Horce_No_2_2 = line[11],
            Horce_No_2_3 = line[12],
            Trio_2 = line[13],
            Trio_pic_2 = line[14],
            Horce_No_3_1 = line[15],
            Horce_No_3_2 = line[16],
            Horce_No_3_3 = line[17],
            Trio_3 = line[18],
            Trio_pic_3 = line[19],
            Trio_total = line[20],
            Trio_sales = line[21]
        )
        trn_trio_dividend_tb3.save()

    def run_tb4(self, line, Trn_Trifecta_dividend_TB4, Mst_Jou):
        # マスターチェック-
        logger.info(f'マスターチェック : {Mst_Jou}')
        self.chk_master_Mst_Jou(line[2], Mst_Jou)

        logger.info(f'insert table : {Trn_Trifecta_dividend_TB4}')
        trn_trifecta_dividend_tb4 = Trn_Trifecta_dividend_TB4(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Horce_No_1_1 = line[5],
            Horce_No_1_2 = line[6],
            Horce_No_1_3 = line[7],
            Trifecta_1 = line[8],
            Trifecta_pic_1 = line[9],
            Horce_No_2_1 = line[10],
            Horce_No_2_2 = line[11],
            Horce_No_2_3 = line[12],
            Trifecta_2 = line[13],
            Trifecta_pic_2 = line[14],
            Horce_No_3_1 = line[15],
            Horce_No_3_2 = line[16],
            Horce_No_3_3 = line[17],
            Trifecta_3 = line[18],
            Trifecta_pic_3 = line[19],
            Horce_No_4_1 = line[20],
            Horce_No_4_2 = line[21],
            Horce_No_4_3 = line[22],
            Trifecta_4 = line[23],
            Trifecta_pic_4 = line[24],
            Horce_No_5_1 = line[25],
            Horce_No_5_2 = line[26],
            Horce_No_5_3 = line[27],
            Trifecta_5 = line[28],
            Trifecta_pic_5 = line[29],
            Horce_No_6_1 = line[30],
            Horce_No_6_2 = line[31],
            Horce_No_6_3 = line[32],
            Trifecta_6 = line[33],
            Trifecta_pic_6 = line[34],
            Trifecta_total = line[35],
            Trifecta_sales = line[36]
        )
        trn_trifecta_dividend_tb4.save()

    def run_bu1(self, line, Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list):
        # マスターチェック-
        logger.info(f'マスターチェック : {Trn_Attached_document_BU1_Mst_list}')
        self.chk_master_bu1(line, Trn_Attached_document_BU1_Mst_list)

        logger.info(f'insert table : {Trn_Attached_document_BU1}')
        trn_attached_document_bu1 = Trn_Attached_document_BU1(
            Data_ID = line[0],
            Race_date = line[1],
            Track_code = Trn_Attached_document_BU1_Mst_list[0].objects.get(Jou_code=line[2]),
            Held_times = line[3],
            Race_No = line[4],
            Output_order = line[5],
            Event_code = Trn_Attached_document_BU1_Mst_list[1].objects.get(Matter_code=line[6]),
            Accident_type_order = line[7],
            Target_person = Trn_Attached_document_BU1_Mst_list[2].objects.get(Target_person_code=line[8]),
            Horse_No = line[9],
            Event_name = line[10],
            Attached_document_1 = line[11],
            Attached_document_2 = line[12],
            Attached_document_3 = line[13],
            Attached_document_4 = line[14],
            Attached_document_5 = line[15],
            Attached_document_6 = line[16],
            Attached_document_7 = line[17],
            Attached_document_8 = line[18],
            Attached_document_9 = line[19],
            Attached_document_10 = line[20],
            Attached_document_11 = line[21],
            Attached_document_12 = line[22],
            Attached_document_13 = line[23],
            Attached_document_14 = line[24],
            Attached_document_15 = line[25],
            Attached_document_16 = line[26]
        )
        trn_attached_document_bu1.save()

    def chk_ID(self, line, \
        Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list, \
        Trn_Result_SU6, Trn_Result_SU6_Mst_list, \
        Trn_Win_place_dividend_WI2, Mst_Jou, \
        Trn_Bracket_quinella_exacta_dividend_BL2, \
        Trn_Quinella_exacta_wide_dividend_QU2, \
        Trn_Trio_dividend_TB3, \
        Trn_Trifecta_dividend_TB4, \
        Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list):

        if RACECARD == line[0]:# 出馬表Aデータ（番組情報）
            logging.info('出馬表Aデータ（番組情報')
            self.run_sua(line, Trn_Running_list_A_SUA,Trn_Running_list_A_SUA_Mst_list)

        elif ARRIVALTIME == line[0]:# 着タイムデータ
            logging.info('着タイムデータ')
            self.run_su6(line, Trn_Result_SU6, Trn_Result_SU6_Mst_list)

        elif BETTINGHANDLE == line[0]:# 単勝複勝払戻データ
            logging.info('単勝複勝払戻データ')
            self.run_wi2(line, Trn_Win_place_dividend_WI2, Mst_Jou)

        elif BRACKETQUINELLA == line[0]:# 枠複枠単払戻データ
            logging.info('枠複枠単払戻データ')
            self.run_bl2(line, Trn_Bracket_quinella_exacta_dividend_BL2, Mst_Jou)

        elif QUINELLA == line[0]:# 馬連馬単ワイド払戻データ
            logging.info('馬連馬単ワイド払戻データ')
            self.run_qu2(line, Trn_Quinella_exacta_wide_dividend_QU2, Mst_Jou)

        elif TIERCES == line[0]:# 三連複払戻データ
            logging.info('三連複払戻データ')
            self.run_tb3(line, Trn_Trio_dividend_TB3, Mst_Jou)

        elif TIERCE == line[0]: # 三連単払戻データ
            logging.info('三連単払戻データ')
            self.run_tb4(line, Trn_Trifecta_dividend_TB4, Mst_Jou)

        elif ADDITIONALDOCUMENT == line[0]: # 付加文書データ
            logging.info('付加文書データ')
            self.run_bu1(line, Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list)

        else:
            logging.error(f'該当しない{line}')
            # 該当しない
            pass

    #簡易競走成績データ_SEI
    def CSV_Schedule_SEI(self, fileName, \
        Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list, \
        Trn_Result_SU6, Trn_Result_SU6_Mst_list, \
        Trn_Win_place_dividend_WI2, Mst_Jou, \
        Trn_Bracket_quinella_exacta_dividend_BL2, \
        Trn_Quinella_exacta_wide_dividend_QU2, \
        Trn_Trio_dividend_TB3, \
        Trn_Trifecta_dividend_TB4, \
        Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list):

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

                logger.info(f'chk_ID : {line[0]}')
                self.chk_ID(line, Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list, \
                    Trn_Result_SU6, Trn_Result_SU6_Mst_list, \
                    Trn_Win_place_dividend_WI2, Mst_Jou, \
                    Trn_Bracket_quinella_exacta_dividend_BL2, \
                    Trn_Quinella_exacta_wide_dividend_QU2, \
                    Trn_Trio_dividend_TB3, \
                    Trn_Trifecta_dividend_TB4, \
                    Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list)

    def insert_or_update_Trn_Sei(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            # 出馬表Ａ_SUA:Trn_Running_list_A_SUA
            # 出馬表Aデータ（番組情報）
            from app_ckeiba.models import Trn_Running_list_A_SUA, Mst_Jou, Mst_Race_type, Mst_Breed_age, Mst_Handicap, Mst_JRA_exchanges, Mst_Grade, Mst_Night_race_class, Mst_Turf_dirt_class, Mst_Course_class, Mst_Clockwise_class, Mst_Weather, Mst_Track_condition
            Trn_Running_list_A_SUA_Mst_list = [Mst_Jou, Mst_Race_type, Mst_Breed_age, Mst_Handicap, Mst_JRA_exchanges, Mst_Grade, Mst_Night_race_class, Mst_Turf_dirt_class, Mst_Course_class, Mst_Clockwise_class, Mst_Weather, Mst_Track_condition]
            # 着タイムデータ
            from app_ckeiba.models import Trn_Result_SU6, Mst_Gender, Mst_Belonging, Mst_Jockey_changed_reason, Mst_Margin, Mst_Accident_type, Mst_Accident_reason
            Trn_Result_SU6_Mst_list = [Mst_Jou, Mst_Gender, Mst_Belonging, Mst_Jockey_changed_reason, Mst_Belonging, Mst_Margin, Mst_Accident_type, Mst_Accident_reason]
            # 単勝複勝払戻データ
            from app_ckeiba.models import Trn_Win_place_dividend_WI2
            # 枠複枠単払戻データ
            from app_ckeiba.models import Trn_Bracket_quinella_exacta_dividend_BL2
            # 馬連馬単ワイド払戻データ
            from app_ckeiba.models import Trn_Quinella_exacta_wide_dividend_QU2
            # 三連複払戻データ
            from app_ckeiba.models import Trn_Trio_dividend_TB3
            # 三連単払戻データ
            from app_ckeiba.models import Trn_Trifecta_dividend_TB4
            # 付加文書データ
            from app_ckeiba.models import Trn_Attached_document_BU1, Mst_Jou, Mst_Matter, Mst_Target_person
            Trn_Attached_document_BU1_Mst_list = [Mst_Jou, Mst_Matter, Mst_Target_person]

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Schedule_SEI Start')
            self.CSV_Schedule_SEI(fileName, \
                Trn_Running_list_A_SUA, Trn_Running_list_A_SUA_Mst_list, \
                Trn_Result_SU6, Trn_Result_SU6_Mst_list, \
                Trn_Win_place_dividend_WI2, Mst_Jou, \
                Trn_Bracket_quinella_exacta_dividend_BL2, \
                Trn_Quinella_exacta_wide_dividend_QU2, \
                Trn_Trio_dividend_TB3, \
                Trn_Trifecta_dividend_TB4, \
                Trn_Attached_document_BU1, Trn_Attached_document_BU1_Mst_list)
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

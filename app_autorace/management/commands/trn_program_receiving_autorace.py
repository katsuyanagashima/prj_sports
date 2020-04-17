_10_import logging
import datetime
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import time
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max
from app_autorace.models import *
from logging import getLogger
from pathlib import Path

#!/usr/bin/env
logger = getLogger(__name__)

# 監視対象ファイルのパターンマッチを指定する
# 番組編成データレコード（mmddhhmmss0000J001.dat）
programID = 2
programData = "programData"
go_recursively = False
# target_file_program_record = '*0000[1-6]001.dat'
target_file_program_record = '*0000[1-6]001.dat'
trn_running_list = 8

# RegexMatchingEventHandler の継承クラスを作成
class FileChangeHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)

    def init_trn_program(self):
        # Trn_Program レース結果データレコード
        self.classification 	=	str()
        self.data_type 		=	str()
        self.track_code 	=	str()
        self.track_name 	=	str()
        self.date_ad 		=	str()
        self.date_japanese_calendar =	str()
        self.held_day 	=	str()
        self.period_days 	=	str()
        self.event_name 	=	str()
        self.first_day_of_the_event =	str()
        self.commemorative_code 	=	str()
        self.special_commemorative_code 	=	str()
        self.race_no 		=	str()
        self.race_name 		=	str()
        self.race_distance 		=	str()
        self.scheduled_start_time 	=	str()
        self.participation 		=	str()
        self.race_prize_amount 		=	str()
        self.handicap_open_code 	=	str()
        self.voting_code 		=	str()
        self.win_ave_totaling_date 	=	str()
        self.totaling_date 		=	str()

    # Trn_Running_list 選手成績テーブル
    def init_trn_running_data(self):
        self.track_code 	=	str()
        self.date_ad 	=	str()
        self.race_no 		=	str()
        self.bracket_no 	=	str()
        self.rider_no 		=	str()
        self.rider_code 		=	str()
        self.rider_full_name 	=	str()
        self.rider_shortened_3_name =	str()
        self.rider_shortened_4_name 	=	str()
        self.lg_name 		=	str()
        self.lg_code 		=	str()
        self.nickname 		=	str()
        self.rider_class_code 	=	str()
        self.race_car_classification_code 	=	str()
        self.handicap 		=	str()
        self.last_run_4 	=	str()
        self.last_run_3 	=	str()
        self.last_run_2 	=	str()
        self.last_run_1 	=	str()
        self.last_run_4_track 		=	str()
        self.last_run_3_track 		=	str()
        self.last_run_2_track 		=	str()
        self.last_run_1_track 		=	str()
        self.last_run_time 			=	str()
        self.avg_time 			=	str()
        self.highest_time 			=	str()
        self.best_time_track 		=	str()
        self.rider_birthplace 		=	str()
        self.rider_age 			=	str()
        self.by_period 			=	str()
        self.avg_win_1 			=	str()
        self.avg_win_2 			=	str()
        self.avg_win_3 			=	str()
        self.avg_win_1_goodrunway 	=	str()
        self.avg_win_2_goodrunway 	=	str()
        self.avg_win_3_goodrunway 	=	str()
        self.avg_win_1_wetrunway 	=	str()
        self.avg_win_2_wetrunway 	=	str()
        self.avg_win_3_wetrunway 	=	str()
        self.avg_win_1_ohter 	=	str()
        self.avg_win_2_ohter 	=	str()
        self.avg_win_3_ohter 	=	str()
        self.last_1_test_run_time =	str()
        self.last_1_time 			=	str()
        self.last_1_lap_time 	=	str()
        self.last_1_run 		=	str()
        self.last_1_track 		=	str()
        self.last_1_st 			=	str()
        self.last_1_handicap 	=	str()
        self.last_1_track_condition 	=	str()
        self.last_2_test_run_time 		=	str()
        self.last_2_time 			=	str()
        self.last_2_lap_time 		=	str()
        self.last_2_run 			=	str()
        self.last_2_track 			=	str()
        self.last_2_st 			=	str()
        self.last_2_handicap 		=	str()
        self.last_2_track_condition 	=	str()
        self.last_3_test_run_time 		=	str()
        self.last_3_time 			=	str()
        self.last_3_lap_time 		=	str()
        self.last_3_run 			=	str()
        self.last_3_track 			=	str()
        self.last_3_st 			=	str()
        self.last_3_handicap 		=	str()
        self.last_3_track_condition 	=	str()
        self.last_4_test_run_time 	=	str()
        self.last_4_time 			=	str()
        self.last_4_lap_time 		=	str()
        self.last_4_run 			=	str()
        self.last_4_track 			=	str()
        self.last_4_st 			=	str()
        self.last_4_handicap=	str()
        self.last_4_track_condition=	str()
        self.last_5_test_run_time=	str()
        self.last_5_time=	str()
        self.last_5_lap_time=	str()
        self.last_5_run=	str()
        self.last_5_track=	str()
        self.last_5_st=	str()
        self.last_5_handicap=	str()
        self.last_5_track_condition=	str()
        self.last_6_test_run_time=	str()
        self.last_6_time=	str()
        self.last_6_lap_time=	str()
        self.last_6_run=	str()
        self.last_6_track=	str()
        self.last_6_st=	str()
        self.last_6_handicap=	str()
        self.last_6_track_condition=	str()
        self.last_7_test_run_time=	str()
        self.last_7_time=	str()
        self.last_7_lap_time=	str()
        self.last_7_run=	str()
        self.last_7_track=	str()
        self.last_7_st=	str()
        self.last_7_handicap=	str()
        self.last_7_track_condition=	str()
        self.last_8_test_run_time=	str()
        self.last_8_time=	str()
        self.last_8_lap_time=	str()
        self.last_8_run=	str()
        self.last_8_track=	str()
        self.last_8_st=	str()
        self.last_8_handicap=	str()
        self.last_8_track_condition=	str()
        self.last_9_test_run_time=	str()
        self.last_9_time=	str()
        self.last_9_lap_time=	str()
        self.last_9_run=	str()
        self.last_9_track=	str()
        self.last_9_st=	str()
        self.last_9_handicap=	str()
        self.last_9_track_condition=	str()
        self.last_10_test_run_time=	str()
        self.last_10_time=	str()
        self.last_10_lap_time=	str()
        self.last_10_run=	str()
        self.last_10_track=	str()
        self.last_10_st=	str()
        self.last_10_handicap=	str()
        self.last_10_track_condition=	str()
        self.total_v=	str()
        self.total_1st=	str()
        self.total_2nd=	str()
        self.total_3rd=	str()
        self.total_other=	str()

    # 正規表現で半角ブランク削除
    def chkBlank(self, lineStr):
        if (not re.sub('\\s|\\S', '', lineStr)):
            return False
        return True

    def update_trn_running_list(self, trn_program):
        # 実体のあるカラム更新
        updateFields = list()
        if self.bracket_no:
            trn_program.Bracket_No=self.bracket_no
            updateFields.append('Bracket_No')
        if self.rider_no:
            trn_program.Rider_No=self.rider_no
            updateFields.append('Rider_No')
        if self.rider_code:
            trn_program.Rider_code=self.rider_code
            updateFields.append('Rider_code')
        if self.rider_full_name:
            trn_program.Rider_full_name=self.rider_full_name
            updateFields.append('Rider_full_name')
        if self.rider_shortened_3_name:
            trn_program.Rider_shortened_3_name=self.rider_shortened_3_name
            updateFields.append('Rider_shortened_3_name')
        if self.rider_shortened_4_name:
            trn_program.Rider_shortened_4_name=self.rider_shortened_4_name
            updateFields.append('Rider_shortened_4_name')
        if self.lg_name:
            trn_program.LG_name=self.lg_name
            updateFields.append('LG_name')
        if self.lg_code:
            trn_program.LG_code=self.lg_code
            updateFields.append('LG_code')
        if self.nickname:
            trn_program.Nickname=self.nickname
            updateFields.append('Nickname')
        if self.rider_class_code:
            trn_program.Rider_class_code=self.rider_class_code
            updateFields.append('Rider_class_code')
        if self.race_car_classification_code:
            trn_program.Race_car_classification_code=self.race_car_classification_code
            updateFields.append('Race_car_classification_code')
        if self.handicap:
            trn_program.Handicap=self.handicap
            updateFields.append('Handicap')
        if self.last_run_4:
            trn_program.Last_run_4=self.last_run_4
            updateFields.append('Last_run_4')
        if self.last_run_3:
            trn_program.Last_run_3=self.last_run_3
            updateFields.append('Last_run_3')
        if self.last_run_2:
            trn_program.Last_run_2=self.last_run_2
            updateFields.append('Last_run_2')
        if self.last_run_1:
            trn_program.Last_run_1=self.last_run_1
            updateFields.append('Last_run_1')
        if self.last_run_4_Track:
            trn_program.Last_run_4_Track=self.last_run_4_Track
            updateFields.append('Last_run_4_Track')
        if self.last_run_3_Track:
            trn_program.Last_run_3_Track=self.last_run_3_Track
            updateFields.append('Last_run_3_Track')
        if self.last_run_2_Track:
            trn_program.Last_run_2_Track=self.last_run_2_Track
            updateFields.append('Last_run_2_Track')
        if self.last_run_1_Track:
            trn_program.Last_run_1_Track=self.last_run_1_Track
            updateFields.append('Last_run_1_Track')
        if self.last_run_time:
            trn_program.Last_run_time=self.last_run_time
            updateFields.append('Last_run_time')
        if self.avg_time:
            trn_program.Avg_time=self.avg_time
            updateFields.append('Avg_time')
        if self.highest_time:
            trn_program.Highest_time=self.highest_time
            updateFields.append('Highest_time')
        if self.best_time_Track:
            trn_program.Best_time_Track=self.best_time_Track
            updateFields.append('Best_time_Track')
        if self.rider_birthplace:
            trn_program.Rider_birthplace=self.rider_birthplace
            updateFields.append('Rider_birthplace')
        if self.rider_age:
            trn_program.Rider_Age=self.rider_age
            updateFields.append('Rider_Age')
        if self.by_period:
            trn_program.By_period=self.by_period
            updateFields.append('By_period')
        if self.avg_win_1:
            trn_program.Avg_win_1=self.avg_win_1
            updateFields.append('Avg_win_1')
        if self.avg_win_2:
            trn_program.Avg_win_2=self.avg_win_2
            updateFields.append('Avg_win_2')
        if self.avg_win_3:
            trn_program.Avg_win_3=self.avg_win_3
            updateFields.append('Avg_win_3')
        if self.avg_win_1_goodrunway:
            trn_program.Avg_win_1_goodrunway=self.avg_win_1_goodrunway
            updateFields.append('Avg_win_1_goodrunway')
        if self.avg_win_2_goodrunway:
            trn_program.Avg_win_2_goodrunway=self.avg_win_2_goodrunway
            updateFields.append('Avg_win_2_goodrunway')
        if self.avg_win_3_goodrunway:
            trn_program.Avg_win_3_goodrunway=self.avg_win_3_goodrunway
            updateFields.append('Avg_win_3_goodrunway')
        if self.avg_win_1_Wetrunway:
            trn_program.Avg_win_1_Wetrunway=self.avg_win_1_Wetrunway
            updateFields.append('Avg_win_1_Wetrunway')
        if self.avg_win_2_Wetrunway:
            trn_program.Avg_win_2_Wetrunway=self.avg_win_2_Wetrunway
            updateFields.append('Avg_win_2_Wetrunway')
        if self.avg_win_3_Wetrunway:
            trn_program.Avg_win_3_Wetrunway=self.avg_win_3_Wetrunway
            updateFields.append('Avg_win_3_Wetrunway')
        if self.avg_win_1_ohter:
            trn_program.Avg_win_1_ohter=self.avg_win_1_ohter
            updateFields.append('Avg_win_1_ohter')
        if self.avg_win_2_ohter:
            trn_program.Avg_win_2_ohter=self.avg_win_2_ohter
            updateFields.append('Avg_win_2_ohter')
        if self.avg_win_3_ohter:
            trn_program.Avg_win_3_ohter=self.avg_win_3_ohter
            updateFields.append('Avg_win_3_ohter')

        if self.last_1_test_run_time:
            trn_program.Last_1_test_run_time=self.last_1_test_run_time
            updateFields.append('Last_1_test_run_time')
        if self.last_1_time:
            trn_program.Last_1_time=self.last_1_time
            updateFields.append('Last_1_time')
        if self.last_1_lap_time:
            trn_program.Last_1_lap_time=self.last_1_lap_time
            updateFields.append('Last_1_lap_time')
        if self.last_1_run:
            trn_program.Last_1_run=self.last_1_run
            updateFields.append('Last_1_run')
        if self.last_1_Track:
            trn_program.Last_1_Track=self.last_1_Track
            updateFields.append('Last_1_Track')
        if self.last_1_st:
            trn_program.Last_1_ST=self.last_1_st
            updateFields.append('Last_1_ST')
        if self.last_1_handicap:
            trn_program.Last_1_Handicap=self.last_1_handicap
            updateFields.append('Last_1_Handicap')
        if self.last_1_track_condition:
            trn_program.Last_1_track_condition=self.last_1_track_condition
            updateFields.append('Last_1_track_condition')

        if self.last_2_test_run_time:
            trn_program.Last_2_test_run_time=self.last_2_test_run_time
            updateFields.append('Last_2_test_run_time')
        if self.last_2_time:
            trn_program.Last_2_time=self.last_2_time
            updateFields.append('Last_2_time')
        if self.last_2_lap_time:
            trn_program.Last_2_lap_time=self.last_2_lap_time
            updateFields.append('Last_2_lap_time')
        if self.last_2_run:
            trn_program.Last_2_run=self.last_2_run
            updateFields.append('Last_2_run')
        if self.last_2_Track:
            trn_program.Last_2_Track=self.last_2_Track
            updateFields.append('Last_2_Track')
        if self.last_2_st:
            trn_program.Last_2_ST=self.last_2_st
            updateFields.append('Last_2_ST')
        if self.last_2_handicap:
            trn_program.Last_2_Handicap=self.last_2_handicap
            updateFields.append('Last_2_Handicap')
        if self.last_2_track_condition:
            trn_program.Last_2_track_condition=self.last_2_track_condition
            updateFields.append('Last_2_track_condition')

        if self.last_3_test_run_time:
            trn_program.Last_3_test_run_time=self.last_3_test_run_time
            updateFields.append('Last_3_test_run_time')
        if self.last_3_time:
            trn_program.Last_3_time=self.last_3_time
            updateFields.append('Last_3_time')
        if self.last_3_lap_time:
            trn_program.Last_3_lap_time=self.last_3_lap_time
            updateFields.append('Last_3_lap_time')
        if self.last_3_run:
            trn_program.Last_3_run=self.last_3_run
            updateFields.append('Last_3_run')
        if self.last_3_Track:
            trn_program.Last_3_Track=self.last_3_Track
            updateFields.append('Last_3_Track')
        if self.last_3_st:
            trn_program.Last_3_ST=self.last_3_st
            updateFields.append('Last_3_ST')
        if self.last_3_handicap:
            trn_program.Last_3_Handicap=self.last_3_handicap
            updateFields.append('Last_3_Handicap')
        if self.last_3_track_condition:
            trn_program.Last_3_track_condition=self.last_3_track_condition
            updateFields.append('Last_3_track_condition')

        if self.last_4_test_run_time:
            trn_program.Last_4_test_run_time=self.last_4_test_run_time
            updateFields.append('Last_4_test_run_time')
        if self.last_4_time:
            trn_program.Last_4_time=self.last_4_time
            updateFields.append('Last_4_time')
        if self.last_4_lap_time:
            trn_program.Last_4_lap_time=self.last_4_lap_time
            updateFields.append('Last_4_lap_time')
        if self.last_4_run:
            trn_program.Last_4_run=self.last_4_run
            updateFields.append('Last_4_run')
        if self.last_4_Track:
            trn_program.Last_4_Track=self.last_4_Track
            updateFields.append('Last_4_Track')
        if self.last_4_st:
            trn_program.Last_4_ST=self.last_4_st
            updateFields.append('Last_4_ST')
        if self.last_4_handicap:
            trn_program.Last_4_Handicap=self.last_4_handicap
            updateFields.append('Last_4_Handicap')
        if self.last_4_track_condition:
            trn_program.Last_4_track_condition=self.last_4_track_condition
            updateFields.append('Last_4_track_condition')

        if self.last_5_test_run_time:
            trn_program.Last_5_test_run_time=self.last_5_test_run_time
            updateFields.append('Last_5_test_run_time')
        if self.last_5_time:
            trn_program.Last_5_time=self.last_5_time
            updateFields.append('Last_5_time')
        if self.last_5_lap_time:
            trn_program.Last_5_lap_time=self.last_5_lap_time
            updateFields.append('Last_5_lap_time')
        if self.last_5_run:
            trn_program.Last_5_run=self.last_5_run
            updateFields.append('Last_5_run')
        if self.last_5_Track:
            trn_program.Last_5_Track=self.last_5_Track
            updateFields.append('Last_5_Track')
        if self.last_5_st:
            trn_program.Last_5_ST=self.last_5_st
            updateFields.append('Last_5_ST')
        if self.last_5_handicap:
            trn_program.Last_5_Handicap=self.last_5_handicap
            updateFields.append('Last_5_Handicap')
        if self.last_5_track_condition:
            trn_program.Last_5_track_condition=self.last_5_track_condition
            updateFields.append('Last_5_track_condition')

        if self.last_6_test_run_time:
            trn_program.Last_6_test_run_time=self.last_6_test_run_time
            updateFields.append('Last_6_test_run_time')
        if self.last_6_time:
            trn_program.Last_6_time=self.last_6_time
            updateFields.append('Last_6_time')
        if self.last_6_lap_time:
            trn_program.Last_6_lap_time=self.last_6_lap_time
            updateFields.append('Last_6_lap_time')
        if self.last_6_run:
            trn_program.Last_6_run=self.last_6_run
            updateFields.append('Last_6_run')
        if self.last_6_Track:
            trn_program.Last_6_Track=self.last_6_Track
            updateFields.append('Last_6_Track')
        if self.last_6_st:
            trn_program.Last_6_ST=self.last_6_st
            updateFields.append('Last_6_ST')
        if self.last_6_handicap:
            trn_program.Last_6_Handicap=self.last_6_handicap
            updateFields.append('Last_6_Handicap')
        if self.last_6_track_condition:
            trn_program.Last_6_track_condition=self.last_6_track_condition
            updateFields.append('Last_6_track_condition')

        if self.last_7_test_run_time:
            trn_program.Last_7_test_run_time=self.last_7_test_run_time
            updateFields.append('Last_7_test_run_time')
        if self.last_7_time:
            trn_program.Last_7_time=self.last_7_time
            updateFields.append('Last_7_time')
        if self.last_7_lap_time:
            trn_program.Last_7_lap_time=self.last_7_lap_time
            updateFields.append('Last_7_lap_time')
        if self.last_7_run:
            trn_program.Last_7_run=self.last_7_run
            updateFields.append('Last_7_run')
        if self.last_7_Track:
            trn_program.Last_7_Track=self.last_7_Track
            updateFields.append('Last_7_Track')
        if self.last_7_st:
            trn_program.Last_7_ST=self.last_7_st
            updateFields.append('Last_7_ST')
        if self.last_7_handicap:
            trn_program.Last_7_Handicap=self.last_7_handicap
            updateFields.append('Last_7_Handicap')
        if self.last_7_track_condition:
            trn_program.Last_7_track_condition=self.last_7_track_condition
            updateFields.append('Last_7_track_condition')

        if self.last_8_test_run_time:
            trn_program.Last_8_test_run_time=self.last_8_test_run_time
            updateFields.append('Last_8_test_run_time')
        if self.last_8_time:
            trn_program.Last_8_time=self.last_8_time
            updateFields.append('Last_8_time')
        if self.last_8_lap_time:
            trn_program.Last_8_lap_time=self.last_8_lap_time
            updateFields.append('Last_8_lap_time')
        if self.last_8_run:
            trn_program.Last_8_run=self.last_8_run
            updateFields.append('Last_8_run')
        if self.last_8_Track:
            trn_program.Last_8_Track=self.last_8_Track
            updateFields.append('Last_8_Track')
        if self.last_8_st:
            trn_program.Last_8_ST=self.last_8_st
            updateFields.append('Last_8_ST')
        if self.last_8_handicap:
            trn_program.Last_8_Handicap=self.last_8_handicap
            updateFields.append('Last_8_Handicap')
        if self.last_8_track_condition:
            trn_program.Last_8_track_condition=self.last_8_track_condition
            updateFields.append('Last_8_track_condition')

        if self.last_9_test_run_time:
            trn_program.Last_9_test_run_time=self.last_9_test_run_time
            updateFields.append('Last_9_test_run_time')
        if self.last_9_time:
            trn_program.Last_9_time=self.last_9_time
            updateFields.append('Last_9_time')
        if self.last_9_lap_time:
            trn_program.Last_9_lap_time=self.last_9_lap_time
            updateFields.append('Last_9_lap_time')
        if self.last_9_run:
            trn_program.Last_9_run=self.last_9_run
            updateFields.append('Last_9_run')
        if self.last_9_Track:
            trn_program.Last_9_Track=self.last_9_Track
            updateFields.append('Last_9_Track')
        if self.last_9_st:
            trn_program.Last_9_ST=self.last_9_st
            updateFields.append('Last_9_ST')
        if self.last_9_handicap:
            trn_program.Last_9_Handicap=self.last_9_handicap
            updateFields.append('Last_9_Handicap')
        if self.last_9_track_condition:
            trn_program.Last_9_track_condition=self.last_9_track_condition
            updateFields.append('Last_9_track_condition')

        if self.last_10_test_run_time:
            trn_program.Last_10_test_run_time=self.last_10_test_run_time
            updateFields.append('Last_10_test_run_time')
        if self.last_10_time:
            trn_program.Last_10_time=self.last_10_time
            updateFields.append('Last_10_time')
        if self.last_10_lap_time:
            trn_program.Last_10_lap_time=self.last_10_lap_time
            updateFields.append('Last_10_lap_time')
        if self.last_10_run:
            trn_program.Last_10_run=self.last_10_run
            updateFields.append('Last_10_run')
        if self.last_10_Track:
            trn_program.Last_10_Track=self.last_10_Track
            updateFields.append('Last_10_Track')
        if self.last_10_st:
            trn_program.Last_10_ST=self.last_10_st
            updateFields.append('Last_10_ST')
        if self.last_10_handicap:
            trn_program.Last_10_Handicap=self.last_10_handicap
            updateFields.append('Last_10_Handicap')
        if self.last_10_track_condition:
            trn_program.Last_10_track_condition=self.last_10_track_condition
            updateFields.append('Last_6_track_condition')

        if self.total_v:
            trn_program.Total_V=self.total_v
            updateFields.append('Total_V')
        if self.total_1st:
            trn_program.Total_1st=self.total_1st
            updateFields.append('Total_1st')
        if self.total_2nd:
            trn_program.v=self.total_2nd
            updateFields.append('Total_2nd')
        if self.total_3rd:
            trn_program.Total_3rd=self.total_3rd
            updateFields.append('Total_3rd')
        if self.total_other:
            trn_program.Total_other=self.total_other
            updateFields.append('Total_other')

        trn_program.save(update_fields=updateFields)

    def setDatData_running_list(self, count, trn_running_list_line):

        count = count * 69

        self.bracket_no 	=	trn_running_list_line[count:count+1]
        self.rider_no 		=	trn_running_list_line[count+1:count+2]
        self.rider_code 		=	trn_running_list_line[count+2:count+6]
        self.rider_full_name 	=	trn_running_list_line[count+6:count+14]
        self.rider_shortened_3_name =	trn_running_list_line[count+14:count+17]
        self.rider_shortened_4_name 	=	trn_running_list_line[count+17:count+21]
        self.lg_name 		=	trn_running_list_line[count+21:count+24]
        self.lg_code 		=	trn_running_list_line[count+24:count+25]
        self.nickname 		=	trn_running_list_line[count:count+1]
        self.rider_class_code 	=	trn_running_list_line[count:count+1]
        self.race_car_classification_code 	=	trn_running_list_line[count:count+1]
        self.handicap 		=	trn_running_list_line[count:count+1]
        self.last_run_4 	=	trn_running_list_line[count:count+1]
        self.last_run_3 	=	trn_running_list_line[count:count+1]
        self.last_run_2 	=	trn_running_list_line[count:count+1]
        self.last_run_1 	=	trn_running_list_line[count:count+1]
        self.last_run_4_track 		=	trn_running_list_line[count:count+1]
        self.last_run_3_track 		=	trn_running_list_line[count:count+1]
        self.last_run_2_track 		=	trn_running_list_line[count:count+1]
        self.last_run_1_track 		=	trn_running_list_line[count:count+1]
        self.last_run_time 			=	trn_running_list_line[count:count+1]
        self.avg_time 			=	trn_running_list_line[count:count+1]
        self.highest_time 			=	trn_running_list_line[count:count+1]
        self.best_time_track 		=	trn_running_list_line[count:count+1]
        self.rider_birthplace 		=	trn_running_list_line[count:count+1]
        self.rider_age 			=	trn_running_list_line[count:count+1]
        self.by_period 			=	trn_running_list_line[count:count+1]
        self.avg_win_1 			=	trn_running_list_line[count:count+1]
        self.avg_win_2 			=	trn_running_list_line[count:count+1]
        self.avg_win_3 			=	trn_running_list_line[count:count+1]
        self.avg_win_1_goodrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_2_goodrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_3_goodrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_1_wetrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_2_wetrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_3_wetrunway 	=	trn_running_list_line[count:count+1]
        self.avg_win_1_ohter 	=	trn_running_list_line[count:count+1]
        self.avg_win_2_ohter 	=	trn_running_list_line[count:count+1]
        self.avg_win_3_ohter 	=	trn_running_list_line[count:count+1]
        self.last_1_test_run_time =	trn_running_list_line[count:count+1]
        self.last_1_time 			=	trn_running_list_line[count:count+1]
        self.last_1_lap_time 	=	trn_running_list_line[count:count+1]
        self.last_1_run 		=	trn_running_list_line[count:count+1]
        self.last_1_track 		=	trn_running_list_line[count:count+1]
        self.last_1_st 			=	trn_running_list_line[count:count+1]
        self.last_1_handicap 	=	trn_running_list_line[count:count+1]
        self.last_1_track_condition 	=	trn_running_list_line[count:count+1]
        self.last_2_test_run_time 		=	trn_running_list_line[count:count+1]
        self.last_2_time 			=	trn_running_list_line[count:count+1]
        self.last_2_lap_time 		=	trn_running_list_line[count:count+1]
        self.last_2_run 			=	trn_running_list_line[count:count+1]
        self.last_2_track 			=	trn_running_list_line[count:count+1]
        self.last_2_st 			=	trn_running_list_line[count:count+1]
        self.last_2_handicap 		=	trn_running_list_line[count:count+1]
        self.last_2_track_condition 	=	trn_running_list_line[count:count+1]
        self.last_3_test_run_time 		=	trn_running_list_line[count:count+1]
        self.last_3_time 			=	trn_running_list_line[count:count+1]
        self.last_3_lap_time 		=	trn_running_list_line[count:count+1]
        self.last_3_run 			=	trn_running_list_line[count:count+1]
        self.last_3_track 			=	trn_running_list_line[count:count+1]
        self.last_3_st 			=	trn_running_list_line[count:count+1]
        self.last_3_handicap 		=	trn_running_list_line[count:count+1]
        self.last_3_track_condition 	=	trn_running_list_line[count:count+1]
        self.last_4_test_run_time 	=	trn_running_list_line[count:count+1]
        self.last_4_time 			=	trn_running_list_line[count:count+1]
        self.last_4_lap_time 		=	trn_running_list_line[count:count+1]
        self.last_4_run 			=	trn_running_list_line[count:count+1]
        self.last_4_track 			=	trn_running_list_line[count:count+1]
        self.last_4_st 			=	trn_running_list_line[count:count+1]
        self.last_4_handicap=	trn_running_list_line[count:count+1]
        self.last_4_track_condition=	trn_running_list_line[count:count+1]
        self.last_5_test_run_time=	trn_running_list_line[count:count+1]
        self.last_5_time=	trn_running_list_line[count:count+1]
        self.last_5_lap_time=	trn_running_list_line[count:count+1]
        self.last_5_run=	trn_running_list_line[count:count+1]
        self.last_5_track=	trn_running_list_line[count:count+1]
        self.last_5_st=	trn_running_list_line[count:count+1]
        self.last_5_handicap=	trn_running_list_line[count:count+1]
        self.last_5_track_condition=	trn_running_list_line[count:count+1]
        self.last_6_test_run_time=	trn_running_list_line[count:count+1]
        self.last_6_time=	trn_running_list_line[count:count+1]
        self.last_6_lap_time=	trn_running_list_line[count:count+1]
        self.last_6_run=	trn_running_list_line[count:count+1]
        self.last_6_track=	trn_running_list_line[count:count+1]
        self.last_6_st=	trn_running_list_line[count:count+1]
        self.last_6_handicap=	trn_running_list_line[count:count+1]
        self.last_6_track_condition=	trn_running_list_line[count:count+1]
        self.last_7_test_run_time=	trn_running_list_line[count:count+1]
        self.last_7_time=	trn_running_list_line[count:count+1]
        self.last_7_lap_time=	trn_running_list_line[count:count+1]
        self.last_7_run=	trn_running_list_line[count:count+1]
        self.last_7_track=	trn_running_list_line[count:count+1]
        self.last_7_st=	trn_running_list_line[count:count+1]
        self.last_7_handicap=	trn_running_list_line[count:count+1]
        self.last_7_track_condition=	trn_running_list_line[count:count+1]
        self.last_8_test_run_time=	trn_running_list_line[count:count+1]
        self.last_8_time=	trn_running_list_line[count:count+1]
        self.last_8_lap_time=	trn_running_list_line[count:count+1]
        self.last_8_run=	trn_running_list_line[count:count+1]
        self.last_8_track=	trn_running_list_line[count:count+1]
        self.last_8_st=	trn_running_list_line[count:count+1]
        self.last_8_handicap=	trn_running_list_line[count:count+1]
        self.last_8_track_condition=	trn_running_list_line[count:count+1]
        self.last_9_test_run_time=	trn_running_list_line[count:count+1]
        self.last_9_time=	trn_running_list_line[count:count+1]
        self.last_9_lap_time=	trn_running_list_line[count:count+1]
        self.last_9_run=	trn_running_list_line[count:count+1]
        self.last_9_track=	trn_running_list_line[count:count+1]
        self.last_9_st=	trn_running_list_line[count:count+1]
        self.last_9_handicap=	trn_running_list_line[count:count+1]
        self.last_9_track_condition=	trn_running_list_line[count:count+1]
        self.last_10_test_run_time=	trn_running_list_line[count:count+1]
        self.last_10_time=	trn_running_list_line[count:count+1]
        self.last_10_lap_time=	trn_running_list_line[count:count+1]
        self.last_10_run=	trn_running_list_line[count:count+1]
        self.last_10_track=	trn_running_list_line[count:count+1]
        self.last_10_st=	trn_running_list_line[count:count+1]
        self.last_10_handicap=	trn_running_list_line[count:count+1]
        self.last_10_track_condition=	trn_running_list_line[count:count+1]
        self.total_v=	trn_running_list_line[count:count+1]
        self.total_1st=	trn_running_list_line[count:count+1]
        self.total_2nd=	trn_running_list_line[count:count+1]
        self.total_3rd=	trn_running_list_line[count:count+1]
        self.total_other=	trn_running_list_line[count:count+1]

    # 選手出走テーブル 繰り返し×8
    def insert_or_update_trn_running_list(self, trn_running_list_line):

        for running_list in range(trn_running_list):

            self.init_trn_program_data()

            self.setDatData_running_list(running_list, trn_running_list_line)

            Trn_Running_list(Track_code=self.track_code, Date_AD = self.date_ad, Race_No=self.race_No).save()

            # 空白チェックして実体があるカラムは更新
            self.update_trn_running_list(Trn_Running_list.objects.get(id=Trn_Running_list.objects.all().aggregate(Max('id')).get('id__max')))

    # datファイル設定する
    def setDatData(self, line):

        # shift_jis 日本語は２バイト
        # Trn_Program
        self.classification 	=	line[0:1]
        self.data_type 		=	line[1:2]
        self.track_code 	=	line[2:3]
        self.track_name 	=	line[3:6]
        self.date_ad 		=	line[6:14]
        self.date_japanese_calendar =	line[14:25]
        self.held_day 	=	line[25:39]
        self.period_days 	=	line[39:43]
        self.event_name 	=	line[43:63]
        self.first_day_of_the_event =	line[63:71]
        self.commemorative_code 	=	line[71:72]
        self.special_commemorative_code 	=	line[72:74]
        self.race_no 		=	line[74:76]
        self.race_name 		=	line[76:89]
        self.race_distance 		=	line[89:93]
        self.scheduled_start_time 	=	line[93:98]
        self.participation 		=	line[98:99]
        self.race_prize_amount 		=	line[99:108]
        self.handicap_open_code 	=	line[108:109]
        self.voting_code 		=	line[109:111]
        self.win_ave_totaling_date 	=	line[111:119]
        self.totaling_date 		=	line[119:127]

        # 出走選手テーブル  ×8
        self.bracket_no 	=	line[127:128]
        self.rider_no 		=	line[119:127]
        self.rider_code 		=	line[119:127]
        self.rider_full_name 	=	line[119:127]
        self.rider_shortened_3_name =	line[119:127]
        self.rider_shortened_4_name 	=	line[119:127]
        self.lg_name 		=	line[119:127]
        self.lg_code 		=	line[119:127]
        self.nickname 		=	line[119:127]
        self.rider_class_code 	=	line[119:127]
        self.race_car_classification_code 	=	line[119:127]
        self.handicap 		=	line[119:127]
        self.last_run_4 	=	line[119:127]
        self.last_run_3 	=	line[119:127]
        self.last_run_2 	=	line[119:127]
        self.last_run_1 	=	line[119:127]
        self.last_run_4_track 		=	line[119:127]
        self.last_run_3_track 		=	line[119:127]
        self.last_run_2_track 		=	line[119:127]
        self.last_run_1_track 		=	line[119:127]
        self.last_run_time 			=	line[119:127]
        self.avg_time 			=	line[119:127]
        self.highest_time 			=	line[119:127]
        self.best_time_track 		=	line[119:127]
        self.rider_birthplace 		=	line[119:127]
        self.rider_age 			=	line[119:127]
        self.by_period 			=	line[119:127]
        self.avg_win_1 			=	line[119:127]
        self.avg_win_2 			=	line[119:127]
        self.avg_win_3 			=	line[119:127]
        self.avg_win_1_goodrunway 	=	line[119:127]
        self.avg_win_2_goodrunway 	=	line[119:127]
        self.avg_win_3_goodrunway 	=	line[119:127]
        self.avg_win_1_wetrunway 	=	line[119:127]
        self.avg_win_2_wetrunway 	=	line[119:127]
        self.avg_win_3_wetrunway 	=	line[119:127]
        self.avg_win_1_ohter 	=	line[119:127]
        self.avg_win_2_ohter 	=	line[119:127]
        self.avg_win_3_ohter 	=	line[119:127]
        self.last_1_test_run_time =	line[119:127]
        self.last_1_time 			=	line[119:127]
        self.last_1_lap_time 	=	line[119:127]
        self.last_1_run 		=	line[119:127]
        self.last_1_track 		=	line[119:127]
        self.last_1_st 			=	line[119:127]
        self.last_1_handicap 	=	line[119:127]
        self.last_1_track_condition 	=	line[119:127]
        self.last_2_test_run_time 		=	line[119:127]
        self.last_2_time 			=	line[119:127]
        self.last_2_lap_time 		=	line[119:127]
        self.last_2_run 			=	line[119:127]
        self.last_2_track 			=	line[119:127]
        self.last_2_st 			=	line[119:127]
        self.last_2_handicap 		=	line[119:127]
        self.last_2_track_condition 	=	line[119:127]
        self.last_3_test_run_time 		=	line[119:127]
        self.last_3_time 			=	line[119:127]
        self.last_3_lap_time 		=	line[119:127]
        self.last_3_run 			=	line[119:127]
        self.last_3_track 			=	line[119:127]
        self.last_3_st 			=	line[119:127]
        self.last_3_handicap 		=	line[119:127]
        self.last_3_track_condition 	=	line[119:127]
        self.last_4_test_run_time 	=	line[119:127]
        self.last_4_time 			=	line[119:127]
        self.last_4_lap_time 		=	line[119:127]
        self.last_4_run 			=	line[119:127]
        self.last_4_track 			=	line[119:127]
        self.last_4_st 			=	line[119:127]
        self.last_4_handicap=	line[119:127]
        self.last_4_track_condition=	line[119:127]
        self.last_5_test_run_time=	line[119:127]
        self.last_5_time=	line[119:127]
        self.last_5_lap_time=	line[119:127]
        self.last_5_run=	line[119:127]
        self.last_5_track=	line[119:127]
        self.last_5_st=	line[119:127]
        self.last_5_handicap=	line[119:127]
        self.last_5_track_condition=	line[119:127]
        self.last_6_test_run_time=	line[119:127]
        self.last_6_time=	line[119:127]
        self.last_6_lap_time=	line[119:127]
        self.last_6_run=	line[119:127]
        self.last_6_track=	line[119:127]
        self.last_6_st=	line[119:127]
        self.last_6_handicap=	line[119:127]
        self.last_6_track_condition=	line[119:127]
        self.last_7_test_run_time=	line[119:127]
        self.last_7_time=	line[119:127]
        self.last_7_lap_time=	line[119:127]
        self.last_7_run=	line[119:127]
        self.last_7_track=	line[119:127]
        self.last_7_st=	line[119:127]
        self.last_7_handicap=	line[119:127]
        self.last_7_track_condition=	line[119:127]
        self.last_8_test_run_time=	line[119:127]
        self.last_8_time=	line[119:127]
        self.last_8_lap_time=	line[119:127]
        self.last_8_run=	line[119:127]
        self.last_8_track=	line[119:127]
        self.last_8_st=	line[119:127]
        self.last_8_handicap=	line[119:127]
        self.last_8_track_condition=	line[119:127]
        self.last_9_test_run_time=	line[119:127]
        self.last_9_time=	line[119:127]
        self.last_9_lap_time=	line[119:127]
        self.last_9_run=	line[119:127]
        self.last_9_track=	line[119:127]
        self.last_9_st=	line[119:127]
        self.last_9_handicap=	line[119:127]
        self.last_9_track_condition=	line[119:127]
        self.last_10_test_run_time=	line[119:127]
        self.last_10_time=	line[119:127]
        self.last_10_lap_time=	line[119:127]
        self.last_10_run=	line[119:127]
        self.last_10_track=	line[119:127]
        self.last_10_st=	line[119:127]
        self.last_10_handicap=	line[119:127]
        self.last_10_track_condition=	line[119:127]
        self.total_v=	line[119:127]
        self.total_1st=	line[119:127]
        self.total_2nd=	line[119:127]
        self.total_3rd=	line[119:127]
        self.total_other=	line[119:127]

    def update_trn_program(self, trn_program):
        # 実体のあるカラム更新
        updateFields = list()

        if self.date_Japanese_calendar:
            trn_program.Date_Japanese_calendar=self.date_Japanese_calendar
            updateFields.append('Date_Japanese_calendar')
        if self.held_day :
            trn_program.Held_day=self.held_day
            updateFields.append('Held_day')
        if self.period_days :
            trn_program.Period_days=self.period_days
            updateFields.append('Period_days')
        if self.event_name :
            trn_program.Event_name=self.event_name
            updateFields.append('Event_name')
        if self.commemorative_code :
            trn_program.Commemorative_code=self.commemorative_code
            updateFields.append('Commemorative_code')
        if self.special_commemorative_code :
            trn_program.Special_commemorative_code=self.special_commemorative_code
            updateFields.append('Special_commemorative_code')
        if self.race_name :
            trn_program.Race_name=self.race_name
            updateFields.append('Race_name')
        if self.scheduled_start_time :
            trn_program.Scheduled_start_time=self.scheduled_start_time
            updateFields.append('Scheduled_start_time')
        if self.participation :
            trn_program.Participation=self.participation
            updateFields.append('Participation')
        if self.race_Prize_Amount :
            trn_program.Race_Prize_Amount=self.race_Prize_Amount
            updateFields.append('Race_Prize_Amount')
        if self.handicap_Open_code :
            trn_program.Handicap_Open_code=self.handicap_Open_code
            updateFields.append('Handicap_Open_code')
        if self.voting_code :
            trn_program.Voting_code=self.voting_code
            updateFields.append('Voting_code')
        if self.win_ave_totaling_date :
            trn_program.Win_Ave_Totaling_Date=self.win_ave_totaling_date
            updateFields.append('Win_Ave_Totaling_Date')
        if self.totaling_date :
            trn_program.Totaling_date=self.totaling_date
            updateFields.append('Totaling_date')

    def insert_or_update_Trn_Program(self, name):
        try:
            # ファイル読み込み　データセット
            file = open(name,'r',encoding='shift_jis')
            for line in file:

                # Q:何度も連打すると何故かうまく行かない。A:PollingObserver使用する。
                self.init_trn_program()

                self.setDatData(line)

                break
            file.close()

            # DB　ファイル登録
            with transaction.atomic():
                # レース結果データレコード
                Trn_Program(Classification=self.classification, Data_type=self.data_type, Track_code=self.track_code, Track_name=self.track_name \
                , Date_AD=self.date_ad, First_day_of_the_event=self.first_day_of_the_event, Race_No=self.race_No, Race_distance=self.race_distance).save()

                # 空白チェックして実体があるカラムは更新
                self.update_trn_program(Trn_Program.objects.get(id=Trn_Program.objects.all().aggregate(Max('id')).get('id__max')))

                # 選手成績テーブル
                self.insert_or_update_trn_running_list(self.trn_running_list_line)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)

    # ファイル作成時のイベント
    def on_created(self, event):
        filepath = event.src_path
        filename_program_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,programData ,filename_program_record))
        # 監視元のフォルダパスを生成

        print('%s created Start' % filename_program_record)
        # ファイル読み込み

        self.insert_or_update_Trn_Program(name)

        print('%s created End' % filename_program_record)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename_program_record = os.path.basename(filepath)
        print('%s changed' % filename_program_record)

    # ファイル削除時のイベント
    def on_deleted(self, event):
        filepath = event.src_path
        filename_program_record = os.path.basename(filepath)
        print('%s deleted' % filename_program_record)

    # ファイル移動時のイベント
    def on_moved(self, event):
        filepath = event.src_path
        filename_program_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,programData ,filename_program_record))
        print('%s moved Start' % filename_program_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Program(name)

        print('%s moved End' % filename_program_record)

# コマンド実行の確認
class Command(BaseCommand):

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'ファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    def add_arguments(self, parser):
        # 今回はprogramという名前で取得する。（引数は最低でも1個, int型）
        parser.add_argument('command_id', nargs='+', type=int)


    """受け取った引数を登録する"""
    def handle(self, *args, **options):
        # ファイル監視の開始
        # 番組編成データレコード（mmddhhmmss0000J001.dat） 2: 番組編成データレコード
        # J 以外固定
        # ・ファイル名称末尾８桁の“J”は場コード（1～6）
        # 監視対象ディレクトリを指定する
        if programID in options['command_id']:
            base_trn_Program = os.path.dirname(os.path.abspath(__file__))
            base = os.path.normpath(os.path.join(base_trn_Program,programData))
            target_dir = os.path.expanduser(base)
            event_handler = FileChangeHandler(target_file_program_record)
            observer = PollingObserver()
            observer.schedule(event_handler, target_dir, recursive=go_recursively)# recursive再帰的
            observer.start()
        else:
            raise ValueError("command_id エラー")

        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

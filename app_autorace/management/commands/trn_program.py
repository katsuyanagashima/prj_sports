import datetime
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import sys
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
sys.path.append("/code/app_autorace/")
from consts import *

logger = getLogger('command')

# 監視対象ファイルのパターンマッチを指定する
# 番組編成データレコード（mmddhhmmss0000J001.dat）

# target_file_program_record = '*0000[1-6]001.dat'
trn_program_repeat = 12 # 番組編成データレコードテーブル　繰り返しの数
trn_running_list = 8
count = 341 
trn_program_running_record = 2979

class Program():

    def init_trn_program(self):
        # Trn_Program 番組編成データレコード
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

    # Trn_Running_list 出走選手テーブル
    def init_trn_running_data(self):

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

    # 出走選手テーブル 繰り返し×8
    def insert_or_update_trn_running_list(self, trn_running_list_line, repeat):

        for running_list_repeat in range(trn_running_list):

            self.init_trn_running_data()

            running_count = count * running_list_repeat + 127

            Trn_Running_list(Track_code=self.track_code, Date_AD = self.date_ad, Race_No=self.race_no).save()
            update_trn_running_list = Trn_Running_list.objects.get(id=Trn_Running_list.objects.all().aggregate(Max('id')).get('id__max'))
            updateFields = list()

            # 実体のあるカラム更新
            if trn_running_list_line[running_count:running_count+1]:
                update_trn_running_list.Bracket_No=trn_running_list_line[running_count:running_count+1]
                updateFields.append('Bracket_No')
            if trn_running_list_line[running_count+1:running_count+2]:
                update_trn_running_list.Rider_No=trn_running_list_line[running_count+1:running_count+2]
                updateFields.append('Rider_No')
            if trn_running_list_line[running_count+2:running_count+6]:
                update_trn_running_list.Rider_code=trn_running_list_line[running_count+2:running_count+6]
                updateFields.append('Rider_code')
            if trn_running_list_line[running_count+6:running_count+14]:
                update_trn_running_list.Rider_full_name=trn_running_list_line[running_count+6:running_count+14]
                updateFields.append('Rider_full_name')
            if trn_running_list_line[running_count+14:running_count+17]:
                update_trn_running_list.Rider_shortened_3_name=trn_running_list_line[running_count+14:running_count+17]
                updateFields.append('Rider_shortened_3_name')
            if trn_running_list_line[running_count+17:running_count+21]:
                update_trn_running_list.Rider_shortened_4_name=trn_running_list_line[running_count+17:running_count+21]
                updateFields.append('Rider_shortened_4_name')
            if trn_running_list_line[running_count+21:running_count+24]:
                update_trn_running_list.LG_name=trn_running_list_line[running_count+21:running_count+24]
                updateFields.append('LG_name')
            if trn_running_list_line[running_count+24:running_count+25]:
                update_trn_running_list.LG_code=trn_running_list_line[running_count+24:running_count+25]
                updateFields.append('LG_code')
            if trn_running_list_line[running_count+25:running_count+37]:
                update_trn_running_list.Nickname=trn_running_list_line[running_count+25:running_count+37]
                updateFields.append('Nickname')
            if trn_running_list_line[running_count+37:running_count+38]:
                update_trn_running_list.Rider_class_code=trn_running_list_line[running_count+37:running_count+38]
                updateFields.append('Rider_class_code')
            if trn_running_list_line[running_count+38:running_count+39]:
                update_trn_running_list.Race_car_classification_code=trn_running_list_line[running_count+38:running_count+39]
                updateFields.append('Race_car_classification_code')
            if trn_running_list_line[running_count+39:running_count+42]:
                update_trn_running_list.Handicap=trn_running_list_line[running_count+39:running_count+42]
                updateFields.append('Handicap')
            if trn_running_list_line[running_count+42:running_count+43]:
                update_trn_running_list.Last_run_4=trn_running_list_line[running_count+42:running_count+43]
                updateFields.append('Last_run_4')
            if trn_running_list_line[running_count+43:running_count+44]:
                update_trn_running_list.Last_run_3=trn_running_list_line[running_count+43:running_count+44]
                updateFields.append('Last_run_3')
            if trn_running_list_line[running_count+44:running_count+45]:
                update_trn_running_list.Last_run_2=trn_running_list_line[running_count+44:running_count+45]
                updateFields.append('Last_run_2')
            if trn_running_list_line[running_count+45:running_count+46]:
                update_trn_running_list.Last_run_1=trn_running_list_line[running_count+45:running_count+46]
                updateFields.append('Last_run_1')
            if trn_running_list_line[running_count+46:running_count+47]:
                update_trn_running_list.Last_run_4_Track=trn_running_list_line[running_count+46:running_count+47]
                updateFields.append('Last_run_4_Track')
            if trn_running_list_line[running_count+47:running_count+48]:
                update_trn_running_list.Last_run_3_Track=trn_running_list_line[running_count+47:running_count+48]
                updateFields.append('Last_run_3_Track')
            if trn_running_list_line[running_count+48:running_count+49]:
                update_trn_running_list.Last_run_2_Track=trn_running_list_line[running_count+48:running_count+49]
                updateFields.append('Last_run_2_Track')
            if trn_running_list_line[running_count+49:running_count+50]:
                update_trn_running_list.Last_run_1_Track=trn_running_list_line[running_count+49:running_count+50]
                updateFields.append('Last_run_1_Track')
            if trn_running_list_line[running_count+50:running_count+54]:
                update_trn_running_list.Last_run_time=trn_running_list_line[running_count+50:running_count+54]
                updateFields.append('Last_run_time')
            if trn_running_list_line[running_count+54:running_count+58]:
                update_trn_running_list.Avg_time=trn_running_list_line[running_count+54:running_count+58]
                updateFields.append('Avg_time')
            if trn_running_list_line[running_count+58:running_count+62]:
                update_trn_running_list.Highest_time=trn_running_list_line[running_count+58:running_count+62]
                updateFields.append('Highest_time')
            if trn_running_list_line[running_count+62:running_count+65]:
                update_trn_running_list.Best_time_Track=trn_running_list_line[running_count+62:running_count+65]
                updateFields.append('Best_time_Track')
            if trn_running_list_line[running_count+65:running_count+68]:
                update_trn_running_list.Rider_birthplace=trn_running_list_line[running_count+65:running_count+68]
                updateFields.append('Rider_birthplace')
            if trn_running_list_line[running_count+68:running_count+70]:
                update_trn_running_list.Rider_Age=trn_running_list_line[running_count+68:running_count+70]
                updateFields.append('Rider_Age')
            if trn_running_list_line[running_count+70:running_count+72]:
                update_trn_running_list.By_period=trn_running_list_line[running_count+70:running_count+72]
                updateFields.append('By_period')
            if trn_running_list_line[running_count+72:running_count+76]:
                update_trn_running_list.Avg_win_1=trn_running_list_line[running_count+72:running_count+76]
                updateFields.append('Avg_win_1')
            if trn_running_list_line[running_count+76:running_count+80]:
                update_trn_running_list.Avg_win_2=trn_running_list_line[running_count+76:running_count+80]
                updateFields.append('Avg_win_2')
            if trn_running_list_line[running_count+80:running_count+84]:
                update_trn_running_list.Avg_win_3=trn_running_list_line[running_count+80:running_count+84]
                updateFields.append('Avg_win_3')
            if trn_running_list_line[running_count+84:running_count+88]:
                update_trn_running_list.Avg_win_1_goodrunway=trn_running_list_line[running_count+84:running_count+88]
                updateFields.append('Avg_win_1_goodrunway')
            if trn_running_list_line[running_count+88:running_count+92]:
                update_trn_running_list.Avg_win_2_goodrunway=trn_running_list_line[running_count+88:running_count+92]
                updateFields.append('Avg_win_2_goodrunway')
            if trn_running_list_line[running_count+92:running_count+96]:
                update_trn_running_list.Avg_win_3_goodrunway=trn_running_list_line[running_count+92:running_count+96]
                updateFields.append('Avg_win_3_goodrunway')
            if trn_running_list_line[running_count+96:running_count+100]:
                update_trn_running_list.Avg_win_1_Wetrunway=trn_running_list_line[running_count+96:running_count+100]
                updateFields.append('Avg_win_1_Wetrunway')
            if trn_running_list_line[running_count+100:running_count+104]:
                update_trn_running_list.Avg_win_2_Wetrunway=trn_running_list_line[running_count+100:running_count+104]
                updateFields.append('Avg_win_2_Wetrunway')
            if trn_running_list_line[running_count+104:running_count+108]:
                update_trn_running_list.Avg_win_3_Wetrunway=trn_running_list_line[running_count+104:running_count+108]
                updateFields.append('Avg_win_3_Wetrunway')
            if trn_running_list_line[running_count+108:running_count+112]:
                update_trn_running_list.Avg_win_1_ohter=trn_running_list_line[running_count+108:running_count+112]
                updateFields.append('Avg_win_1_ohter')
            if trn_running_list_line[running_count+112:running_count+116]:
                update_trn_running_list.Avg_win_2_ohter=trn_running_list_line[running_count+112:running_count+116]
                updateFields.append('Avg_win_2_ohter')
            if trn_running_list_line[running_count+116:running_count+120]:
                update_trn_running_list.Avg_win_3_ohter=trn_running_list_line[running_count+116:running_count+120]
                updateFields.append('Avg_win_3_ohter')

            # 繰り返し　×　10　過去１走前～１０走前の順
            if trn_running_list_line[running_count+120:running_count+124]:
                update_trn_running_list.Last_1_test_run_time=trn_running_list_line[running_count+120:running_count+124]
                updateFields.append('Last_1_test_run_time')
            if trn_running_list_line[running_count+124:running_count+128]:
                update_trn_running_list.Last_1_time=trn_running_list_line[running_count+124:running_count+128]
                updateFields.append('Last_1_time')
            if trn_running_list_line[running_count+128:running_count+132]:
                update_trn_running_list.Last_1_lap_time=trn_running_list_line[running_count+128:running_count+132]
                updateFields.append('Last_1_lap_time')
            if trn_running_list_line[running_count+132:running_count+133]:
                update_trn_running_list.Last_1_run=trn_running_list_line[running_count+132:running_count+133]
                updateFields.append('Last_1_run')
            if trn_running_list_line[running_count+133:running_count+134]:
                update_trn_running_list.Last_1_Track=trn_running_list_line[running_count+133:running_count+134]
                updateFields.append('Last_1_Track')
            if trn_running_list_line[running_count+134:running_count+136]:
                update_trn_running_list.Last_1_ST=trn_running_list_line[running_count+134:running_count+136]
                updateFields.append('Last_1_ST')
            if trn_running_list_line[running_count+136:running_count+139]:
                update_trn_running_list.Last_1_Handicap=trn_running_list_line[running_count+136:running_count+139]
                updateFields.append('Last_1_Handicap')
            if trn_running_list_line[running_count+139:running_count+140]:
                update_trn_running_list.Last_1_track_condition=trn_running_list_line[running_count+139:running_count+140]
                updateFields.append('Last_1_track_condition')

            if trn_running_list_line[running_count+140:running_count+144]:
                update_trn_running_list.Last_2_test_run_time=trn_running_list_line[running_count+140:running_count+144]
                updateFields.append('Last_2_test_run_time')
            if trn_running_list_line[running_count+144:running_count+148]:
                update_trn_running_list.Last_2_time=trn_running_list_line[running_count+144:running_count+148]
                updateFields.append('Last_2_time')
            if trn_running_list_line[running_count+148:running_count+152]:
                update_trn_running_list.Last_2_lap_time=trn_running_list_line[running_count+148:running_count+152]
                updateFields.append('Last_2_lap_time')
            if trn_running_list_line[running_count+152:running_count+153]:
                update_trn_running_list.Last_2_run=trn_running_list_line[running_count+152:running_count+153]
                updateFields.append('Last_2_run')
            if trn_running_list_line[running_count+153:running_count+154]:
                update_trn_running_list.Last_2_Track=trn_running_list_line[running_count+153:running_count+154]
                updateFields.append('Last_2_Track')
            if trn_running_list_line[running_count+154:running_count+156]:
                update_trn_running_list.Last_2_ST=trn_running_list_line[running_count+154:running_count+156]
                updateFields.append('Last_2_ST')
            if trn_running_list_line[running_count+156:running_count+159]:
                update_trn_running_list.Last_2_Handicap=trn_running_list_line[running_count+156:running_count+159]
                updateFields.append('Last_2_Handicap')
            if trn_running_list_line[running_count+159:running_count+160]:
                update_trn_running_list.Last_2_track_condition=trn_running_list_line[running_count+159:running_count+160]
                updateFields.append('Last_2_track_condition')

            if trn_running_list_line[running_count+160:running_count+164]:
                update_trn_running_list.Last_3_test_run_time=trn_running_list_line[running_count+160:running_count+164]
                updateFields.append('Last_3_test_run_time')
            if trn_running_list_line[running_count+164:running_count+168]:
                update_trn_running_list.Last_3_time=trn_running_list_line[running_count+164:running_count+168]
                updateFields.append('Last_3_time')
            if trn_running_list_line[running_count+168:running_count+172]:
                update_trn_running_list.Last_3_lap_time=trn_running_list_line[running_count+168:running_count+172]
                updateFields.append('Last_3_lap_time')
            if trn_running_list_line[running_count+172:running_count+173]:
                update_trn_running_list.Last_3_run=trn_running_list_line[running_count+172:running_count+173]
                updateFields.append('Last_3_run')
            if trn_running_list_line[running_count+173:running_count+174]:
                update_trn_running_list.Last_3_Track=trn_running_list_line[running_count+173:running_count+174]
                updateFields.append('Last_3_Track')
            if trn_running_list_line[running_count+174:running_count+176]:
                update_trn_running_list.Last_3_ST=trn_running_list_line[running_count+174:running_count+176]
                updateFields.append('Last_3_ST')
            if trn_running_list_line[running_count+176:running_count+179]:
                update_trn_running_list.Last_3_Handicap=trn_running_list_line[running_count+176:running_count+179]
                updateFields.append('Last_3_Handicap')
            if trn_running_list_line[running_count+179:running_count+180]:
                update_trn_running_list.Last_3_track_condition=trn_running_list_line[running_count+179:running_count+180]
                updateFields.append('Last_3_track_condition')

            if trn_running_list_line[running_count+180:running_count+184]:
                update_trn_running_list.Last_4_test_run_time=trn_running_list_line[running_count+180:running_count+184]
                updateFields.append('Last_4_test_run_time')
            if trn_running_list_line[running_count+184:running_count+188]:
                update_trn_running_list.Last_4_time=trn_running_list_line[running_count+184:running_count+188]
                updateFields.append('Last_4_time')
            if trn_running_list_line[running_count+188:running_count+192]:
                update_trn_running_list.Last_4_lap_time=trn_running_list_line[running_count+188:running_count+192]
                updateFields.append('Last_4_lap_time')
            if trn_running_list_line[running_count+192:running_count+193]:
                update_trn_running_list.Last_4_run=trn_running_list_line[running_count+192:running_count+193]
                updateFields.append('Last_4_run')
            if trn_running_list_line[running_count+193:running_count+194]:
                update_trn_running_list.Last_4_Track=trn_running_list_line[running_count+193:running_count+194]
                updateFields.append('Last_4_Track')
            if trn_running_list_line[running_count+194:running_count+196]:
                update_trn_running_list.Last_4_ST=trn_running_list_line[running_count+194:running_count+196]
                updateFields.append('Last_4_ST')
            if trn_running_list_line[running_count+196:running_count+199]:
                update_trn_running_list.Last_4_Handicap=trn_running_list_line[running_count+196:running_count+199]
                updateFields.append('Last_4_Handicap')	
            if trn_running_list_line[running_count+199:running_count+200]:
                update_trn_running_list.Last_4_track_condition=trn_running_list_line[running_count+199:running_count+200]
                updateFields.append('Last_4_track_condition')

            if trn_running_list_line[running_count+200:running_count+204]:
                update_trn_running_list.Last_5_test_run_time=trn_running_list_line[running_count+200:running_count+204]
                updateFields.append('Last_5_test_run_time')
            if trn_running_list_line[running_count+204:running_count+208]:
                update_trn_running_list.Last_5_time=trn_running_list_line[running_count+204:running_count+208]
                updateFields.append('Last_5_time')
            if trn_running_list_line[running_count+208:running_count+212]:
                update_trn_running_list.Last_5_lap_time=trn_running_list_line[running_count+208:running_count+212]
                updateFields.append('Last_5_lap_time')
            if trn_running_list_line[running_count+212:running_count+213]:
                update_trn_running_list.Last_5_run=trn_running_list_line[running_count+212:running_count+213]
                updateFields.append('Last_5_run')
            if trn_running_list_line[running_count+213:running_count+214]:
                update_trn_running_list.Last_5_Track=trn_running_list_line[running_count+213:running_count+214]
                updateFields.append('Last_5_Track')
            if trn_running_list_line[running_count+214:running_count+216]:
                update_trn_running_list.Last_5_ST=trn_running_list_line[running_count+214:running_count+216]
                updateFields.append('Last_5_ST')
            if trn_running_list_line[running_count+216:running_count+219]:
                update_trn_running_list.Last_5_Handicap=trn_running_list_line[running_count+216:running_count+219]
                updateFields.append('Last_5_Handicap')
            if trn_running_list_line[running_count+219:running_count+220]:
                update_trn_running_list.Last_5_track_condition=trn_running_list_line[running_count+219:running_count+220]
                updateFields.append('Last_5_track_condition')

            if trn_running_list_line[running_count+220:running_count+224]:
                update_trn_running_list.Last_6_test_run_time=trn_running_list_line[running_count+220:running_count+224]
                updateFields.append('Last_6_test_run_time')
            if trn_running_list_line[running_count+224:running_count+228]:
                update_trn_running_list.Last_6_time=trn_running_list_line[running_count+224:running_count+228]
                updateFields.append('Last_6_time')	
            if trn_running_list_line[running_count+228:running_count+232]:
                update_trn_running_list.Last_6_lap_time=trn_running_list_line[running_count+228:running_count+232]
                updateFields.append('Last_6_lap_time')
            if trn_running_list_line[running_count+232:running_count+233]:
                update_trn_running_list.Last_6_run=trn_running_list_line[running_count+232:running_count+233]
                updateFields.append('Last_6_run')
            if trn_running_list_line[running_count+233:running_count+234]:
                update_trn_running_list.Last_6_Track=trn_running_list_line[running_count+233:running_count+234]
                updateFields.append('Last_6_Track')
            if trn_running_list_line[running_count+234:running_count+236]:
                update_trn_running_list.Last_6_ST=trn_running_list_line[running_count+234:running_count+236]
                updateFields.append('Last_6_ST')
            if trn_running_list_line[running_count+236:running_count+239]:
                update_trn_running_list.Last_6_Handicap=trn_running_list_line[running_count+236:running_count+239]
                updateFields.append('Last_6_Handicap')
            if trn_running_list_line[running_count+239:running_count+240]:
                update_trn_running_list.Last_6_track_condition=trn_running_list_line[running_count+239:running_count+240]
                updateFields.append('Last_6_track_condition')

            if trn_running_list_line[running_count+240:running_count+244]:
                update_trn_running_list.Last_7_test_run_time=trn_running_list_line[running_count+240:running_count+244]
                updateFields.append('Last_7_test_run_time')
            if trn_running_list_line[running_count+244:running_count+248]:
                update_trn_running_list.Last_7_time=trn_running_list_line[running_count+244:running_count+248]
                updateFields.append('Last_7_time')
            if trn_running_list_line[running_count+248:running_count+252]:
                update_trn_running_list.Last_7_lap_time=trn_running_list_line[running_count+248:running_count+252]
                updateFields.append('Last_7_lap_time')
            if trn_running_list_line[running_count+252:running_count+253]:
                update_trn_running_list.Last_7_run=trn_running_list_line[running_count+252:running_count+253]
                updateFields.append('Last_7_run')
            if trn_running_list_line[running_count+253:running_count+254]:
                update_trn_running_list.Last_7_Track=trn_running_list_line[running_count+253:running_count+254]
                updateFields.append('Last_7_Track')
            if trn_running_list_line[running_count+254:running_count+256]:
                update_trn_running_list.Last_7_ST=trn_running_list_line[running_count+254:running_count+256]
                updateFields.append('Last_7_ST')
            if trn_running_list_line[running_count+256:running_count+259]:
                update_trn_running_list.Last_7_Handicap=trn_running_list_line[running_count+256:running_count+259]
                updateFields.append('Last_7_Handicap')
            if trn_running_list_line[running_count+259:running_count+260]:
                update_trn_running_list.Last_7_track_condition=trn_running_list_line[running_count+259:running_count+260]
                updateFields.append('Last_7_track_condition')

            if trn_running_list_line[running_count+260:running_count+264]:
                update_trn_running_list.Last_8_test_run_time=trn_running_list_line[running_count+260:running_count+264]
                updateFields.append('Last_8_test_run_time')
            if trn_running_list_line[running_count+264:running_count+268]:
                update_trn_running_list.Last_8_time=trn_running_list_line[running_count+264:running_count+268]
                updateFields.append('Last_8_time')
            if trn_running_list_line[running_count+268:running_count+272]:
                update_trn_running_list.Last_8_lap_time=trn_running_list_line[running_count+268:running_count+272]
                updateFields.append('Last_8_lap_time')
            if trn_running_list_line[running_count+272:running_count+273]:
                update_trn_running_list.Last_8_run=trn_running_list_line[running_count+272:running_count+273]
                updateFields.append('Last_8_run')
            if trn_running_list_line[running_count+273:running_count+274]:
                update_trn_running_list.Last_8_Track=trn_running_list_line[running_count+273:running_count+274]
                updateFields.append('Last_8_Track')
            if trn_running_list_line[running_count+274:running_count+276]:
                update_trn_running_list.Last_8_ST=trn_running_list_line[running_count+274:running_count+276]
                updateFields.append('Last_8_ST')
            if trn_running_list_line[running_count+276:running_count+279]:
                update_trn_running_list.Last_8_Handicap=trn_running_list_line[running_count+276:running_count+279]
                updateFields.append('Last_8_Handicap')
            if trn_running_list_line[running_count+279:running_count+280]:
                update_trn_running_list.Last_8_track_condition=trn_running_list_line[running_count+279:running_count+280]
                updateFields.append('Last_8_track_condition')

            if trn_running_list_line[running_count+280:running_count+284]:
                update_trn_running_list.Last_9_test_run_time=trn_running_list_line[running_count+280:running_count+284]
                updateFields.append('Last_9_test_run_time')
            if trn_running_list_line[running_count+284:running_count+288]:
                update_trn_running_list.Last_9_time=trn_running_list_line[running_count+284:running_count+288]
                updateFields.append('Last_9_time')
            if trn_running_list_line[running_count+288:running_count+292]:
                update_trn_running_list.Last_9_lap_time=trn_running_list_line[running_count+288:running_count+292]
                updateFields.append('Last_9_lap_time')
            if trn_running_list_line[running_count+292:running_count+293]:
                update_trn_running_list.Last_9_run=trn_running_list_line[running_count+292:running_count+293]
                updateFields.append('Last_9_run')
            if trn_running_list_line[running_count+293:running_count+294]:
                update_trn_running_list.Last_9_Track=trn_running_list_line[running_count+293:running_count+294]
                updateFields.append('Last_9_Track')
            if trn_running_list_line[running_count+294:running_count+296]:
                update_trn_running_list.Last_9_ST=trn_running_list_line[running_count+294:running_count+296]
                updateFields.append('Last_9_ST')
            if trn_running_list_line[running_count+296:running_count+299]:
                update_trn_running_list.Last_9_Handicap=trn_running_list_line[running_count+296:running_count+299]
                updateFields.append('Last_9_Handicap')
            if trn_running_list_line[running_count+299:running_count+300]:
                update_trn_running_list.Last_9_track_condition=trn_running_list_line[running_count+299:running_count+300]
                updateFields.append('Last_9_track_condition')

            if trn_running_list_line[running_count+300:running_count+304]:
                update_trn_running_list.Last_10_test_run_time=trn_running_list_line[running_count+300:running_count+304]
                updateFields.append('Last_10_test_run_time')
            if trn_running_list_line[running_count+304:running_count+308]:
                update_trn_running_list.Last_10_time=trn_running_list_line[running_count+304:running_count+308]
                updateFields.append('Last_10_time')
            if trn_running_list_line[running_count+308:running_count+312]:
                update_trn_running_list.Last_10_lap_time=trn_running_list_line[running_count+308:running_count+312]
                updateFields.append('Last_10_lap_time')
            if trn_running_list_line[running_count+312:running_count+313]:
                update_trn_running_list.Last_10_run=trn_running_list_line[running_count+312:running_count+313]
                updateFields.append('Last_10_run')
            if trn_running_list_line[running_count+313:running_count+314]:
                update_trn_running_list.Last_10_Track=trn_running_list_line[running_count+313:running_count+314]
                updateFields.append('Last_10_Track')
            if trn_running_list_line[running_count+314:running_count+316]:
                update_trn_running_list.Last_10_ST=trn_running_list_line[running_count+314:running_count+316]
                updateFields.append('Last_10_ST')
            if trn_running_list_line[running_count+316:running_count+319]:
                update_trn_running_list.Last_10_Handicap=trn_running_list_line[running_count+316:running_count+319]
                updateFields.append('Last_10_Handicap')
            if trn_running_list_line[running_count+319:running_count+320]:
                update_trn_running_list.Last_10_track_condition=trn_running_list_line[running_count+319:running_count+320]
                updateFields.append('Last_6_track_condition')

            # End 繰り返し × 10 
            if trn_running_list_line[running_count+320:running_count+324]:
                update_trn_running_list.Total_V=trn_running_list_line[running_count+320:running_count+324]
                updateFields.append('Total_V')
            if trn_running_list_line[running_count+324:running_count+328]:
                update_trn_running_list.Total_1st=trn_running_list_line[running_count+324:running_count+328]
                updateFields.append('Total_1st')
            if trn_running_list_line[running_count+328:running_count+332]:
                update_trn_running_list.v=trn_running_list_line[running_count+328:running_count+332]
                updateFields.append('Total_2nd')
            if trn_running_list_line[running_count+332:running_count+336]:
                update_trn_running_list.Total_3rd=trn_running_list_line[running_count+332:running_count+336]
                updateFields.append('Total_3rd')
            if trn_running_list_line[running_count+336:running_count+341]:
                update_trn_running_list.Total_other=trn_running_list_line[running_count+336:running_count+341]
                updateFields.append('Total_other')

            update_trn_running_list.save(update_fields=updateFields)


    def update_trn_program(self, line, trn_program):
        # 実体のあるカラム更新
        updateFields = list()

        if self.date_japanese_calendar:
            trn_program.Date_Japanese_calendar=self.date_japanese_calendar
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
        if self.race_prize_amount :
            trn_program.Race_Prize_Amount=self.race_prize_amount
            updateFields.append('Race_Prize_Amount')
        if self.handicap_open_code :
            trn_program.Handicap_Open_code=self.handicap_open_code
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
        if self.reserve :
            trn_program.Reserve=self.reserve
            updateFields.append('Reserve')
        trn_program.save(update_fields=updateFields)

    def insert_or_update_trn_program_list(self, line, repeat):

        program_count = repeat * trn_program_running_record

        self.init_trn_program()
        # shift_jis 日本語は２バイト
        # Trn_Program
        self.classification 	=	line[program_count:program_count+1]
        self.data_type 		=	line[program_count+1:program_count+2]
        self.track_code 	=	line[program_count+2:program_count+3]
        self.track_name 	=	line[program_count+3:program_count+6]
        self.date_ad 		=	line[program_count+6:program_count+14]
        self.date_japanese_calendar =	line[program_count+14:program_count+25]
        self.held_day 	=	line[program_count+25:program_count+39]
        self.period_days 	=	line[program_count+39:program_count+43]
        self.event_name 	=	line[program_count+43:program_count+63]
        self.first_day_of_the_event =	line[program_count+63:program_count+71]
        self.commemorative_code 	=	line[program_count+71:program_count+72]
        self.special_commemorative_code 	=	line[program_count+72:program_count+74]
        self.race_no 		=	line[program_count+74:program_count+76]
        self.race_name 		=	line[program_count+76:program_count+89]
        self.race_distance 		=	line[program_count+89:program_count+93]
        self.scheduled_start_time 	=	line[program_count+93:program_count+98]
        self.participation 		=	line[program_count+98:program_count+99]
        self.race_prize_amount 		=	line[program_count+99:program_count+108]
        self.handicap_open_code 	=	line[program_count+108:program_count+109]
        self.voting_code 		=	line[program_count+109:program_count+111]
        self.win_ave_totaling_date 	=	line[program_count+111:program_count+119]
        self.totaling_date 		=	line[program_count+119:program_count+127]
        self.reserve = line[program_count+2855:program_count+2979]


        # 番組編成データレコード
        Trn_Program(Classification=self.classification, Data_type=self.data_type, Track_code=self.track_code, Track_name=self.track_name \
        , Date_AD=self.date_ad, First_day_of_the_event=self.first_day_of_the_event, Race_No=self.race_no, Race_distance=self.race_distance).save()

        # 空白チェックして実体があるカラムは更新
        self.update_trn_program(line, Trn_Program.objects.get(id=Trn_Program.objects.all().aggregate(Max('id')).get('id__max')))

        # 出走選手テーブル
        self.insert_or_update_trn_running_list(line, repeat)
                    

    def insert_or_update_Trn_Program(self, fileName):
        try:
            # ファイル読み込み　データセット
   
            file = open(fileName,'r', encoding='cp932')
            for line in file:

                # Q:何度も連打すると何故かうまく行かない。A:PollingObserver使用する。
                # DB　ファイル登録
                with transaction.atomic():

                    for repeat in range(trn_program_repeat):

                        self.insert_or_update_trn_program_list(line, repeat)

            file.close()
            return NORMAL

        except FileNotFoundError as e:
            logger.warn(e)
            return ABNORMAL
        except UnboundLocalError as e:
            logger.warn(e)
            return ABNORMAL
        except ValueError as e:
            logger.warn(e)
            return ABNORMAL
        except Exception as e:
            logger.warn(e)
            return ABNORMAL
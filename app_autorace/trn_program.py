import datetime
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import sys
import time
import locale
import chardet

from logging import getLogger
from pathlib import Path

from django.db import transaction
from django.db.models import Max
# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_autorace.consts import *
from app_autorace import commons

logger = getLogger('app_autorace')

# 監視対象ファイルのパターンマッチを指定する
# 番組編成データレコード（mmddhhmmss0000J001.dat）

# target_file_program_record = '*0000[1-6]001.dat'
trn_program_repeat = 12 # 番組編成データレコードテーブル　繰り返しの数
trn_running_list = 8
trn_program_count = 127
count = 341
trn_program_running_record = 2979

class Program():

    # 出走選手テーブル 繰り返し×8
    def insert_or_update_trn_running_list(self, line, program_count, repeat, Trn_Running_list):

        for running_list_repeat in range(trn_running_list):

            running_count = count*running_list_repeat + trn_program_count
            logger.info(f'running_count :{running_count}')

            Trn_Running_list(Track_code=line[program_count+2:program_count+3], Date_AD = line[program_count+6:program_count+14]\
            , Race_No=line[program_count+74:program_count+76]).save()
            update_trn_running_list = Trn_Running_list.objects.get(id=Trn_Running_list.objects.all().aggregate(Max('id')).get('id__max'))
            updateFields = list()

            # 実体のあるカラム更新
            if line[running_count:running_count+1]:
                update_trn_running_list.Bracket_No=line[running_count:running_count+1]
                updateFields.append('Bracket_No')
            if line[running_count+1:running_count+2]:
                update_trn_running_list.Rider_No=line[running_count+1:running_count+2]
                updateFields.append('Rider_No')
            if line[running_count+2:running_count+6]:
                update_trn_running_list.Rider_code=line[running_count+2:running_count+6]
                updateFields.append('Rider_code')
            if line[running_count+6:running_count+14]:
                update_trn_running_list.Rider_full_name=line[running_count+6:running_count+14]
                updateFields.append('Rider_full_name')
            if line[running_count+14:running_count+17]:
                update_trn_running_list.Rider_shortened_3_name=line[running_count+14:running_count+17]
                updateFields.append('Rider_shortened_3_name')
            if line[running_count+17:running_count+21]:
                update_trn_running_list.Rider_shortened_4_name=line[running_count+17:running_count+21]
                updateFields.append('Rider_shortened_4_name')
            if line[running_count+21:running_count+24]:
                update_trn_running_list.LG_name=line[running_count+21:running_count+24]
                updateFields.append('LG_name')
            if line[running_count+24:running_count+25]:
                update_trn_running_list.LG_code=line[running_count+24:running_count+25]
                updateFields.append('LG_code')
            if line[running_count+25:running_count+37]:
                update_trn_running_list.Nickname=line[running_count+25:running_count+37]
                updateFields.append('Nickname')
            if line[running_count+37:running_count+38]:
                update_trn_running_list.Rider_class_code=line[running_count+37:running_count+38]
                updateFields.append('Rider_class_code')
            if line[running_count+38:running_count+39]:
                update_trn_running_list.Race_car_classification_code=line[running_count+38:running_count+39]
                updateFields.append('Race_car_classification_code')
            if line[running_count+39:running_count+42]:
                update_trn_running_list.Handicap=line[running_count+39:running_count+42]
                updateFields.append('Handicap')
            if line[running_count+42:running_count+43]:
                update_trn_running_list.Last_run_4=line[running_count+42:running_count+43]
                updateFields.append('Last_run_4')
            if line[running_count+43:running_count+44]:
                update_trn_running_list.Last_run_3=line[running_count+43:running_count+44]
                updateFields.append('Last_run_3')
            if line[running_count+44:running_count+45]:
                update_trn_running_list.Last_run_2=line[running_count+44:running_count+45]
                updateFields.append('Last_run_2')
            if line[running_count+45:running_count+46]:
                update_trn_running_list.Last_run_1=line[running_count+45:running_count+46]
                updateFields.append('Last_run_1')
            if line[running_count+46:running_count+47]:
                update_trn_running_list.Last_run_4_Track=line[running_count+46:running_count+47]
                updateFields.append('Last_run_4_Track')
            if line[running_count+47:running_count+48]:
                update_trn_running_list.Last_run_3_Track=line[running_count+47:running_count+48]
                updateFields.append('Last_run_3_Track')
            if line[running_count+48:running_count+49]:
                update_trn_running_list.Last_run_2_Track=line[running_count+48:running_count+49]
                updateFields.append('Last_run_2_Track')
            if line[running_count+49:running_count+50]:
                update_trn_running_list.Last_run_1_Track=line[running_count+49:running_count+50]
                updateFields.append('Last_run_1_Track')
            if line[running_count+50:running_count+54]:
                update_trn_running_list.Last_run_time=line[running_count+50:running_count+54]
                updateFields.append('Last_run_time')
            if line[running_count+54:running_count+58]:
                update_trn_running_list.Avg_time=line[running_count+54:running_count+58]
                updateFields.append('Avg_time')
            if line[running_count+58:running_count+62]:
                update_trn_running_list.Highest_time=line[running_count+58:running_count+62]
                updateFields.append('Highest_time')
            if line[running_count+62:running_count+65]:
                update_trn_running_list.Best_time_Track=line[running_count+62:running_count+65]
                updateFields.append('Best_time_Track')
            if line[running_count+65:running_count+68]:
                update_trn_running_list.Rider_birthplace=line[running_count+65:running_count+68]
                updateFields.append('Rider_birthplace')
            if line[running_count+68:running_count+70]:
                update_trn_running_list.Rider_Age=line[running_count+68:running_count+70]
                updateFields.append('Rider_Age')
            if line[running_count+70:running_count+72]:
                update_trn_running_list.By_period=line[running_count+70:running_count+72]
                updateFields.append('By_period')
            if line[running_count+72:running_count+76]:
                update_trn_running_list.Avg_win_1=line[running_count+72:running_count+76]
                updateFields.append('Avg_win_1')
            if line[running_count+76:running_count+80]:
                update_trn_running_list.Avg_win_2=line[running_count+76:running_count+80]
                updateFields.append('Avg_win_2')
            if line[running_count+80:running_count+84]:
                update_trn_running_list.Avg_win_3=line[running_count+80:running_count+84]
                updateFields.append('Avg_win_3')
            if line[running_count+84:running_count+88]:
                update_trn_running_list.Avg_win_1_goodrunway=line[running_count+84:running_count+88]
                updateFields.append('Avg_win_1_goodrunway')
            if line[running_count+88:running_count+92]:
                update_trn_running_list.Avg_win_2_goodrunway=line[running_count+88:running_count+92]
                updateFields.append('Avg_win_2_goodrunway')
            if line[running_count+92:running_count+96]:
                update_trn_running_list.Avg_win_3_goodrunway=line[running_count+92:running_count+96]
                updateFields.append('Avg_win_3_goodrunway')
            if line[running_count+96:running_count+100]:
                update_trn_running_list.Avg_win_1_Wetrunway=line[running_count+96:running_count+100]
                updateFields.append('Avg_win_1_Wetrunway')
            if line[running_count+100:running_count+104]:
                update_trn_running_list.Avg_win_2_Wetrunway=line[running_count+100:running_count+104]
                updateFields.append('Avg_win_2_Wetrunway')
            if line[running_count+104:running_count+108]:
                update_trn_running_list.Avg_win_3_Wetrunway=line[running_count+104:running_count+108]
                updateFields.append('Avg_win_3_Wetrunway')
            if line[running_count+108:running_count+112]:
                update_trn_running_list.Avg_win_1_ohter=line[running_count+108:running_count+112]
                updateFields.append('Avg_win_1_ohter')
            if line[running_count+112:running_count+116]:
                update_trn_running_list.Avg_win_2_ohter=line[running_count+112:running_count+116]
                updateFields.append('Avg_win_2_ohter')
            if line[running_count+116:running_count+120]:
                update_trn_running_list.Avg_win_3_ohter=line[running_count+116:running_count+120]
                updateFields.append('Avg_win_3_ohter')

            # 繰り返し　×　10　過去１走前～１０走前の順
            if line[running_count+120:running_count+124]:
                update_trn_running_list.Last_1_test_run_time=line[running_count+120:running_count+124]
                updateFields.append('Last_1_test_run_time')
            if line[running_count+124:running_count+128]:
                update_trn_running_list.Last_1_time=line[running_count+124:running_count+128]
                updateFields.append('Last_1_time')
            if line[running_count+128:running_count+132]:
                update_trn_running_list.Last_1_lap_time=line[running_count+128:running_count+132]
                updateFields.append('Last_1_lap_time')
            if line[running_count+132:running_count+133]:
                update_trn_running_list.Last_1_run=line[running_count+132:running_count+133]
                updateFields.append('Last_1_run')
            if line[running_count+133:running_count+134]:
                update_trn_running_list.Last_1_Track=line[running_count+133:running_count+134]
                updateFields.append('Last_1_Track')
            if line[running_count+134:running_count+136]:
                update_trn_running_list.Last_1_ST=line[running_count+134:running_count+136]
                updateFields.append('Last_1_ST')
            if line[running_count+136:running_count+139]:
                update_trn_running_list.Last_1_Handicap=line[running_count+136:running_count+139]
                updateFields.append('Last_1_Handicap')
            if line[running_count+139:running_count+140]:
                update_trn_running_list.Last_1_track_condition=line[running_count+139:running_count+140]
                updateFields.append('Last_1_track_condition')

            if line[running_count+140:running_count+144]:
                update_trn_running_list.Last_2_test_run_time=line[running_count+140:running_count+144]
                updateFields.append('Last_2_test_run_time')
            if line[running_count+144:running_count+148]:
                update_trn_running_list.Last_2_time=line[running_count+144:running_count+148]
                updateFields.append('Last_2_time')
            if line[running_count+148:running_count+152]:
                update_trn_running_list.Last_2_lap_time=line[running_count+148:running_count+152]
                updateFields.append('Last_2_lap_time')
            if line[running_count+152:running_count+153]:
                update_trn_running_list.Last_2_run=line[running_count+152:running_count+153]
                updateFields.append('Last_2_run')
            if line[running_count+153:running_count+154]:
                update_trn_running_list.Last_2_Track=line[running_count+153:running_count+154]
                updateFields.append('Last_2_Track')
            if line[running_count+154:running_count+156]:
                update_trn_running_list.Last_2_ST=line[running_count+154:running_count+156]
                updateFields.append('Last_2_ST')
            if line[running_count+156:running_count+159]:
                update_trn_running_list.Last_2_Handicap=line[running_count+156:running_count+159]
                updateFields.append('Last_2_Handicap')
            if line[running_count+159:running_count+160]:
                update_trn_running_list.Last_2_track_condition=line[running_count+159:running_count+160]
                updateFields.append('Last_2_track_condition')

            if line[running_count+160:running_count+164]:
                update_trn_running_list.Last_3_test_run_time=line[running_count+160:running_count+164]
                updateFields.append('Last_3_test_run_time')
            if line[running_count+164:running_count+168]:
                update_trn_running_list.Last_3_time=line[running_count+164:running_count+168]
                updateFields.append('Last_3_time')
            if line[running_count+168:running_count+172]:
                update_trn_running_list.Last_3_lap_time=line[running_count+168:running_count+172]
                updateFields.append('Last_3_lap_time')
            if line[running_count+172:running_count+173]:
                update_trn_running_list.Last_3_run=line[running_count+172:running_count+173]
                updateFields.append('Last_3_run')
            if line[running_count+173:running_count+174]:
                update_trn_running_list.Last_3_Track=line[running_count+173:running_count+174]
                updateFields.append('Last_3_Track')
            if line[running_count+174:running_count+176]:
                update_trn_running_list.Last_3_ST=line[running_count+174:running_count+176]
                updateFields.append('Last_3_ST')
            if line[running_count+176:running_count+179]:
                update_trn_running_list.Last_3_Handicap=line[running_count+176:running_count+179]
                updateFields.append('Last_3_Handicap')
            if line[running_count+179:running_count+180]:
                update_trn_running_list.Last_3_track_condition=line[running_count+179:running_count+180]
                updateFields.append('Last_3_track_condition')

            if line[running_count+180:running_count+184]:
                update_trn_running_list.Last_4_test_run_time=line[running_count+180:running_count+184]
                updateFields.append('Last_4_test_run_time')
            if line[running_count+184:running_count+188]:
                update_trn_running_list.Last_4_time=line[running_count+184:running_count+188]
                updateFields.append('Last_4_time')
            if line[running_count+188:running_count+192]:
                update_trn_running_list.Last_4_lap_time=line[running_count+188:running_count+192]
                updateFields.append('Last_4_lap_time')
            if line[running_count+192:running_count+193]:
                update_trn_running_list.Last_4_run=line[running_count+192:running_count+193]
                updateFields.append('Last_4_run')
            if line[running_count+193:running_count+194]:
                update_trn_running_list.Last_4_Track=line[running_count+193:running_count+194]
                updateFields.append('Last_4_Track')
            if line[running_count+194:running_count+196]:
                update_trn_running_list.Last_4_ST=line[running_count+194:running_count+196]
                updateFields.append('Last_4_ST')
            if line[running_count+196:running_count+199]:
                update_trn_running_list.Last_4_Handicap=line[running_count+196:running_count+199]
                updateFields.append('Last_4_Handicap')
            if line[running_count+199:running_count+200]:
                update_trn_running_list.Last_4_track_condition=line[running_count+199:running_count+200]
                updateFields.append('Last_4_track_condition')

            if line[running_count+200:running_count+204]:
                update_trn_running_list.Last_5_test_run_time=line[running_count+200:running_count+204]
                updateFields.append('Last_5_test_run_time')
            if line[running_count+204:running_count+208]:
                update_trn_running_list.Last_5_time=line[running_count+204:running_count+208]
                updateFields.append('Last_5_time')
            if line[running_count+208:running_count+212]:
                update_trn_running_list.Last_5_lap_time=line[running_count+208:running_count+212]
                updateFields.append('Last_5_lap_time')
            if line[running_count+212:running_count+213]:
                update_trn_running_list.Last_5_run=line[running_count+212:running_count+213]
                updateFields.append('Last_5_run')
            if line[running_count+213:running_count+214]:
                update_trn_running_list.Last_5_Track=line[running_count+213:running_count+214]
                updateFields.append('Last_5_Track')
            if line[running_count+214:running_count+216]:
                update_trn_running_list.Last_5_ST=line[running_count+214:running_count+216]
                updateFields.append('Last_5_ST')
            if line[running_count+216:running_count+219]:
                update_trn_running_list.Last_5_Handicap=line[running_count+216:running_count+219]
                updateFields.append('Last_5_Handicap')
            if line[running_count+219:running_count+220]:
                update_trn_running_list.Last_5_track_condition=line[running_count+219:running_count+220]
                updateFields.append('Last_5_track_condition')

            if line[running_count+220:running_count+224]:
                update_trn_running_list.Last_6_test_run_time=line[running_count+220:running_count+224]
                updateFields.append('Last_6_test_run_time')
            if line[running_count+224:running_count+228]:
                update_trn_running_list.Last_6_time=line[running_count+224:running_count+228]
                updateFields.append('Last_6_time')
            if line[running_count+228:running_count+232]:
                update_trn_running_list.Last_6_lap_time=line[running_count+228:running_count+232]
                updateFields.append('Last_6_lap_time')
            if line[running_count+232:running_count+233]:
                update_trn_running_list.Last_6_run=line[running_count+232:running_count+233]
                updateFields.append('Last_6_run')
            if line[running_count+233:running_count+234]:
                update_trn_running_list.Last_6_Track=line[running_count+233:running_count+234]
                updateFields.append('Last_6_Track')
            if line[running_count+234:running_count+236]:
                update_trn_running_list.Last_6_ST=line[running_count+234:running_count+236]
                updateFields.append('Last_6_ST')
            if line[running_count+236:running_count+239]:
                update_trn_running_list.Last_6_Handicap=line[running_count+236:running_count+239]
                updateFields.append('Last_6_Handicap')
            if line[running_count+239:running_count+240]:
                update_trn_running_list.Last_6_track_condition=line[running_count+239:running_count+240]
                updateFields.append('Last_6_track_condition')

            if line[running_count+240:running_count+244]:
                update_trn_running_list.Last_7_test_run_time=line[running_count+240:running_count+244]
                updateFields.append('Last_7_test_run_time')
            if line[running_count+244:running_count+248]:
                update_trn_running_list.Last_7_time=line[running_count+244:running_count+248]
                updateFields.append('Last_7_time')
            if line[running_count+248:running_count+252]:
                update_trn_running_list.Last_7_lap_time=line[running_count+248:running_count+252]
                updateFields.append('Last_7_lap_time')
            if line[running_count+252:running_count+253]:
                update_trn_running_list.Last_7_run=line[running_count+252:running_count+253]
                updateFields.append('Last_7_run')
            if line[running_count+253:running_count+254]:
                update_trn_running_list.Last_7_Track=line[running_count+253:running_count+254]
                updateFields.append('Last_7_Track')
            if line[running_count+254:running_count+256]:
                update_trn_running_list.Last_7_ST=line[running_count+254:running_count+256]
                updateFields.append('Last_7_ST')
            if line[running_count+256:running_count+259]:
                update_trn_running_list.Last_7_Handicap=line[running_count+256:running_count+259]
                updateFields.append('Last_7_Handicap')
            if line[running_count+259:running_count+260]:
                update_trn_running_list.Last_7_track_condition=line[running_count+259:running_count+260]
                updateFields.append('Last_7_track_condition')

            if line[running_count+260:running_count+264]:
                update_trn_running_list.Last_8_test_run_time=line[running_count+260:running_count+264]
                updateFields.append('Last_8_test_run_time')
            if line[running_count+264:running_count+268]:
                update_trn_running_list.Last_8_time=line[running_count+264:running_count+268]
                updateFields.append('Last_8_time')
            if line[running_count+268:running_count+272]:
                update_trn_running_list.Last_8_lap_time=line[running_count+268:running_count+272]
                updateFields.append('Last_8_lap_time')
            if line[running_count+272:running_count+273]:
                update_trn_running_list.Last_8_run=line[running_count+272:running_count+273]
                updateFields.append('Last_8_run')
            if line[running_count+273:running_count+274]:
                update_trn_running_list.Last_8_Track=line[running_count+273:running_count+274]
                updateFields.append('Last_8_Track')
            if line[running_count+274:running_count+276]:
                update_trn_running_list.Last_8_ST=line[running_count+274:running_count+276]
                updateFields.append('Last_8_ST')
            if line[running_count+276:running_count+279]:
                update_trn_running_list.Last_8_Handicap=line[running_count+276:running_count+279]
                updateFields.append('Last_8_Handicap')
            if line[running_count+279:running_count+280]:
                update_trn_running_list.Last_8_track_condition=line[running_count+279:running_count+280]
                updateFields.append('Last_8_track_condition')

            if line[running_count+280:running_count+284]:
                update_trn_running_list.Last_9_test_run_time=line[running_count+280:running_count+284]
                updateFields.append('Last_9_test_run_time')
            if line[running_count+284:running_count+288]:
                update_trn_running_list.Last_9_time=line[running_count+284:running_count+288]
                updateFields.append('Last_9_time')
            if line[running_count+288:running_count+292]:
                update_trn_running_list.Last_9_lap_time=line[running_count+288:running_count+292]
                updateFields.append('Last_9_lap_time')
            if line[running_count+292:running_count+293]:
                update_trn_running_list.Last_9_run=line[running_count+292:running_count+293]
                updateFields.append('Last_9_run')
            if line[running_count+293:running_count+294]:
                update_trn_running_list.Last_9_Track=line[running_count+293:running_count+294]
                updateFields.append('Last_9_Track')
            if line[running_count+294:running_count+296]:
                update_trn_running_list.Last_9_ST=line[running_count+294:running_count+296]
                updateFields.append('Last_9_ST')
            if line[running_count+296:running_count+299]:
                update_trn_running_list.Last_9_Handicap=line[running_count+296:running_count+299]
                updateFields.append('Last_9_Handicap')
            if line[running_count+299:running_count+300]:
                update_trn_running_list.Last_9_track_condition=line[running_count+299:running_count+300]
                updateFields.append('Last_9_track_condition')

            if line[running_count+300:running_count+304]:
                update_trn_running_list.Last_10_test_run_time=line[running_count+300:running_count+304]
                updateFields.append('Last_10_test_run_time')
            if line[running_count+304:running_count+308]:
                update_trn_running_list.Last_10_time=line[running_count+304:running_count+308]
                updateFields.append('Last_10_time')
            if line[running_count+308:running_count+312]:
                update_trn_running_list.Last_10_lap_time=line[running_count+308:running_count+312]
                updateFields.append('Last_10_lap_time')
            if line[running_count+312:running_count+313]:
                update_trn_running_list.Last_10_run=line[running_count+312:running_count+313]
                updateFields.append('Last_10_run')
            if line[running_count+313:running_count+314]:
                update_trn_running_list.Last_10_Track=line[running_count+313:running_count+314]
                updateFields.append('Last_10_Track')
            if line[running_count+314:running_count+316]:
                update_trn_running_list.Last_10_ST=line[running_count+314:running_count+316]
                updateFields.append('Last_10_ST')
            if line[running_count+316:running_count+319]:
                update_trn_running_list.Last_10_Handicap=line[running_count+316:running_count+319]
                updateFields.append('Last_10_Handicap')
            if line[running_count+319:running_count+320]:
                update_trn_running_list.Last_10_track_condition=line[running_count+319:running_count+320]
                updateFields.append('Last_6_track_condition')

            # End 繰り返し × 10
            if line[running_count+320:running_count+324]:
                update_trn_running_list.Total_V=line[running_count+320:running_count+324]
                updateFields.append('Total_V')
            if line[running_count+324:running_count+328]:
                update_trn_running_list.Total_1st=line[running_count+324:running_count+328]
                updateFields.append('Total_1st')
            if line[running_count+328:running_count+332]:
                update_trn_running_list.v=line[running_count+328:running_count+332]
                updateFields.append('Total_2nd')
            if line[running_count+332:running_count+336]:
                update_trn_running_list.Total_3rd=line[running_count+332:running_count+336]
                updateFields.append('Total_3rd')
            if line[running_count+336:running_count+341]:
                update_trn_running_list.Total_other=line[running_count+336:running_count+341]
                updateFields.append('Total_other')

            update_trn_running_list.save(update_fields=updateFields)


    def update_trn_program(self, line, program_count, trn_program):
        # 実体のあるカラム更新
        updateFields = list()

        if line[program_count+25:program_count+39]:
            trn_program.Held_day=line[program_count+25:program_count+39]
            updateFields.append('Held_day')
        if line[program_count+39:program_count+43]:
            trn_program.Period_days=line[program_count+39:program_count+43]
            updateFields.append('Period_days')
        if line[program_count+43:program_count+63]:
            trn_program.Event_name=line[program_count+43:program_count+63]
            updateFields.append('Event_name')
        if line[program_count+71:program_count+72]:
            trn_program.Commemorative_code=line[program_count+71:program_count+72]
            updateFields.append('Commemorative_code')
        if line[program_count+72:program_count+74]:
            trn_program.Special_commemorative_code=line[program_count+72:program_count+74]
            updateFields.append('Special_commemorative_code')
        if line[program_count+76:program_count+89]:
            trn_program.Race_name=line[program_count+76:program_count+89]
            updateFields.append('Race_name')
        if line[program_count+98:program_count+99]:
            trn_program.Participation=line[program_count+98:program_count+99]
            updateFields.append('Participation')
        if line[program_count+99:program_count+108]:
            trn_program.Race_Prize_Amount=line[program_count+99:program_count+108]
            updateFields.append('Race_Prize_Amount')
        if line[program_count+108:program_count+109]:
            trn_program.Handicap_Open_code=line[program_count+108:program_count+109]
            updateFields.append('Handicap_Open_code')
        if line[program_count+109:program_count+111]:
            trn_program.Voting_code=line[program_count+109:program_count+111]
            updateFields.append('Voting_code')
        if line[program_count+111:program_count+119]:
            trn_program.Win_Ave_Totaling_Date=line[program_count+111:program_count+119]
            updateFields.append('Win_Ave_Totaling_Date')
        if line[program_count+119:program_count+127]:
            trn_program.Totaling_date=line[program_count+119:program_count+127]
            updateFields.append('Totaling_date')
        if line[program_count+2855:program_count+2979]:
            trn_program.Reserve=line[program_count+2855:program_count+2979]
            updateFields.append('Reserve')
        trn_program.save(update_fields=updateFields)

    def insert_or_update_trn_program_list(self, line, program_count, repeat, Trn_Program, Trn_Running_list):

        # shift_jis 日本語は２バイト
        # Trn_Program
        # 番組編成データレコード
        Trn_Program(Classification=line[program_count:program_count+1], Data_type=line[program_count+1:program_count+2]\
        , Track_code=line[program_count+2:program_count+3], Track_name=line[program_count+3:program_count+6]\
        , Date_AD=line[program_count+6:program_count+14], Date_Japanese_calendar=line[program_count+14:program_count+25]\
        , First_day_of_the_event=line[program_count+63:program_count+71], Race_No=line[program_count+74:program_count+76]\
        , Race_distance=line[program_count+89:program_count+93], Scheduled_start_time=line[program_count+93:program_count+98]).save()

        # 空白チェックして実体があるカラムは更新
        logger.info( f'内容:update_trn_program Start : {repeat}')
        self.update_trn_program(line ,program_count ,Trn_Program.objects.get(id=Trn_Program.objects.all().aggregate(Max('id')).get('id__max')))
        logger.info( "内容:update_trn_program End")

        # 出走選手テーブル
        logger.info( f'内容:insert_or_update_trn_running_list Start : {repeat}')
        self.insert_or_update_trn_running_list(line, program_count, repeat, Trn_Running_list)
        logger.info( "内容:insert_or_update_trn_running_list End")


    def insert_or_update_Trn_Program(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_autorace.models import Trn_Program, Trn_Running_list
            cmn = commons.Common()

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            file = open(fileName,'r', encoding='cp932')
            for line in file:

                # ファイル文字サイズ
                logger.info(f'{fileName}はファイルサイズ{len(line)}')

                # Q:何度も連打すると何故かうまく行かない。A:PollingObserver使用する。
                # DB　ファイル登録
                with transaction.atomic():

                    for repeat in range(trn_program_repeat):

                        program_count = repeat * trn_program_running_record

                        # insert チェックする。データがからのときはスキップ
                        chkline = line[program_count:]
                        # logger.info(f'データチェック :{chkline}') # 量が多いので
                        if not cmn.chkBlank(chkline):
                            logger.info( "データチェックがからのため End")
                            break

                        logger.info( f'内容:insert_or_update_trn_program_list Start:詳細:ファイルデータ: outsidetrack_record :{repeat}' )
                        self.insert_or_update_trn_program_list(line, program_count, repeat, Trn_Program, Trn_Running_list)
                        logger.info( "内容:insert_Trn_Outside_track End")

            file.close()
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

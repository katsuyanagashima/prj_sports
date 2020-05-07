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

from app_autorace.consts import *
from app_autorace import commons

logger = getLogger('app_autorace')

# 監視対象ファイルのパターンマッチを指定する
# 場外売場情報レコード（mmddhhmmss00000004.dat）


outsidetrack_repeat = 6 # 場情報　繰り返しの数
outsidetrackNum = 472

class Outside_track():

    def update_trn_outside_track(self, outsidetrack, outsidetrackLine, trn_Update):
        updateFields = list()

        # 場情報  繰り返しの数
        if outsidetrackLine[outsidetrack:outsidetrack+1]:
            trn_Update.Track_code=outsidetrackLine[outsidetrack:outsidetrack+1]
            updateFields.append('Track_code')
        if outsidetrackLine[outsidetrack+1:outsidetrack+4]:
            trn_Update.Track_name=outsidetrackLine[outsidetrack+1:outsidetrack+4]
            updateFields.append('Track_name')
        if outsidetrackLine[outsidetrack+4:outsidetrack+12]:
            trn_Update.Date_AD= outsidetrackLine[outsidetrack+4:outsidetrack+12]
            updateFields.append('Date_AD')
        if outsidetrackLine[outsidetrack+12:outsidetrack+23]:
            trn_Update.Date_Japanese_calendar= outsidetrackLine[outsidetrack+12:outsidetrack+23]
            updateFields.append('Date_Japanese_calendar')
        if outsidetrackLine[outsidetrack+23:outsidetrack+37]:
            trn_Update.Held_day= outsidetrackLine[outsidetrack+23:outsidetrack+37]
            updateFields.append('Held_day')
        if outsidetrackLine[outsidetrack+37:outsidetrack+41]:
            trn_Update.Period_days= outsidetrackLine[outsidetrack+37:outsidetrack+41]
            updateFields.append('Period_days')
        if outsidetrackLine[outsidetrack+41:outsidetrack+61]:
            trn_Update.Event_name= outsidetrackLine[outsidetrack+41:outsidetrack+61]
            updateFields.append('Event_name')
        if outsidetrackLine[outsidetrack+61:outsidetrack+69]:
            trn_Update.First_day_of_the_event= outsidetrackLine[61:69]
            updateFields.append('First_day_of_the_event')
        if outsidetrackLine[outsidetrack+69:outsidetrack+70]:
            trn_Update.Commemorative_code=outsidetrackLine[outsidetrack+69:outsidetrack+70]
            updateFields.append('Commemorative_code')
        if outsidetrackLine[outsidetrack+70:outsidetrack+72]:
            trn_Update.Special_commemorative_code=outsidetrackLine[outsidetrack+70:outsidetrack+72]
            updateFields.append('Special_commemorative_code')

        # 場外売場情報 繰り返し 1×20
        if outsidetrackLine[outsidetrack+72:outsidetrack+73]:
            trn_Update.OTB_code_1=outsidetrackLine[outsidetrack+72:outsidetrack+73]
            updateFields.append('OTB_code_1')
        if outsidetrackLine[outsidetrack+73:outsidetrack+76]:
            trn_Update.OTB_1=outsidetrackLine[outsidetrack+73:outsidetrack+76]
            updateFields.append('OTB_1')
        if outsidetrackLine[outsidetrack+76:outsidetrack+77]:
            trn_Update.OTB_Classification_1=outsidetrackLine[outsidetrack+76:outsidetrack+77]
            updateFields.append('OTB_Classification_1')
        if outsidetrackLine[outsidetrack+77:outsidetrack+78]:
            trn_Update.Held_Classification_1=outsidetrackLine[outsidetrack+77:outsidetrack+78]
            updateFields.append('Held_Classification_1')
        if outsidetrackLine[outsidetrack+78:outsidetrack+80]:
            trn_Update.Note_code_1=outsidetrackLine[outsidetrack+78:outsidetrack+80]
            updateFields.append('Note_code_1')
        if outsidetrackLine[outsidetrack+80:outsidetrack+81]:
            trn_Update.race_1_1=outsidetrackLine[outsidetrack+80:outsidetrack+81]
            updateFields.append('race_1_1')
        if outsidetrackLine[outsidetrack+81:outsidetrack+82]:
            trn_Update.race_2_1=outsidetrackLine[outsidetrack+81:outsidetrack+82]
            updateFields.append('race_2_1')
        if outsidetrackLine[outsidetrack+82:outsidetrack+83]:
            trn_Update.race_3_1=outsidetrackLine[outsidetrack+82:outsidetrack+83]
            updateFields.append('race_3_1')
        if outsidetrackLine[outsidetrack+83:outsidetrack+84]:
            trn_Update.race_4_1=outsidetrackLine[outsidetrack+83:outsidetrack+84]
            updateFields.append('race_4_1')
        if outsidetrackLine[outsidetrack+84:outsidetrack+85]:
            trn_Update.race_5_1=outsidetrackLine[outsidetrack+84:outsidetrack+85]
            updateFields.append('race_5_1')
        if outsidetrackLine[outsidetrack+85:outsidetrack+86]:
            trn_Update.race_6_1=outsidetrackLine[outsidetrack+85:outsidetrack+86]
            updateFields.append('race_6_1')
        if outsidetrackLine[outsidetrack+86:outsidetrack+87]:
            trn_Update.race_7_1=outsidetrackLine[outsidetrack+86:outsidetrack+87]
            updateFields.append('race_7_1')
        if outsidetrackLine[outsidetrack+87:outsidetrack+88]:
            trn_Update.race_8_1=outsidetrackLine[outsidetrack+87:outsidetrack+88]
            updateFields.append('race_8_1')
        if outsidetrackLine[outsidetrack+88:outsidetrack+89]:
            trn_Update.race_9_1=outsidetrackLine[outsidetrack+88:outsidetrack+89]
            updateFields.append('race_9_1')
        if outsidetrackLine[outsidetrack+89:outsidetrack+90]:
            trn_Update.race_10_1=outsidetrackLine[outsidetrack+89:outsidetrack+90]
            updateFields.append('race_10_1')
        if outsidetrackLine[outsidetrack+90:outsidetrack+91]:
            trn_Update.race_11_1=outsidetrackLine[outsidetrack+90:outsidetrack+91]
            updateFields.append('race_11_1')
        if outsidetrackLine[outsidetrack+91:outsidetrack+92]:
            trn_Update.race_12_1=outsidetrackLine[outsidetrack+91:outsidetrack+92]
            updateFields.append('race_12_1')

        # 場外売場情報 繰り返し 2×20
        if outsidetrackLine[outsidetrack+92:outsidetrack+93]:
            trn_Update.OTB_code_2=outsidetrackLine[outsidetrack+92:outsidetrack+93]
            updateFields.append('OTB_code_2')
        if outsidetrackLine[outsidetrack+93:outsidetrack+96]:
            trn_Update.OTB_2=outsidetrackLine[outsidetrack+93:outsidetrack+96]
            updateFields.append('OTB_2')
        if outsidetrackLine[outsidetrack+96:outsidetrack+97]:
            trn_Update.OTB_Classification_2=outsidetrackLine[outsidetrack+96:outsidetrack+97]
            updateFields.append('OTB_Classification_2')
        if outsidetrackLine[outsidetrack+97:outsidetrack+98]:
            trn_Update.Held_Classification_2=outsidetrackLine[outsidetrack+97:outsidetrack+98]
            updateFields.append('Held_Classification_2')
        if outsidetrackLine[outsidetrack+98:outsidetrack+100]:
            trn_Update.Note_code_2=outsidetrackLine[outsidetrack+98:outsidetrack+100]
            updateFields.append('Note_code_2')
        if outsidetrackLine[outsidetrack+100:outsidetrack+101]:
            trn_Update.race_1_2=outsidetrackLine[outsidetrack+100:outsidetrack+101]
            updateFields.append('race_1_2')
        if outsidetrackLine[outsidetrack+101:outsidetrack+102]:
            trn_Update.race_2_2=outsidetrackLine[outsidetrack+101:outsidetrack+102]
            updateFields.append('race_2_2')
        if outsidetrackLine[outsidetrack+102:outsidetrack+103]:
            trn_Update.race_3_2=outsidetrackLine[outsidetrack+102:outsidetrack+103]
            updateFields.append('race_3_2')
        if outsidetrackLine[outsidetrack+103:outsidetrack+104]:
            trn_Update.race_4_2=outsidetrackLine[outsidetrack+103:outsidetrack+104]
            updateFields.append('race_4_2')
        if outsidetrackLine[outsidetrack+104:outsidetrack+105]:
            trn_Update.race_5_2=outsidetrackLine[outsidetrack+104:outsidetrack+105]
            updateFields.append('race_5_2')
        if outsidetrackLine[outsidetrack+105:outsidetrack+106]:
            trn_Update.race_6_2=outsidetrackLine[outsidetrack+105:outsidetrack+106]
            updateFields.append('race_6_2')
        if outsidetrackLine[outsidetrack+106:outsidetrack+107]:
            trn_Update.race_7_2=outsidetrackLine[outsidetrack+106:outsidetrack+107]
            updateFields.append('race_7_2')
        if outsidetrackLine[outsidetrack+107:outsidetrack+108]:
            trn_Update.race_8_2=outsidetrackLine[outsidetrack+107:outsidetrack+108]
            updateFields.append('race_8_2')
        if outsidetrackLine[outsidetrack+108:outsidetrack+109]:
            trn_Update.race_9_2=outsidetrackLine[outsidetrack+108:outsidetrack+109]
            updateFields.append('race_9_2')
        if outsidetrackLine[outsidetrack+109:outsidetrack+110]:
            trn_Update.race_10_2=outsidetrackLine[outsidetrack+109:outsidetrack+110]
            updateFields.append('race_10_2')
        if outsidetrackLine[outsidetrack+110:outsidetrack+111]:
            trn_Update.race_11_2=outsidetrackLine[outsidetrack+110:outsidetrack+111]
            updateFields.append('race_11_2')
        if outsidetrackLine[outsidetrack+111:outsidetrack+112]:
            trn_Update.race_12_2=outsidetrackLine[outsidetrack+111:outsidetrack+112]
            updateFields.append('race_12_2')

        # 場外売場情報 繰り返し 3×20
        if outsidetrackLine[outsidetrack+112:outsidetrack+113]:
            trn_Update.OTB_code_3=outsidetrackLine[outsidetrack+112:outsidetrack+113]
            updateFields.append('OTB_code_3')
        if outsidetrackLine[outsidetrack+113:outsidetrack+116]:
            trn_Update.OTB_3=outsidetrackLine[outsidetrack+113:outsidetrack+116]
            updateFields.append('OTB_3')
        if outsidetrackLine[outsidetrack+116:outsidetrack+117]:
            trn_Update.OTB_Classification_3=outsidetrackLine[outsidetrack+116:outsidetrack+117]
            updateFields.append('OTB_Classification_3')
        if outsidetrackLine[outsidetrack+117:outsidetrack+118]:
            trn_Update.Held_Classification_3=outsidetrackLine[outsidetrack+117:outsidetrack+118]
            updateFields.append('Held_Classification_3')
        if outsidetrackLine[outsidetrack+118:outsidetrack+120]:
            trn_Update.Note_code_3=outsidetrackLine[outsidetrack+118:outsidetrack+120]
            updateFields.append('Note_code_3')
        if outsidetrackLine[outsidetrack+120:outsidetrack+121]:
            trn_Update.race_1_3=outsidetrackLine[outsidetrack+120:outsidetrack+121]
            updateFields.append('race_1_3')
        if outsidetrackLine[outsidetrack+121:outsidetrack+122]:
            trn_Update.race_2_3=outsidetrackLine[outsidetrack+121:outsidetrack+122]
            updateFields.append('race_2_3')
        if outsidetrackLine[outsidetrack+122:outsidetrack+123]:
            trn_Update.race_3_3=outsidetrackLine[outsidetrack+122:outsidetrack+123]
            updateFields.append('race_3_3')
        if outsidetrackLine[outsidetrack+123:outsidetrack+124]:
            trn_Update.race_4_3=outsidetrackLine[outsidetrack+123:outsidetrack+124]
            updateFields.append('race_4_3')
        if outsidetrackLine[outsidetrack+124:outsidetrack+125]:
            trn_Update.race_5_3=outsidetrackLine[outsidetrack+124:outsidetrack+125]
            updateFields.append('race_5_3')
        if outsidetrackLine[outsidetrack+125:outsidetrack+126]:
            trn_Update.race_6_3=outsidetrackLine[outsidetrack+125:outsidetrack+126]
            updateFields.append('race_6_3')
        if outsidetrackLine[outsidetrack+126:outsidetrack+127]:
            trn_Update.race_7_3=outsidetrackLine[outsidetrack+126:outsidetrack+127]
            updateFields.append('race_7_3')
        if outsidetrackLine[outsidetrack+127:outsidetrack+128]:
            trn_Update.race_12_3=outsidetrackLine[outsidetrack+127:outsidetrack+128]
            updateFields.append('race_8_3')
        if outsidetrackLine[outsidetrack+128:outsidetrack+129]:
            trn_Update.race_9_3=outsidetrackLine[outsidetrack+128:outsidetrack+129]
            updateFields.append('race_9_3')
        if outsidetrackLine[outsidetrack+129:outsidetrack+130]:
            trn_Update.race_10_3=outsidetrackLine[outsidetrack+129:outsidetrack+130]
            updateFields.append('race_10_3')
        if outsidetrackLine[outsidetrack+130:outsidetrack+131]:
            trn_Update.race_11_3=outsidetrackLine[outsidetrack+130:outsidetrack+131]
            updateFields.append('race_11_3')
        if outsidetrackLine[outsidetrack+131:outsidetrack+132]:
            trn_Update.race_12_3=outsidetrackLine[outsidetrack+131:outsidetrack+132]
            updateFields.append('race_12_3')

        # 場外売場情報 繰り返し 4×20
        if outsidetrackLine[outsidetrack+132:outsidetrack+133]:
            trn_Update.OTB_code_4=outsidetrackLine[outsidetrack+132:outsidetrack+133]
            updateFields.append('OTB_code_4')
        if outsidetrackLine[outsidetrack+133:outsidetrack+136]:
            trn_Update.OTB_4=outsidetrackLine[outsidetrack+133:outsidetrack+136]
            updateFields.append('OTB_4')
        if outsidetrackLine[outsidetrack+136:outsidetrack+137]:
            trn_Update.OTB_Classification_4=outsidetrackLine[outsidetrack+136:outsidetrack+137]
            updateFields.append('OTB_Classification_4')
        if outsidetrackLine[outsidetrack+137:outsidetrack+138]:
            trn_Update.Held_Classification_4=outsidetrackLine[outsidetrack+137:outsidetrack+138]
            updateFields.append('Held_Classification_4')
        if outsidetrackLine[outsidetrack+138:outsidetrack+140]:
            trn_Update.Note_code_4=outsidetrackLine[outsidetrack+138:outsidetrack+140]
            updateFields.append('Note_code_4')
        if outsidetrackLine[outsidetrack+140:outsidetrack+141]:
            trn_Update.race_1_4=outsidetrackLine[outsidetrack+140:outsidetrack+141]
            updateFields.append('race_1_4')
        if outsidetrackLine[outsidetrack+141:outsidetrack+142]:
            trn_Update.race_2_4=outsidetrackLine[outsidetrack+141:outsidetrack+142]
            updateFields.append('race_2_4')
        if outsidetrackLine[outsidetrack+142:outsidetrack+143]:
            trn_Update.race_3_4=outsidetrackLine[outsidetrack+142:outsidetrack+143]
            updateFields.append('race_3_4')
        if outsidetrackLine[outsidetrack+143:outsidetrack+144]:
            trn_Update.race_4_4=outsidetrackLine[outsidetrack+143:outsidetrack+144]
            updateFields.append('race_4_4')
        if outsidetrackLine[outsidetrack+144:outsidetrack+145]:
            trn_Update.race_5_4=outsidetrackLine[outsidetrack+144:outsidetrack+145]
            updateFields.append('race_5_4')
        if outsidetrackLine[outsidetrack+145:outsidetrack+146]:
            trn_Update.race_6_4=outsidetrackLine[outsidetrack+145:outsidetrack+146]
            updateFields.append('race_6_4')
        if outsidetrackLine[outsidetrack+146:outsidetrack+147]:
            trn_Update.race_7_4=outsidetrackLine[outsidetrack+146:outsidetrack+147]
            updateFields.append('race_7_4')
        if outsidetrackLine[outsidetrack+147:outsidetrack+148]:
            trn_Update.race_14_4=outsidetrackLine[outsidetrack+147:outsidetrack+148]
            updateFields.append('race_8_4')
        if outsidetrackLine[outsidetrack+148:outsidetrack+149]:
            trn_Update.race_9_4=outsidetrackLine[outsidetrack+148:outsidetrack+149]
            updateFields.append('race_9_4')
        if outsidetrackLine[outsidetrack+149:outsidetrack+150]:
            trn_Update.race_10_4=outsidetrackLine[outsidetrack+149:outsidetrack+150]
            updateFields.append('race_10_4')
        if outsidetrackLine[outsidetrack+150:outsidetrack+151]:
            trn_Update.race_11_4=outsidetrackLine[outsidetrack+150:outsidetrack+151]
            updateFields.append('race_11_4')
        if outsidetrackLine[outsidetrack+151:outsidetrack+152]:
            trn_Update.race_12_4=outsidetrackLine[outsidetrack+151:outsidetrack+152]
            updateFields.append('race_12_4')

        # 場外売場情報 繰り返し 5×20
        if outsidetrackLine[outsidetrack+152:outsidetrack+153]:
            trn_Update.OTB_code_5=outsidetrackLine[outsidetrack+152:outsidetrack+153]
            updateFields.append('OTB_code_5')
        if outsidetrackLine[outsidetrack+153:outsidetrack+156]:
            trn_Update.OTB_5=outsidetrackLine[outsidetrack+153:outsidetrack+156]
            updateFields.append('OTB_5')
        if outsidetrackLine[outsidetrack+156:outsidetrack+157]:
            trn_Update.OTB_Classification_5=outsidetrackLine[outsidetrack+156:outsidetrack+157]
            updateFields.append('OTB_Classification_5')
        if outsidetrackLine[outsidetrack+157:outsidetrack+158]:
            trn_Update.Held_Classification_5=outsidetrackLine[outsidetrack+157:outsidetrack+158]
            updateFields.append('Held_Classification_5')
        if outsidetrackLine[outsidetrack+158:outsidetrack+160]:
            trn_Update.Note_code_5=outsidetrackLine[outsidetrack+158:outsidetrack+160]
            updateFields.append('Note_code_5')
        if outsidetrackLine[outsidetrack+160:outsidetrack+161]:
            trn_Update.race_1_5=outsidetrackLine[outsidetrack+160:outsidetrack+161]
            updateFields.append('race_1_5')
        if outsidetrackLine[outsidetrack+161:outsidetrack+162]:
            trn_Update.race_2_5=outsidetrackLine[outsidetrack+161:outsidetrack+162]
            updateFields.append('race_2_5')
        if outsidetrackLine[outsidetrack+162:outsidetrack+163]:
            trn_Update.race_3_5=outsidetrackLine[outsidetrack+162:outsidetrack+163]
            updateFields.append('race_3_5')
        if outsidetrackLine[outsidetrack+163:outsidetrack+164]:
            trn_Update.race_4_5=outsidetrackLine[outsidetrack+163:outsidetrack+164]
            updateFields.append('race_4_5')
        if outsidetrackLine[outsidetrack+164:outsidetrack+165]:
            trn_Update.race_5_5=outsidetrackLine[outsidetrack+164:outsidetrack+165]
            updateFields.append('race_5_5')
        if outsidetrackLine[outsidetrack+165:outsidetrack+166]:
            trn_Update.race_6_5=outsidetrackLine[outsidetrack+165:outsidetrack+166]
            updateFields.append('race_6_5')
        if outsidetrackLine[outsidetrack+166:outsidetrack+167]:
            trn_Update.race_7_5=outsidetrackLine[outsidetrack+166:outsidetrack+167]
            updateFields.append('race_7_5')
        if outsidetrackLine[outsidetrack+167:outsidetrack+168]:
            trn_Update.race_8_5=outsidetrackLine[outsidetrack+167:outsidetrack+168]
            updateFields.append('race_8_5')
        if outsidetrackLine[outsidetrack+168:outsidetrack+169]:
            trn_Update.race_9_5=outsidetrackLine[outsidetrack+168:outsidetrack+169]
            updateFields.append('race_9_5')
        if outsidetrackLine[outsidetrack+169:outsidetrack+170]:
            trn_Update.race_10_5=outsidetrackLine[outsidetrack+169:outsidetrack+170]
            updateFields.append('race_10_5')
        if outsidetrackLine[outsidetrack+170:outsidetrack+171]:
            trn_Update.race_11_5=outsidetrackLine[outsidetrack+170:outsidetrack+171]
            updateFields.append('race_11_5')
        if outsidetrackLine[outsidetrack+171:outsidetrack+172]:
            trn_Update.race_12_5=outsidetrackLine[outsidetrack+171:outsidetrack+172]
            updateFields.append('race_12_5')

        # 場外売場情報 繰り返し 6×20
        if outsidetrackLine[outsidetrack+172:outsidetrack+173]:
            trn_Update.OTB_code_6=outsidetrackLine[outsidetrack+172:outsidetrack+173]
            updateFields.append('OTB_code_6')
        if outsidetrackLine[outsidetrack+173:outsidetrack+176]:
            trn_Update.OTB_6=outsidetrackLine[outsidetrack+173:outsidetrack+176]
            updateFields.append('OTB_6')
        if outsidetrackLine[outsidetrack+176:outsidetrack+177]:
            trn_Update.OTB_Classification_6=outsidetrackLine[outsidetrack+176:outsidetrack+177]
            updateFields.append('OTB_Classification_6')
        if outsidetrackLine[outsidetrack+177:outsidetrack+178]:
            trn_Update.Held_Classification_6=outsidetrackLine[outsidetrack+177:outsidetrack+178]
            updateFields.append('Held_Classification_6')
        if outsidetrackLine[outsidetrack+178:outsidetrack+180]:
            trn_Update.Note_code_6=outsidetrackLine[outsidetrack+178:outsidetrack+180]
            updateFields.append('Note_code_6')
        if outsidetrackLine[outsidetrack+180:outsidetrack+181]:
            trn_Update.race_1_6=outsidetrackLine[outsidetrack+180:outsidetrack+181]
            updateFields.append('race_1_6')
        if outsidetrackLine[outsidetrack+181:outsidetrack+182]:
            trn_Update.race_2_6=outsidetrackLine[outsidetrack+181:outsidetrack+182]
            updateFields.append('race_2_6')
        if outsidetrackLine[outsidetrack+182:outsidetrack+183]:
            trn_Update.race_3_6=outsidetrackLine[outsidetrack+182:outsidetrack+183]
            updateFields.append('race_3_6')
        if outsidetrackLine[outsidetrack+183:outsidetrack+184]:
            trn_Update.race_4_6=outsidetrackLine[outsidetrack+183:outsidetrack+184]
            updateFields.append('race_4_6')
        if outsidetrackLine[outsidetrack+184:outsidetrack+185]:
            trn_Update.race_5_6=outsidetrackLine[outsidetrack+184:outsidetrack+185]
            updateFields.append('race_5_6')
        if outsidetrackLine[outsidetrack+185:outsidetrack+186]:
            trn_Update.race_6_6=outsidetrackLine[outsidetrack+185:outsidetrack+186]
            updateFields.append('race_6_6')
        if outsidetrackLine[outsidetrack+186:outsidetrack+187]:
            trn_Update.race_7_6=outsidetrackLine[outsidetrack+186:outsidetrack+187]
            updateFields.append('race_7_6')
        if outsidetrackLine[outsidetrack+187:outsidetrack+188]:
            trn_Update.race_8_6=outsidetrackLine[outsidetrack+187:outsidetrack+188]
            updateFields.append('race_8_6')
        if outsidetrackLine[outsidetrack+188:outsidetrack+189]:
            trn_Update.race_9_6=outsidetrackLine[outsidetrack+188:outsidetrack+189]
            updateFields.append('race_9_6')
        if outsidetrackLine[outsidetrack+189:outsidetrack+190]:
            trn_Update.race_10_6=outsidetrackLine[outsidetrack+189:outsidetrack+190]
            updateFields.append('race_10_6')
        if outsidetrackLine[outsidetrack+190:outsidetrack+191]:
            trn_Update.race_11_6=outsidetrackLine[outsidetrack+190:outsidetrack+191]
            updateFields.append('race_11_6')
        if outsidetrackLine[outsidetrack+191:outsidetrack+192]:
            trn_Update.race_12_6=outsidetrackLine[outsidetrack+191:outsidetrack+192]
            updateFields.append('race_12_6')

        # 場外売場情報 繰り返し 7×20
        if outsidetrackLine[outsidetrack+192:outsidetrack+193]:
            trn_Update.OTB_code_7=outsidetrackLine[outsidetrack+192:outsidetrack+193]
            updateFields.append('OTB_code_7')
        if outsidetrackLine[outsidetrack+193:outsidetrack+196]:
            trn_Update.OTB_7=outsidetrackLine[outsidetrack+193:outsidetrack+196]
            updateFields.append('OTB_7')
        if outsidetrackLine[outsidetrack+196:outsidetrack+197]:
            trn_Update.OTB_Classification_7=outsidetrackLine[outsidetrack+196:outsidetrack+197]
            updateFields.append('OTB_Classification_7')
        if outsidetrackLine[outsidetrack+197:outsidetrack+198]:
            trn_Update.Held_Classification_7=outsidetrackLine[outsidetrack+197:outsidetrack+198]
            updateFields.append('Held_Classification_7')
        if outsidetrackLine[outsidetrack+198:outsidetrack+200]:
            trn_Update.Note_code_7=outsidetrackLine[outsidetrack+198:outsidetrack+200]
            updateFields.append('Note_code_7')
        if outsidetrackLine[outsidetrack+200:outsidetrack+201]:
            trn_Update.race_1_7=outsidetrackLine[outsidetrack+200:outsidetrack+201]
            updateFields.append('race_1_7')
        if outsidetrackLine[outsidetrack+201:outsidetrack+202]:
            trn_Update.race_2_7=outsidetrackLine[outsidetrack+201:outsidetrack+202]
            updateFields.append('race_2_7')
        if outsidetrackLine[outsidetrack+202:outsidetrack+203]:
            trn_Update.race_3_7=outsidetrackLine[outsidetrack+202:outsidetrack+203]
            updateFields.append('race_3_7')
        if outsidetrackLine[outsidetrack+203:outsidetrack+204]:
            trn_Update.race_4_7=outsidetrackLine[outsidetrack+203:outsidetrack+204]
            updateFields.append('race_4_7')
        if outsidetrackLine[outsidetrack+204:outsidetrack+205]:
            trn_Update.race_5_7=outsidetrackLine[outsidetrack+204:outsidetrack+205]
            updateFields.append('race_5_7')
        if outsidetrackLine[outsidetrack+205:outsidetrack+206]:
            trn_Update.race_6_7=outsidetrackLine[outsidetrack+205:outsidetrack+206]
            updateFields.append('race_6_7')
        if outsidetrackLine[outsidetrack+206:outsidetrack+207]:
            trn_Update.race_7_7=outsidetrackLine[outsidetrack+206:outsidetrack+207]
            updateFields.append('race_7_7')
        if outsidetrackLine[outsidetrack+207:outsidetrack+208]:
            trn_Update.race_8_7=outsidetrackLine[outsidetrack+207:outsidetrack+208]
            updateFields.append('race_8_7')
        if outsidetrackLine[outsidetrack+208:outsidetrack+209]:
            trn_Update.race_9_7=outsidetrackLine[outsidetrack+208:outsidetrack+209]
            updateFields.append('race_9_7')
        if outsidetrackLine[outsidetrack+209:outsidetrack+210]:
            trn_Update.race_10_7=outsidetrackLine[outsidetrack+209:outsidetrack+210]
            updateFields.append('race_10_7')
        if outsidetrackLine[outsidetrack+210:outsidetrack+211]:
            trn_Update.race_11_7=outsidetrackLine[outsidetrack+210:outsidetrack+211]
            updateFields.append('race_11_7')
        if outsidetrackLine[outsidetrack+211:outsidetrack+212]:
            trn_Update.race_12_7=outsidetrackLine[outsidetrack+211:outsidetrack+212]
            updateFields.append('race_12_7')

        # 場外売場情報 繰り返し 8×20
        if outsidetrackLine[outsidetrack+212:outsidetrack+213]:
            trn_Update.OTB_code_8=outsidetrackLine[outsidetrack+212:outsidetrack+213]
            updateFields.append('OTB_code_8')
        if outsidetrackLine[outsidetrack+213:outsidetrack+216]:
            trn_Update.OTB_8=outsidetrackLine[outsidetrack+213:outsidetrack+216]
            updateFields.append('OTB_8')
        if outsidetrackLine[outsidetrack+216:outsidetrack+217]:
            trn_Update.OTB_Classification_8=outsidetrackLine[outsidetrack+216:outsidetrack+217]
            updateFields.append('OTB_Classification_8')
        if outsidetrackLine[outsidetrack+217:outsidetrack+218]:
            trn_Update.Held_Classification_8=outsidetrackLine[outsidetrack+217:outsidetrack+218]
            updateFields.append('Held_Classification_8')
        if outsidetrackLine[outsidetrack+218:outsidetrack+220]:
            trn_Update.Note_code_8=outsidetrackLine[outsidetrack+218:outsidetrack+220]
            updateFields.append('Note_code_8')
        if outsidetrackLine[outsidetrack+220:outsidetrack+221]:
            trn_Update.race_1_8=outsidetrackLine[outsidetrack+220:outsidetrack+221]
            updateFields.append('race_1_8')
        if outsidetrackLine[outsidetrack+221:outsidetrack+222]:
            trn_Update.race_2_8=outsidetrackLine[outsidetrack+221:outsidetrack+222]
            updateFields.append('race_2_8')
        if outsidetrackLine[outsidetrack+222:outsidetrack+223]:
            trn_Update.race_3_8=outsidetrackLine[outsidetrack+222:outsidetrack+223]
            updateFields.append('race_3_8')
        if outsidetrackLine[outsidetrack+223:outsidetrack+224]:
            trn_Update.race_4_8=outsidetrackLine[outsidetrack+223:outsidetrack+224]
            updateFields.append('race_4_8')
        if outsidetrackLine[outsidetrack+224:outsidetrack+225]:
            trn_Update.race_5_8=outsidetrackLine[outsidetrack+224:outsidetrack+225]
            updateFields.append('race_5_8')
        if outsidetrackLine[outsidetrack+225:outsidetrack+226]:
            trn_Update.race_6_8=outsidetrackLine[outsidetrack+225:outsidetrack+226]
            updateFields.append('race_6_8')
        if outsidetrackLine[outsidetrack+226:outsidetrack+227]:
            trn_Update.race_7_8=outsidetrackLine[outsidetrack+226:outsidetrack+227]
            updateFields.append('race_7_8')
        if outsidetrackLine[outsidetrack+227:outsidetrack+228]:
            trn_Update.race_8_8=outsidetrackLine[outsidetrack+227:outsidetrack+228]
            updateFields.append('race_8_8')
        if outsidetrackLine[outsidetrack+228:outsidetrack+229]:
            trn_Update.race_9_8=outsidetrackLine[outsidetrack+228:outsidetrack+229]
            updateFields.append('race_9_8')
        if outsidetrackLine[outsidetrack+229:outsidetrack+230]:
            trn_Update.race_10_8=outsidetrackLine[outsidetrack+229:outsidetrack+230]
            updateFields.append('race_10_8')
        if outsidetrackLine[outsidetrack+230:outsidetrack+231]:
            trn_Update.race_11_8=outsidetrackLine[outsidetrack+230:outsidetrack+231]
            updateFields.append('race_11_8')
        if outsidetrackLine[outsidetrack+231:outsidetrack+232]:
            trn_Update.race_12_8=outsidetrackLine[outsidetrack+231:outsidetrack+232]
            updateFields.append('race_12_8')

        # 場外売場情報 繰り返し 9×20
        if outsidetrackLine[outsidetrack+232:outsidetrack+233]:
            trn_Update.OTB_code_9=outsidetrackLine[outsidetrack+232:outsidetrack+233]
            updateFields.append('OTB_code_9')
        if outsidetrackLine[outsidetrack+233:outsidetrack+236]:
            trn_Update.OTB_9=outsidetrackLine[outsidetrack+233:outsidetrack+236]
            updateFields.append('OTB_9')
        if outsidetrackLine[outsidetrack+236:outsidetrack+237]:
            trn_Update.OTB_Classification_9=outsidetrackLine[outsidetrack+236:outsidetrack+237]
            updateFields.append('OTB_Classification_9')
        if outsidetrackLine[outsidetrack+237:outsidetrack+238]:
            trn_Update.Held_Classification_9=outsidetrackLine[outsidetrack+237:outsidetrack+238]
            updateFields.append('Held_Classification_9')
        if outsidetrackLine[outsidetrack+238:outsidetrack+240]:
            trn_Update.Note_code_9=outsidetrackLine[outsidetrack+238:outsidetrack+240]
            updateFields.append('Note_code_9')
        if outsidetrackLine[outsidetrack+240:outsidetrack+241]:
            trn_Update.race_1_9=outsidetrackLine[outsidetrack+240:outsidetrack+241]
            updateFields.append('race_1_9')
        if outsidetrackLine[outsidetrack+241:outsidetrack+242]:
            trn_Update.race_2_9=outsidetrackLine[outsidetrack+241:outsidetrack+242]
            updateFields.append('race_2_9')
        if outsidetrackLine[outsidetrack+242:outsidetrack+243]:
            trn_Update.race_3_9=outsidetrackLine[outsidetrack+242:outsidetrack+243]
            updateFields.append('race_3_9')
        if outsidetrackLine[outsidetrack+243:outsidetrack+244]:
            trn_Update.race_4_9=outsidetrackLine[outsidetrack+243:outsidetrack+244]
            updateFields.append('race_4_9')
        if outsidetrackLine[outsidetrack+244:outsidetrack+245]:
            trn_Update.race_5_9=outsidetrackLine[outsidetrack+244:outsidetrack+245]
            updateFields.append('race_5_9')
        if outsidetrackLine[outsidetrack+245:outsidetrack+246]:
            trn_Update.race_6_9=outsidetrackLine[outsidetrack+245:outsidetrack+246]
            updateFields.append('race_6_9')
        if outsidetrackLine[outsidetrack+246:outsidetrack+247]:
            trn_Update.race_7_9=outsidetrackLine[outsidetrack+246:outsidetrack+247]
            updateFields.append('race_7_9')
        if outsidetrackLine[outsidetrack+247:outsidetrack+248]:
            trn_Update.race_8_9=outsidetrackLine[outsidetrack+247:outsidetrack+248]
            updateFields.append('race_8_9')
        if outsidetrackLine[outsidetrack+248:outsidetrack+249]:
            trn_Update.race_9_9=outsidetrackLine[outsidetrack+248:outsidetrack+249]
            updateFields.append('race_9_9')
        if outsidetrackLine[outsidetrack+249:outsidetrack+250]:
            trn_Update.race_10_9=outsidetrackLine[outsidetrack+249:outsidetrack+250]
            updateFields.append('race_10_9')
        if outsidetrackLine[outsidetrack+250:outsidetrack+251]:
            trn_Update.race_11_9=outsidetrackLine[outsidetrack+250:outsidetrack+251]
            updateFields.append('race_11_9')
        if outsidetrackLine[outsidetrack+251:outsidetrack+252]:
            trn_Update.race_12_9=outsidetrackLine[outsidetrack+251:outsidetrack+252]
            updateFields.append('race_12_9')

        # 場外売場情報 繰り返し 10×20
        if outsidetrackLine[outsidetrack+252:outsidetrack+253]:
            trn_Update.OTB_code_10=outsidetrackLine[outsidetrack+252:outsidetrack+253]
            updateFields.append('OTB_code_10')
        if outsidetrackLine[outsidetrack+253:outsidetrack+256]:
            trn_Update.OTB_10=outsidetrackLine[outsidetrack+253:outsidetrack+256]
            updateFields.append('OTB_10')
        if outsidetrackLine[outsidetrack+256:outsidetrack+257]:
            trn_Update.OTB_Classification_10=outsidetrackLine[outsidetrack+256:outsidetrack+257]
            updateFields.append('OTB_Classification_10')
        if outsidetrackLine[outsidetrack+257:outsidetrack+258]:
            trn_Update.Held_Classification_10=outsidetrackLine[outsidetrack+257:outsidetrack+258]
            updateFields.append('Held_Classification_10')
        if outsidetrackLine[outsidetrack+258:outsidetrack+260]:
            trn_Update.Note_code_10=outsidetrackLine[outsidetrack+258:outsidetrack+260]
            updateFields.append('Note_code_10')
        if outsidetrackLine[outsidetrack+260:outsidetrack+261]:
            trn_Update.race_1_10=outsidetrackLine[outsidetrack+260:outsidetrack+261]
            updateFields.append('race_1_10')
        if outsidetrackLine[outsidetrack+261:outsidetrack+262]:
            trn_Update.race_2_10=outsidetrackLine[outsidetrack+261:outsidetrack+262]
            updateFields.append('race_2_10')
        if outsidetrackLine[outsidetrack+262:outsidetrack+263]:
            trn_Update.race_3_10=outsidetrackLine[outsidetrack+262:outsidetrack+263]
            updateFields.append('race_3_10')
        if outsidetrackLine[outsidetrack+263:outsidetrack+264]:
            trn_Update.race_4_10=outsidetrackLine[outsidetrack+263:outsidetrack+264]
            updateFields.append('race_4_10')
        if outsidetrackLine[outsidetrack+264:outsidetrack+265]:
            trn_Update.race_5_10=outsidetrackLine[outsidetrack+264:outsidetrack+265]
            updateFields.append('race_5_10')
        if outsidetrackLine[outsidetrack+265:outsidetrack+266]:
            trn_Update.race_6_10=outsidetrackLine[outsidetrack+265:outsidetrack+266]
            updateFields.append('race_6_10')
        if outsidetrackLine[outsidetrack+266:outsidetrack+267]:
            trn_Update.race_7_10=outsidetrackLine[outsidetrack+266:outsidetrack+267]
            updateFields.append('race_7_10')
        if outsidetrackLine[outsidetrack+267:outsidetrack+268]:
            trn_Update.race_8_10=outsidetrackLine[outsidetrack+267:outsidetrack+268]
            updateFields.append('race_8_10')
        if outsidetrackLine[outsidetrack+268:outsidetrack+269]:
            trn_Update.race_9_10=outsidetrackLine[outsidetrack+268:outsidetrack+269]
            updateFields.append('race_9_10')
        if outsidetrackLine[outsidetrack+269:outsidetrack+270]:
            trn_Update.race_10_10=outsidetrackLine[outsidetrack+269:outsidetrack+270]
            updateFields.append('race_10_10')
        if outsidetrackLine[outsidetrack+270:outsidetrack+271]:
            trn_Update.race_11_10=outsidetrackLine[outsidetrack+270:outsidetrack+271]
            updateFields.append('race_11_10')
        if outsidetrackLine[outsidetrack+271:outsidetrack+272]:
            trn_Update.race_12_10=outsidetrackLine[outsidetrack+271:outsidetrack+272]
            updateFields.append('race_12_10')

        # 場外売場情報 繰り返し 11×20
        if outsidetrackLine[outsidetrack+272:outsidetrack+273]:
            trn_Update.OTB_code_11=outsidetrackLine[outsidetrack+272:outsidetrack+273]
            updateFields.append('OTB_code_11')
        if outsidetrackLine[outsidetrack+273:outsidetrack+276]:
            trn_Update.OTB_11=outsidetrackLine[outsidetrack+273:outsidetrack+276]
            updateFields.append('OTB_11')
        if outsidetrackLine[outsidetrack+276:outsidetrack+277]:
            trn_Update.OTB_Classification_11=outsidetrackLine[outsidetrack+276:outsidetrack+277]
            updateFields.append('OTB_Classification_11')
        if outsidetrackLine[outsidetrack+277:outsidetrack+278]:
            trn_Update.Held_Classification_11=outsidetrackLine[outsidetrack+277:outsidetrack+278]
            updateFields.append('Held_Classification_11')
        if outsidetrackLine[outsidetrack+278:outsidetrack+280]:
            trn_Update.Note_code_11=outsidetrackLine[outsidetrack+278:outsidetrack+280]
            updateFields.append('Note_code_11')
        if outsidetrackLine[outsidetrack+280:outsidetrack+281]:
            trn_Update.race_1_11=outsidetrackLine[outsidetrack+280:outsidetrack+281]
            updateFields.append('race_1_11')
        if outsidetrackLine[outsidetrack+281:outsidetrack+282]:
            trn_Update.race_2_11=outsidetrackLine[outsidetrack+281:outsidetrack+282]
            updateFields.append('race_2_11')
        if outsidetrackLine[outsidetrack+282:outsidetrack+283]:
            trn_Update.race_3_11=outsidetrackLine[outsidetrack+282:outsidetrack+283]
            updateFields.append('race_3_11')
        if outsidetrackLine[outsidetrack+283:outsidetrack+284]:
            trn_Update.race_4_11=outsidetrackLine[outsidetrack+283:outsidetrack+284]
            updateFields.append('race_4_11')
        if outsidetrackLine[outsidetrack+284:outsidetrack+285]:
            trn_Update.race_5_11=outsidetrackLine[outsidetrack+284:outsidetrack+285]
            updateFields.append('race_5_11')
        if outsidetrackLine[outsidetrack+285:outsidetrack+286]:
            trn_Update.race_6_11=outsidetrackLine[outsidetrack+285:outsidetrack+286]
            updateFields.append('race_6_11')
        if outsidetrackLine[outsidetrack+286:outsidetrack+287]:
            trn_Update.race_7_11=outsidetrackLine[outsidetrack+286:outsidetrack+287]
            updateFields.append('race_7_11')
        if outsidetrackLine[outsidetrack+287:outsidetrack+288]:
            trn_Update.race_8_11=outsidetrackLine[outsidetrack+287:outsidetrack+288]
            updateFields.append('race_8_11')
        if outsidetrackLine[outsidetrack+288:outsidetrack+289]:
            trn_Update.race_9_11=outsidetrackLine[outsidetrack+288:outsidetrack+289]
            updateFields.append('race_9_11')
        if outsidetrackLine[outsidetrack+289:outsidetrack+290]:
            trn_Update.race_10_11=outsidetrackLine[outsidetrack+289:outsidetrack+290]
            updateFields.append('race_10_11')
        if outsidetrackLine[outsidetrack+290:outsidetrack+291]:
            trn_Update.race_11_11=outsidetrackLine[outsidetrack+290:outsidetrack+291]
            updateFields.append('race_11_11')
        if outsidetrackLine[outsidetrack+291:outsidetrack+292]:
            trn_Update.race_12_11=outsidetrackLine[outsidetrack+291:outsidetrack+292]
            updateFields.append('race_12_11')

        # 場外売場情報 繰り返し 12×20
        if outsidetrackLine[outsidetrack+292:outsidetrack+293]:
            trn_Update.OTB_code_12=outsidetrackLine[outsidetrack+292:outsidetrack+293]
            updateFields.append('OTB_code_12')
        if outsidetrackLine[outsidetrack+293:outsidetrack+296]:
            trn_Update.OTB_12=outsidetrackLine[outsidetrack+293:outsidetrack+296]
            updateFields.append('OTB_12')
        if outsidetrackLine[outsidetrack+296:outsidetrack+297]:
            trn_Update.OTB_Classification_12=outsidetrackLine[outsidetrack+296:outsidetrack+297]
            updateFields.append('OTB_Classification_12')
        if outsidetrackLine[outsidetrack+297:outsidetrack+298]:
            trn_Update.Held_Classification_12=outsidetrackLine[outsidetrack+297:outsidetrack+298]
            updateFields.append('Held_Classification_12')
        if outsidetrackLine[outsidetrack+298:outsidetrack+300]:
            trn_Update.Note_code_12=outsidetrackLine[outsidetrack+298:outsidetrack+300]
            updateFields.append('Note_code_12')
        if outsidetrackLine[outsidetrack+300:outsidetrack+301]:
            trn_Update.race_1_12=outsidetrackLine[outsidetrack+300:outsidetrack+301]
            updateFields.append('race_1_12')
        if outsidetrackLine[outsidetrack+301:outsidetrack+302]:
            trn_Update.race_2_12=outsidetrackLine[outsidetrack+301:outsidetrack+302]
            updateFields.append('race_2_12')
        if outsidetrackLine[outsidetrack+302:outsidetrack+303]:
            trn_Update.race_3_12=outsidetrackLine[outsidetrack+302:outsidetrack+303]
            updateFields.append('race_3_12')
        if outsidetrackLine[outsidetrack+303:outsidetrack+304]:
            trn_Update.race_4_12=outsidetrackLine[outsidetrack+303:outsidetrack+304]
            updateFields.append('race_4_12')
        if outsidetrackLine[outsidetrack+304:outsidetrack+305]:
            trn_Update.race_5_12=outsidetrackLine[outsidetrack+304:outsidetrack+305]
            updateFields.append('race_5_12')
        if outsidetrackLine[outsidetrack+305:outsidetrack+306]:
            trn_Update.race_6_12=outsidetrackLine[outsidetrack+305:outsidetrack+306]
            updateFields.append('race_6_12')
        if outsidetrackLine[outsidetrack+306:outsidetrack+307]:
            trn_Update.race_7_12=outsidetrackLine[outsidetrack+306:outsidetrack+307]
            updateFields.append('race_7_12')
        if outsidetrackLine[outsidetrack+307:outsidetrack+308]:
            trn_Update.race_8_12=outsidetrackLine[outsidetrack+307:outsidetrack+308]
            updateFields.append('race_8_12')
        if outsidetrackLine[outsidetrack+308:outsidetrack+309]:
            trn_Update.race_9_12=outsidetrackLine[outsidetrack+308:outsidetrack+309]
            updateFields.append('race_9_12')
        if outsidetrackLine[outsidetrack+309:outsidetrack+90]:
            trn_Update.race_10_12=outsidetrackLine[outsidetrack+309:outsidetrack+310]
            updateFields.append('race_10_12')
        if outsidetrackLine[outsidetrack+310:outsidetrack+311]:
            trn_Update.race_11_12=outsidetrackLine[outsidetrack+310:outsidetrack+311]
            updateFields.append('race_11_12')
        if outsidetrackLine[outsidetrack+311:outsidetrack+312]:
            trn_Update.race_12_12=outsidetrackLine[outsidetrack+311:outsidetrack+312]
            updateFields.append('race_12_12')

        # 場外売場情報 繰り返し 13×20
        if outsidetrackLine[outsidetrack+312:outsidetrack+313]:
            trn_Update.OTB_code_13=outsidetrackLine[outsidetrack+312:outsidetrack+313]
            updateFields.append('OTB_code_13')
        if outsidetrackLine[outsidetrack+313:outsidetrack+316]:
            trn_Update.OTB_13=outsidetrackLine[outsidetrack+313:outsidetrack+316]
            updateFields.append('OTB_13')
        if outsidetrackLine[outsidetrack+316:outsidetrack+317]:
            trn_Update.OTB_Classification_13=outsidetrackLine[outsidetrack+316:outsidetrack+317]
            updateFields.append('OTB_Classification_13')
        if outsidetrackLine[outsidetrack+317:outsidetrack+318]:
            trn_Update.Held_Classification_13=outsidetrackLine[outsidetrack+317:outsidetrack+318]
            updateFields.append('Held_Classification_13')
        if outsidetrackLine[outsidetrack+318:outsidetrack+320]:
            trn_Update.Note_code_13=outsidetrackLine[outsidetrack+318:outsidetrack+320]
            updateFields.append('Note_code_13')
        if outsidetrackLine[outsidetrack+320:outsidetrack+321]:
            trn_Update.race_1_13=outsidetrackLine[outsidetrack+320:outsidetrack+321]
            updateFields.append('race_1_13')
        if outsidetrackLine[outsidetrack+321:outsidetrack+322]:
            trn_Update.race_2_13=outsidetrackLine[outsidetrack+321:outsidetrack+322]
            updateFields.append('race_2_13')
        if outsidetrackLine[outsidetrack+322:outsidetrack+323]:
            trn_Update.race_3_13=outsidetrackLine[outsidetrack+322:outsidetrack+323]
            updateFields.append('race_3_13')
        if outsidetrackLine[outsidetrack+323:outsidetrack+324]:
            trn_Update.race_4_13=outsidetrackLine[outsidetrack+323:outsidetrack+324]
            updateFields.append('race_4_13')
        if outsidetrackLine[outsidetrack+324:outsidetrack+325]:
            trn_Update.race_5_13=outsidetrackLine[outsidetrack+324:outsidetrack+325]
            updateFields.append('race_5_13')
        if outsidetrackLine[outsidetrack+325:outsidetrack+326]:
            trn_Update.race_6_13=outsidetrackLine[outsidetrack+325:outsidetrack+326]
            updateFields.append('race_6_13')
        if outsidetrackLine[outsidetrack+326:outsidetrack+327]:
            trn_Update.race_7_13=outsidetrackLine[outsidetrack+326:outsidetrack+327]
            updateFields.append('race_7_13')
        if outsidetrackLine[outsidetrack+327:outsidetrack+328]:
            trn_Update.race_8_13=outsidetrackLine[outsidetrack+327:outsidetrack+328]
            updateFields.append('race_8_13')
        if outsidetrackLine[outsidetrack+328:outsidetrack+329]:
            trn_Update.race_9_13=outsidetrackLine[outsidetrack+328:outsidetrack+329]
            updateFields.append('race_9_13')
        if outsidetrackLine[outsidetrack+329:outsidetrack+330]:
            trn_Update.race_10_13=outsidetrackLine[outsidetrack+329:outsidetrack+330]
            updateFields.append('race_10_13')
        if outsidetrackLine[outsidetrack+330:outsidetrack+331]:
            trn_Update.race_11_13=outsidetrackLine[outsidetrack+330:outsidetrack+331]
            updateFields.append('race_11_13')
        if outsidetrackLine[outsidetrack+331:outsidetrack+332]:
            trn_Update.race_12_13=outsidetrackLine[outsidetrack+331:outsidetrack+332]
            updateFields.append('race_12_13')

        # 場外売場情報 繰り返し 14×20
        if outsidetrackLine[outsidetrack+332:outsidetrack+333]:
            trn_Update.OTB_code_14=outsidetrackLine[outsidetrack+332:outsidetrack+333]
            updateFields.append('OTB_code_14')
        if outsidetrackLine[outsidetrack+333:outsidetrack+336]:
            trn_Update.OTB_14=outsidetrackLine[outsidetrack+333:outsidetrack+336]
            updateFields.append('OTB_14')
        if outsidetrackLine[outsidetrack+336:outsidetrack+337]:
            trn_Update.OTB_Classification_14=outsidetrackLine[outsidetrack+336:outsidetrack+337]
            updateFields.append('OTB_Classification_14')
        if outsidetrackLine[outsidetrack+337:outsidetrack+338]:
            trn_Update.Held_Classification_14=outsidetrackLine[outsidetrack+337:outsidetrack+338]
            updateFields.append('Held_Classification_14')
        if outsidetrackLine[outsidetrack+338:outsidetrack+340]:
            trn_Update.Note_code_14=outsidetrackLine[outsidetrack+338:outsidetrack+340]
            updateFields.append('Note_code_14')
        if outsidetrackLine[outsidetrack+340:outsidetrack+341]:
            trn_Update.race_1_14=outsidetrackLine[outsidetrack+340:outsidetrack+341]
            updateFields.append('race_1_14')
        if outsidetrackLine[outsidetrack+341:outsidetrack+342]:
            trn_Update.race_2_14=outsidetrackLine[outsidetrack+341:outsidetrack+342]
            updateFields.append('race_2_14')
        if outsidetrackLine[outsidetrack+342:outsidetrack+343]:
            trn_Update.race_3_14=outsidetrackLine[outsidetrack+342:outsidetrack+343]
            updateFields.append('race_3_14')
        if outsidetrackLine[outsidetrack+343:outsidetrack+344]:
            trn_Update.race_4_14=outsidetrackLine[outsidetrack+343:outsidetrack+344]
            updateFields.append('race_4_14')
        if outsidetrackLine[outsidetrack+344:outsidetrack+345]:
            trn_Update.race_5_14=outsidetrackLine[outsidetrack+344:outsidetrack+345]
            updateFields.append('race_5_14')
        if outsidetrackLine[outsidetrack+345:outsidetrack+346]:
            trn_Update.race_6_14=outsidetrackLine[outsidetrack+345:outsidetrack+346]
            updateFields.append('race_6_14')
        if outsidetrackLine[outsidetrack+346:outsidetrack+347]:
            trn_Update.race_7_14=outsidetrackLine[outsidetrack+346:outsidetrack+347]
            updateFields.append('race_7_14')
        if outsidetrackLine[outsidetrack+347:outsidetrack+348]:
            trn_Update.race_8_14=outsidetrackLine[outsidetrack+347:outsidetrack+348]
            updateFields.append('race_8_14')
        if outsidetrackLine[outsidetrack+348:outsidetrack+349]:
            trn_Update.race_9_14=outsidetrackLine[outsidetrack+348:outsidetrack+349]
            updateFields.append('race_9_14')
        if outsidetrackLine[outsidetrack+349:outsidetrack+350]:
            trn_Update.race_10_14=outsidetrackLine[outsidetrack+349:outsidetrack+350]
            updateFields.append('race_10_14')
        if outsidetrackLine[outsidetrack+350:outsidetrack+351]:
            trn_Update.race_11_14=outsidetrackLine[outsidetrack+350:outsidetrack+351]
            updateFields.append('race_11_14')
        if outsidetrackLine[outsidetrack+351:outsidetrack+352]:
            trn_Update.race_12_14=outsidetrackLine[outsidetrack+351:outsidetrack+352]
            updateFields.append('race_12_14')

        # 場外売場情報 繰り返し 15×20
        if outsidetrackLine[outsidetrack+352:outsidetrack+353]:
            trn_Update.OTB_code_15=outsidetrackLine[outsidetrack+352:outsidetrack+353]
            updateFields.append('OTB_code_15')
        if outsidetrackLine[outsidetrack+353:outsidetrack+356]:
            trn_Update.OTB_15=outsidetrackLine[outsidetrack+353:outsidetrack+356]
            updateFields.append('OTB_15')
        if outsidetrackLine[outsidetrack+356:outsidetrack+357]:
            trn_Update.OTB_Classification_15=outsidetrackLine[outsidetrack+356:outsidetrack+357]
            updateFields.append('OTB_Classification_15')
        if outsidetrackLine[outsidetrack+357:outsidetrack+358]:
            trn_Update.Held_Classification_15=outsidetrackLine[outsidetrack+357:outsidetrack+358]
            updateFields.append('Held_Classification_15')
        if outsidetrackLine[outsidetrack+358:outsidetrack+360]:
            trn_Update.Note_code_15=outsidetrackLine[outsidetrack+358:outsidetrack+360]
            updateFields.append('Note_code_15')
        if outsidetrackLine[outsidetrack+360:outsidetrack+361]:
            trn_Update.race_1_15=outsidetrackLine[outsidetrack+360:outsidetrack+361]
            updateFields.append('race_1_15')
        if outsidetrackLine[outsidetrack+361:outsidetrack+362]:
            trn_Update.race_2_15=outsidetrackLine[outsidetrack+361:outsidetrack+362]
            updateFields.append('race_2_15')
        if outsidetrackLine[outsidetrack+362:outsidetrack+363]:
            trn_Update.race_3_15=outsidetrackLine[outsidetrack+362:outsidetrack+363]
            updateFields.append('race_3_15')
        if outsidetrackLine[outsidetrack+363:outsidetrack+364]:
            trn_Update.race_4_15=outsidetrackLine[outsidetrack+363:outsidetrack+364]
            updateFields.append('race_4_15')
        if outsidetrackLine[outsidetrack+364:outsidetrack+365]:
            trn_Update.race_5_15=outsidetrackLine[outsidetrack+364:outsidetrack+365]
            updateFields.append('race_5_15')
        if outsidetrackLine[outsidetrack+365:outsidetrack+366]:
            trn_Update.race_6_15=outsidetrackLine[outsidetrack+365:outsidetrack+366]
            updateFields.append('race_6_15')
        if outsidetrackLine[outsidetrack+366:outsidetrack+367]:
            trn_Update.race_7_15=outsidetrackLine[outsidetrack+366:outsidetrack+367]
            updateFields.append('race_7_15')
        if outsidetrackLine[outsidetrack+367:outsidetrack+368]:
            trn_Update.race_8_15=outsidetrackLine[outsidetrack+367:outsidetrack+368]
            updateFields.append('race_8_15')
        if outsidetrackLine[outsidetrack+368:outsidetrack+369]:
            trn_Update.race_9_15=outsidetrackLine[outsidetrack+368:outsidetrack+369]
            updateFields.append('race_9_15')
        if outsidetrackLine[outsidetrack+369:outsidetrack+370]:
            trn_Update.race_10_15=outsidetrackLine[outsidetrack+369:outsidetrack+370]
            updateFields.append('race_10_15')
        if outsidetrackLine[outsidetrack+370:outsidetrack+371]:
            trn_Update.race_11_15=outsidetrackLine[outsidetrack+370:outsidetrack+371]
            updateFields.append('race_11_15')
        if outsidetrackLine[outsidetrack+371:outsidetrack+372]:
            trn_Update.race_12_15=outsidetrackLine[outsidetrack+371:outsidetrack+372]
            updateFields.append('race_12_15')

        # 場外売場情報 繰り返し 16×20
        if outsidetrackLine[outsidetrack+372:outsidetrack+373]:
            trn_Update.OTB_code_16=outsidetrackLine[outsidetrack+372:outsidetrack+373]
            updateFields.append('OTB_code_16')
        if outsidetrackLine[outsidetrack+373:outsidetrack+376]:
            trn_Update.OTB_16=outsidetrackLine[outsidetrack+373:outsidetrack+376]
            updateFields.append('OTB_16')
        if outsidetrackLine[outsidetrack+376:outsidetrack+377]:
            trn_Update.OTB_Classification_16=outsidetrackLine[outsidetrack+376:outsidetrack+377]
            updateFields.append('OTB_Classification_16')
        if outsidetrackLine[outsidetrack+377:outsidetrack+378]:
            trn_Update.Held_Classification_16=outsidetrackLine[outsidetrack+377:outsidetrack+378]
            updateFields.append('Held_Classification_16')
        if outsidetrackLine[outsidetrack+378:outsidetrack+380]:
            trn_Update.Note_code_16=outsidetrackLine[outsidetrack+378:outsidetrack+380]
            updateFields.append('Note_code_16')
        if outsidetrackLine[outsidetrack+380:outsidetrack+381]:
            trn_Update.race_1_16=outsidetrackLine[outsidetrack+380:outsidetrack+381]
            updateFields.append('race_1_16')
        if outsidetrackLine[outsidetrack+381:outsidetrack+382]:
            trn_Update.race_2_16=outsidetrackLine[outsidetrack+381:outsidetrack+382]
            updateFields.append('race_2_16')
        if outsidetrackLine[outsidetrack+382:outsidetrack+383]:
            trn_Update.race_3_16=outsidetrackLine[outsidetrack+382:outsidetrack+383]
            updateFields.append('race_3_16')
        if outsidetrackLine[outsidetrack+383:outsidetrack+384]:
            trn_Update.race_4_16=outsidetrackLine[outsidetrack+383:outsidetrack+384]
            updateFields.append('race_4_16')
        if outsidetrackLine[outsidetrack+384:outsidetrack+385]:
            trn_Update.race_5_16=outsidetrackLine[outsidetrack+384:outsidetrack+385]
            updateFields.append('race_5_16')
        if outsidetrackLine[outsidetrack+385:outsidetrack+386]:
            trn_Update.race_6_16=outsidetrackLine[outsidetrack+385:outsidetrack+386]
            updateFields.append('race_6_16')
        if outsidetrackLine[outsidetrack+386:outsidetrack+387]:
            trn_Update.race_7_16=outsidetrackLine[outsidetrack+386:outsidetrack+387]
            updateFields.append('race_7_16')
        if outsidetrackLine[outsidetrack+387:outsidetrack+388]:
            trn_Update.race_8_16=outsidetrackLine[outsidetrack+387:outsidetrack+388]
            updateFields.append('race_8_16')
        if outsidetrackLine[outsidetrack+388:outsidetrack+389]:
            trn_Update.race_9_16=outsidetrackLine[outsidetrack+388:outsidetrack+389]
            updateFields.append('race_9_16')
        if outsidetrackLine[outsidetrack+389:outsidetrack+390]:
            trn_Update.race_10_16=outsidetrackLine[outsidetrack+389:outsidetrack+390]
            updateFields.append('race_10_16')
        if outsidetrackLine[outsidetrack+390:outsidetrack+391]:
            trn_Update.race_11_16=outsidetrackLine[outsidetrack+390:outsidetrack+391]
            updateFields.append('race_11_16')
        if outsidetrackLine[outsidetrack+391:outsidetrack+392]:
            trn_Update.race_12_16=outsidetrackLine[outsidetrack+391:outsidetrack+392]
            updateFields.append('race_12_16')

        # 場外売場情報 繰り返し 17×20
        if outsidetrackLine[outsidetrack+392:outsidetrack+393]:
            trn_Update.OTB_code_17=outsidetrackLine[outsidetrack+392:outsidetrack+393]
            updateFields.append('OTB_code_17')
        if outsidetrackLine[outsidetrack+393:outsidetrack+396]:
            trn_Update.OTB_17=outsidetrackLine[outsidetrack+393:outsidetrack+396]
            updateFields.append('OTB_17')
        if outsidetrackLine[outsidetrack+396:outsidetrack+397]:
            trn_Update.OTB_Classification_17=outsidetrackLine[outsidetrack+396:outsidetrack+397]
            updateFields.append('OTB_Classification_17')
        if outsidetrackLine[outsidetrack+397:outsidetrack+398]:
            trn_Update.Held_Classification_17=outsidetrackLine[outsidetrack+397:outsidetrack+398]
            updateFields.append('Held_Classification_17')
        if outsidetrackLine[outsidetrack+398:outsidetrack+400]:
            trn_Update.Note_code_17=outsidetrackLine[outsidetrack+398:outsidetrack+400]
            updateFields.append('Note_code_17')
        if outsidetrackLine[outsidetrack+400:outsidetrack+401]:
            trn_Update.race_1_17=outsidetrackLine[outsidetrack+400:outsidetrack+401]
            updateFields.append('race_1_17')
        if outsidetrackLine[outsidetrack+401:outsidetrack+402]:
            trn_Update.race_2_17=outsidetrackLine[outsidetrack+401:outsidetrack+402]
            updateFields.append('race_2_17')
        if outsidetrackLine[outsidetrack+402:outsidetrack+403]:
            trn_Update.race_3_17=outsidetrackLine[outsidetrack+402:outsidetrack+403]
            updateFields.append('race_3_17')
        if outsidetrackLine[outsidetrack+403:outsidetrack+404]:
            trn_Update.race_4_17=outsidetrackLine[outsidetrack+403:outsidetrack+404]
            updateFields.append('race_4_17')
        if outsidetrackLine[outsidetrack+404:outsidetrack+405]:
            trn_Update.race_5_17=outsidetrackLine[outsidetrack+404:outsidetrack+405]
            updateFields.append('race_5_17')
        if outsidetrackLine[outsidetrack+405:outsidetrack+406]:
            trn_Update.race_6_17=outsidetrackLine[outsidetrack+405:outsidetrack+406]
            updateFields.append('race_6_17')
        if outsidetrackLine[outsidetrack+406:outsidetrack+407]:
            trn_Update.race_7_17=outsidetrackLine[outsidetrack+406:outsidetrack+407]
            updateFields.append('race_7_17')
        if outsidetrackLine[outsidetrack+407:outsidetrack+408]:
            trn_Update.race_8_17=outsidetrackLine[outsidetrack+407:outsidetrack+408]
            updateFields.append('race_8_17')
        if outsidetrackLine[outsidetrack+408:outsidetrack+409]:
            trn_Update.race_9_17=outsidetrackLine[outsidetrack+408:outsidetrack+409]
            updateFields.append('race_9_17')
        if outsidetrackLine[outsidetrack+409:outsidetrack+410]:
            trn_Update.race_10_17=outsidetrackLine[outsidetrack+409:outsidetrack+410]
            updateFields.append('race_10_17')
        if outsidetrackLine[outsidetrack+410:outsidetrack+411]:
            trn_Update.race_11_17=outsidetrackLine[outsidetrack+410:outsidetrack+411]
            updateFields.append('race_11_17')
        if outsidetrackLine[outsidetrack+411:outsidetrack+412]:
            trn_Update.race_12_17=outsidetrackLine[outsidetrack+411:outsidetrack+412]
            updateFields.append('race_12_17')

        # 場外売場情報 繰り返し 18×20
        if outsidetrackLine[outsidetrack+412:outsidetrack+413]:
            trn_Update.OTB_code_18=outsidetrackLine[outsidetrack+412:outsidetrack+413]
            updateFields.append('OTB_code_18')
        if outsidetrackLine[outsidetrack+413:outsidetrack+416]:
            trn_Update.OTB_18=outsidetrackLine[outsidetrack+413:outsidetrack+416]
            updateFields.append('OTB_18')
        if outsidetrackLine[outsidetrack+416:outsidetrack+417]:
            trn_Update.OTB_Classification_18=outsidetrackLine[outsidetrack+416:outsidetrack+417]
            updateFields.append('OTB_Classification_18')
        if outsidetrackLine[outsidetrack+417:outsidetrack+418]:
            trn_Update.Held_Classification_18=outsidetrackLine[outsidetrack+417:outsidetrack+418]
            updateFields.append('Held_Classification_18')
        if outsidetrackLine[outsidetrack+418:outsidetrack+420]:
            trn_Update.Note_code_18=outsidetrackLine[outsidetrack+418:outsidetrack+420]
            updateFields.append('Note_code_18')
        if outsidetrackLine[outsidetrack+420:outsidetrack+421]:
            trn_Update.race_1_18=outsidetrackLine[outsidetrack+420:outsidetrack+421]
            updateFields.append('race_1_18')
        if outsidetrackLine[outsidetrack+421:outsidetrack+422]:
            trn_Update.race_2_18=outsidetrackLine[outsidetrack+421:outsidetrack+422]
            updateFields.append('race_2_18')
        if outsidetrackLine[outsidetrack+422:outsidetrack+423]:
            trn_Update.race_3_18=outsidetrackLine[outsidetrack+422:outsidetrack+423]
            updateFields.append('race_3_18')
        if outsidetrackLine[outsidetrack+423:outsidetrack+424]:
            trn_Update.race_4_18=outsidetrackLine[outsidetrack+423:outsidetrack+424]
            updateFields.append('race_4_18')
        if outsidetrackLine[outsidetrack+424:outsidetrack+425]:
            trn_Update.race_5_18=outsidetrackLine[outsidetrack+424:outsidetrack+425]
            updateFields.append('race_5_18')
        if outsidetrackLine[outsidetrack+425:outsidetrack+426]:
            trn_Update.race_6_18=outsidetrackLine[outsidetrack+425:outsidetrack+426]
            updateFields.append('race_6_18')
        if outsidetrackLine[outsidetrack+426:outsidetrack+427]:
            trn_Update.race_7_18=outsidetrackLine[outsidetrack+426:outsidetrack+427]
            updateFields.append('race_7_18')
        if outsidetrackLine[outsidetrack+427:outsidetrack+428]:
            trn_Update.race_8_18=outsidetrackLine[outsidetrack+427:outsidetrack+428]
            updateFields.append('race_8_18')
        if outsidetrackLine[outsidetrack+428:outsidetrack+429]:
            trn_Update.race_9_18=outsidetrackLine[outsidetrack+428:outsidetrack+429]
            updateFields.append('race_9_18')
        if outsidetrackLine[outsidetrack+429:outsidetrack+430]:
            trn_Update.race_10_18=outsidetrackLine[outsidetrack+429:outsidetrack+430]
            updateFields.append('race_10_18')
        if outsidetrackLine[outsidetrack+430:outsidetrack+431]:
            trn_Update.race_11_18=outsidetrackLine[outsidetrack+430:outsidetrack+431]
            updateFields.append('race_11_18')
        if outsidetrackLine[outsidetrack+431:outsidetrack+432]:
            trn_Update.race_12_18=outsidetrackLine[outsidetrack+431:outsidetrack+432]
            updateFields.append('race_12_18')

        # 場外売場情報 繰り返し 19×20
        if outsidetrackLine[outsidetrack+432:outsidetrack+433]:
            trn_Update.OTB_code_19=outsidetrackLine[outsidetrack+432:outsidetrack+433]
            updateFields.append('OTB_code_19')
        if outsidetrackLine[outsidetrack+433:outsidetrack+436]:
            trn_Update.OTB_19=outsidetrackLine[outsidetrack+433:outsidetrack+436]
            updateFields.append('OTB_19')
        if outsidetrackLine[outsidetrack+436:outsidetrack+437]:
            trn_Update.OTB_Classification_19=outsidetrackLine[outsidetrack+436:outsidetrack+437]
            updateFields.append('OTB_Classification_19')
        if outsidetrackLine[outsidetrack+437:outsidetrack+438]:
            trn_Update.Held_Classification_19=outsidetrackLine[outsidetrack+437:outsidetrack+438]
            updateFields.append('Held_Classification_19')
        if outsidetrackLine[outsidetrack+438:outsidetrack+440]:
            trn_Update.Note_code_19=outsidetrackLine[outsidetrack+438:outsidetrack+440]
            updateFields.append('Note_code_19')
        if outsidetrackLine[outsidetrack+440:outsidetrack+441]:
            trn_Update.race_1_19=outsidetrackLine[outsidetrack+440:outsidetrack+441]
            updateFields.append('race_1_19')
        if outsidetrackLine[outsidetrack+441:outsidetrack+442]:
            trn_Update.race_2_19=outsidetrackLine[outsidetrack+441:outsidetrack+442]
            updateFields.append('race_2_19')
        if outsidetrackLine[outsidetrack+442:outsidetrack+443]:
            trn_Update.race_3_19=outsidetrackLine[outsidetrack+442:outsidetrack+443]
            updateFields.append('race_3_19')
        if outsidetrackLine[outsidetrack+443:outsidetrack+444]:
            trn_Update.race_4_19=outsidetrackLine[outsidetrack+443:outsidetrack+444]
            updateFields.append('race_4_19')
        if outsidetrackLine[outsidetrack+444:outsidetrack+445]:
            trn_Update.race_5_19=outsidetrackLine[outsidetrack+444:outsidetrack+445]
            updateFields.append('race_5_19')
        if outsidetrackLine[outsidetrack+445:outsidetrack+446]:
            trn_Update.race_6_19=outsidetrackLine[outsidetrack+445:outsidetrack+446]
            updateFields.append('race_6_19')
        if outsidetrackLine[outsidetrack+446:outsidetrack+447]:
            trn_Update.race_7_19=outsidetrackLine[outsidetrack+446:outsidetrack+447]
            updateFields.append('race_7_19')
        if outsidetrackLine[outsidetrack+447:outsidetrack+448]:
            trn_Update.race_8_19=outsidetrackLine[outsidetrack+447:outsidetrack+448]
            updateFields.append('race_8_19')
        if outsidetrackLine[outsidetrack+448:outsidetrack+449]:
            trn_Update.race_9_19=outsidetrackLine[outsidetrack+448:outsidetrack+449]
            updateFields.append('race_9_19')
        if outsidetrackLine[outsidetrack+449:outsidetrack+450]:
            trn_Update.race_10_19=outsidetrackLine[outsidetrack+449:outsidetrack+450]
            updateFields.append('race_10_19')
        if outsidetrackLine[outsidetrack+450:outsidetrack+451]:
            trn_Update.race_11_19=outsidetrackLine[outsidetrack+450:outsidetrack+451]
            updateFields.append('race_11_19')
        if outsidetrackLine[outsidetrack+451:outsidetrack+452]:
            trn_Update.race_12_19=outsidetrackLine[outsidetrack+451:outsidetrack+452]
            updateFields.append('race_12_19')

        # 場外売場情報 繰り返し 20×20
        if outsidetrackLine[outsidetrack+452:outsidetrack+453]:
            trn_Update.OTB_code_20=outsidetrackLine[outsidetrack+452:outsidetrack+453]
            updateFields.append('OTB_code_20')
        if outsidetrackLine[outsidetrack+453:outsidetrack+456]:
            trn_Update.OTB_20=outsidetrackLine[outsidetrack+453:outsidetrack+456]
            updateFields.append('OTB_20')
        if outsidetrackLine[outsidetrack+456:outsidetrack+457]:
            trn_Update.OTB_Classification_20=outsidetrackLine[outsidetrack+456:outsidetrack+457]
            updateFields.append('OTB_Classification_20')
        if outsidetrackLine[outsidetrack+457:outsidetrack+458]:
            trn_Update.Held_Classification_20=outsidetrackLine[outsidetrack+457:outsidetrack+458]
            updateFields.append('Held_Classification_20')
        if outsidetrackLine[outsidetrack+458:outsidetrack+460]:
            trn_Update.Note_code_20=outsidetrackLine[outsidetrack+458:outsidetrack+460]
            updateFields.append('Note_code_20')
        if outsidetrackLine[outsidetrack+460:outsidetrack+461]:
            trn_Update.race_1_20=outsidetrackLine[outsidetrack+460:outsidetrack+461]
            updateFields.append('race_1_20')
        if outsidetrackLine[outsidetrack+461:outsidetrack+462]:
            trn_Update.race_2_20=outsidetrackLine[outsidetrack+461:outsidetrack+462]
            updateFields.append('race_2_20')
        if outsidetrackLine[outsidetrack+462:outsidetrack+463]:
            trn_Update.race_3_20=outsidetrackLine[outsidetrack+462:outsidetrack+463]
            updateFields.append('race_3_20')
        if outsidetrackLine[outsidetrack+463:outsidetrack+464]:
            trn_Update.race_4_20=outsidetrackLine[outsidetrack+463:outsidetrack+464]
            updateFields.append('race_4_20')
        if outsidetrackLine[outsidetrack+464:outsidetrack+465]:
            trn_Update.race_5_20=outsidetrackLine[outsidetrack+464:outsidetrack+465]
            updateFields.append('race_5_20')
        if outsidetrackLine[outsidetrack+465:outsidetrack+466]:
            trn_Update.race_6_20=outsidetrackLine[outsidetrack+465:outsidetrack+466]
            updateFields.append('race_6_20')
        if outsidetrackLine[outsidetrack+466:outsidetrack+467]:
            trn_Update.race_7_20=outsidetrackLine[outsidetrack+466:outsidetrack+467]
            updateFields.append('race_7_20')
        if outsidetrackLine[outsidetrack+467:outsidetrack+468]:
            trn_Update.race_8_20=outsidetrackLine[outsidetrack+467:outsidetrack+468]
            updateFields.append('race_8_20')
        if outsidetrackLine[outsidetrack+468:outsidetrack+469]:
            trn_Update.race_9_20=outsidetrackLine[outsidetrack+468:outsidetrack+469]
            updateFields.append('race_9_20')
        if outsidetrackLine[outsidetrack+469:outsidetrack+470]:
            trn_Update.race_10_20=outsidetrackLine[outsidetrack+469:outsidetrack+470]
            updateFields.append('race_10_20')
        if outsidetrackLine[outsidetrack+470:outsidetrack+471]:
            trn_Update.race_11_20=outsidetrackLine[outsidetrack+470:outsidetrack+471]
            updateFields.append('race_11_20')
        if outsidetrackLine[outsidetrack+471:outsidetrack+472]:
            trn_Update.race_12_20=outsidetrackLine[outsidetrack+471:outsidetrack+472]
            updateFields.append('race_12_20')

        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)

    def insert_or_update_Trn_Outside_track(self, fileName):

        try:
            # モデル読み込みがここでしか読み込みできない
            from app_autorace.models import Trn_Outside_track
            cmn = commons.Common()

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            file = open(fileName,'r',encoding='shift_jis')
            for line in file: # 1行しかない
                # ファイル文字サイズ
                logger.info(f'{fileName}はファイルサイズ {len(line)}')

                # DB　ファイル登録
                # 必須項目のみ
                #INSERTが実行される
                with transaction.atomic():

                    # 場外売場情報
                    for outsidetrack_record in range(outsidetrack_repeat):
                        outsidetrack = outsidetrackNum * outsidetrack_record
                        outsidetrackLine = line[2:]

                        chkline = outsidetrackLine[outsidetrack:]
                        # insert チェックする。データがからのときはスキップ
                        logger.info(f'データチェック{chkline}')
                        if not cmn.chkBlank(chkline):
                            logger.info( "データチェックがからのため End")
                            break

                        logger.info( f'内容:insert_Trn_Outside_track Start:詳細:ファイルデータ: 繰り返し{outsidetrack_record}: 先頭番号{outsidetrack}')
                        Trn_Outside_track(Cllasification=line[0:1], Data_type=line[1:2]).save()
                        logger.info( "内容:insert_Trn_Outside_track End")

                        # 空白チェックして実体があるカラムは更新
                        logger.info( "内容:update_trn_outside_track Start:" + str(outsidetrack))
                        self.update_trn_outside_track(outsidetrack, outsidetrackLine, Trn_Outside_track.objects.get(id=Trn_Outside_track.objects.all().aggregate(Max('id')).get('id__max')))
                        logger.info( "内容:update_trn_outside_track End")

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

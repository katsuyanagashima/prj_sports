34343231import logging
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
# 場外売場情報レコード（mmddhhmmss00000004.dat）


outsidetrack = 6 # 場情報　繰り返しの数

class Outside_track():


    def init_trn_outside_track(self):
        self.classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
        self.data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
        self.track_code	 = str()
        self.track_name	 = str()
        self.date_ad	 = str()
        self.date_japanese_calender	 = str()
        self.held_day = str()
        self.period_days	 = str()
        self.event_name = str()
        self.first_day_of_the_event	 = str()
        self.commemorative_code = str()
        self.special_commemorative_code	 = str()
        self.otb_code_1 = str()
        self.otb_1	 = str()
        self.otb_classification_1 = str()
        self.held_classification_1	 = str()
        self.note_code_1	 = str()
        self.race_1_1	 = str()
        self.race_2_1	 = str()
        self.race_3_1	 = str()
        self.race_4_1	 = str()
        self.race_5_1	 = str()
        self.race_6_1	 = str()
        self.race_7_1	 = str()
        self.race_8_1	 = str()
        self.race_9_1	 = str()
        self.race_10_1	 = str()
        self.race_11_1	 = str()
        self.race_12_1	 = str()
        self.otb_code_2 = str()
        self.otb_2	 = str()
        self.otb_classification_2 = str()
        self.held_classification_2	 = str()
        self.note_code_2	 = str()
        self.race_1_2	 = str()
        self.race_2_2	 = str()
        self.race_3_2	 = str()
        self.race_4_2	 = str()
        self.race_5_2	 = str()
        self.race_6_2	 = str()
        self.race_7_2	 = str()
        self.race_8_2	 = str()
        self.race_9_2	 = str()
        self.race_10_2	 = str()
        self.race_11_2	 = str()
        self.race_12_2	 = str()
        self.otb_code_3 = str()
        self.otb_3	 = str()
        self.otb_classification_3 = str()
        self.held_classification_3	 = str()
        self.note_code_3	 = str()
        self.race_1_3	 = str()
        self.race_2_3	 = str()
        self.race_3_3	 = str()
        self.race_4_3	 = str()
        self.race_5_3	 = str()
        self.race_6_3	 = str()
        self.race_7_3	 = str()
        self.race_8_3	 = str()
        self.race_9_3	 = str()
        self.race_10_3	 = str()
        self.race_11_3	 = str()
        self.race_12_3	 = str()
        self.otb_code_4 = str()
        self.otb_4	 = str()
        self.otb_classification_4 = str()
        self.held_classification_4	 = str()
        self.note_code_4	 = str()
        self.race_1_4	 = str()
        self.race_2_4	 = str()
        self.race_3_4	 = str()
        self.race_4_4	 = str()
        self.race_5_4	 = str()
        self.race_6_4	 = str()
        self.race_7_4	 = str()
        self.race_8_4	 = str()
        self.race_9_4	 = str()
        self.race_10_4	 = str()
        self.race_11_4	 = str()
        self.race_12_4	 = str()
        self.otb_code_5 = str()
        self.otb_5	 = str()
        self.otb_classification_5 = str()
        self.held_classification_5	 = str()
        self.note_code_5	 = str()
        self.race_1_5	 = str()
        self.race_2_5	 = str()
        self.race_3_5	 = str()
        self.race_4_5	 = str()
        self.race_5_5	 = str()
        self.race_6_5	 = str()
        self.race_7_5	 = str()
        self.race_8_5	 = str()
        self.race_9_5	 = str()
        self.race_10_5	 = str()
        self.race_11_5	 = str()
        self.race_12_5	 = str()
        self.otb_code_6 = str()
        self.otb_6	 = str()
        self.otb_classification_6 = str()
        self.held_classification_6	 = str()
        self.note_code_6	 = str()
        self.race_1_6	 = str()
        self.race_2_6	 = str()
        self.race_3_6	 = str()
        self.race_4_6	 = str()
        self.race_5_6	 = str()
        self.race_6_6	 = str()
        self.race_7_6	 = str()
        self.race_8_6	 = str()
        self.race_9_6	 = str()
        self.race_10_6	 = str()
        self.race_11_6	 = str()
        self.race_12_6	 = str()
        self.otb_code_7 = str()
        self.otb_7	 = str()
        self.otb_classification_7 = str()
        self.held_classification_7	 = str()
        self.note_code_7	 = str()
        self.race_1_7	 = str()
        self.race_2_7	 = str()
        self.race_3_7	 = str()
        self.race_4_7	 = str()
        self.race_5_7	 = str()
        self.race_6_7	 = str()
        self.race_7_7	 = str()
        self.race_8_7	 = str()
        self.race_9_7	 = str()
        self.race_10_7	 = str()
        self.race_11_7	 = str()
        self.race_12_7	 = str()
        self.otb_code_8 = str()
        self.otb_8	 = str()
        self.otb_classification_8 = str()
        self.held_classification_8	 = str()
        self.note_code_8	 = str()
        self.race_1_8	 = str()
        self.race_2_8	 = str()
        self.race_3_8	 = str()
        self.race_4_8	 = str()
        self.race_5_8	 = str()
        self.race_6_8	 = str()
        self.race_7_8	 = str()
        self.race_8_8	 = str()
        self.race_9_8	 = str()
        self.race_10_8	 = str()
        self.race_11_8	 = str()
        self.race_12_8	 = str()
        self.otb_code_9 = str()
        self.otb_9	 = str()
        self.otb_classification_9 = str()
        self.held_classification_9	 = str()
        self.note_code_9	 = str()
        self.race_1_9	 = str()
        self.race_2_9	 = str()
        self.race_3_9	 = str()
        self.race_4_9	 = str()
        self.race_5_9	 = str()
        self.race_6_9	 = str()
        self.race_7_9	 = str()
        self.race_8_9	 = str()
        self.race_9_9	 = str()
        self.race_10_9	 = str()
        self.race_11_9	 = str()
        self.race_12_9	 = str()
        self.otb_code_10 = str()
        self.otb_10	 = str()
        self.otb_classification_10 = str()
        self.held_classification_10	 = str()
        self.note_code_10	 = str()
        self.race_1_10	 = str()
        self.race_2_10	 = str()
        self.race_3_10	 = str()
        self.race_4_10	 = str()
        self.race_5_10	 = str()
        self.race_6_10	 = str()
        self.race_7_10	 = str()
        self.race_8_10	 = str()
        self.race_9_10	 = str()
        self.race_10_10	 = str()
        self.race_11_10	 = str()
        self.race_12_10	 = str()
        self.otb_code_11 = str()
        self.otb_11	 = str()
        self.otb_classification_11 = str()
        self.held_classification_11	 = str()
        self.note_code_11	 = str()
        self.race_1_11	 = str()
        self.race_2_11	 = str()
        self.race_3_11	 = str()
        self.race_4_11	 = str()
        self.race_5_11	 = str()
        self.race_6_11	 = str()
        self.race_7_11	 = str()
        self.race_8_11	 = str()
        self.race_9_11	 = str()
        self.race_10_11	 = str()
        self.race_11_11	 = str()
        self.race_12_11	 = str()
        self.otb_code_12 = str()
        self.otb_12	 = str()
        self.otb_classification_12 = str()
        self.held_classification_12	 = str()
        self.note_code_12	 = str()
        self.race_1_12	 = str()
        self.race_2_12	 = str()
        self.race_3_12	 = str()
        self.race_4_12	 = str()
        self.race_5_12	 = str()
        self.race_6_12	 = str()
        self.race_7_12	 = str()
        self.race_8_12	 = str()
        self.race_9_12	 = str()
        self.race_10_12	 = str()
        self.race_11_12	 = str()
        self.race_12_12	 = str()
        self.otb_code_13 = str()
        self.otb_13	 = str()
        self.otb_classification_13 = str()
        self.held_classification_13	 = str()
        self.note_code_13	 = str()
        self.race_1_13	 = str()
        self.race_2_13	 = str()
        self.race_3_13	 = str()
        self.race_4_13	 = str()
        self.race_5_13	 = str()
        self.race_6_13	 = str()
        self.race_7_13	 = str()
        self.race_8_13	 = str()
        self.race_9_13	 = str()
        self.race_10_13	 = str()
        self.race_11_13	 = str()
        self.race_12_13	 = str()
        self.otb_code_14 = str()
        self.otb_14	 = str()
        self.otb_classification_14 = str()
        self.held_classification_14	 = str()
        self.note_code_14	 = str()
        self.race_1_14	 = str()
        self.race_2_14	 = str()
        self.race_3_14	 = str()
        self.race_4_14	 = str()
        self.race_5_14	 = str()
        self.race_6_14	 = str()
        self.race_7_14	 = str()
        self.race_8_14	 = str()
        self.race_9_14	 = str()
        self.race_10_14	 = str()
        self.race_11_14	 = str()
        self.race_12_14	 = str()
        self.otb_code_15 = str()
        self.otb_15	 = str()
        self.otb_classification_15 = str()
        self.held_classification_15	 = str()
        self.note_code_15	 = str()
        self.race_1_15	 = str()
        self.race_2_15	 = str()
        self.race_3_15	 = str()
        self.race_4_15	 = str()
        self.race_5_15	 = str()
        self.race_6_15	 = str()
        self.race_7_15	 = str()
        self.race_8_15	 = str()
        self.race_9_15	 = str()
        self.race_10_15	 = str()
        self.race_11_15	 = str()
        self.race_12_15	 = str()
        self.otb_code_16 = str()
        self.otb_16	 = str()
        self.otb_classification_16 = str()
        self.held_classification_16	 = str()
        self.note_code_16	 = str()
        self.race_1_16	 = str()
        self.race_2_16	 = str()
        self.race_3_16	 = str()
        self.race_4_16	 = str()
        self.race_5_16	 = str()
        self.race_6_16	 = str()
        self.race_7_16	 = str()
        self.race_8_16	 = str()
        self.race_9_16	 = str()
        self.race_10_16	 = str()
        self.race_11_16	 = str()
        self.race_12_16	 = str()
        self.otb_code_17 = str()
        self.otb_17	 = str()
        self.otb_classification_17 = str()
        self.held_classification_17	 = str()
        self.note_code_17	 = str()
        self.race_1_17	 = str()
        self.race_2_17	 = str()
        self.race_3_17	 = str()
        self.race_4_17	 = str()
        self.race_5_17	 = str()
        self.race_6_17	 = str()
        self.race_7_17	 = str()
        self.race_8_17	 = str()
        self.race_9_17	 = str()
        self.race_10_17	 = str()
        self.race_11_17	 = str()
        self.race_12_17	 = str()
        self.otb_code_18 = str()
        self.otb_18	 = str()
        self.otb_classification_18 = str()
        self.held_classification_18	 = str()
        self.note_code_18	 = str()
        self.race_1_18	 = str()
        self.race_2_18	 = str()
        self.race_3_18	 = str()
        self.race_4_18	 = str()
        self.race_5_18	 = str()
        self.race_6_18	 = str()
        self.race_7_18	 = str()
        self.race_8_18	 = str()
        self.race_9_18	 = str()
        self.race_10_18	 = str()
        self.race_11_18	 = str()
        self.race_12_18	 = str()
        self.otb_code_19 = str()
        self.otb_19	 = str()
        self.otb_classification_19 = str()
        self.held_classification_19	 = str()
        self.note_code_19	 = str()
        self.race_1_19	 = str()
        self.race_2_19	 = str()
        self.race_3_19	 = str()
        self.race_4_19	 = str()
        self.race_5_19	 = str()
        self.race_6_19	 = str()
        self.race_7_19	 = str()
        self.race_8_19	 = str()
        self.race_9_19	 = str()
        self.race_10_19	 = str()
        self.race_11_19	 = str()
        self.race_12_19	 = str()
        self.otb_code_20 = str()
        self.otb_20	 = str()
        self.otb_classification_20 = str()
        self.held_classification_20	 = str()
        self.note_code_20	 = str()
        self.race_1_20	 = str()
        self.race_2_20	 = str()
        self.race_3_20	 = str()
        self.race_4_20	 = str()
        self.race_5_20	 = str()
        self.race_6_20	 = str()
        self.race_7_20	 = str()
        self.race_8_20	 = str()
        self.race_9_20	 = str()
        self.race_10_20	 = str()
        self.race_11_20	 = str()
        self.race_12_20	 = str()

    # 正規表現で半角ブランク削除
    def chkBlank(self, outsidetrackLineStr):
        if (not re.sub('\\s', '', outsidetrackLineStr)):
            return False
        return True

    # datファイル設定する
    def setDatData(self, outsidetrackLine):

        # DB　ファイル登録
        # 必須項目のみ
        #INSERTが実行される
        with transaction.atomic():

            # 場外売場情報
            for s in range(outsidetrack):

                Trn_Outside_track(Cllasification=self.classification, Data_type=self.data_type).save()
                self.init_trn_outside_track()

                if self.chkBlank(outsidetrackLine[0:1]):
                    self.track_code = outsidetrackLine[0:1]
                if self.chkBlank(outsidetrackLine[1:4]):
                    self.track_name	 = outsidetrackLine[1:4]
                if self.chkBlank(outsidetrackLine[4:12]):
                    self.date_ad	 = outsidetrackLine[4:12]
                if self.chkBlank(outsidetrackLine[12:23]):
                    self.date_japanese_calender	 = outsidetrackLine[12:23]
                if self.chkBlank(outsidetrackLine[23:37]):
                    self.held_day	 = outsidetrackLine[23:37]
                if self.chkBlank(outsidetrackLine[37:41]):
                    self.period_days	 = outsidetrackLine[37:41]
                if self.chkBlank(outsidetrackLine[41:61]):
                    self.event_name	 = outsidetrackLine[41:61]
                if self.chkBlank(outsidetrackLine[61:69]):
                    self.first_day_of_the_event	 = outsidetrackLine[61:69]
                if self.chkBlank(outsidetrackLine[69:70]):
                    self.commemorative_code	 = outsidetrackLine[69:70]
                if self.chkBlank(outsidetrackLine[70:72]):
                    self.special_commemorative_code	 = outsidetrackLine[70:72]

                # 場外売場情報 繰り返し ×20
                if self.chkBlank(outsidetrackLine[72:73]):
                    self.otb_code_1	 = outsidetrackLine[72:73]
                if self.chkBlank(outsidetrackLine[73:76]):
                    self.otb_1	 = outsidetrackLine[73:76]
                if self.chkBlank(outsidetrackLine[76:77]):
                    self.otb_classification_1	 = outsidetrackLine[76:77]
                if self.chkBlank(outsidetrackLine[77:78]):
                    self.held_classification_1	 = outsidetrackLine[77:78]
                if self.chkBlank(outsidetrackLine[78:80]):
                    self.note_code_1	 = outsidetrackLine[78:80]
                if self.chkBlank(outsidetrackLine[80:81]):
                    self.race_1_1	 = outsidetrackLine[80:81]
                if self.chkBlank(outsidetrackLine[81:82]):
                    self.race_2_1	 = outsidetrackLine[81:82]
                if self.chkBlank(outsidetrackLine[82:83]):
                    self.race_3_1	 = outsidetrackLine[82:83]
                if self.chkBlank(outsidetrackLine[83:84]):
                    self.race_4_1	 = outsidetrackLine[83:84]
                if self.chkBlank(outsidetrackLine[84:85]):
                    self.race_5_1	 = outsidetrackLine[84:85]
                if self.chkBlank(outsidetrackLine[85:86]):
                    self.race_6_1	 = outsidetrackLine[85:86]
                if self.chkBlank(outsidetrackLine[86:87]):
                    self.race_7_1	 = outsidetrackLine[86:87]
                if self.chkBlank(outsidetrackLine[87:88]):
                    self.race_8_1	 = outsidetrackLine[87:88]
                if self.chkBlank(outsidetrackLine[88:89]):
                    self.race_9_1	 = outsidetrackLine[88:89]
                if self.chkBlank(outsidetrackLine[89:90]):
                    self.race_10_1	 = outsidetrackLine[89:90]
                if self.chkBlank(outsidetrackLine[90:91]):
                    self.race_11_1	 = outsidetrackLine[90:91]
                if self.chkBlank(outsidetrackLine[91:92]):
                    self.race_12_1	 = outsidetrackLine[91:92]

                if self.chkBlank(outsidetrackLine[92:93]):
                    self.otb_code_2	 = outsidetrackLine[92:93]
                if self.chkBlank(outsidetrackLine[93:96]):
                    self.otb_2	 = outsidetrackLine[93:96]
                if self.chkBlank(outsidetrackLine[96:97]):
                    self.otb_classification_2	 = outsidetrackLine[96:97]
                if self.chkBlank(outsidetrackLine[97:98]):
                    self.held_classification_2	 = outsidetrackLine[97:98]
                if self.chkBlank(outsidetrackLine[98:100]):
                    self.note_code_2	 = outsidetrackLine[98:100]
                if self.chkBlank(outsidetrackLine[100:101]):
                    self.race_1_2	 = outsidetrackLine[100:101]
                if self.chkBlank(outsidetrackLine[101:102]):
                    self.race_2_2	 = outsidetrackLine[101:102]
                if self.chkBlank(outsidetrackLine[102:103]):
                    self.race_3_2	 = outsidetrackLine[102:103]
                if self.chkBlank(outsidetrackLine[103:104]):
                    self.race_4_2	 = outsidetrackLine[103:104]
                if self.chkBlank(outsidetrackLine[104:105]):
                    self.race_5_2	 = outsidetrackLine[104:105]
                if self.chkBlank(outsidetrackLine[105:106]):
                    self.race_6_2	 = outsidetrackLine[105:106]
                if self.chkBlank(outsidetrackLine[106:107]):
                    self.race_7_2	 = outsidetrackLine[106:107]
                if self.chkBlank(outsidetrackLine[107:108]):
                    self.race_8_2	 = outsidetrackLine[107:108]
                if self.chkBlank(outsidetrackLine[108:109]):
                    self.race_9_2	 = outsidetrackLine[108:109]
                if self.chkBlank(outsidetrackLine[109:100]):
                    self.race_10_2	 = outsidetrackLine[109:110]
                if self.chkBlank(outsidetrackLine[110:111]):
                    self.race_11_2	 = outsidetrackLine[110:111]
                if self.chkBlank(outsidetrackLine[111:112]):
                    self.race_12_2	 = outsidetrackLine[111:112]

                if self.chkBlank(outsidetrackLine[112:113]):
                    self.otb_code_3	 = outsidetrackLine[112:113]
                if self.chkBlank(outsidetrackLine[113:116]):
                    self.otb_3	 = outsidetrackLine[113:116]
                if self.chkBlank(outsidetrackLine[116:117]):
                    self.otb_classification_3	 = outsidetrackLine[116:117]
                if self.chkBlank(outsidetrackLine[117:118]):
                    self.held_classification_3	 = outsidetrackLine[117:118]
                if self.chkBlank(outsidetrackLine[118:120]):
                    self.note_code_3	 = outsidetrackLine[118:120]
                if self.chkBlank(outsidetrackLine[120:121]):
                    self.race_1_3	 = outsidetrackLine[120:121]
                if self.chkBlank(outsidetrackLine[121:122]):
                    self.race_2_3	 = outsidetrackLine[121:122]
                if self.chkBlank(outsidetrackLine[122:123]):
                    self.race_3_3	 = outsidetrackLine[122:123]
                if self.chkBlank(outsidetrackLine[123:124]):
                    self.race_4_3	 = outsidetrackLine[123:124]
                if self.chkBlank(outsidetrackLine[124:125]):
                    self.race_5_3	 = outsidetrackLine[124:125]
                if self.chkBlank(outsidetrackLine[125:126]):
                    self.race_6_3	 = outsidetrackLine[125:126]
                if self.chkBlank(outsidetrackLine[126:127]):
                    self.race_7_3	 = outsidetrackLine[126:127]
                if self.chkBlank(outsidetrackLine[127:128]):
                    self.race_8_3	 = outsidetrackLine[127:128]
                if self.chkBlank(outsidetrackLine[128:129]):
                    self.race_9_3	 = outsidetrackLine[128:129]
                if self.chkBlank(outsidetrackLine[129:130]):
                    self.race_10_3	 = outsidetrackLine[129:130]
                if self.chkBlank(outsidetrackLine[130:131]):
                    self.race_11_3	 = outsidetrackLine[130:131]
                if self.chkBlank(outsidetrackLine[131:132]):
                    self.race_12_3	 = outsidetrackLine[131:132]

                if self.chkBlank(outsidetrackLine[132:133]):
                    self.otb_code_4	 = outsidetrackLine[132:133]
                if self.chkBlank(outsidetrackLine[133:136]):
                    self.otb_4	 = outsidetrackLine[133:136]
                if self.chkBlank(outsidetrackLine[136:137]):
                    self.otb_classification_4	 = outsidetrackLine[136:137]
                if self.chkBlank(outsidetrackLine[137:138]):
                    self.held_classification_4	 = outsidetrackLine[137:138]
                if self.chkBlank(outsidetrackLine[138:140]):
                    self.note_code_4	 = outsidetrackLine[138:140]
                if self.chkBlank(outsidetrackLine[140:141]):
                    self.race_1_4	 = outsidetrackLine[140:141]
                if self.chkBlank(outsidetrackLine[141:142]):
                    self.race_2_4	 = outsidetrackLine[141:142]
                if self.chkBlank(outsidetrackLine[142:143]):
                    self.race_3_4	 = outsidetrackLine[142:143]
                if self.chkBlank(outsidetrackLine[143:144]):
                    self.race_4_4	 = outsidetrackLine[143:144]
                if self.chkBlank(outsidetrackLine[144:145]):
                    self.race_5_4	 = outsidetrackLine[144:145]
                if self.chkBlank(outsidetrackLine[145:146]):
                    self.race_6_4	 = outsidetrackLine[145:146]
                if self.chkBlank(outsidetrackLine[146:147]):
                    self.race_7_4	 = outsidetrackLine[146:147]
                if self.chkBlank(outsidetrackLine[147:148]):
                    self.race_8_4	 = outsidetrackLine[147:148]
                if self.chkBlank(outsidetrackLine[148:149]):
                    self.race_9_4	 = outsidetrackLine[148:149]
                if self.chkBlank(outsidetrackLine[149:150]):
                    self.race_10_4	 = outsidetrackLine[149:150]
                if self.chkBlank(outsidetrackLine[150:151]):
                    self.race_11_4	 = outsidetrackLine[150:151]
                if self.chkBlank(outsidetrackLine[151:152]):
                    self.race_12_4	 = outsidetrackLine[151:152]

                if self.chkBlank(outsidetrackLine[152:153]):
                    self.otb_code_5	 = outsidetrackLine[152:153]
                if self.chkBlank(outsidetrackLine[153:156]):
                    self.otb_5	 = outsidetrackLine[153:156]
                if self.chkBlank(outsidetrackLine[156:157]):
                    self.otb_classification_5	 = outsidetrackLine[156:157]
                if self.chkBlank(outsidetrackLine[157:158]):
                    self.held_classification_5	 = outsidetrackLine[157:158]
                if self.chkBlank(outsidetrackLine[158:160]):
                    self.note_code_5	 = outsidetrackLine[158:160]
                if self.chkBlank(outsidetrackLine[160:161]):
                    self.race_1_5	 = outsidetrackLine[160:161]
                if self.chkBlank(outsidetrackLine[161:162]):
                    self.race_2_5	 = outsidetrackLine[161:162]
                if self.chkBlank(outsidetrackLine[162:163]):
                    self.race_3_5	 = outsidetrackLine[162:163]
                if self.chkBlank(outsidetrackLine[163:164]):
                    self.race_4_5	 = outsidetrackLine[163:164]
                if self.chkBlank(outsidetrackLine[164:165]):
                    self.race_5_5	 = outsidetrackLine[164:165]
                if self.chkBlank(outsidetrackLine[165:166]):
                    self.race_6_5	 = outsidetrackLine[165:166]
                if self.chkBlank(outsidetrackLine[166:167]):
                    self.race_7_5	 = outsidetrackLine[166:167]
                if self.chkBlank(outsidetrackLine[167:168]):
                    self.race_8_5	 = outsidetrackLine[167:168]
                if self.chkBlank(outsidetrackLine[168:169]):
                    self.race_9_5	 = outsidetrackLine[168:169]
                if self.chkBlank(outsidetrackLine[169:170]):
                    self.race_10_5	 = outsidetrackLine[169:170]
                if self.chkBlank(outsidetrackLine[170:171]):
                    self.race_11_5	 = outsidetrackLine[170:171]
                if self.chkBlank(outsidetrackLine[171:172]):
                    self.race_12_5	 = outsidetrackLine[171:172]

                if self.chkBlank(outsidetrackLine[172:173]):
                    self.otb_code_6	 = outsidetrackLine[172:173]
                if self.chkBlank(outsidetrackLine[173:176]):
                    self.otb_6	 = outsidetrackLine[173:176]
                if self.chkBlank(outsidetrackLine[176:177]):
                    self.otb_classification_6	 = outsidetrackLine[176:177]
                if self.chkBlank(outsidetrackLine[177:178]):
                    self.held_classification_6	 = outsidetrackLine[177:178]
                if self.chkBlank(outsidetrackLine[178:180]):
                    self.note_code_6	 = outsidetrackLine[178:180]
                if self.chkBlank(outsidetrackLine[180:181]):
                    self.race_1_6	 = outsidetrackLine[180:181]
                if self.chkBlank(outsidetrackLine[181:182]):
                    self.race_2_6	 = outsidetrackLine[181:182]
                if self.chkBlank(outsidetrackLine[182:183]):
                    self.race_3_6	 = outsidetrackLine[182:183]
                if self.chkBlank(outsidetrackLine[183:184]):
                    self.race_4_6	 = outsidetrackLine[183:184]
                if self.chkBlank(outsidetrackLine[184:185]):
                    self.race_5_6	 = outsidetrackLine[184:185]
                if self.chkBlank(outsidetrackLine[185:186]):
                    self.race_6_6	 = outsidetrackLine[185:186]
                if self.chkBlank(outsidetrackLine[186:187]):
                    self.race_7_6	 = outsidetrackLine[186:187]
                if self.chkBlank(outsidetrackLine[187:188]):
                    self.race_8_6	 = outsidetrackLine[187:188]
                if self.chkBlank(outsidetrackLine[188:189]):
                    self.race_9_6	 = outsidetrackLine[188:189]
                if self.chkBlank(outsidetrackLine[189:190]):
                    self.race_10_6	 = outsidetrackLine[189:190]
                if self.chkBlank(outsidetrackLine[190:191]):
                    self.race_11_6	 = outsidetrackLine[190:191]
                if self.chkBlank(outsidetrackLine[191:192]):
                    self.race_12_6	 = outsidetrackLine[191:192]

                if self.chkBlank(outsidetrackLine[192:193]):
                    self.otb_code_7	 = outsidetrackLine[192:193]
                if self.chkBlank(outsidetrackLine[193:196]):
                    self.otb_7	 = outsidetrackLine[193:196]
                if self.chkBlank(outsidetrackLine[196:197]):
                    self.otb_classification_7	 = outsidetrackLine[196:197]
                if self.chkBlank(outsidetrackLine[197:198]):
                    self.held_classification_7	 = outsidetrackLine[197:198]
                if self.chkBlank(outsidetrackLine[198:200]):
                    self.note_code_7	 = outsidetrackLine[198:200]
                if self.chkBlank(outsidetrackLine[200:201]):
                    self.race_1_7	 = outsidetrackLine[200:201]
                if self.chkBlank(outsidetrackLine[201:202]):
                    self.race_2_7	 = outsidetrackLine[201:202]
                if self.chkBlank(outsidetrackLine[202:203]):
                    self.race_3_7	 = outsidetrackLine[202:203]
                if self.chkBlank(outsidetrackLine[203:204]):
                    self.race_4_7	 = outsidetrackLine[203:204]
                if self.chkBlank(outsidetrackLine[204:205]):
                    self.race_5_7	 = outsidetrackLine[204:205]
                if self.chkBlank(outsidetrackLine[205:206]):
                    self.race_6_7	 = outsidetrackLine[205:206]
                if self.chkBlank(outsidetrackLine[206:207]):
                    self.race_7_7	 = outsidetrackLine[206:207]
                if self.chkBlank(outsidetrackLine[207:208]):
                    self.race_8_7	 = outsidetrackLine[207:208]
                if self.chkBlank(outsidetrackLine[208:209]):
                    self.race_9_7	 = outsidetrackLine[208:209]
                if self.chkBlank(outsidetrackLine[209:210]):
                    self.race_10_7	 = outsidetrackLine[209:210]
                if self.chkBlank(outsidetrackLine[210:211]):
                    self.race_11_7	 = outsidetrackLine[210:211]
                if self.chkBlank(outsidetrackLine[211:212]):
                    self.race_12_7	 = outsidetrackLine[211:212]

                if self.chkBlank(outsidetrackLine[212:213]):
                    self.otb_code_8	 = outsidetrackLine[212:213]
                if self.chkBlank(outsidetrackLine[213:216]):
                    self.otb_8	 = outsidetrackLine[213:216]
                if self.chkBlank(outsidetrackLine[216:217]):
                    self.otb_classification_8	 = outsidetrackLine[216:217]
                if self.chkBlank(outsidetrackLine[217:218]):
                    self.held_classification_8	 = outsidetrackLine[217:218]
                if self.chkBlank(outsidetrackLine[218:220]):
                    self.note_code_8	 = outsidetrackLine[218:220]
                if self.chkBlank(outsidetrackLine[220:221]):
                    self.race_1_8	 = outsidetrackLine[220:221]
                if self.chkBlank(outsidetrackLine[221:222]):
                    self.race_2_8	 = outsidetrackLine[221:222]
                if self.chkBlank(outsidetrackLine[222:223]):
                    self.race_3_8	 = outsidetrackLine[222:223]
                if self.chkBlank(outsidetrackLine[223:224]):
                    self.race_4_8	 = outsidetrackLine[223:224]
                if self.chkBlank(outsidetrackLine[224:225]):
                    self.race_5_8	 = outsidetrackLine[224:225]
                if self.chkBlank(outsidetrackLine[225:226]):
                    self.race_6_8	 = outsidetrackLine[225:226]
                if self.chkBlank(outsidetrackLine[226:227]):
                    self.race_7_8	 = outsidetrackLine[226:227]
                if self.chkBlank(outsidetrackLine[227:228]):
                    self.race_8_8	 = outsidetrackLine[227:228]
                if self.chkBlank(outsidetrackLine[228:229]):
                    self.race_9_8	 = outsidetrackLine[228:229]
                if self.chkBlank(outsidetrackLine[229:230]):
                    self.race_10_8	 = outsidetrackLine[229:230]
                if self.chkBlank(outsidetrackLine[230:231]):
                    self.race_11_8	 = outsidetrackLine[230:231]
                if self.chkBlank(outsidetrackLine[231:232]):
                    self.race_12_8	 = outsidetrackLine[231:232]

                if self.chkBlank(outsidetrackLine[232:233]):
                    self.otb_code_9	 = outsidetrackLine[232:233]
                if self.chkBlank(outsidetrackLine[233:236]):
                    self.otb_9	 = outsidetrackLine[233:236]
                if self.chkBlank(outsidetrackLine[236:237]):
                    self.otb_classification_9	 = outsidetrackLine[236:237]
                if self.chkBlank(outsidetrackLine[237:238]):
                    self.held_classification_9	 = outsidetrackLine[237:238]
                if self.chkBlank(outsidetrackLine[238:240]):
                    self.note_code_9	 = outsidetrackLine[238:240]
                if self.chkBlank(outsidetrackLine[240:241]):
                    self.race_1_9	 = outsidetrackLine[240:241]
                if self.chkBlank(outsidetrackLine[241:242]):
                    self.race_2_9	 = outsidetrackLine[241:242]
                if self.chkBlank(outsidetrackLine[242:243]):
                    self.race_3_9	 = outsidetrackLine[242:243]
                if self.chkBlank(outsidetrackLine[243:244]):
                    self.race_4_9	 = outsidetrackLine[243:244]
                if self.chkBlank(outsidetrackLine[244:245]):
                    self.race_5_9	 = outsidetrackLine[244:245]
                if self.chkBlank(outsidetrackLine[245:246]):
                    self.race_6_9	 = outsidetrackLine[245:246]
                if self.chkBlank(outsidetrackLine[246:247]):
                    self.race_7_9	 = outsidetrackLine[246:247]
                if self.chkBlank(outsidetrackLine[247:248]):
                    self.race_8_9	 = outsidetrackLine[247:248]
                if self.chkBlank(outsidetrackLine[248:249]):
                    self.race_9_9	 = outsidetrackLine[248:249]
                if self.chkBlank(outsidetrackLine[249:250]):
                    self.race_10_9	 = outsidetrackLine[249:250]
                if self.chkBlank(outsidetrackLine[250:251]):
                    self.race_11_9	 = outsidetrackLine[250:251]
                if self.chkBlank(outsidetrackLine[251:252]):
                    self.race_12_9	 = outsidetrackLine[251:252]

                if self.chkBlank(outsidetrackLine[252:253]):
                    self.otb_code_10	 = outsidetrackLine[252:253]
                if self.chkBlank(outsidetrackLine[253:256]):
                    self.otb_10	 = outsidetrackLine[253:256]
                if self.chkBlank(outsidetrackLine[256:257]):
                    self.otb_classification_10	 = outsidetrackLine[256:257]
                if self.chkBlank(outsidetrackLine[257:258]):
                    self.held_classification_10	 = outsidetrackLine[257:258]
                if self.chkBlank(outsidetrackLine[258:260]):
                    self.note_code_10	 = outsidetrackLine[258:260]
                if self.chkBlank(outsidetrackLine[260:261]):
                    self.race_1_10	 = outsidetrackLine[260:261]
                if self.chkBlank(outsidetrackLine[261:262]):
                    self.race_2_10	 = outsidetrackLine[261:262]
                if self.chkBlank(outsidetrackLine[262:263]):
                    self.race_3_10	 = outsidetrackLine[262:263]
                if self.chkBlank(outsidetrackLine[263:264]):
                    self.race_4_10	 = outsidetrackLine[263:264]
                if self.chkBlank(outsidetrackLine[264:265]):
                    self.race_5_10	 = outsidetrackLine[264:265]
                if self.chkBlank(outsidetrackLine[265:266]):
                    self.race_6_10	 = outsidetrackLine[265:266]
                if self.chkBlank(outsidetrackLine[266:267]):
                    self.race_7_10	 = outsidetrackLine[266:267]
                if self.chkBlank(outsidetrackLine[267:268]):
                    self.race_8_10	 = outsidetrackLine[267:268]
                if self.chkBlank(outsidetrackLine[268:269]):
                    self.race_9_10	 = outsidetrackLine[268:269]
                if self.chkBlank(outsidetrackLine[269:270]):
                    self.race_10_10	 = outsidetrackLine[269:270]
                if self.chkBlank(outsidetrackLine[270:271]):
                    self.race_11_10	 = outsidetrackLine[270:271]
                if self.chkBlank(outsidetrackLine[271:272]):
                    self.race_12_10	 = outsidetrackLine[271:272]

                if self.chkBlank(outsidetrackLine[272:273]):
                    self.otb_code_11	 = outsidetrackLine[272:273]
                if self.chkBlank(outsidetrackLine[273:276]):
                    self.otb_11	 = outsidetrackLine[273:276]
                if self.chkBlank(outsidetrackLine[276:277]):
                    self.otb_classification_11	 = outsidetrackLine[276:277]
                if self.chkBlank(outsidetrackLine[277:278]):
                    self.held_classification_11	 = outsidetrackLine[277:278]
                if self.chkBlank(outsidetrackLine[278:280]):
                    self.note_code_11	 = outsidetrackLine[278:280]
                if self.chkBlank(outsidetrackLine[280:281]):
                    self.race_1_11	 = outsidetrackLine[280:281]
                if self.chkBlank(outsidetrackLine[281:282]):
                    self.race_2_11	 = outsidetrackLine[281:282]
                if self.chkBlank(outsidetrackLine[282:283]):
                    self.race_3_11	 = outsidetrackLine[282:283]
                if self.chkBlank(outsidetrackLine[283:284]):
                    self.race_4_11	 = outsidetrackLine[283:284]
                if self.chkBlank(outsidetrackLine[284:285]):
                    self.race_5_11	 = outsidetrackLine[284:285]
                if self.chkBlank(outsidetrackLine[285:286]):
                    self.race_6_11	 = outsidetrackLine[285:286]
                if self.chkBlank(outsidetrackLine[286:287]):
                    self.race_7_11	 = outsidetrackLine[286:287]
                if self.chkBlank(outsidetrackLine[287:288]):
                    self.race_8_11	 = outsidetrackLine[287:288]
                if self.chkBlank(outsidetrackLine[288:289]):
                    self.race_9_11	 = outsidetrackLine[288:289]
                if self.chkBlank(outsidetrackLine[289:290]):
                    self.race_10_11	 = outsidetrackLine[289:290]
                if self.chkBlank(outsidetrackLine[290:291]):
                    self.race_11_11	 = outsidetrackLine[290:291]
                if self.chkBlank(outsidetrackLine[291:292]):
                    self.race_12_11	 = outsidetrackLine[291:292]

                if self.chkBlank(outsidetrackLine[292:293]):
                    self.otb_code_12	 = outsidetrackLine[292:293]
                if self.chkBlank(outsidetrackLine[293:296]):
                    self.otb_12	 = outsidetrackLine[293:296]
                if self.chkBlank(outsidetrackLine[296:297]):
                    self.otb_classification_12	 = outsidetrackLine[296:297]
                if self.chkBlank(outsidetrackLine[297:298]):
                    self.held_classification_12	 = outsidetrackLine[297:298]
                if self.chkBlank(outsidetrackLine[298:300]):
                    self.note_code_12	 = outsidetrackLine[298:300]
                if self.chkBlank(outsidetrackLine[300:301]):
                    self.race_1_12	 = outsidetrackLine[300:301]
                if self.chkBlank(outsidetrackLine[301:302]):
                    self.race_2_12	 = outsidetrackLine[301:302]
                if self.chkBlank(outsidetrackLine[302:303]):
                    self.race_3_12	 = outsidetrackLine[302:303]
                if self.chkBlank(outsidetrackLine[303:304]):
                    self.race_4_12	 = outsidetrackLine[303:304]
                if self.chkBlank(outsidetrackLine[304:305]):
                    self.race_5_12	 = outsidetrackLine[304:305]
                if self.chkBlank(outsidetrackLine[305:306]):
                    self.race_6_12	 = outsidetrackLine[305:306]
                if self.chkBlank(outsidetrackLine[306:307]):
                    self.race_7_12	 = outsidetrackLine[306:307]
                if self.chkBlank(outsidetrackLine[307:308]):
                    self.race_8_12	 = outsidetrackLine[307:308]
                if self.chkBlank(outsidetrackLine[308:309]):
                    self.race_9_12	 = outsidetrackLine[308:309]
                if self.chkBlank(outsidetrackLine[309:310]):
                    self.race_10_12	 = outsidetrackLine[309:310]
                if self.chkBlank(outsidetrackLine[310:311]):
                    self.race_11_12	 = outsidetrackLine[310:311]
                if self.chkBlank(outsidetrackLine[311:312]):
                    self.race_12_12	 = outsidetrackLine[311:312]

                if self.chkBlank(outsidetrackLine[312:313]):
                    self.otb_code_13	 = outsidetrackLine[312:313]
                if self.chkBlank(outsidetrackLine[313:316]):
                    self.otb_13	 = outsidetrackLine[313:316]
                if self.chkBlank(outsidetrackLine[316:317]):
                    self.otb_classification_13	 = outsidetrackLine[316:317]
                if self.chkBlank(outsidetrackLine[317:318]):
                    self.held_classification_13	 = outsidetrackLine[317:318]
                if self.chkBlank(outsidetrackLine[318:320]):
                    self.note_code_13	 = outsidetrackLine[318:320]
                if self.chkBlank(outsidetrackLine[320:321]):
                    self.race_1_13	 = outsidetrackLine[320:321]
                if self.chkBlank(outsidetrackLine[321:322]):
                    self.race_2_13	 = outsidetrackLine[321:322]
                if self.chkBlank(outsidetrackLine[322:323]):
                    self.race_3_13	 = outsidetrackLine[322:323]
                if self.chkBlank(outsidetrackLine[323:324]):
                    self.race_4_13	 = outsidetrackLine[323:324]
                if self.chkBlank(outsidetrackLine[324:325]):
                    self.race_5_13	 = outsidetrackLine[324:325]
                if self.chkBlank(outsidetrackLine[325:326]):
                    self.race_6_13	 = outsidetrackLine[325:326]
                if self.chkBlank(outsidetrackLine[326:327]):
                    self.race_7_13	 = outsidetrackLine[326:327]
                if self.chkBlank(outsidetrackLine[327:328]):
                    self.race_8_13	 = outsidetrackLine[327:328]
                if self.chkBlank(outsidetrackLine[328:329]):
                    self.race_9_13	 = outsidetrackLine[328:329]
                if self.chkBlank(outsidetrackLine[329:330]):
                    self.race_10_13	 = outsidetrackLine[329:330]
                if self.chkBlank(outsidetrackLine[330:331]):
                    self.race_11_13	 = outsidetrackLine[330:331]
                if self.chkBlank(outsidetrackLine[331:332]):
                    self.race_12_13	 = outsidetrackLine[331:332]

                if self.chkBlank(outsidetrackLine[332:333]):
                    self.otb_code_14	 = outsidetrackLine[332:333]
                if self.chkBlank(outsidetrackLine[333:336]):
                    self.otb_14	 = outsidetrackLine[333:336]
                if self.chkBlank(outsidetrackLine[336:337]):
                    self.otb_classification_14	 = outsidetrackLine[336:337]
                if self.chkBlank(outsidetrackLine[337:338]):
                    self.held_classification_14	 = outsidetrackLine[337:338]
                if self.chkBlank(outsidetrackLine[338:340]):
                    self.note_code_14	 = outsidetrackLine[338:340]
                if self.chkBlank(outsidetrackLine[340:341]):
                    self.race_1_14	 = outsidetrackLine[340:341]
                if self.chkBlank(outsidetrackLine[341:342]):
                    self.race_2_14	 = outsidetrackLine[341:342]
                if self.chkBlank(outsidetrackLine[342:343]):
                    self.race_3_14	 = outsidetrackLine[342:343]
                if self.chkBlank(outsidetrackLine[343:344]):
                    self.race_4_14	 = outsidetrackLine[343:344]
                if self.chkBlank(outsidetrackLine[344:345]):
                    self.race_5_14	 = outsidetrackLine[344:345]
                if self.chkBlank(outsidetrackLine[345:346]):
                    self.race_6_14	 = outsidetrackLine[345:346]
                if self.chkBlank(outsidetrackLine[346:347]):
                    self.race_7_14	 = outsidetrackLine[346:347]
                if self.chkBlank(outsidetrackLine[347:348]):
                    self.race_8_14	 = outsidetrackLine[347:348]
                if self.chkBlank(outsidetrackLine[348:349]):
                    self.race_9_14	 = outsidetrackLine[348:349]
                if self.chkBlank(outsidetrackLine[349:350]):
                    self.race_10_14	 = outsidetrackLine[349:350]
                if self.chkBlank(outsidetrackLine[350:351]):
                    self.race_11_14	 = outsidetrackLine[350:351]
                if self.chkBlank(outsidetrackLine[351:352]):
                    self.race_12_14	 = outsidetrackLine[351:352]

                # 空白チェックして実体があるカラムは更新
                self.update_trn_outside_track(Trn_Outside_track.objects.get(id=Trn_Outside_track.objects.all().aggregate(Max('id')).get('id__max')))


    def update_trn_outside_track(self, trn_Update):
        updateFields = list()
        if self.track_code:
            trn_Update.Track_code=self.track_code
            updateFields.append('Track_code')
        if self.track_name:
            trn_Update.Track_name=self.track_name
            updateFields.append('Track_name')
        if self.date_ad:
            trn_Update.Date_AD= self.date_ad
            updateFields.append('Date_AD')
        if self.date_japanese_calendar:
            trn_Update.Date_Japanese_calendar= self.date_japanese_calendar
            updateFields.append('Date_Japanese_calendar')
        if self.held_day:
            trn_Update.Held_day= self.held_day
            updateFields.append('Held_day')
        if self.period_days:
            trn_Update.Period_days= self.period_days
            updateFields.append('Period_days')
        if self.event_name:
            trn_Update.Event_name= self.event_name
            updateFields.append('Event_name')
        if self.first_day_of_the_event:
            trn_Update.First_day_of_the_event= self.first_day_of_the_event
            updateFields.append('First_day_of_the_event')
        if self.commemorative_code:
            trn_Update.Commemorative_code=self.commemorative_code
            updateFields.append('Commemorative_code')
        if self.special_commemorative_code:
            trn_Update.Special_commemorative_code=self.special_commemorative_code
            updateFields.append('Special_commemorative_code')
        if self.otb_code:
            trn_Update.OTB_code=self.otb_code
            updateFields.append('OTB_code')
        if self.otb:
            trn_Update.OTB=self.otb
            updateFields.append('OTB')
        if self.otb_classification:
            trn_Update.OTB_Classification=self.otb_classification
            updateFields.append('OTB_Classification')
        if self.held_classification:
            trn_Update.Held_Classification=self.held_classification
            updateFields.append('Held_Classification')
        if self.note_code:
            trn_Update.Note_code=self.note_code
            updateFields.append('Note_code')
        if self.race_1:
            trn_Update.race_1=self.race_1
            updateFields.append('race_1')
        if self.race_2:
            trn_Update.race_2=self.race_2
            updateFields.append('race_2')
        if self.race_3:
            trn_Update.race_3=self.race_3
            updateFields.append('race_3')
        if self.race_4:
            trn_Update.race_4=self.race_4
            updateFields.append('race_4')
        if self.race_5:
            trn_Update.race_5=self.race_5
            updateFields.append('race_5')
        if self.race_6:
            trn_Update.race_6=self.race_6
            updateFields.append('race_6')
        if self.race_7:
            trn_Update.race_7=self.race_7
            updateFields.append('race_7')
        if self.race_8:
            trn_Update.race_8=self.race_8
            updateFields.append('race_8')
        if self.race_9:
            trn_Update.race_9=self.race_9
            updateFields.append('race_9')
        if self.race_10:
            trn_Update.race_10=self.race_10
            updateFields.append('race_10')
        if self.race_11:
            trn_Update.race_11=self.race_11
            updateFields.append('race_11')
        if self.race_12:
            trn_Update.race_12=self.race_12
            updateFields.append('race_12')

        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)


    def insert_or_update_Trn_Outside_track(self, name):

        try:
            file = open(name,'r',encoding='shift_jis')
            for line in file: # 1行しかない

                self.classification = line[0:1]
                self.data_type = line[1:2]

                outsidetrackLine = line[2:]

                self.setDatData(outsidetrackLine)

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

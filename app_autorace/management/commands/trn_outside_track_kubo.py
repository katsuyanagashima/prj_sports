_234343231import logging
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
        self.date_japanese_calendar	 = str()
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
                    self.date_japanese_calendar	 = outsidetrackLine[12:23]
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

                if self.chkBlank(outsidetrackLine[352:353]):
                    self.otb_code_15	 = outsidetrackLine[352:353]
                if self.chkBlank(outsidetrackLine[353:356]):
                    self.otb_15	 = outsidetrackLine[353:356]
                if self.chkBlank(outsidetrackLine[356:357]):
                    self.otb_classification_15	 = outsidetrackLine[356:357]
                if self.chkBlank(outsidetrackLine[357:358]):
                    self.held_classification_15	 = outsidetrackLine[357:358]
                if self.chkBlank(outsidetrackLine[358:360]):
                    self.note_code_15	 = outsidetrackLine[358:360]
                if self.chkBlank(outsidetrackLine[360:361]):
                    self.race_1_15	 = outsidetrackLine[360:361]
                if self.chkBlank(outsidetrackLine[361:362]):
                    self.race_2_15	 = outsidetrackLine[361:362]
                if self.chkBlank(outsidetrackLine[362:363]):
                    self.race_3_15	 = outsidetrackLine[362:363]
                if self.chkBlank(outsidetrackLine[363:364]):
                    self.race_4_15	 = outsidetrackLine[363:364]
                if self.chkBlank(outsidetrackLine[364:365]):
                    self.race_5_15	 = outsidetrackLine[364:365]
                if self.chkBlank(outsidetrackLine[365:366]):
                    self.race_6_15	 = outsidetrackLine[365:366]
                if self.chkBlank(outsidetrackLine[366:367]):
                    self.race_7_15	 = outsidetrackLine[366:367]
                if self.chkBlank(outsidetrackLine[367:368]):
                    self.race_8_15	 = outsidetrackLine[367:368]
                if self.chkBlank(outsidetrackLine[368:369]):
                    self.race_9_15	 = outsidetrackLine[368:369]
                if self.chkBlank(outsidetrackLine[369:370]):
                    self.race_10_15	 = outsidetrackLine[369:370]
                if self.chkBlank(outsidetrackLine[370:371]):
                    self.race_11_15	 = outsidetrackLine[370:371]
                if self.chkBlank(outsidetrackLine[371:372]):
                    self.race_12_15	 = outsidetrackLine[371:372]

                if self.chkBlank(outsidetrackLine[372:373]):
                    self.otb_code_16	 = outsidetrackLine[372:373]
                if self.chkBlank(outsidetrackLine[373:376]):
                    self.otb_16	 = outsidetrackLine[373:376]
                if self.chkBlank(outsidetrackLine[376:377]):
                    self.otb_classification_16	 = outsidetrackLine[376:377]
                if self.chkBlank(outsidetrackLine[377:378]):
                    self.held_classification_16	 = outsidetrackLine[377:378]
                if self.chkBlank(outsidetrackLine[378:380]):
                    self.note_code_16	 = outsidetrackLine[378:380]
                if self.chkBlank(outsidetrackLine[380:381]):
                    self.race_1_16	 = outsidetrackLine[380:381]
                if self.chkBlank(outsidetrackLine[381:382]):
                    self.race_2_16	 = outsidetrackLine[381:382]
                if self.chkBlank(outsidetrackLine[382:383]):
                    self.race_3_16	 = outsidetrackLine[382:383]
                if self.chkBlank(outsidetrackLine[383:384]):
                    self.race_4_16	 = outsidetrackLine[383:384]
                if self.chkBlank(outsidetrackLine[384:385]):
                    self.race_5_16	 = outsidetrackLine[384:385]
                if self.chkBlank(outsidetrackLine[385:386]):
                    self.race_6_16	 = outsidetrackLine[385:386]
                if self.chkBlank(outsidetrackLine[386:387]):
                    self.race_7_16	 = outsidetrackLine[386:387]
                if self.chkBlank(outsidetrackLine[387:388]):
                    self.race_8_16	 = outsidetrackLine[387:388]
                if self.chkBlank(outsidetrackLine[388:389]):
                    self.race_9_16	 = outsidetrackLine[388:389]
                if self.chkBlank(outsidetrackLine[389:390]):
                    self.race_10_16	 = outsidetrackLine[389:390]
                if self.chkBlank(outsidetrackLine[390:391]):
                    self.race_11_16	 = outsidetrackLine[390:391]
                if self.chkBlank(outsidetrackLine[391:392]):
                    self.race_12_16	 = outsidetrackLine[391:392]

                if self.chkBlank(outsidetrackLine[392:393]):
                    self.otb_code_17	 = outsidetrackLine[392:393]
                if self.chkBlank(outsidetrackLine[393:396]):
                    self.otb_17	 = outsidetrackLine[393:396]
                if self.chkBlank(outsidetrackLine[396:397]):
                    self.otb_classification_17	 = outsidetrackLine[396:397]
                if self.chkBlank(outsidetrackLine[397:398]):
                    self.held_classification_17	 = outsidetrackLine[397:398]
                if self.chkBlank(outsidetrackLine[398:400]):
                    self.note_code_17	 = outsidetrackLine[398:400]
                if self.chkBlank(outsidetrackLine[400:401]):
                    self.race_1_17	 = outsidetrackLine[400:401]
                if self.chkBlank(outsidetrackLine[401:402]):
                    self.race_2_17	 = outsidetrackLine[401:402]
                if self.chkBlank(outsidetrackLine[402:403]):
                    self.race_3_17	 = outsidetrackLine[402:403]
                if self.chkBlank(outsidetrackLine[403:404]):
                    self.race_4_17	 = outsidetrackLine[403:404]
                if self.chkBlank(outsidetrackLine[404:405]):
                    self.race_5_17	 = outsidetrackLine[404:405]
                if self.chkBlank(outsidetrackLine[405:406]):
                    self.race_6_17	 = outsidetrackLine[405:406]
                if self.chkBlank(outsidetrackLine[406:407]):
                    self.race_7_17	 = outsidetrackLine[406:407]
                if self.chkBlank(outsidetrackLine[407:408]):
                    self.race_8_17	 = outsidetrackLine[407:408]
                if self.chkBlank(outsidetrackLine[408:409]):
                    self.race_9_17	 = outsidetrackLine[408:409]
                if self.chkBlank(outsidetrackLine[409:410]):
                    self.race_10_17	 = outsidetrackLine[409:410]
                if self.chkBlank(outsidetrackLine[410:411]):
                    self.race_11_17	 = outsidetrackLine[410:411]
                if self.chkBlank(outsidetrackLine[411:412]):
                    self.race_12_17	 = outsidetrackLine[411:412]

                if self.chkBlank(outsidetrackLine[412:413]):
                    self.otb_code_18	 = outsidetrackLine[412:413]
                if self.chkBlank(outsidetrackLine[413:416]):
                    self.otb_18	 = outsidetrackLine[413:416]
                if self.chkBlank(outsidetrackLine[416:417]):
                    self.otb_classification_18	 = outsidetrackLine[416:417]
                if self.chkBlank(outsidetrackLine[417:418]):
                    self.held_classification_18	 = outsidetrackLine[417:418]
                if self.chkBlank(outsidetrackLine[418:420]):
                    self.note_code_18	 = outsidetrackLine[418:420]
                if self.chkBlank(outsidetrackLine[420:421]):
                    self.race_1_18	 = outsidetrackLine[420:421]
                if self.chkBlank(outsidetrackLine[421:422]):
                    self.race_2_18	 = outsidetrackLine[421:422]
                if self.chkBlank(outsidetrackLine[422:423]):
                    self.race_3_18	 = outsidetrackLine[422:423]
                if self.chkBlank(outsidetrackLine[423:424]):
                    self.race_4_18	 = outsidetrackLine[423:424]
                if self.chkBlank(outsidetrackLine[424:425]):
                    self.race_5_18	 = outsidetrackLine[424:425]
                if self.chkBlank(outsidetrackLine[425:426]):
                    self.race_6_18	 = outsidetrackLine[425:426]
                if self.chkBlank(outsidetrackLine[426:427]):
                    self.race_7_18	 = outsidetrackLine[426:427]
                if self.chkBlank(outsidetrackLine[427:428]):
                    self.race_8_18	 = outsidetrackLine[427:428]
                if self.chkBlank(outsidetrackLine[428:429]):
                    self.race_9_18	 = outsidetrackLine[428:429]
                if self.chkBlank(outsidetrackLine[429:430]):
                    self.race_10_18	 = outsidetrackLine[429:430]
                if self.chkBlank(outsidetrackLine[430:431]):
                    self.race_11_18	 = outsidetrackLine[430:431]
                if self.chkBlank(outsidetrackLine[431:432]):
                    self.race_12_18	 = outsidetrackLine[431:432]

                if self.chkBlank(outsidetrackLine[432:433]):
                    self.otb_code_19	 = outsidetrackLine[432:433]
                if self.chkBlank(outsidetrackLine[433:436]):
                    self.otb_19	 = outsidetrackLine[433:436]
                if self.chkBlank(outsidetrackLine[436:437]):
                    self.otb_classification_19	 = outsidetrackLine[436:437]
                if self.chkBlank(outsidetrackLine[437:438]):
                    self.held_classification_19	 = outsidetrackLine[437:438]
                if self.chkBlank(outsidetrackLine[438:440]):
                    self.note_code_19	 = outsidetrackLine[438:440]
                if self.chkBlank(outsidetrackLine[440:441]):
                    self.race_1_19	 = outsidetrackLine[440:441]
                if self.chkBlank(outsidetrackLine[441:442]):
                    self.race_2_19	 = outsidetrackLine[441:442]
                if self.chkBlank(outsidetrackLine[442:443]):
                    self.race_3_19	 = outsidetrackLine[442:443]
                if self.chkBlank(outsidetrackLine[443:444]):
                    self.race_4_19	 = outsidetrackLine[443:444]
                if self.chkBlank(outsidetrackLine[444:445]):
                    self.race_5_19	 = outsidetrackLine[444:445]
                if self.chkBlank(outsidetrackLine[445:446]):
                    self.race_6_19	 = outsidetrackLine[445:446]
                if self.chkBlank(outsidetrackLine[446:447]):
                    self.race_7_19	 = outsidetrackLine[446:447]
                if self.chkBlank(outsidetrackLine[447:448]):
                    self.race_8_19	 = outsidetrackLine[447:448]
                if self.chkBlank(outsidetrackLine[448:449]):
                    self.race_9_19	 = outsidetrackLine[448:449]
                if self.chkBlank(outsidetrackLine[449:450]):
                    self.race_10_19	 = outsidetrackLine[449:450]
                if self.chkBlank(outsidetrackLine[450:451]):
                    self.race_11_19	 = outsidetrackLine[450:451]
                if self.chkBlank(outsidetrackLine[451:452]):
                    self.race_12_19	 = outsidetrackLine[451:452]

                if self.chkBlank(outsidetrackLine[452:453]):
                    self.otb_code_20	 = outsidetrackLine[452:453]
                if self.chkBlank(outsidetrackLine[453:456]):
                    self.otb_20	 = outsidetrackLine[453:456]
                if self.chkBlank(outsidetrackLine[456:457]):
                    self.otb_classification_20	 = outsidetrackLine[456:457]
                if self.chkBlank(outsidetrackLine[457:458]):
                    self.held_classification_20	 = outsidetrackLine[457:458]
                if self.chkBlank(outsidetrackLine[458:460]):
                    self.note_code_20	 = outsidetrackLine[458:460]
                if self.chkBlank(outsidetrackLine[460:461]):
                    self.race_1_20	 = outsidetrackLine[460:461]
                if self.chkBlank(outsidetrackLine[461:462]):
                    self.race_2_20	 = outsidetrackLine[461:462]
                if self.chkBlank(outsidetrackLine[462:463]):
                    self.race_3_20	 = outsidetrackLine[462:463]
                if self.chkBlank(outsidetrackLine[463:464]):
                    self.race_4_20	 = outsidetrackLine[463:464]
                if self.chkBlank(outsidetrackLine[464:465]):
                    self.race_5_20	 = outsidetrackLine[464:465]
                if self.chkBlank(outsidetrackLine[465:466]):
                    self.race_6_20	 = outsidetrackLine[465:466]
                if self.chkBlank(outsidetrackLine[466:467]):
                    self.race_7_20	 = outsidetrackLine[466:467]
                if self.chkBlank(outsidetrackLine[467:468]):
                    self.race_8_20	 = outsidetrackLine[467:468]
                if self.chkBlank(outsidetrackLine[468:469]):
                    self.race_9_20	 = outsidetrackLine[468:469]
                if self.chkBlank(outsidetrackLine[469:470]):
                    self.race_10_20	 = outsidetrackLine[469:470]
                if self.chkBlank(outsidetrackLine[470:471]):
                    self.race_11_20	 = outsidetrackLine[470:471]
                if self.chkBlank(outsidetrackLine[471:472]):
                    self.race_12_20	 = outsidetrackLine[471:472]

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
        if self.otb_code_1:
            trn_Update.OTB_code_1=self.otb_code_1
            updateFields.append('OTB_code_1')
        if self.otb_1:
            trn_Update.OTB_1=self.otb_1
            updateFields.append('OTB_1')
        if self.otb_classification_1:
            trn_Update.OTB_Classification_1=self.otb_classification_1
            updateFields.append('OTB_Classification_1')
        if self.held_classification_1:
            trn_Update.Held_Classification_1=self.held_classification_1
            updateFields.append('Held_Classification_1')
        if self.note_code_1:
            trn_Update.Note_code_1=self.note_code_1
            updateFields.append('Note_code_1')
        if self.race_1_1:
            trn_Update.race_1_1=self.race_1_1
            updateFields.append('race_1_1')
        if self.race_2_1:
            trn_Update.race_2_1=self.race_2_1
            updateFields.append('race_2_1')
        if self.race_3_1:
            trn_Update.race_3_1=self.race_3_1
            updateFields.append('race_3_1')
        if self.race_4_1:
            trn_Update.race_4_1=self.race_4_1
            updateFields.append('race_4_1')
        if self.race_5_1:
            trn_Update.race_5_1=self.race_5_1
            updateFields.append('race_5_1')
        if self.race_6_1:
            trn_Update.race_6_1=self.race_6_1
            updateFields.append('race_6_1')
        if self.race_7_1:
            trn_Update.race_7_1=self.race_7_1
            updateFields.append('race_7_1')
        if self.race_8_1:
            trn_Update.race_8_1=self.race_8_1
            updateFields.append('race_8_1')
        if self.race_9_1:
            trn_Update.race_9_1=self.race_9_1
            updateFields.append('race_9_1')
        if self.race_10_1:
            trn_Update.race_10_1=self.race_10_1
            updateFields.append('race_10_1')
        if self.race_11_1:
            trn_Update.race_11_1=self.race_11_1
            updateFields.append('race_11_1')
        if self.race_12_1:
            trn_Update.race_12_1=self.race_12_1
            updateFields.append('race_12_1')

        if self.otb_code_2:
            trn_Update.OTB_code_2=self.otb_code_2
            updateFields.append('OTB_code_2')
        if self.otb_2:
            trn_Update.OTB_2=self.otb_2
            updateFields.append('OTB_2')
        if self.otb_classification_2:
            trn_Update.OTB_Classification_2=self.otb_classification_2
            updateFields.append('OTB_Classification_2')
        if self.held_classification_2:
            trn_Update.Held_Classification_2=self.held_classification_2
            updateFields.append('Held_Classification_2')
        if self.note_code_2:
            trn_Update.Note_code_2=self.note_code_2
            updateFields.append('Note_code_2')
        if self.race_1_2:
            trn_Update.race_1_2=self.race_1_2
            updateFields.append('race_1_2')
        if self.race_2_2:
            trn_Update.race_2_2=self.race_2_2
            updateFields.append('race_2_2')
        if self.race_3_2:
            trn_Update.race_3_2=self.race_3_2
            updateFields.append('race_3_2')
        if self.race_4_2:
            trn_Update.race_4_2=self.race_4_2
            updateFields.append('race_4_2')
        if self.race_5_2:
            trn_Update.race_5_2=self.race_5_2
            updateFields.append('race_5_2')
        if self.race_6_2:
            trn_Update.race_6_2=self.race_6_2
            updateFields.append('race_6_2')
        if self.race_7_2:
            trn_Update.race_7_2=self.race_7_2
            updateFields.append('race_7_2')
        if self.race_8_2:
            trn_Update.race_8_2=self.race_8_2
            updateFields.append('race_8_2')
        if self.race_9_2:
            trn_Update.race_9_2=self.race_9_2
            updateFields.append('race_9_2')
        if self.race_10_2:
            trn_Update.race_10_2=self.race_10_2
            updateFields.append('race_10_2')
        if self.race_11_2:
            trn_Update.race_11_2=self.race_11_2
            updateFields.append('race_11_2')
        if self.race_12_2:
            trn_Update.race_12_2=self.race_12_2
            updateFields.append('race_12_2')

        if self.otb_code_3:
            trn_Update.OTB_code_3=self.otb_code_3
            updateFields.append('OTB_code_3')
        if self.otb_3:
            trn_Update.OTB_3=self.otb_3
            updateFields.append('OTB_3')
        if self.otb_classification_3:
            trn_Update.OTB_Classification_3=self.otb_classification_3
            updateFields.append('OTB_Classification_3')
        if self.held_classification_3:
            trn_Update.Held_Classification_3=self.held_classification_3
            updateFields.append('Held_Classification_3')
        if self.note_code_3:
            trn_Update.Note_code_3=self.note_code_3
            updateFields.append('Note_code_3')
        if self.race_1_3:
            trn_Update.race_1_3=self.race_1_3
            updateFields.append('race_1_3')
        if self.race_2_3:
            trn_Update.race_2_3=self.race_2_3
            updateFields.append('race_2_3')
        if self.race_3_3:
            trn_Update.race_3_3=self.race_3_3
            updateFields.append('race_3_3')
        if self.race_4_3:
            trn_Update.race_4_3=self.race_4_3
            updateFields.append('race_4_3')
        if self.race_5_3:
            trn_Update.race_5_3=self.race_5_3
            updateFields.append('race_5_3')
        if self.race_6_3:
            trn_Update.race_6_3=self.race_6_3
            updateFields.append('race_6_3')
        if self.race_7_3:
            trn_Update.race_7_3=self.race_7_3
            updateFields.append('race_7_3')
        if self.race_8_3:
            trn_Update.race_8_3=self.race_8_3
            updateFields.append('race_8_3')
        if self.race_9_3:
            trn_Update.race_9_3=self.race_9_3
            updateFields.append('race_9_3')
        if self.race_10_3:
            trn_Update.race_10_3=self.race_10_3
            updateFields.append('race_10_3')
        if self.race_11_3:
            trn_Update.race_11_3=self.race_11_3
            updateFields.append('race_11_3')
        if self.race_12_3:
            trn_Update.race_12_3=self.race_12_3
            updateFields.append('race_12_3')

        if self.otb_code_4:
            trn_Update.OTB_code_4=self.otb_code_4
            updateFields.append('OTB_code_4')
        if self.otb_4:
            trn_Update.OTB_4=self.otb_4
            updateFields.append('OTB_4')
        if self.otb_classification_4:
            trn_Update.OTB_Classification_4=self.otb_classification_4
            updateFields.append('OTB_Classification_4')
        if self.held_classification_4:
            trn_Update.Held_Classification_4=self.held_classification_4
            updateFields.append('Held_Classification_4')
        if self.note_code_4:
            trn_Update.Note_code_4=self.note_code_4
            updateFields.append('Note_code_4')
        if self.race_1_4:
            trn_Update.race_1_4=self.race_1_4
            updateFields.append('race_1_4')
        if self.race_2_4:
            trn_Update.race_2_4=self.race_2_4
            updateFields.append('race_2_4')
        if self.race_3_4:
            trn_Update.race_3_4=self.race_3_4
            updateFields.append('race_3_4')
        if self.race_4_4:
            trn_Update.race_4_4=self.race_4_4
            updateFields.append('race_4_4')
        if self.race_5_4:
            trn_Update.race_5_4=self.race_5_4
            updateFields.append('race_5_4')
        if self.race_6_4:
            trn_Update.race_6_4=self.race_6_4
            updateFields.append('race_6_4')
        if self.race_7_4:
            trn_Update.race_7_4=self.race_7_4
            updateFields.append('race_7_4')
        if self.race_8_4:
            trn_Update.race_8_4=self.race_8_4
            updateFields.append('race_8_4')
        if self.race_9_4:
            trn_Update.race_9_4=self.race_9_4
            updateFields.append('race_9_4')
        if self.race_10_4:
            trn_Update.race_10_4=self.race_10_4
            updateFields.append('race_10_4')
        if self.race_11_4:
            trn_Update.race_11_4=self.race_11_4
            updateFields.append('race_11_4')
        if self.race_12_4:
            trn_Update.race_12_4=self.race_12_4
            updateFields.append('race_12_4')

        if self.otb_code_5:
            trn_Update.OTB_code_5=self.otb_code_5
            updateFields.append('OTB_code_5')
        if self.otb_5:
            trn_Update.OTB_5=self.otb_5
            updateFields.append('OTB_5')
        if self.otb_classification_5:
            trn_Update.OTB_Classification_5=self.otb_classification_5
            updateFields.append('OTB_Classification_5')
        if self.held_classification_5:
            trn_Update.Held_Classification_5=self.held_classification_5
            updateFields.append('Held_Classification_5')
        if self.note_code_5:
            trn_Update.Note_code_5=self.note_code_5
            updateFields.append('Note_code_5')
        if self.race_1_5:
            trn_Update.race_1_5=self.race_1_5
            updateFields.append('race_1_5')
        if self.race_2_5:
            trn_Update.race_2_5=self.race_2_5
            updateFields.append('race_2_5')
        if self.race_3_5:
            trn_Update.race_3_5=self.race_3_5
            updateFields.append('race_3_5')
        if self.race_4_5:
            trn_Update.race_4_5=self.race_4_5
            updateFields.append('race_4_5')
        if self.race_5_5:
            trn_Update.race_5_5=self.race_5_5
            updateFields.append('race_5_5')
        if self.race_6_5:
            trn_Update.race_6_5=self.race_6_5
            updateFields.append('race_6_5')
        if self.race_7_5:
            trn_Update.race_7_5=self.race_7_5
            updateFields.append('race_7_5')
        if self.race_8_5:
            trn_Update.race_8_5=self.race_8_5
            updateFields.append('race_8_5')
        if self.race_9_5:
            trn_Update.race_9_5=self.race_9_5
            updateFields.append('race_9_5')
        if self.race_10_5:
            trn_Update.race_10_5=self.race_10_5
            updateFields.append('race_10_5')
        if self.race_11_5:
            trn_Update.race_11_5=self.race_11_5
            updateFields.append('race_11_5')
        if self.race_12_5:
            trn_Update.race_12_5=self.race_12_5
            updateFields.append('race_12_5')

        if self.otb_code_6:
            trn_Update.OTB_code_6=self.otb_code_6
            updateFields.append('OTB_code_6')
        if self.otb_6:
            trn_Update.OTB_6=self.otb_6
            updateFields.append('OTB_6')
        if self.otb_classification_6:
            trn_Update.OTB_Classification_6=self.otb_classification_6
            updateFields.append('OTB_Classification_6')
        if self.held_classification_6:
            trn_Update.Held_Classification_6=self.held_classification_6
            updateFields.append('Held_Classification_6')
        if self.note_code_6:
            trn_Update.Note_code_6=self.note_code_6
            updateFields.append('Note_code_6')
        if self.race_1_6:
            trn_Update.race_1_6=self.race_1_6
            updateFields.append('race_1_6')
        if self.race_2_6:
            trn_Update.race_2_6=self.race_2_6
            updateFields.append('race_2_6')
        if self.race_3_6:
            trn_Update.race_3_6=self.race_3_6
            updateFields.append('race_3_6')
        if self.race_4_6:
            trn_Update.race_4_6=self.race_4_6
            updateFields.append('race_4_6')
        if self.race_5_6:
            trn_Update.race_5_6=self.race_5_6
            updateFields.append('race_5_6')
        if self.race_6_6:
            trn_Update.race_6_6=self.race_6_6
            updateFields.append('race_6_6')
        if self.race_7_6:
            trn_Update.race_7_6=self.race_7_6
            updateFields.append('race_7_6')
        if self.race_8_6:
            trn_Update.race_8_6=self.race_8_6
            updateFields.append('race_8_6')
        if self.race_9_6:
            trn_Update.race_9_6=self.race_9_6
            updateFields.append('race_9_6')
        if self.race_10_6:
            trn_Update.race_10_6=self.race_10_6
            updateFields.append('race_10_6')
        if self.race_11_6:
            trn_Update.race_11_6=self.race_11_6
            updateFields.append('race_11_6')
        if self.race_12_6:
            trn_Update.race_12_6=self.race_12_6
            updateFields.append('race_12_6')

        if self.otb_code_7:
            trn_Update.OTB_code_7=self.otb_code_7
            updateFields.append('OTB_code_7')
        if self.otb_7:
            trn_Update.OTB_7=self.otb_7
            updateFields.append('OTB_7')
        if self.otb_classification_7:
            trn_Update.OTB_Classification_7=self.otb_classification_7
            updateFields.append('OTB_Classification_7')
        if self.held_classification_7:
            trn_Update.Held_Classification_7=self.held_classification_7
            updateFields.append('Held_Classification_7')
        if self.note_code_7:
            trn_Update.Note_code_7=self.note_code_7
            updateFields.append('Note_code_7')
        if self.race_1_7:
            trn_Update.race_1_7=self.race_1_7
            updateFields.append('race_1_7')
        if self.race_2_7:
            trn_Update.race_2_7=self.race_2_7
            updateFields.append('race_2_7')
        if self.race_3_7:
            trn_Update.race_3_7=self.race_3_7
            updateFields.append('race_3_7')
        if self.race_4_7:
            trn_Update.race_4_7=self.race_4_7
            updateFields.append('race_4_7')
        if self.race_5_7:
            trn_Update.race_5_7=self.race_5_7
            updateFields.append('race_5_7')
        if self.race_6_7:
            trn_Update.race_6_7=self.race_6_7
            updateFields.append('race_6_7')
        if self.race_7_7:
            trn_Update.race_7_7=self.race_7_7
            updateFields.append('race_7_7')
        if self.race_8_7:
            trn_Update.race_8_7=self.race_8_7
            updateFields.append('race_8_7')
        if self.race_9_7:
            trn_Update.race_9_7=self.race_9_7
            updateFields.append('race_9_7')
        if self.race_10_7:
            trn_Update.race_10_7=self.race_10_7
            updateFields.append('race_10_7')
        if self.race_11_7:
            trn_Update.race_11_7=self.race_11_7
            updateFields.append('race_11_7')
        if self.race_12_7:
            trn_Update.race_12_7=self.race_12_7
            updateFields.append('race_12_7')

        if self.otb_code_8:
            trn_Update.OTB_code_8=self.otb_code_8
            updateFields.append('OTB_code_8')
        if self.otb_8:
            trn_Update.OTB_8=self.otb_8
            updateFields.append('OTB_8')
        if self.otb_classification_8:
            trn_Update.OTB_Classification_8=self.otb_classification_8
            updateFields.append('OTB_Classification_8')
        if self.held_classification_8:
            trn_Update.Held_Classification_8=self.held_classification_8
            updateFields.append('Held_Classification_8')
        if self.note_code_8:
            trn_Update.Note_code_8=self.note_code_8
            updateFields.append('Note_code_8')
        if self.race_1_8:
            trn_Update.race_1_8=self.race_1_8
            updateFields.append('race_1_8')
        if self.race_2_8:
            trn_Update.race_2_8=self.race_2_8
            updateFields.append('race_2_8')
        if self.race_3_8:
            trn_Update.race_3_8=self.race_3_8
            updateFields.append('race_3_8')
        if self.race_4_8:
            trn_Update.race_4_8=self.race_4_8
            updateFields.append('race_4_8')
        if self.race_5_8:
            trn_Update.race_5_8=self.race_5_8
            updateFields.append('race_5_8')
        if self.race_6_8:
            trn_Update.race_6_8=self.race_6_8
            updateFields.append('race_6_8')
        if self.race_7_8:
            trn_Update.race_7_8=self.race_7_8
            updateFields.append('race_7_8')
        if self.race_8_8:
            trn_Update.race_8_8=self.race_8_8
            updateFields.append('race_8_8')
        if self.race_9_8:
            trn_Update.race_9_8=self.race_9_8
            updateFields.append('race_9_8')
        if self.race_10_8:
            trn_Update.race_10_8=self.race_10_8
            updateFields.append('race_10_8')
        if self.race_11_8:
            trn_Update.race_11_8=self.race_11_8
            updateFields.append('race_11_8')
        if self.race_12_8:
            trn_Update.race_12_8=self.race_12_8
            updateFields.append('race_12_8')

        if self.otb_code_9:
            trn_Update.OTB_code_9=self.otb_code_9
            updateFields.append('OTB_code_9')
        if self.otb_9:
            trn_Update.OTB_9=self.otb_9
            updateFields.append('OTB_9')
        if self.otb_classification_9:
            trn_Update.OTB_Classification_9=self.otb_classification_9
            updateFields.append('OTB_Classification_9')
        if self.held_classification_9:
            trn_Update.Held_Classification_9=self.held_classification_9
            updateFields.append('Held_Classification_9')
        if self.note_code_9:
            trn_Update.Note_code_9=self.note_code_9
            updateFields.append('Note_code_9')
        if self.race_1_9:
            trn_Update.race_1_9=self.race_1_9
            updateFields.append('race_1_9')
        if self.race_2_9:
            trn_Update.race_2_9=self.race_2_9
            updateFields.append('race_2_9')
        if self.race_3_9:
            trn_Update.race_3_9=self.race_3_9
            updateFields.append('race_3_9')
        if self.race_4_9:
            trn_Update.race_4_9=self.race_4_9
            updateFields.append('race_4_9')
        if self.race_5_9:
            trn_Update.race_5_9=self.race_5_9
            updateFields.append('race_5_9')
        if self.race_6_9:
            trn_Update.race_6_9=self.race_6_9
            updateFields.append('race_6_9')
        if self.race_7_9:
            trn_Update.race_7_9=self.race_7_9
            updateFields.append('race_7_9')
        if self.race_8_9:
            trn_Update.race_8_9=self.race_8_9
            updateFields.append('race_8_9')
        if self.race_9_9:
            trn_Update.race_9_9=self.race_9_9
            updateFields.append('race_9_9')
        if self.race_10_9:
            trn_Update.race_10_9=self.race_10_9
            updateFields.append('race_10_9')
        if self.race_11_9:
            trn_Update.race_11_9=self.race_11_9
            updateFields.append('race_11_9')
        if self.race_12_9:
            trn_Update.race_12_9=self.race_12_9
            updateFields.append('race_12_9')

        if self.otb_code_10:
            trn_Update.OTB_code_10=self.otb_code_10
            updateFields.append('OTB_code_10')
        if self.otb_10:
            trn_Update.OTB_10=self.otb_10
            updateFields.append('OTB_10')
        if self.otb_classification_10:
            trn_Update.OTB_Classification_10=self.otb_classification_10
            updateFields.append('OTB_Classification_10')
        if self.held_classification_10:
            trn_Update.Held_Classification_10=self.held_classification_10
            updateFields.append('Held_Classification_10')
        if self.note_code_10:
            trn_Update.Note_code_10=self.note_code_10
            updateFields.append('Note_code_10')
        if self.race_1_10:
            trn_Update.race_1_10=self.race_1_10
            updateFields.append('race_1_10')
        if self.race_2_10:
            trn_Update.race_2_10=self.race_2_10
            updateFields.append('race_2_10')
        if self.race_3_10:
            trn_Update.race_3_10=self.race_3_10
            updateFields.append('race_3_10')
        if self.race_4_10:
            trn_Update.race_4_10=self.race_4_10
            updateFields.append('race_4_10')
        if self.race_5_10:
            trn_Update.race_5_10=self.race_5_10
            updateFields.append('race_5_10')
        if self.race_6_10:
            trn_Update.race_6_10=self.race_6_10
            updateFields.append('race_6_10')
        if self.race_7_10:
            trn_Update.race_7_10=self.race_7_10
            updateFields.append('race_7_10')
        if self.race_8_10:
            trn_Update.race_8_10=self.race_8_10
            updateFields.append('race_8_10')
        if self.race_9_10:
            trn_Update.race_9_10=self.race_9_10
            updateFields.append('race_9_10')
        if self.race_10_10:
            trn_Update.race_10_10=self.race_10_10
            updateFields.append('race_10_10')
        if self.race_11_10:
            trn_Update.race_11_10=self.race_11_10
            updateFields.append('race_11_10')
        if self.race_12_10:
            trn_Update.race_12_10=self.race_12_10
            updateFields.append('race_12_10')

        if self.otb_code_11:
            trn_Update.OTB_code_11=self.otb_code_11
            updateFields.append('OTB_code_11')
        if self.otb_11:
            trn_Update.OTB_11=self.otb_11
            updateFields.append('OTB_11')
        if self.otb_classification_11:
            trn_Update.OTB_Classification_11=self.otb_classification_11
            updateFields.append('OTB_Classification_11')
        if self.held_classification_11:
            trn_Update.Held_Classification_11=self.held_classification_11
            updateFields.append('Held_Classification_11')
        if self.note_code_11:
            trn_Update.Note_code_11=self.note_code_11
            updateFields.append('Note_code_11')
        if self.race_1_11:
            trn_Update.race_1_11=self.race_1_11
            updateFields.append('race_1_11')
        if self.race_2_11:
            trn_Update.race_2_11=self.race_2_11
            updateFields.append('race_2_11')
        if self.race_3_11:
            trn_Update.race_3_11=self.race_3_11
            updateFields.append('race_3_11')
        if self.race_4_11:
            trn_Update.race_4_11=self.race_4_11
            updateFields.append('race_4_11')
        if self.race_5_11:
            trn_Update.race_5_11=self.race_5_11
            updateFields.append('race_5_11')
        if self.race_6_11:
            trn_Update.race_6_11=self.race_6_11
            updateFields.append('race_6_11')
        if self.race_7_11:
            trn_Update.race_7_11=self.race_7_11
            updateFields.append('race_7_11')
        if self.race_8_11:
            trn_Update.race_8_11=self.race_8_11
            updateFields.append('race_8_11')
        if self.race_9_11:
            trn_Update.race_9_11=self.race_9_11
            updateFields.append('race_9_11')
        if self.race_10_11:
            trn_Update.race_10_11=self.race_10_11
            updateFields.append('race_10_11')
        if self.race_11_11:
            trn_Update.race_11_11=self.race_11_11
            updateFields.append('race_11_11')
        if self.race_12_11:
            trn_Update.race_12_11=self.race_12_11
            updateFields.append('race_12_11')

        if self.otb_code_12:
            trn_Update.OTB_code_12=self.otb_code_12
            updateFields.append('OTB_code_12')
        if self.otb_12:
            trn_Update.OTB_12=self.otb_12
            updateFields.append('OTB_12')
        if self.otb_classification_12:
            trn_Update.OTB_Classification_12=self.otb_classification_12
            updateFields.append('OTB_Classification_12')
        if self.held_classification_12:
            trn_Update.Held_Classification_12=self.held_classification_12
            updateFields.append('Held_Classification_12')
        if self.note_code_12:
            trn_Update.Note_code_12=self.note_code_12
            updateFields.append('Note_code_12')
        if self.race_1_12:
            trn_Update.race_1_12=self.race_1_12
            updateFields.append('race_1_12')
        if self.race_2_12:
            trn_Update.race_2_12=self.race_2_12
            updateFields.append('race_2_12')
        if self.race_3_12:
            trn_Update.race_3_12=self.race_3_12
            updateFields.append('race_3_12')
        if self.race_4_12:
            trn_Update.race_4_12=self.race_4_12
            updateFields.append('race_4_12')
        if self.race_5_12:
            trn_Update.race_5_12=self.race_5_12
            updateFields.append('race_5_12')
        if self.race_6_12:
            trn_Update.race_6_12=self.race_6_12
            updateFields.append('race_6_12')
        if self.race_7_12:
            trn_Update.race_7_12=self.race_7_12
            updateFields.append('race_7_12')
        if self.race_8_12:
            trn_Update.race_8_12=self.race_8_12
            updateFields.append('race_8_12')
        if self.race_9_12:
            trn_Update.race_9_12=self.race_9_12
            updateFields.append('race_9_12')
        if self.race_10_12:
            trn_Update.race_10_12=self.race_10_12
            updateFields.append('race_10_12')
        if self.race_11_12:
            trn_Update.race_11_12=self.race_11_12
            updateFields.append('race_11_12')
        if self.race_12_12:
            trn_Update.race_12_12=self.race_12_12
            updateFields.append('race_12_12')

        if self.otb_code_13:
            trn_Update.OTB_code_13=self.otb_code_13
            updateFields.append('OTB_code_13')
        if self.otb_13:
            trn_Update.OTB_13=self.otb_13
            updateFields.append('OTB_13')
        if self.otb_classification_13:
            trn_Update.OTB_Classification_13=self.otb_classification_13
            updateFields.append('OTB_Classification_13')
        if self.held_classification_13:
            trn_Update.Held_Classification_13=self.held_classification_13
            updateFields.append('Held_Classification_13')
        if self.note_code_13:
            trn_Update.Note_code_13=self.note_code_13
            updateFields.append('Note_code_13')
        if self.race_1_13:
            trn_Update.race_1_13=self.race_1_13
            updateFields.append('race_1_13')
        if self.race_2_13:
            trn_Update.race_2_13=self.race_2_13
            updateFields.append('race_2_13')
        if self.race_3_13:
            trn_Update.race_3_13=self.race_3_13
            updateFields.append('race_3_13')
        if self.race_4_13:
            trn_Update.race_4_13=self.race_4_13
            updateFields.append('race_4_13')
        if self.race_5_13:
            trn_Update.race_5_13=self.race_5_13
            updateFields.append('race_5_13')
        if self.race_6_13:
            trn_Update.race_6_13=self.race_6_13
            updateFields.append('race_6_13')
        if self.race_7_13:
            trn_Update.race_7_13=self.race_7_13
            updateFields.append('race_7_13')
        if self.race_8_13:
            trn_Update.race_8_13=self.race_8_13
            updateFields.append('race_8_13')
        if self.race_9_13:
            trn_Update.race_9_13=self.race_9_13
            updateFields.append('race_9_13')
        if self.race_10_13:
            trn_Update.race_10_13=self.race_10_13
            updateFields.append('race_10_13')
        if self.race_11_13:
            trn_Update.race_11_13=self.race_11_13
            updateFields.append('race_11_13')
        if self.race_12_13:
            trn_Update.race_12_13=self.race_12_13
            updateFields.append('race_12_13')

        if self.otb_code_14:
            trn_Update.OTB_code_14=self.otb_code_14
            updateFields.append('OTB_code_14')
        if self.otb_14:
            trn_Update.OTB_14=self.otb_14
            updateFields.append('OTB_14')
        if self.otb_classification_14:
            trn_Update.OTB_Classification_14=self.otb_classification_14
            updateFields.append('OTB_Classification_14')
        if self.held_classification_14:
            trn_Update.Held_Classification_14=self.held_classification_14
            updateFields.append('Held_Classification_14')
        if self.note_code_14:
            trn_Update.Note_code_14=self.note_code_14
            updateFields.append('Note_code_14')
        if self.race_1_14:
            trn_Update.race_1_14=self.race_1_14
            updateFields.append('race_1_14')
        if self.race_2_14:
            trn_Update.race_2_14=self.race_2_14
            updateFields.append('race_2_14')
        if self.race_3_14:
            trn_Update.race_3_14=self.race_3_14
            updateFields.append('race_3_14')
        if self.race_4_14:
            trn_Update.race_4_14=self.race_4_14
            updateFields.append('race_4_14')
        if self.race_5_14:
            trn_Update.race_5_14=self.race_5_14
            updateFields.append('race_5_14')
        if self.race_6_14:
            trn_Update.race_6_14=self.race_6_14
            updateFields.append('race_6_14')
        if self.race_7_14:
            trn_Update.race_7_14=self.race_7_14
            updateFields.append('race_7_14')
        if self.race_8_14:
            trn_Update.race_8_14=self.race_8_14
            updateFields.append('race_8_14')
        if self.race_9_14:
            trn_Update.race_9_14=self.race_9_14
            updateFields.append('race_9_14')
        if self.race_10_14:
            trn_Update.race_10_14=self.race_10_14
            updateFields.append('race_10_14')
        if self.race_11_14:
            trn_Update.race_11_14=self.race_11_14
            updateFields.append('race_11_14')
        if self.race_12_14:
            trn_Update.race_12_14=self.race_12_14
            updateFields.append('race_12_14')

        if self.otb_code_15:
            trn_Update.OTB_code_15=self.otb_code_15
            updateFields.append('OTB_code_15')
        if self.otb_15:
            trn_Update.OTB_15=self.otb_15
            updateFields.append('OTB_15')
        if self.otb_classification_15:
            trn_Update.OTB_Classification_15=self.otb_classification_15
            updateFields.append('OTB_Classification_15')
        if self.held_classification_15:
            trn_Update.Held_Classification_15=self.held_classification_15
            updateFields.append('Held_Classification_15')
        if self.note_code_15:
            trn_Update.Note_code_15=self.note_code_15
            updateFields.append('Note_code_15')
        if self.race_1_15:
            trn_Update.race_1_15=self.race_1_15
            updateFields.append('race_1_15')
        if self.race_2_15:
            trn_Update.race_2_15=self.race_2_15
            updateFields.append('race_2_15')
        if self.race_3_15:
            trn_Update.race_3_15=self.race_3_15
            updateFields.append('race_3_15')
        if self.race_4_15:
            trn_Update.race_4_15=self.race_4_15
            updateFields.append('race_4_15')
        if self.race_5_15:
            trn_Update.race_5_15=self.race_5_15
            updateFields.append('race_5_15')
        if self.race_6_15:
            trn_Update.race_6_15=self.race_6_15
            updateFields.append('race_6_15')
        if self.race_7_15:
            trn_Update.race_7_15=self.race_7_15
            updateFields.append('race_7_15')
        if self.race_8_15:
            trn_Update.race_8_15=self.race_8_15
            updateFields.append('race_8_15')
        if self.race_9_15:
            trn_Update.race_9_15=self.race_9_15
            updateFields.append('race_9_15')
        if self.race_10_15:
            trn_Update.race_10_15=self.race_10_15
            updateFields.append('race_10_15')
        if self.race_11_15:
            trn_Update.race_11_15=self.race_11_15
            updateFields.append('race_11_15')
        if self.race_12_15:
            trn_Update.race_12_15=self.race_12_15
            updateFields.append('race_12_15')

        if self.otb_code_16:
            trn_Update.OTB_code_16=self.otb_code_16
            updateFields.append('OTB_code_16')
        if self.otb_16:
            trn_Update.OTB_16=self.otb_16
            updateFields.append('OTB_16')
        if self.otb_classification_16:
            trn_Update.OTB_Classification_16=self.otb_classification_16
            updateFields.append('OTB_Classification_16')
        if self.held_classification_16:
            trn_Update.Held_Classification_16=self.held_classification_16
            updateFields.append('Held_Classification_16')
        if self.note_code_16:
            trn_Update.Note_code_16=self.note_code_16
            updateFields.append('Note_code_16')
        if self.race_1_16:
            trn_Update.race_1_16=self.race_1_16
            updateFields.append('race_1_16')
        if self.race_2_16:
            trn_Update.race_2_16=self.race_2_16
            updateFields.append('race_2_16')
        if self.race_3_16:
            trn_Update.race_3_16=self.race_3_16
            updateFields.append('race_3_16')
        if self.race_4_16:
            trn_Update.race_4_16=self.race_4_16
            updateFields.append('race_4_16')
        if self.race_5_16:
            trn_Update.race_5_16=self.race_5_16
            updateFields.append('race_5_16')
        if self.race_6_16:
            trn_Update.race_6_16=self.race_6_16
            updateFields.append('race_6_16')
        if self.race_7_16:
            trn_Update.race_7_16=self.race_7_16
            updateFields.append('race_7_16')
        if self.race_8_16:
            trn_Update.race_8_16=self.race_8_16
            updateFields.append('race_8_16')
        if self.race_9_16:
            trn_Update.race_9_16=self.race_9_16
            updateFields.append('race_9_16')
        if self.race_10_16:
            trn_Update.race_10_16=self.race_10_16
            updateFields.append('race_10_16')
        if self.race_11_16:
            trn_Update.race_11_16=self.race_11_16
            updateFields.append('race_11_16')
        if self.race_12_16:
            trn_Update.race_12_16=self.race_12_16
            updateFields.append('race_12_16')

        if self.otb_code_17:
            trn_Update.OTB_code_17=self.otb_code_17
            updateFields.append('OTB_code_17')
        if self.otb_17:
            trn_Update.OTB_17=self.otb_17
            updateFields.append('OTB_17')
        if self.otb_classification_17:
            trn_Update.OTB_Classification_17=self.otb_classification_17
            updateFields.append('OTB_Classification_17')
        if self.held_classification_17:
            trn_Update.Held_Classification_17=self.held_classification_17
            updateFields.append('Held_Classification_17')
        if self.note_code_17:
            trn_Update.Note_code_17=self.note_code_17
            updateFields.append('Note_code_17')
        if self.race_1_17:
            trn_Update.race_1_17=self.race_1_17
            updateFields.append('race_1_17')
        if self.race_2_17:
            trn_Update.race_2_17=self.race_2_17
            updateFields.append('race_2_17')
        if self.race_3_17:
            trn_Update.race_3_17=self.race_3_17
            updateFields.append('race_3_17')
        if self.race_4_17:
            trn_Update.race_4_17=self.race_4_17
            updateFields.append('race_4_17')
        if self.race_5_17:
            trn_Update.race_5_17=self.race_5_17
            updateFields.append('race_5_17')
        if self.race_6_17:
            trn_Update.race_6_17=self.race_6_17
            updateFields.append('race_6_17')
        if self.race_7_17:
            trn_Update.race_7_17=self.race_7_17
            updateFields.append('race_7_17')
        if self.race_8_17:
            trn_Update.race_8_17=self.race_8_17
            updateFields.append('race_8_17')
        if self.race_9_17:
            trn_Update.race_9_17=self.race_9_17
            updateFields.append('race_9_17')
        if self.race_10_17:
            trn_Update.race_10_17=self.race_10_17
            updateFields.append('race_10_17')
        if self.race_11_17:
            trn_Update.race_11_17=self.race_11_17
            updateFields.append('race_11_17')
        if self.race_12_17:
            trn_Update.race_12_17=self.race_12_17
            updateFields.append('race_12_17')

        if self.otb_code_18:
            trn_Update.OTB_code_18=self.otb_code_18
            updateFields.append('OTB_code_18')
        if self.otb_18:
            trn_Update.OTB_18=self.otb_18
            updateFields.append('OTB_18')
        if self.otb_classification_18:
            trn_Update.OTB_Classification_18=self.otb_classification_18
            updateFields.append('OTB_Classification_18')
        if self.held_classification_18:
            trn_Update.Held_Classification_18=self.held_classification_18
            updateFields.append('Held_Classification_18')
        if self.note_code_18:
            trn_Update.Note_code_18=self.note_code_18
            updateFields.append('Note_code_18')
        if self.race_1_18:
            trn_Update.race_1_18=self.race_1_18
            updateFields.append('race_1_18')
        if self.race_2_18:
            trn_Update.race_2_18=self.race_2_18
            updateFields.append('race_2_18')
        if self.race_3_18:
            trn_Update.race_3_18=self.race_3_18
            updateFields.append('race_3_18')
        if self.race_4_18:
            trn_Update.race_4_18=self.race_4_18
            updateFields.append('race_4_18')
        if self.race_5_18:
            trn_Update.race_5_18=self.race_5_18
            updateFields.append('race_5_18')
        if self.race_6_18:
            trn_Update.race_6_18=self.race_6_18
            updateFields.append('race_6_18')
        if self.race_7_18:
            trn_Update.race_7_18=self.race_7_18
            updateFields.append('race_7_18')
        if self.race_8_18:
            trn_Update.race_8_18=self.race_8_18
            updateFields.append('race_8_18')
        if self.race_9_18:
            trn_Update.race_9_18=self.race_9_18
            updateFields.append('race_9_18')
        if self.race_10_18:
            trn_Update.race_10_18=self.race_10_18
            updateFields.append('race_10_18')
        if self.race_11_18:
            trn_Update.race_11_18=self.race_11_18
            updateFields.append('race_11_18')
        if self.race_12_18:
            trn_Update.race_12_18=self.race_12_18
            updateFields.append('race_12_18')

        if self.otb_code_19:
            trn_Update.OTB_code_19=self.otb_code_19
            updateFields.append('OTB_code_19')
        if self.otb_19:
            trn_Update.OTB_19=self.otb_19
            updateFields.append('OTB_19')
        if self.otb_classification_19:
            trn_Update.OTB_Classification_19=self.otb_classification_19
            updateFields.append('OTB_Classification_19')
        if self.held_classification_19:
            trn_Update.Held_Classification_19=self.held_classification_19
            updateFields.append('Held_Classification_19')
        if self.note_code_19:
            trn_Update.Note_code_19=self.note_code_19
            updateFields.append('Note_code_19')
        if self.race_1_19:
            trn_Update.race_1_19=self.race_1_19
            updateFields.append('race_1_19')
        if self.race_2_19:
            trn_Update.race_2_19=self.race_2_19
            updateFields.append('race_2_19')
        if self.race_3_19:
            trn_Update.race_3_19=self.race_3_19
            updateFields.append('race_3_19')
        if self.race_4_19:
            trn_Update.race_4_19=self.race_4_19
            updateFields.append('race_4_19')
        if self.race_5_19:
            trn_Update.race_5_19=self.race_5_19
            updateFields.append('race_5_19')
        if self.race_6_19:
            trn_Update.race_6_19=self.race_6_19
            updateFields.append('race_6_19')
        if self.race_7_19:
            trn_Update.race_7_19=self.race_7_19
            updateFields.append('race_7_19')
        if self.race_8_19:
            trn_Update.race_8_19=self.race_8_19
            updateFields.append('race_8_19')
        if self.race_9_19:
            trn_Update.race_9_19=self.race_9_19
            updateFields.append('race_9_19')
        if self.race_10_19:
            trn_Update.race_10_19=self.race_10_19
            updateFields.append('race_10_19')
        if self.race_11_19:
            trn_Update.race_11_19=self.race_11_19
            updateFields.append('race_11_19')
        if self.race_12_19:
            trn_Update.race_12_19=self.race_12_19
            updateFields.append('race_12_19')

        if self.otb_code_20:
            trn_Update.OTB_code_20=self.otb_code_20
            updateFields.append('OTB_code_20')
        if self.otb_20:
            trn_Update.OTB_20=self.otb_20
            updateFields.append('OTB_20')
        if self.otb_classification_20:
            trn_Update.OTB_Classification_20=self.otb_classification_20
            updateFields.append('OTB_Classification_20')
        if self.held_classification_20:
            trn_Update.Held_Classification_20=self.held_classification_20
            updateFields.append('Held_Classification_20')
        if self.note_code_20:
            trn_Update.Note_code_20=self.note_code_20
            updateFields.append('Note_code_20')
        if self.race_1_20:
            trn_Update.race_1_20=self.race_1_20
            updateFields.append('race_1_20')
        if self.race_2_20:
            trn_Update.race_2_20=self.race_2_20
            updateFields.append('race_2_20')
        if self.race_3_20:
            trn_Update.race_3_20=self.race_3_20
            updateFields.append('race_3_20')
        if self.race_4_20:
            trn_Update.race_4_20=self.race_4_20
            updateFields.append('race_4_20')
        if self.race_5_20:
            trn_Update.race_5_20=self.race_5_20
            updateFields.append('race_5_20')
        if self.race_6_20:
            trn_Update.race_6_20=self.race_6_20
            updateFields.append('race_6_20')
        if self.race_7_20:
            trn_Update.race_7_20=self.race_7_20
            updateFields.append('race_7_20')
        if self.race_8_20:
            trn_Update.race_8_20=self.race_8_20
            updateFields.append('race_8_20')
        if self.race_9_20:
            trn_Update.race_9_20=self.race_9_20
            updateFields.append('race_9_20')
        if self.race_10_20:
            trn_Update.race_10_20=self.race_10_20
            updateFields.append('race_10_20')
        if self.race_11_20:
            trn_Update.race_11_20=self.race_11_20
            updateFields.append('race_11_20')
        if self.race_12_20:
            trn_Update.race_12_20=self.race_12_20
            updateFields.append('race_12_20')

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

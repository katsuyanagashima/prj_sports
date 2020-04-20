import logging
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
# 場外売場情報レコード（mmddhhmmss00000004.dat）
scheduleID = 5
outsidetrackData = "outsidetrackData"

outsidetrack = 6 # 場情報　繰り返しの数

class Outside_track():


    def init_trn_outside_track(self):
        self.classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
        self.data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
        self.track_code	 = int()
        self.track_name	 = str()
        self.date_ad	 = str()
        self.date_japanese_calender	 = str()
        self.held_day = str()
        self.period_days	 = str()
        self.event_name = str()
        self.first_day_of_the_event	 = str()
        self.commemorative_code = int()
        self.special_commemorative_code	 = int()
        self.otb_code = int()
        self.otb	 = str()
        self.otb_classification = str()
        self.held_classification	 = str()
        self.note_code	 = int()
        self.race_1	 = str()
        self.race_2	 = str()
        self.race_3	 = str()
        self.race_4	 = str()
        self.race_5	 = str()
        self.race_6	 = str()
        self.race_7	 = str()
        self.race_8	 = str()
        self.race_9	 = str()
        self.race_10	 = str()
        self.race_11	 = str()
        self.race_12	 = str()

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
                    self.otb_code	 = outsidetrackLine[72:73]
                if self.chkBlank(outsidetrackLine[73:76]):
                    self.otb	 = outsidetrackLine[73:76]
                if self.chkBlank(outsidetrackLine[76:77]):
                    self.otb_classification	 = outsidetrackLine[76:77]
                if self.chkBlank(outsidetrackLine[77:78]):
                    self.held_classification	 = outsidetrackLine[77:78]
                if self.chkBlank(outsidetrackLine[78:80]):
                    self.note_code	 = outsidetrackLine[78:80]
                if self.chkBlank(outsidetrackLine[80:81]):
                    self.race_1	 = outsidetrackLine[80:81]
                if self.chkBlank(outsidetrackLine[81:82]):
                    self.race_2	 = outsidetrackLine[81:82]
                if self.chkBlank(outsidetrackLine[82:83]):
                    self.race_3	 = outsidetrackLine[82:83]
                if self.chkBlank(outsidetrackLine[83:84]):
                    self.race_4	 = outsidetrackLine[83:84]
                if self.chkBlank(outsidetrackLine[84:85]):
                    self.race_5	 = outsidetrackLine[84:85]
                if self.chkBlank(outsidetrackLine[85:86]):
                    self.race_6	 = outsidetrackLine[85:86]
                if self.chkBlank(outsidetrackLine[86:87]):
                    self.race_7	 = outsidetrackLine[86:87]
                if self.chkBlank(outsidetrackLine[87:88]):
                    self.race_8	 = outsidetrackLine[87:88]
                if self.chkBlank(outsidetrackLine[88:89]):
                    self.race_9	 = outsidetrackLine[88:89]
                if self.chkBlank(outsidetrackLine[89:90]):
                    self.race_10	 = outsidetrackLine[89:90]
                if self.chkBlank(outsidetrackLine[90:91]):
                    self.race_11	 = outsidetrackLine[90:91]
                if self.chkBlank(outsidetrackLine[91:92]):
                    self.race_12	 = outsidetrackLine[91:92]

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
                break
            file.close()

        except FileNotFoundError as e:
            print(e)
        except UnboundLocalError as e:
            print(e)
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)



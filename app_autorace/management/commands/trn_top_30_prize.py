import logging
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

top30prize = 50 # 取得賞金テーブル　繰り返しの数
top30prizeNum = 45

class Top_30_prize():
        

    def init_trn_top_30_prize(self):
        self.classification	 = str()                # ファイル名をキーとして区分を記憶する辞書
        self.data_type	 = str()                    # ファイル名をキーとしてデータ種別を記憶する
        self.send_date	 = str()                    # ファイル名をキーとして送信日を記憶する
        self.totaling_date	 = str()
        self.ranking	 = str()
        self.rider_code	 = int()
        self.rider_full_name = str()
        self.rider_shortened_3_name	 = str()
        self.rider_shortened_4_name = str()
        self.lg_code	 = int()
        self.lg_name = str()
        self.rider_class_code	 = int()
        self.by_period = str()
        self.rider_birthplace	 = str()
        self.rider_age = str()
        self.prize	 = str()

    # 正規表現で半角ブランク削除
    def chkBlank(self, top30prizeLineStr):
        if (not re.sub('\\s', '', top30prizeLineStr)):
            return False
        return True

    # datファイル設定する
    def setDatData(self, top30prizeLine):

        # DB　ファイル登録
        # 必須項目のみ
        #INSERTが実行される
        with transaction.atomic():

            # 選手取得賞金上位３０位
            for s in range(top30prize):

                Trn_Top_30_Prize(Cllasification=self.classification, Data_type=self.data_type, Send_date=self.send_date, Totaling_date=self.totaling_date).save()
                self.init_trn_top_30_prize()
                s = s * top30prizeNum

                if self.chkBlank(top30prizeLine[0:2]):
                    self.ranking = top30prizeLine[0:2]
                if self.chkBlank(top30prizeLine[2:6]):
                    self.rider_code	 = top30prizeLine[2:6]
                if self.chkBlank(top30prizeLine[6:14]):
                    self.rider_full_name	 = top30prizeLine[6:14]
                if self.chkBlank(top30prizeLine[14:17]):
                    self.rider_shortened_3_name	 = top30prizeLine[14:17]
                if self.chkBlank(top30prizeLine[17:21]):
                    self.rider_shortened_4_name	 = top30prizeLine[17:21]
                if self.chkBlank(top30prizeLine[21:22]):
                    self.lg_code	 = top30prizeLine[21:22]
                if self.chkBlank(top30prizeLine[22:25]):
                    self.lg_name	 = top30prizeLine[22:25]
                if self.chkBlank(top30prizeLine[25:26]):
                    self.rider_class_code	 = top30prizeLine[25:26]
                if self.chkBlank(top30prizeLine[26:28]):
                    self.by_period	 = top30prizeLine[26:28]
                if self.chkBlank(top30prizeLine[28:31]):
                    self.rider_birthplace	 = top30prizeLine[28:31]
                if self.chkBlank(top30prizeLine[31:33]):
                    self.rider_age	 = top30prizeLine[31:33]
                if self.chkBlank(top30prizeLine[33:45]):
                    self.prize	 = top30prizeLine[33:45]

                # 空白チェックして実体があるカラムは更新
                self.update_Trn_Top_30_Prize(Trn_Top_30_Prize.objects.get(id=Trn_Top_30_Prize.objects.all().aggregate(Max('id')).get('id__max')))
    

    def update_Trn_Top_30_Prize(self, trn_Update):
        updateFields = list()
        if self.ranking:
            trn_Update.Ranking=self.ranking
            updateFields.append('Ranking')
        if self.rider_code:
            trn_Update.Rider_code=self.rider_code
            updateFields.append('Rider_code')
        if self.rider_full_name:
            trn_Update.Rider_full_name= self.rider_full_name
            updateFields.append('Rider_full_name')
        if self.rider_shortened_3_name:
            trn_Update.Rider_shortened_3_name= self.rider_shortened_3_name
            updateFields.append('Rider_shortened_3_name')
        if self.rider_shortened_4_name:
            trn_Update.Rider_shortened_4_name= self.rider_shortened_4_name
            updateFields.append('Rider_shortened_4_name')
        if self.lg_name:
            trn_Update.LG_name= self.lg_name
            updateFields.append('LG_name')
        if self.by_period:
            trn_Update.By_period= self.by_period
            updateFields.append('By_period')
        if self.rider_birthplace:
            trn_Update.Rider_birthplace= self.rider_birthplace
            updateFields.append('Rider_birthplace')
        if self.rider_age:
            trn_Update.Rider_Age=self.rider_age
            updateFields.append('Rider_Age')
        if self.prize:
            trn_Update.Prize=self.prize
            updateFields.append('Prize')

        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)


    def insert_or_update_Trn_Top_30_Prize(self, name):
        
        try:
            file = open(name,'r',encoding='shift_jis')
            for line in file: # 1行しかない

                self.classification = line[0:1]
                self.data_type = line[1:2]
                self.send_date = line[2:10]
                self.totaling_date = line[10:18]

                top30prizeLine = line[18:]
                
                self.setDatData(top30prizeLine)

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



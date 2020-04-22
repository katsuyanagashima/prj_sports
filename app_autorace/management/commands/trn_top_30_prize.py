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
        

    def update_Trn_Top_30_Prize(self, top30prize_record, top30prizeLine, trn_Top_30_Prize):

        updateFields = list()
        if top30prizeLine[top30prize_record:top30prize_record+2]:
            trn_Top_30_Prize.Ranking=top30prizeLine[top30prize_record:top30prize_record+2]
            updateFields.append('Ranking')
        if top30prizeLine[top30prize_record+2:top30prize_record+6]:
            trn_Top_30_Prize.Rider_code=top30prizeLine[top30prize_record+2:top30prize_record+6]
            updateFields.append('Rider_code')
        if top30prizeLine[top30prize_record+6:top30prize_record+14]:
            trn_Top_30_Prize.Rider_full_name= top30prizeLine[top30prize_record+6:top30prize_record+14]
            updateFields.append('Rider_full_name')
        if top30prizeLine[top30prize_record+14:top30prize_record+17]:
            trn_Top_30_Prize.Rider_shortened_3_name= top30prizeLine[top30prize_record+14:top30prize_record+17]
            updateFields.append('Rider_shortened_3_name')
        if top30prizeLine[top30prize_record+17:top30prize_record+21]:
            trn_Top_30_Prize.Rider_shortened_4_name= top30prizeLine[top30prize_record+17:top30prize_record+21]
            updateFields.append('Rider_shortened_4_name')
        if top30prizeLine[top30prize_record+21:top30prize_record+22]:
            trn_Top_30_Prize.LG_code	 = top30prizeLine[top30prize_record+21:top30prize_record+22]
            updateFields.append('LG_code')
        if top30prizeLine[top30prize_record+22:top30prize_record+25]:
            trn_Top_30_Prize.LG_name= top30prizeLine[top30prize_record+22:top30prize_record+25]
            updateFields.append('LG_name')
        if top30prizeLine[top30prize_record+25:top30prize_record+26]:
            trn_Top_30_Prize.Rider_class_code= top30prizeLine[top30prize_record+25:top30prize_record+26]
            updateFields.append('Rider_class_code')
        if top30prizeLine[top30prize_record+26:top30prize_record+28]:
            trn_Top_30_Prize.By_period= top30prizeLine[top30prize_record+26:top30prize_record+28]
            updateFields.append('By_period')
        if top30prizeLine[top30prize_record+28:top30prize_record+31]:
            trn_Top_30_Prize.Rider_birthplace= top30prizeLine[top30prize_record+28:top30prize_record+31]
            updateFields.append('Rider_birthplace')
        if top30prizeLine[top30prize_record+31:top30prize_record+33]:
            trn_Top_30_Prize.Rider_Age=top30prizeLine[top30prize_record+31:top30prize_record+33]
            updateFields.append('Rider_Age')
        if top30prizeLine[top30prize_record+33:top30prize_record+45]:
            trn_Top_30_Prize.Prize=top30prizeLine[top30prize_record+33:top30prize_record+45]
            updateFields.append('Prize')
      
        # 実体のあるカラム更新
        trn_Top_30_Prize.save(update_fields=updateFields)


    def insert_or_update_Trn_Top_30_Prize(self, fileName):
        
        try:
            file = open(fileName,'r',encoding='shift_jis')
            for line in file: # 1行しかない

                top30prizeLine = line[18:]
                
                # DB　ファイル登録
                # 必須項目のみ
                #INSERTが実行される
                with transaction.atomic():

                    # 選手取得賞金上位３０位
                    for top30prize_record in range(top30prize):

                        logger.info( "内容:insert_Trn_Top_30_Prize Start:")
                        Trn_Top_30_Prize(Cllasification=line[0:1], Data_type=line[1:2], Send_date=line[2:10], Totaling_date=line[10:18]).save()

                        top30prize_record = top30prize_record * top30prizeNum

                        # 空白チェックして実体があるカラムは更新
                        self.update_Trn_Top_30_Prize(top30prize_record, top30prizeLine, Trn_Top_30_Prize.objects.get(id=Trn_Top_30_Prize.objects.all().aggregate(Max('id')).get('id__max')))
            


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



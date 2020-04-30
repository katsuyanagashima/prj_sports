import logging
# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import re
import sys
import time
from logging import getLogger
from pathlib import Path

# ファイル変更イベント検出のため、watchdogをインポート
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers.polling import PollingObserver

from app_autorace.models import *
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.db.models import Max
sys.path.append("/code/app_autorace/")
from consts import *

logger = getLogger('command')

# 監視対象ファイルのパターンマッチを指定する
# スケジュールレコード（mmddhhmmss00000000.dat）

class Schedule():
    # datファイル設定する
    def update_Trn_Schedule(self, scheduleLine):

        # 正規表現で半角ブランク削除
        def chkBlank(scheduleLineStr):
            if (not re.sub('\\s', '', scheduleLineStr)):       
                return False    
            return True

        # 空白チェックして実体があるカラムは更新
        trn_Update = Trn_Schedule.objects.get(id=Trn_Schedule.objects.all().aggregate(Max('id')).get('id__max'))
        # updateFields
        updateFields = list()
        # スケジュール × 1
        if chkBlank(scheduleLine[0:8]):
            trn_Update.Race_date_1=scheduleLine[0:8]
            updateFields.append('Race_date_1')
        if chkBlank(scheduleLine[8:9]):    
            trn_Update.Outside_1=scheduleLine[8:9]
            updateFields.append('Outside_1')
        # 場スケジュール 繰り返し ×6
        if chkBlank(scheduleLine[9:10]):
            trn_Update.Track_code1_1=scheduleLine[9:10]
            updateFields.append('Track_code1_1')
        if chkBlank(scheduleLine[10:12]):
            trn_Update.races_1_1=scheduleLine[10:12]
            updateFields.append('races_1_1')
        if chkBlank(scheduleLine[12:13]):
            trn_Update.Track_code1_2=scheduleLine[12:13]
            updateFields.append('Track_code1_2')
        if chkBlank(scheduleLine[13:15]):
            trn_Update.races_1_2=scheduleLine[13:15]
            updateFields.append('races_1_2')
        if chkBlank(scheduleLine[15:16]):
            trn_Update.Track_code1_3=scheduleLine[15:16]
            updateFields.append('Track_code1_3')
        if chkBlank(scheduleLine[16:18]):
            trn_Update.races_1_3=scheduleLine[16:18]
            updateFields.append('races_1_3')                      
        if chkBlank(scheduleLine[18:19]):
            trn_Update.Track_code1_4=scheduleLine[18:19]
            updateFields.append('Track_code1_4')
        if chkBlank(scheduleLine[19:21]):
            trn_Update.races_1_4=scheduleLine[19:21]
            updateFields.append('races_1_4')
        if chkBlank(scheduleLine[21:22]):                           
            trn_Update.Track_code1_5=scheduleLine[21:22]
            updateFields.append('Track_code1_5')
        if chkBlank(scheduleLine[22:24]):
            trn_Update.races_1_5=scheduleLine[22:24]
            updateFields.append('races_1_5')
        if chkBlank(scheduleLine[24:25]):
            trn_Update.Track_code1_6=scheduleLine[24:25]
            updateFields.append('Track_code1_6')
        if chkBlank(scheduleLine[25:27]):
            trn_Update.races_1_6=scheduleLine[25:27]
            updateFields.append('races_1_6')
        # スケジュール × 2
        if chkBlank(scheduleLine[27:35]):
            trn_Update.Race_date_2=scheduleLine[27:35]
            updateFields.append('Race_date_2')
        if chkBlank(scheduleLine[35:36]):
            trn_Update.Outside_2=scheduleLine[35:36]
            updateFields.append('Outside_2')
        # 場スケジュール 繰り返し ×6
        if chkBlank(scheduleLine[36:37]):
            trn_Update.Track_code2_1=scheduleLine[36:37]
            updateFields.append('Track_code2_1')
        if chkBlank(scheduleLine[37:39]):
            trn_Update.races_2_1=scheduleLine[37:39]
            updateFields.append('races_2_1')
        if chkBlank(scheduleLine[39:40]):  
            trn_Update.Track_code2_2=scheduleLine[39:40]
            updateFields.append('Track_code2_2')
        if chkBlank(scheduleLine[40:42]):
            trn_Update.races_2_2=scheduleLine[40:42]
            updateFields.append('races_2_2')                          
        if chkBlank(scheduleLine[42:43]):
            trn_Update.Track_code2_3=scheduleLine[42:43]
            updateFields.append('Track_code2_3')
        if chkBlank(scheduleLine[43:45]):
            trn_Update.races_2_3=scheduleLine[43:45]
            updateFields.append('races_2_3')
        if chkBlank(scheduleLine[45:46]):
            trn_Update.Track_code2_4=scheduleLine[45:46]
            updateFields.append('Track_code2_4')
        if chkBlank(scheduleLine[46:48]):
            trn_Update.races_2_4=scheduleLine[46:48]
            updateFields.append('races_2_4')
        if chkBlank(scheduleLine[48:49]):
            trn_Update.Track_code2_5=scheduleLine[48:49]
            updateFields.append('Track_code2_5')
        if chkBlank(scheduleLine[49:51]):
            trn_Update.races_2_5=scheduleLine[49:51]
            updateFields.append('races_2_5')
        if chkBlank(scheduleLine[51:52]):
            trn_Update.Track_code2_6=scheduleLine[51:52]
            updateFields.append('Track_code2_6')
        if chkBlank(scheduleLine[52:54]):
            trn_Update.races_2_6=scheduleLine[52:54]
            updateFields.append('races_2_6')
        # スケジュール × 3
        if chkBlank(scheduleLine[54:62]):
            trn_Update.Race_date_3=scheduleLine[54:62]
            updateFields.append('Race_date_3')
        if chkBlank(scheduleLine[62:63]):  
            trn_Update.Outside_3=scheduleLine[62:63]
            updateFields.append('Outside_3')
        # 場スケジュール 繰り返し ×6
        if chkBlank(scheduleLine[63:64]):
            trn_Update.Track_code3_1=scheduleLine[63:64]
            updateFields.append('Track_code3_1')
        if chkBlank(scheduleLine[64:66]):  
            trn_Update.races_3_1=scheduleLine[64:66]
            updateFields.append('races_3_1')
        if chkBlank(scheduleLine[66:67]):
            trn_Update.Track_code3_2=scheduleLine[66:67]
            updateFields.append('Track_code3_2')
        if chkBlank(scheduleLine[67:69]):  
            trn_Update.races_3_2=scheduleLine[67:69]
            updateFields.append('races_3_2')
        if chkBlank(scheduleLine[69:70]):  
            trn_Update.Track_code3_3=scheduleLine[69:70]
            updateFields.append('Track_code3_3')
        if chkBlank(scheduleLine[70:72]):  
            trn_Update.races_3_3=scheduleLine[70:72]
            updateFields.append('races_3_3')
        if chkBlank(scheduleLine[72:73]):  
            trn_Update.Track_code3_4=scheduleLine[72:73]
            updateFields.append('Track_code3_4')
        if chkBlank(scheduleLine[73:75]):  
            trn_Update.races_3_4=scheduleLine[73:75]
            updateFields.append('races_3_4')
        if chkBlank(scheduleLine[75:76]):  
            trn_Update.Track_code3_5=scheduleLine[75:76]
            updateFields.append('Track_code3_5')
        if chkBlank(scheduleLine[76:78]):  
            trn_Update.races_3_5=scheduleLine[76:78]
            updateFields.append('races_3_5')
        if chkBlank(scheduleLine[78:79]):  
            trn_Update.Track_code3_6=scheduleLine[78:79]
            updateFields.append('Track_code3_6')
        if chkBlank(scheduleLine[79:81]):    
            trn_Update.races_3_6=scheduleLine[79:81]
            updateFields.append('races_3_6')
        if chkBlank(scheduleLine[-1]):
            trn_Update.Top_30_prizes=scheduleLine[-1]
            updateFields.append('Top_30_prizes')

        # 実体のあるカラム更新
        trn_Update.save(update_fields=updateFields)   

    def insert_Trn_Schedule(self, line):
        classification = line[0:1]
        data_type = line[1:2]
        send_date = line[2:10]
        Trn_Schedule(Cllasification=classification, Data_type=data_type, Send_date=send_date).save() 
        
    def insert_or_update_Trn_Schedule(self, fileName):
        try:
            file = open(fileName, 'r', encoding='shift_jis')
            for line in file: # 1行しかない
                # DB　ファイル登録
                with transaction.atomic():
                    #必須項目のみ INSERTが実行される
                    logger.info( "内容:insert_Trn_Schedule Start:" + "詳細:ファイルデータ:" + line[0:10])
                    self.insert_Trn_Schedule(line[0:10])
                    logger.info( "内容:insert_Trn_Schedule End")

                    logger.info( "内容:update_Trn_Schedule Start:" + "詳細:ファイルデータ:" + line[10:])
                    self.update_Trn_Schedule(line[10:])
                    logger.info( "内容:update_Trn_Schedule End")
                          
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

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
from app_autorace.commons import Common

logger = getLogger('app_autorace')

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
            # モデル読み込みがここでしか読み込みできない
            from app_autorace.models import Trn_Top_30_Prize
            cmn = Common()

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

                    # 選手取得賞金上位３０位
                    for top30prize_record in range(top30prize):
                        top30prize_record = top30prize_record * top30prizeNum
                        top30prizeLine = line[18:]
                        chkline = top30prizeLine[top30prize_record:]
                        # insert チェックする。データがからのときはスキップ
                        logger.info(f'データチェック{chkline}')
                        if not cmn.chkBlank(chkline):
                            logger.info( "データチェックがからのため End")
                            break

                        logger.info( "内容:Trn_Top_30_Prize Start:")
                        Trn_Top_30_Prize(Cllasification=line[0:1], Data_type=line[1:2], Send_date=line[2:10], Totaling_date=line[10:18]).save()
                        logger.info( "内容:Trn_Top_30_Prize End")

                        # 空白チェックして実体があるカラムは更新
                        logger.info( "内容:update_Trn_Top_30_Prize Start:")
                        self.update_Trn_Top_30_Prize(top30prize_record, top30prizeLine, Trn_Top_30_Prize.objects.get(id=Trn_Top_30_Prize.objects.all().aggregate(Max('id')).get('id__max')))
                        logger.info( "内容:update_Trn_Top_30_Prize End")

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


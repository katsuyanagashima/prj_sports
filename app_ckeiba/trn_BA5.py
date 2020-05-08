import csv
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

from app_ckeiba.consts import *

logger = getLogger('app_ckeiba')

class Ba5():

    def chk_master(self, line, Mst_Jou):

        if not Mst_Jou.objects.filter(Jou_code=line[2]):
            logger.info(f'競馬場マスタ にJou_code :{line[2]} ないので登録します。')
            jou = Mst_Jou(Jou_code=line[2],Jou_name=JOU_NAME,Jou_seisekiA=JOU_SEISEKIA,Jou_3char=JOU_3CHAR,Jou_banei=JOU_BANEI)
            jou.save()
            logger.warning(f'競馬場マスタ にJou_code {line[2]}：Jou_name {JOU_NAME}:Jou_seisekiA {JOU_SEISEKIA}:Jou_3char {JOU_3CHAR}:Jou_banei :{JOU_BANEI}を登録しました。')

    #入場人員_BA5
    def CSV_Trn_Visitors_BA5(self, fileName, Trn_Visitors_BA5, Mst_Jou):

        with open(fileName, encoding='shift_jis') as f:

            reader = csv.reader(f, delimiter=',')

            # bulk createを使った場合
            '''
            Trn_Visitors_BA5.objects.bulk_create([Trn_Visitors_BA5(
                共通　カラム設定
            ) for line in reader])
            '''

            # forを使った場合
            for line in reader:

                # マスターチェック
                logger.info(f'マスターチェック: {Mst_Jou} ')
                self.chk_master(line, Mst_Jou)

                trn_visitors_ba5 = Trn_Visitors_BA5(
                    Data_ID = line[0],
                    Race_date = line[1],
                    Track_code = Mst_Jou.objects.get(Jou_code=line[2]),
                    Held_times = line[3],
                    Paid_visitors = line[4],
                    Free_visitors = line[5],
                )
                trn_visitors_ba5.save()

    def insert_or_update_Trn_Visitors_BA5(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_ckeiba.models import Trn_Visitors_BA5, Mst_Jou

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            logger.info( '内容:insert_Trn_Visitors_BA5 Start')
            self.CSV_Trn_Visitors_BA5(fileName, Trn_Visitors_BA5, Mst_Jou)
            logger.info( "内容:insert_Trn_Visitors_BA5 End")

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

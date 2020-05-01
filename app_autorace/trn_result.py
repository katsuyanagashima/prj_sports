import datetime
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

# 監視対象ファイルのパターンマッチを指定する
# レース結果データレコード（mmddhhmmss0000JRR2.dat）

trn_rider_result_list = 8

class Result():

    def update_trn_rider_results(self,rider_results, trn_rider_results_line, trn_result):

        count = rider_results * 69
        updateFields = list()

        # 実体のあるカラム更新
        if trn_rider_results_line[count:count+1]:
            trn_result.Bracket_No=trn_rider_results_line[count:count+1]
            updateFields.append('Bracket_No')
        if trn_rider_results_line[count+1:count+2]:
            trn_result.Rider_No=trn_rider_results_line[count+1:count+2]
            updateFields.append('Rider_No')
        if trn_rider_results_line[count+2:count+6]:
            trn_result.Rider_code=trn_rider_results_line[count+2:count+6]
            updateFields.append('Rider_code')
        if trn_rider_results_line[count+6:count+14]:
            trn_result.Rider_full_name=trn_rider_results_line[count+6:count+14]
            updateFields.append('Rider_full_name')
        if trn_rider_results_line[count+14:count+17]:
            trn_result.Rider_shortened_3_name=trn_rider_results_line[count+14:count+17]
            updateFields.append('Rider_shortened_3_name')
        if trn_rider_results_line[count+17:count+21]:
            trn_result.Rider_shortened_4_name=trn_rider_results_line[count+17:count+21]
            updateFields.append('Rider_shortened_4_name')
        if trn_rider_results_line[count+21:count+24]:
            trn_result.LG_name=trn_rider_results_line[count+21:count+24]
            updateFields.append('LG_name')
        if trn_rider_results_line[count+24:count+25]:
            trn_result.LG_code=trn_rider_results_line[count+24:count+25]
            updateFields.append('LG_code')
        if trn_rider_results_line[count+25:count+37]:
            trn_result.Nickname=trn_rider_results_line[count+25:count+37]
            updateFields.append('Nickname')
        if trn_rider_results_line[count+37:count+40]:
            trn_result.Rider_birthplace=trn_rider_results_line[count+37:count+40]
            updateFields.append('Rider_birthplace')
        if trn_rider_results_line[count+40:count+42]:
            trn_result.Rider_Age=trn_rider_results_line[count+40:count+42]
            updateFields.append('Rider_Age')
        if trn_rider_results_line[count+42:count+44]:
            trn_result.By_period=trn_rider_results_line[count+42:count+44]
            updateFields.append('By_period')
        if trn_rider_results_line[count+44:count+47]:
            trn_result.Handicap=trn_rider_results_line[count+44:count+47]
            updateFields.append('Handicap')
        if trn_rider_results_line[count+47:count+48]:
            trn_result.Result=trn_rider_results_line[count+47:count+48]
            updateFields.append('Result')
        if trn_rider_results_line[count+48:count+50]:
            trn_result.Accident_code=trn_rider_results_line[count+48:count+50]
            updateFields.append('Accident_code')
        if trn_rider_results_line[count+50:count+53]:
            trn_result.Accident_name=trn_rider_results_line[count+50:count+53]
            updateFields.append('Accident_name')
        if trn_rider_results_line[count+53:count+54]:
            trn_result.Illegal_start_code=trn_rider_results_line[count+53:count+54]
            updateFields.append('Illegal_start_code')
        if trn_rider_results_line[count+54:count+55]:
            trn_result.Disturbed_code=trn_rider_results_line[count+54:count+55]
            updateFields.append('Disturbed_code')
        if trn_rider_results_line[count+55:count+59]:
            trn_result.Test_run_time=trn_rider_results_line[count+55:count+59]
            updateFields.append('Test_run_time')
        if trn_rider_results_line[count+59:count+63]:
            trn_result.Race_time=trn_rider_results_line[count+59:count+63]
            updateFields.append('Race_time')
        if trn_rider_results_line[count+63:count+67]:
            trn_result.Minute_second=trn_rider_results_line[count+63:count+67]
            updateFields.append('Minute_second')
        if trn_rider_results_line[count+67:count+69]:
            trn_result.Start_timing=trn_rider_results_line[count+67:count+69]
            updateFields.append('Start_timing')

        trn_result.save(update_fields=updateFields)

    def update_trn_results(self, line, trn_result):
        # 実体のあるカラム更新
        updateFields = list()

        # 日本語２バイト
        if line[14:25]:
            trn_result.Date_Japanese_calendar=line[14:25]
            updateFields.append('Date_Japanese_calendar')

        # 日本語２バイト
        if line[25:39]:
            trn_result.Held_day=line[25:39]
            updateFields.append('Held_day')
        if line[39:43]:
        # 日本語２バイト
            trn_result.Period_days=line[39:43]
            updateFields.append('Period_days')
        if line[43:63]:
            trn_result.Event_name=line[43:63]
            updateFields.append('Event_name')
        if line[71:72]:
            trn_result.Commemorative_code=line[71:72]
            updateFields.append('Commemorative_code')
        if line[72:74]:
            trn_result.Special_commemorative_code=line[72:74]
            updateFields.append('Special_commemorative_code')
        if line[74:88]:
            trn_result.Net_sales_day=line[74:88]
            updateFields.append('Net_sales_day')
        if line[88:102]:
            trn_result.Net_sales_period=line[88:102]
            updateFields.append('Net_sales_period')
        if line[102:116]:
            trn_result.Net_sales_held=line[102:116]
            updateFields.append('Net_sales_held')
        if line[116:123]:
            trn_result.visitors_day=line[116:123]
            updateFields.append('visitors_day')
        if line[123:130]:
            trn_result.visitors_period=line[123:130]
            updateFields.append('visitors_period')
        if line[130:137]:
            trn_result.visitors_held=line[130:137]
            updateFields.append('visitors_held')
        # 日本語２バイト
        if line[139:152]:
            trn_result.Race_name=line[139:152]
            updateFields.append('Race_name')
        if line[156:157]:
            trn_result.Participant_No=line[156:157]
            updateFields.append('Participant_No')
        if line[157:158]:
            trn_result.Race_Approved=line[157:158]
            updateFields.append('Race_Approved')
        if line[158:159]:
            trn_result.Race_postponed=line[158:159]
            updateFields.append('Race_postponed')
        if line[159:160]:
            trn_result.Handicap_Open=line[159:160]
            updateFields.append('Handicap_Open')
        if line[160:173]:
            trn_result.Race_Sales=line[160:173]
            updateFields.append('Race_Sales')
        if line[173:186]:
            trn_result.Race_Pay_back=line[173:186]
            updateFields.append('Race_Pay_back')
        if line[186:194]:
            trn_result.Win_prize=line[186:194]
            updateFields.append('Win_prize')
        if line[194:196]:
            trn_result.Voting_code=line[194:196]
            updateFields.append('Voting_code')

        # Trn_Result
        if line[748:751]:
            trn_result.Exacta_No_1=line[748:751]
            updateFields.append('Exacta_No_1')
        if line[751:758] :
            trn_result.Exacta_1=line[751:758]
            updateFields.append('Exacta_1')
        if line[758:760] :
            trn_result.Exacta_pick_1=line[758:760]
            updateFields.append('Exacta_pick_1')
        if line[760:763] :
            trn_result.Exacta_No_2=line[760:763]
            updateFields.append('Exacta_No_2')
        if line[763:770] :
            trn_result.Exacta_2=line[763:770]
            updateFields.append('Exacta_2')
        if line[770:772] :
            trn_result.Exacta_pick_2=line[770:772]
            updateFields.append('Exacta_pick_2')
        if line[772:775] :
            trn_result.Quinella_No_1=line[772:775]
            updateFields.append('Quinella_No_1')
        if line[775:782] :
            trn_result.Quinella_1=line[775:782]
            updateFields.append('Quinella_1')
        if line[782:784] :
            trn_result.Quinella_pick_1=line[782:784]
            updateFields.append('Quinella_pick_1')
        if line[784:787] :
            trn_result.Quinella_No_2=line[784:787]
            updateFields.append('Quinella_No_2')
        if line[787:794] :
            trn_result.Quinella_2=line[787:794]
            updateFields.append('Quinella_2')
        if line[794:796] :
            trn_result.Quinella_pick_2=line[794:796]
            updateFields.append('Quinella_pick_2')

        if line[798:799] :
            trn_result.Trifecta_approved=line[798:799]
            updateFields.append('Trifecta_approved')
        # 組番 繰り返す× 4
        if line[799:804] :
            trn_result.Trifecta_No_1=line[799:804]
            updateFields.append('Trifecta_No_1')
        if line[804:809] :
            trn_result.Trifecta_No_2=line[804:809]
            updateFields.append('Trifecta_No_2')

        if line[809:814] :
            trn_result.Trifecta_No_3=line[809:814]
            updateFields.append('Trifecta_No_3')
        if line[814:819] :
            trn_result.Trifecta_No_4=line[814:819]
            updateFields.append('Trifecta_No_4')
        # 払戻金
        if line[819:826] :
            trn_result.Trifecta_1=line[819:826]
            updateFields.append('Trifecta_1')
        if line[826:833] :
            trn_result.Trifecta_2=line[826:833]
            updateFields.append('Trifecta_2')
        if line[833:840] :
            trn_result.Trifecta_3=line[833:840]
            updateFields.append('Trifecta_3')
        if line[840:847] :
            trn_result.Trifecta_4=line[840:847]
            updateFields.append('Trifecta_4')
        # 人気
        if line[847:850] :
            trn_result.Trifecta_pick_1=line[847:850]
            updateFields.append('Trifecta_pick_1')
        if line[850:853] :
            trn_result.Trifecta_pick_2=line[850:853]
            updateFields.append('Trifecta_pick_2')
        if line[853:856] :
            trn_result.Trifecta_pick_3=line[853:856]
            updateFields.append('Trifecta_pick_3')
        if line[856:859]:
            trn_result.Trifecta_pick_4=line[856:859]
            updateFields.append('Trifecta_pick_4')
        if line[859:860]:
            trn_result.Betting_type_4=line[859:860]
            updateFields.append('Betting_type_4')
        if line[860:861]:
            trn_result.Wide_On_sale=line[860:861]
            updateFields.append('Wide_On_sale')
        # 不成立
        if line[861:862]:
            trn_result.Wide_approved_1=line[861:862]
            updateFields.append('Wide_approved_1')
        if line[862:863]:
            trn_result.Wide_approved_2=line[862:863]
            updateFields.append('Wide_approved_2')
        if line[863:864]:
            trn_result.Wide_approved_3=line[863:864]
            updateFields.append('Wide_approved_3')
        # 組番
        if line[864:867]:
            trn_result.Wide_No_1=line[864:867]
            updateFields.append('Wide_No_1')
        if line[867:870]:
            trn_result.Wide_No_2=line[867:870]
            updateFields.append('Wide_No_2')
        if line[870:873]:
            trn_result.Wide_No_3=line[870:873]
            updateFields.append('Wide_No_3')
        if line[873:876]:
            trn_result.Wide_No_4=line[873:876]
            updateFields.append('Wide_No_4')
        if line[876:879]:
            trn_result.Wide_No_5=line[876:879]
            updateFields.append('Wide_No_5')
        # 払戻金
        if line[879:886]:
            trn_result.Wide_1=line[879:886]
            updateFields.append('Wide_1')
        if line[886:893]:
            trn_result.Wide_2=line[886:893]
            updateFields.append('Wide_2')
        if line[893:900]:
            trn_result.Wide_3=line[893:900]
            updateFields.append('Wide_3')
        if line[900:907]:
            trn_result.Wide_4=line[900:907]
            updateFields.append('Wide_4')
        if line[907:914]:
            trn_result.Wide_5=line[907:914]
            updateFields.append('Wide_5')
        # 人気
        if line[914:917]:
            trn_result.Wide_pick_1=line[914:917]
            updateFields.append('Wide_pick_1')
        if line[917:920]:
            trn_result.Wide_pick_2=line[917:920]
            updateFields.append('Wide_pick_2')
        if line[920:923]:
            trn_result.Wide_pick_3=line[920:923]
            updateFields.append('Wide_pick_3')
        if line[923:926]:
            trn_result.Wide_pick_4=line[923:926]
            updateFields.append('Wide_pick_4')
        if line[926:929]:
            trn_result.Wide_pick_5=line[926:929]
            updateFields.append('Wide_pick_5')
        if line[931:932] :
            trn_result.Trio_approved=line[931:932]
            updateFields.append('Trio_approved')
        # 組番
        if line[932:937]:
            trn_result.Trio_No_1=line[932:937]
            updateFields.append('Trio_No_1')
        if line[937:942]:
            trn_result.Trio_No_2=line[937:942]
            updateFields.append('Trio_No_2')
        if line[942:947]:
            trn_result.Trio_No_3=line[942:947]
            updateFields.append('Trio_No_3')
        if line[947:952]:
            trn_result.Trio_No_4=line[947:952]
            updateFields.append('Trio_No_4')
        # 払戻金
        if line[952:959]:
            trn_result.Trio_1=line[952:959]
            updateFields.append('Trio_1')
        if line[959:966]:
            trn_result.Trio_2=line[959:966]
            updateFields.append('Trio_2')
        if line[966:973]:
            trn_result.Trio_3=line[966:973]
            updateFields.append('Trio_3')
        if line[973:980]:
            trn_result.Trio_4=line[973:980]
            updateFields.append('Trio_4')
        # 人気
        if line[980:983]:
            trn_result.Trio_pick_1=line[980:983]
            updateFields.append('Trio_pick_1')
        if line[983:986]:
            trn_result.Trio_pick_2=line[983:986]
            updateFields.append('Trio_pick_2')
        if line[986:989]:
            trn_result.Trio_pick_3=line[986:989]
            updateFields.append('Trio_pick_3')
        if line[989:992]:
            trn_result.Trio_pick_4=line[989:992]
            updateFields.append('Trio_pick_4')
        # 返還情報
        if line[992:995]:
            trn_result.Put_out_rider_1=line[992:995]
            updateFields.append('Put_out_rider_1')
        if line[995:996]:
            trn_result.Put_out_Reason_1=line[995:996]
            updateFields.append('Put_out_Reason_1')
        if line[996:999]:
            trn_result.Put_out_rider_2=line[996:999]
            updateFields.append('Put_out_rider_2')
        if line[999:1000]:
            trn_result.Put_out_Reason_2=line[999:1000]
            updateFields.append('Put_out_Reason_2')
        if line[1000:1003]:
            trn_result.Put_out_rider_3=line[1000:1003]
            updateFields.append('Put_out_rider_3')
        if line[1003:1004]:
            trn_result.Put_out_Reason_3=line[1003:1004]
            updateFields.append('Put_out_Reason_3')
        if line[1004:1007]:
            trn_result.Put_out_rider_4=line[1004:1007]
            updateFields.append('Put_out_rider_4')
        if line[1007:1008]:
            trn_result.Put_out_Reason_4=line[1007:1008]
            updateFields.append('Put_out_Reason_4')
        if line[1008:1011]:
            trn_result.Put_out_rider_5=line[1008:1011]
            updateFields.append('Put_out_rider_5')
        if line[1011:1012]:
            trn_result.Put_out_Reason_5=line[1011:1012]
            updateFields.append('Put_out_Reason_5')
        if line[1012:1013]:
            trn_result.Runway_status_code=line[1012:1013]
            updateFields.append('Runway_status_code')
        if line[1013:1014]:
            trn_result.Track_conditions=line[1013:1014]
            updateFields.append('Track_conditions')
        if line[1014:1807]:
            trn_result.Reserve=line[1014:1807]
            updateFields.append('Reserve')
        trn_result.save(update_fields=updateFields)

    def insert_Trn_Trn_Result(self, line, Trn_Result):
        # shift_jis 日本語は２バイト
        # Trn_Result
        Trn_Result(Classification=line[0:1], Data_type=line[1:2], Track_code=line[2:3], Track_name=line[3:6] \
        , Date_AD=line[6:14], First_day_of_the_event=line[63:71], Race_No=line[137:139], Race_distance=line[152:156] \
        , Betting_type_3=line[796:797] , Trifecta_On_sale=line[797:798] , Betting_type_5=line[929:930] , Trio_On_sale=line[930:931] ).save()

    # 選手成績テーブル 繰り返し×8
    def insert_or_update_trn_rider_results(self, trn_rider_results_line, Trn_Rider_results):

        for rider_results in range(trn_rider_result_list):

            Trn_Rider_results(Track_code=trn_rider_results_line[2:3], Date_AD = trn_rider_results_line[6:14], Race_No=trn_rider_results_line[137:139]).save()

            # 空白チェックして実体があるカラムは更新
            self.update_trn_rider_results(rider_results, trn_rider_results_line[196:748], Trn_Rider_results.objects.get(id=Trn_Rider_results.objects.all().aggregate(Max('id')).get('id__max')))

    def insert_or_update_Trn_Result(self, fileName):
        try:
            # モデル読み込みがここでしか読み込みできない
            from app_autorace.models import Trn_Result, Trn_Rider_results
            cmn = Common()

            # ファイル読み込み　データセット
            logger.info('文字コード確認')
            with open(fileName, 'rb') as f:
                logger.info(chardet.detect(f.read()))

            # ファイル読み込み　データセット
            file = open(fileName, 'r', encoding='shift_jis')
            for line in file:
                # ファイル文字サイズ
                logger.info(f'{fileName}はファイルサイズ {len(line)}')

                # DB　ファイル登録
                with transaction.atomic():
                    # レース結果データレコード
                    #必須項目のみ INSERTが実行される
                    logger.info( f'内容:insert_Trn_Trn_Result Start:詳細:ファイルデータ: {line}')
                    self.insert_Trn_Trn_Result(line, Trn_Result)
                    logger.info( "内容:insert_Trn_Trn_Result End")

                    # 空白チェックして実体があるカラムは更新
                    self.update_trn_results(line, Trn_Result.objects.get(id=Trn_Result.objects.all().aggregate(Max('id')).get('id__max')))

                    # insert チェックする。データがからのときはスキップ
                    chkline = line[196:748]
                    logger.info(f'データチェック{chkline}')
                    if not cmn.chkBlank(chkline):
                        logger.info( "データチェックがからのため End")
                        break

                    # 選手成績テーブル
                    logger.info( f'内容:insert_or_update_trn_rider_results Start:詳細:ファイルデータ:  {line[196:748]}')
                    self.insert_or_update_trn_rider_results(line, Trn_Rider_results)
                    logger.info( "内容:insert_or_update_trn_rider_results End")

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

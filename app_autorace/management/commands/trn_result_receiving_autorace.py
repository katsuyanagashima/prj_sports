import logging
import datetime
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
# レース結果データレコード（mmddhhmmss0000JRR2.dat）
resultID = 3
resultData = "resultData"
go_recursively = False
# target_file_result_record = '*0000[1-6]0[1-9]|1[0-2]2.dat'
target_file_result_record = ['*0000[1-6]0[1-9]2.dat','*0000[1-6]1[0-2]2.dat']
trn_rider_result_list = 8

# RegexMatchingEventHandler の継承クラスを作成
class FileChangeHandler(PatternMatchingEventHandler):
    # クラス初期化
    def __init__(self, patterns):
        super(FileChangeHandler, self).__init__(patterns=patterns)

    def init_trn_result(self):
        # Trn_Result レース結果データレコード
        self.classification	=	str()
        self.data_type	=	str() 
        self.track_code	=	str() 
        self.track_name	=	str() 
        self.date_ad	=	str()
        self.date_japanese_calendar	=	str() 
        self.held_day	=	str() 
        self.period_days	=	str() 
        self.event_name	=	str() 
        self.first_day_of_the_event	=	str() 
        self.commemorative_code	=	str() 
        self.special_commemorative_code	=	str() 
        self.net_sales_day	=	str() 
        self.net_sales_period	=	str() 
        self.net_sales_held	=	str() 
        self.visitors_day	=	str() 
        self.visitors_period	=	str() 
        self.visitors_held	=	str() 
        self.race_no	=	str() 
        self.race_name	=	str() 
        self.race_distance	=	str() 
        self.participant_no	=	str() 
        self.race_approved	=	str() 
        self.race_postponed	=	str() 
        self.handicap_open	=	str() 
        self.race_sales	=	str() 
        self.race_pay_back	=	str() 
        self.win_prize	=	str() 
        self.voting_code	=	str() 
        self.exacta_no_1	=	str() 
        self.exacta_1	=	str() 
        self.exacta_pick_1	=	str() 
        self.exacta_no_2	=	str() 
        self.exacta_2	=	str() 
        self.exacta_pick_2	=	str() 
        self.quinella_no_1	=	str() 
        self.quinella_1	=	str() 
        self.quinella_pick_1	=	str() 
        self.quinella_no_2	=	str() 
        self.quinella_2	=	str() 
        self.quinella_pick_2	=	str() 
        self.betting_type_3	=	str() 
        self.trifecta_on_sale	=	str() 
        self.trifecta_approved	=	str() 
        self.trifecta_no_1	=	str() 
        self.trifecta_no_2	=	str() 
        self.trifecta_no_3	=	str()
        self.trifecta_no_4	=	str()
        self.trifecta_1	=	str() 
        self.trifecta_2	=	str() 
        self.trifecta_3	=	str()
        self.trifecta_4	=	str()
        self.trifecta_pick_1	=	str() 
        self.trifecta_pick_2	=	str() 
        self.trifecta_pick_3	=	str() 
        self.trifecta_pick_4	=	str()
        self.betting_type_4	=	str() 
        self.wide_on_sale	=	str() 
        self.wide_approved_1	=	str() 
        self.wide_approved_2	=	str() 
        self.wide_approved_3	=	str() 
        self.wide_no_1	=	str() 
        self.wide_no_2	=	str() 
        self.wide_no_3	=	str() 
        self.wide_no_4	=	str() 
        self.wide_no_5	=	str() 
        self.wide_1	=	str() 
        self.wide_2	=	str() 
        self.wide_3	=	str() 
        self.wide_4	=	str() 
        self.wide_5	=	str() 
        self.wide_pick_1	=	str() 
        self.wide_pick_2	=	str() 
        self.wide_pick_3	=	str() 
        self.wide_pick_4	=	str() 
        self.wide_pick_5	=	str() 
        self.betting_type_5	=	str() 
        self.trio_on_sale	=	str() 
        self.trio_approved	=	str() 
        self.trio_no_1	=	str() 
        self.trio_no_2	=	str() 
        self.trio_no_3	=	str() 
        self.trio_no_4	=	str() 
        self.trio_1	=	str() 
        self.trio_2	=	str() 
        self.trio_3	=	str() 
        self.trio_4	=	str() 
        self.trio_pick_1	=	str() 
        self.trio_4	=	str() 
        self.trio_pick_2	=	str() 
        self.trio_pick_3	=	str() 
        self.trio_pick_4	=	str() 
        self.put_out_rider_1	=	str() 
        self.put_out_reason_1	=	str() 
        self.put_out_rider_2	=	str() 
        self.put_out_reason_2	=	str() 
        self.put_out_rider_3	=	str() 
        self.put_out_reason_3	=	str() 
        self.put_out_rider_4	=	str() 
        self.put_out_reason_4	=	str() 
        self.put_out_rider_5	=	str() 
        self.put_out_reason_5	=	str() 
        self.runway_status_code	=	str() 
        self.track_conditions	=	str() 
        self.reserve =	str() 

        self.trn_rider_results_line = str()

             
    # Trn_Running_list 選手成績テーブル
    def init_trn_running_data(self):

        self.bracket_no	=	str()
        self.rider_no	=	str()
        self.rider_code	=	str()
        self.rider_full_name	=	str()
        self.rider_shortened_3_name	=	str()
        self.rider_shortened_4_name	=	str()
        self.lg_name	=	str()
        self.lg_code	=	str()
        self.nickname	=	str()
        self.rider_birthplace	=	str()
        self.rider_age	=	str()
        self.by_period	=	str()
        self.handicap	=	str()
        self.result	=	str()
        self.accident_code	=	str()
        self.accident_name	=	str()
        self.illegal_start_code	=	str()
        self.disturbed_code	=	str()
        self.test_run_time	=	str()
        self.race_time	=	str()
        self.minute_second	=	str()
        self.start_timing	=	str()


    # 正規表現で半角ブランク削除
    def chkBlank(self, lineStr):
        if (not re.sub('\\s|\\S', '', lineStr)):       
            return False    
        return True

    def update_trn_rider_results(self, trn_result):
        # 実体のあるカラム更新
        updateFields = list()
        if self.bracket_no:
            trn_result.Bracket_No=self.bracket_no
            updateFields.append('Bracket_No')
        if self.rider_no:
            trn_result.Rider_No=self.rider_no
            updateFields.append('Rider_No')            
        if self.rider_code:
            trn_result.Rider_code=self.rider_code
            updateFields.append('Rider_code')      
        if self.rider_full_name:
            trn_result.Rider_full_name=self.rider_full_name
            updateFields.append('Rider_full_name')      
        if self.rider_shortened_3_name:
            trn_result.Rider_shortened_3_name=self.rider_shortened_3_name
            updateFields.append('Rider_shortened_3_name')      
        if self.rider_shortened_4_name:
            trn_result.Rider_shortened_4_name=self.rider_shortened_4_name
            updateFields.append('Rider_shortened_4_name')      
        if self.lg_name:
            trn_result.LG_name=self.lg_name
            updateFields.append('LG_name')      
        if self.lg_code:
            trn_result.LG_code=self.lg_code
            updateFields.append('LG_code')      
        if self.nickname:
            trn_result.Nickname=self.nickname
            updateFields.append('Nickname')      
        if self.rider_birthplace:
            trn_result.Rider_birthplace=self.rider_birthplace
            updateFields.append('Rider_birthplace')      
        if self.rider_age:
            trn_result.Rider_Age=self.rider_age
            updateFields.append('Rider_Age')      
        if self.by_period:
            trn_result.By_period=self.by_period
            updateFields.append('By_period')      
        if self.handicap:
            trn_result.Handicap=self.handicap
            updateFields.append('Handicap')      
        if self.result:
            trn_result.Result=self.result
            updateFields.append('Result')      
        if self.accident_code:
            trn_result.Accident_code=self.accident_code
            updateFields.append('Accident_code')      
        if self.accident_name:
            trn_result.Accident_name=self.accident_name
            updateFields.append('Accident_name')      
        if self.illegal_start_code:
            trn_result.Illegal_start_code=self.illegal_start_code
            updateFields.append('Illegal_start_code')      
        if self.disturbed_code:
            trn_result.Disturbed_code=self.disturbed_code
            updateFields.append('Disturbed_code')      
        if self.test_run_time:
            trn_result.Test_run_time=self.test_run_time
            updateFields.append('Test_run_time')      
        if self.race_time:
            trn_result.Race_time=self.race_time
            updateFields.append('Race_time')      
        if self.minute_second:
            trn_result.Minute_second=self.minute_second
            updateFields.append('Minute_second')      
        if self.start_timing:
            trn_result.Start_timing=self.start_timing
            updateFields.append('Start_timing')      

        trn_result.save(update_fields=updateFields)

    def setDatData_rider_results(self, count, trn_rider_results_line):

        count = count * 69

        self.bracket_no	=	trn_rider_results_line[count:count+1]
        self.rider_no	=	trn_rider_results_line[count+1:count+2]
        self.rider_code	=	trn_rider_results_line[count+2:count+6]
        self.rider_full_name	=	trn_rider_results_line[count+6:count+14]
        self.rider_shortened_3_name	=	trn_rider_results_line[count+14:count+17]
        self.rider_shortened_4_name	=	trn_rider_results_line[count+17:count+21]
        self.lg_name	=	trn_rider_results_line[count+21:count+24]
        self.lg_code	=	trn_rider_results_line[count+24:count+25]
        self.nickname	=	trn_rider_results_line[count+25:count+37]
        self.rider_birthplace	=	trn_rider_results_line[count+37:count+40]
        self.rider_age	=	trn_rider_results_line[count+40:count+42]
        self.by_period	=	trn_rider_results_line[count+42:count+44]
        self.handicap	=	trn_rider_results_line[count+44:count+47]
        self.result	=	trn_rider_results_line[count+47:count+48]
        self.accident_code	=	trn_rider_results_line[count+48:count+50]
        self.accident_name	=	trn_rider_results_line[count+50:count+53]
        self.illegal_start_code	=	trn_rider_results_line[count+53:count+54]
        self.disturbed_code	=	trn_rider_results_line[count+54:count+55]
        self.test_run_time	=	trn_rider_results_line[count+55:count+59]
        self.race_time	=	trn_rider_results_line[count+59:count+63]
        self.minute_second	=	trn_rider_results_line[count+63:count+67]
        self.start_timing	=	trn_rider_results_line[count+67:count+69]   

    # 選手成績テーブル 繰り返し×8
    def insert_or_update_trn_rider_results(self, trn_rider_results_line):
        
        for rider_results in range(trn_rider_result_list):
            
            self.init_trn_running_data()

            self.setDatData_rider_results(rider_results, trn_rider_results_line)

            Trn_Rider_results(Track_code=self.track_code, Date_AD = self.date_ad, Race_No=self.race_No).save()

            # 空白チェックして実体があるカラムは更新
            self.update_trn_rider_results(Trn_Rider_results.objects.get(id=Trn_Rider_results.objects.all().aggregate(Max('id')).get('id__max')))

    # datファイル設定する
    def setDatData(self, line):
        
        # shift_jis 日本語は２バイト
        # Trn_Result
        self.classification = line[0:1]
        self.data_type = line[1:2]
        self.track_code = line[2:3]
        # 日本語２バイト
        self.track_name = line[3:6]
        self.date_ad = line[6:14]
        # 日本語２バイト
        self.date_Japanese_calendar = line[14:25]
        # 日本語２バイト
        self.held_day = line[25:39]
        self.period_days = line[39:43]
        # 日本語２バイト
        self.event_name = line[43:63]
        self.first_day_of_the_event = line[63:71]
        self.commemorative_code = line[71:72]
        self.special_commemorative_code = line[72:74]
        self.net_sales_day = line[74:88]
        self.net_sales_period = line[88:102]
        self.net_sales_held = line[102:116]
        self.visitors_day = line[116:123]
        self.visitors_period = line[123:130]
        self.visitors_held = line[130:137]
        self.race_No = line[137:139]
        # 日本語２バイト
        self.race_name = line[139:152]
        self.race_distance = line[152:156]
        self.participant_No = line[156:157]
        self.race_Approved = line[157:158]
        self.race_postponed = line[158:159]
        self.handicap_Open = line[159:160]
        self.race_Sales = line[160:173]
        self.race_Pay_back = line[173:186]
        self.win_prize = line[186:194]
        self.voting_code = line[194:196]

        # 選手成績テーブル  ×8
        self.trn_rider_results_line = line[196:748]

        # Trn_Result
        self.exacta_no_1	=	line[748:751]
        self.exacta_1	=	line[751:758] 
        self.exacta_pick_1	=	line[758:760] 
        self.exacta_no_2	=	line[760:763] 
        self.exacta_2	=	line[763:770] 
        self.exacta_pick_2	=	line[770:772] 
        self.quinella_no_1	=	line[772:775] 
        self.quinella_1	=	line[775:782] 
        self.quinella_pick_1	=	line[782:784] 
        self.quinella_no_2	=	line[784:787] 
        self.quinella_2	=	line[787:794] 
        self.quinella_pick_2	=	line[794:796] 
        self.betting_type_3	=	line[796:797] 
        self.trifecta_on_sale	=	line[797:798] 
        self.trifecta_approved	=	line[798:799] 
        # 組番 繰り返す× 4
        self.trifecta_no_1	=	line[799:804] 
        self.trifecta_no_2	=	line[804:809] 
        self.trifecta_no_3	=	line[809:814] 
        self.trifecta_no_4	=	line[814:819] 
        # 払戻金
        self.trifecta_1	=	line[819:826] 
        self.trifecta_2	=	line[826:833] 
        self.trifecta_3	=	line[833:840] 
        self.trifecta_4	=	line[840:847] 
        # 人気
        self.trifecta_pick_1	=	line[847:850] 
        self.trifecta_pick_2	=	line[850:853] 
        self.trifecta_pick_3	=	line[853:856] 
        self.trifecta_pick_4	=	line[856:859]

        self.betting_type_4	=	line[859:860] 
        self.wide_on_sale	=	line[860:861] 
        # 不成立
        self.wide_approved_1	=	line[861:862] 
        self.wide_approved_2	=	line[862:863] 
        self.wide_approved_3	=	line[863:864] 
        # 組番
        self.wide_no_1	=	line[864:867] 
        self.wide_no_2	=	line[867:870] 
        self.wide_no_3	=	line[870:873] 
        self.wide_no_4	=	line[873:876] 
        self.wide_no_5	=	line[876:879] 
        # 払戻金
        self.wide_1	=	line[879:886] 
        self.wide_2	=	line[886:893] 
        self.wide_3	=	line[893:900] 
        self.wide_4	=	line[900:907] 
        self.wide_5	=	line[907:914] 
        # 人気
        self.wide_pick_1	=	line[914:917] 
        self.wide_pick_2	=	line[917:920] 
        self.wide_pick_3	=	line[920:923] 
        self.wide_pick_4	=	line[923:926] 
        self.wide_pick_5	=	line[926:929] 

        self.betting_type_5	=	line[929:930] 
        self.trio_on_sale	=	line[930:931] 
        self.trio_approved	=	line[931:932] 
        # 組番
        self.trio_no_1	=	line[932:937] 
        self.trio_no_2	=	line[937:942] 
        self.trio_no_3	=	line[942:947] 
        self.trio_no_4	=	line[947:952] 
        # 払戻金
        self.trio_1	=	line[952:959] 
        self.trio_2	=	line[959:966] 
        self.trio_3	=	line[966:973] 
        self.trio_4	=	line[973:980] 
        # 人気
        self.trio_pick_1	=	line[980:983] 
        self.trio_pick_2	=	line[983:986] 
        self.trio_pick_3	=	line[986:989] 
        self.trio_pick_4	=	line[989:992] 
        # 返還情報
        self.put_out_rider_1	=	line[992:995] 
        self.put_out_reason_1	=	line[995:996] 
        self.put_out_rider_2	=	line[996:999] 
        self.put_out_reason_2	=	line[999:1000] 
        self.put_out_rider_3	=	line[1000:1003] 
        self.put_out_reason_3	=	line[1003:1004] 
        self.put_out_rider_4	=	line[1004:1007] 
        self.put_out_reason_4	=	line[1007:1008] 
        self.put_out_rider_5	=	line[1008:1011] 
        self.put_out_reason_5	=	line[1011:1012] 
        self.runway_status_code	=	line[1012:1013] 
        self.track_conditions	=	line[1013:1014] 
        self.reserve =	line[1014:1807] 

        # 必須項目を先ず登録
        # 区分
        # データ種別
        # 場コード
        # 場名
        # 開催日（西暦）
        # 開催初日
        # レース№
        # 競走距離
        # 発売有無
        # 賭式区分
        # 発売有無
        # 賭式
        # 発売有無

    def update_trn_results(self, trn_result):
        # 実体のあるカラム更新
        updateFields = list()
 
        # 日本語２バイト
        if self.date_Japanese_calendar:
            trn_result.Date_Japanese_calendar=self.date_Japanese_calendar
            updateFields.append('Date_Japanese_calendar')  

        # 日本語２バイト
        if self.held_day :
            trn_result.Held_day=self.held_day
            updateFields.append('Held_day')             
        if self.period_days :
        # 日本語２バイト
            trn_result.Period_days=self.period_days
            updateFields.append('Period_days')         
        if self.event_name :
            trn_result.Event_name=self.event_name
            updateFields.append('Event_name')   
        if self.commemorative_code :
            trn_result.Commemorative_code=self.commemorative_code
            updateFields.append('Commemorative_code')   
        if self.special_commemorative_code :
            trn_result.Special_commemorative_code=self.special_commemorative_code
            updateFields.append('Special_commemorative_code')   
        if self.net_sales_day :
            trn_result.Net_sales_day=self.net_sales_day
            updateFields.append('Net_sales_day')   
        if self.net_sales_period :
            trn_result.Net_sales_period=self.net_sales_period
            updateFields.append('Net_sales_period')   
        if self.net_sales_held :
            trn_result.Net_sales_held=self.net_sales_held
            updateFields.append('Net_sales_held')   
        if self.visitors_day :
            trn_result.visitors_day=self.visitors_day
            updateFields.append('visitors_day')   
        if self.visitors_period :
            trn_result.visitors_period=self.visitors_period
            updateFields.append('visitors_period')   
        if self.visitors_held :
            trn_result.visitors_held=self.visitors_held
            updateFields.append('visitors_held')   
        # 日本語２バイト
        if self.race_name :
            trn_result.Race_name=self.race_name
            updateFields.append('Race_name')   
        if self.participant_No :
            trn_result.Participant_No=self.participant_No
            updateFields.append('Participant_No')   
        if self.race_Approved :
            trn_result.Race_Approved=self.race_Approved
            updateFields.append('Race_Approved')   
        if self.race_postponed :
            trn_result.Race_postponed=self.race_postponed
            updateFields.append('Race_postponed')   
        if self.handicap_Open :
            trn_result.Handicap_Open=self.handicap_Open
            updateFields.append('Handicap_Open')   
        if self.race_Sales :
            trn_result.Race_Sales=self.race_Sales
            updateFields.append('Race_Sales')   
        if self.race_Pay_back :
            trn_result.Race_Pay_back=self.race_Pay_back
            updateFields.append('Race_Pay_back')   
        if self.win_prize :
            trn_result.Win_prize=self.win_prize
            updateFields.append('Win_prize')   
        if self.voting_code :
            trn_result.Voting_code=self.voting_code
            updateFields.append('Voting_code')   

        # Trn_Result
        if self.exacta_no_1:
            trn_result.Exacta_No_1=self.exacta_no_1
            updateFields.append('Exacta_No_1')   
        if self.exacta_1:
            trn_result.Exacta_1=self.exacta_1
            updateFields.append('Exacta_1')   
        if self.exacta_pick_1:
            trn_result.Exacta_pick_1=self.exacta_pick_1
            updateFields.append('Exacta_pick_1')   
        if self.exacta_no_2:
            trn_result.Exacta_No_2=self.exacta_no_2
            updateFields.append('Exacta_No_2')   
        if self.exacta_2:
            trn_result.Exacta_2=self.exacta_2
            updateFields.append('Exacta_2')   
        if self.exacta_pick_2:
            trn_result.Exacta_pick_2=self.exacta_pick_2
            updateFields.append('Exacta_pick_2')   
        if self.quinella_no_1:
            trn_result.Quinella_No_1=self.quinella_no_1
            updateFields.append('Quinella_No_1')   
        if self.quinella_1:
            trn_result.Quinella_1=self.quinella_1
            updateFields.append('Quinella_1')   
        if self.quinella_pick_1:
            trn_result.Quinella_pick_1=self.quinella_pick_1
            updateFields.append('Quinella_pick_1')   
        if self.quinella_no_2:
            trn_result.Quinella_No_2=self.quinella_no_2
            updateFields.append('Quinella_No_2')   
        if self.quinella_2:
            trn_result.Quinella_2=self.quinella_2
            updateFields.append('Quinella_2')   
        if self.quinella_pick_2:
            trn_result.Quinella_pick_2=self.quinella_pick_2
            updateFields.append('Quinella_pick_2')   

        if self.trifecta_approved:
            trn_result.Trifecta_approved=self.trifecta_approved
            updateFields.append('Trifecta_approved')   
        # 組番 繰り返す× 4
        if self.trifecta_no_1:
            trn_result.Trifecta_No_1=self.trifecta_no_1
            updateFields.append('Trifecta_No_1')   
        if self.trifecta_no_2:
            trn_result.Trifecta_No_2=self.trifecta_no_2
            updateFields.append('Trifecta_No_2')   

        if self.trifecta_no_3:
            trn_result.Trifecta_No_3=self.trifecta_no_3
            updateFields.append('Trifecta_No_3')   
        if self.trifecta_no_4:
            trn_result.Trifecta_No_4=self.trifecta_no_4
            updateFields.append('Trifecta_No_4')   
        # 払戻金
        if self.trifecta_1:
            trn_result.Trifecta_1=self.trifecta_1
            updateFields.append('Trifecta_1')   
        if self.trifecta_2:
            trn_result.Trifecta_2=self.trifecta_2
            updateFields.append('Trifecta_2')   
        if self.trifecta_3:
            trn_result.Trifecta_3=self.trifecta_3
            updateFields.append('Trifecta_3')   
        if self.trifecta_4:
            trn_result.Trifecta_4=self.trifecta_4
            updateFields.append('Trifecta_4')   
        # 人気
        if self.trifecta_pick_1:
            trn_result.Trifecta_pick_1=self.trifecta_pick_1
            updateFields.append('Trifecta_pick_1')   
        if self.trifecta_pick_2:
            trn_result.Trifecta_pick_2=self.trifecta_pick_2
            updateFields.append('Trifecta_pick_2')   
        if self.trifecta_pick_3:
            trn_result.Trifecta_pick_3=self.trifecta_pick_3
            updateFields.append('Trifecta_pick_3')   
        if self.trifecta_pick_4:
            trn_result.Trifecta_pick_4=self.trifecta_pick_4
            updateFields.append('Trifecta_pick_4')   
        if self.betting_type_4:
            trn_result.Betting_type_4=self.betting_type_4
            updateFields.append('Betting_type_4')   
        if self.wide_on_sale:
            trn_result.Wide_On_sale=self.wide_on_sale
            updateFields.append('Wide_On_sale')   
        # 不成立
        if self.wide_approved_1:
            trn_result.Wide_approved_1=self.wide_approved_1
            updateFields.append('Wide_approved_1')   
        if self.wide_approved_2:
            trn_result.Wide_approved_2=self.wide_approved_2
            updateFields.append('Wide_approved_2')   
        if self.wide_approved_3: 
            trn_result.Wide_approved_3=self.wide_approved_3
            updateFields.append('Wide_approved_3')   
        # 組番
        if self.wide_no_1:
            trn_result.Wide_No_1=self.wide_no_1
            updateFields.append('Wide_No_1')   
        if self.wide_no_2: 
            trn_result.Wide_No_2=self.wide_no_2
            updateFields.append('Wide_No_2')   
        if self.wide_no_3:
            trn_result.Wide_No_3=self.wide_no_3
            updateFields.append('Wide_No_3')   
        if self.wide_no_4:
            trn_result.Wide_No_4=self.wide_no_4
            updateFields.append('Wide_No_4')   
        if self.wide_no_5:
            trn_result.Wide_No_5=self.wide_no_5
            updateFields.append('Wide_No_5')   
        # 払戻金
        if self.wide_1:
            trn_result.Wide_1=self.wide_1
            updateFields.append('Wide_1')   
        if self.wide_2:
            trn_result.Wide_2=self.wide_2
            updateFields.append('Wide_2')   
        if self.wide_3:
            trn_result.Wide_3=self.wide_3
            updateFields.append('Wide_3')   
        if self.wide_4:
            trn_result.Wide_4=self.wide_4
            updateFields.append('Wide_4')   
        if self.wide_5:
            trn_result.Wide_5=self.wide_5
            updateFields.append('Wide_5')   
        # 人気
        if self.wide_pick_1:
            trn_result.Wide_pick_1=self.wide_pick_1
            updateFields.append('Wide_pick_1')   
        if self.wide_pick_2:
            trn_result.Wide_pick_2=self.wide_pick_2
            updateFields.append('Wide_pick_2')   
        if self.wide_pick_3:
            trn_result.Wide_pick_3=self.wide_pick_3
            updateFields.append('Wide_pick_3')   
        if self.wide_pick_4:
            trn_result.Wide_pick_4=self.wide_pick_4
            updateFields.append('Wide_pick_4')   
        if self.wide_pick_5:
            trn_result.Wide_pick_5=self.wide_pick_5
            updateFields.append('Wide_pick_5')   
        if self.trio_approved:
            trn_result.Trio_approved=self.trio_approved
            updateFields.append('Trio_approved')   
        # 組番
        if self.trio_no_1:
            trn_result.Trio_No_1=self.trio_no_1
            updateFields.append('Trio_No_1')   
        if self.trio_no_2: 
            trn_result.Trio_No_2=self.trio_no_2
            updateFields.append('Trio_No_2')   
        if self.trio_no_3:
            trn_result.Trio_No_3=self.trio_no_3
            updateFields.append('Trio_No_3')   
        if self.trio_no_4:
            trn_result.Trio_No_4=self.trio_no_4
            updateFields.append('Trio_No_4')   
        # 払戻金
        if self.trio_1:
            trn_result.Trio_1=self.trio_1
            updateFields.append('Trio_1')   
        if self.trio_2: 
            trn_result.Trio_2=self.trio_2
            updateFields.append('Trio_2')   
        if self.trio_3: 
            trn_result.Trio_3=self.trio_3
            updateFields.append('Trio_3')   
        if self.trio_4:
            trn_result.Trio_4=self.trio_4
            updateFields.append('Trio_4')   
        # 人気
        if self.trio_pick_1:
            trn_result.Trio_pick_1=self.trio_pick_1
            updateFields.append('Trio_pick_1')   
        if self.trio_pick_2:
            trn_result.Trio_pick_2=self.trio_pick_2
            updateFields.append('Trio_pick_2')   
        if self.trio_pick_3:
            trn_result.Trio_pick_3=self.trio_pick_3
            updateFields.append('Trio_pick_3')   
        if self.trio_pick_4:
            trn_result.Trio_pick_4=self.trio_pick_4
            updateFields.append('Trio_pick_4')   
        # 返還情報
        if self.put_out_rider_1:
            trn_result.Put_out_rider_1=self.put_out_rider_1
            updateFields.append('Put_out_rider_1')   
        if self.put_out_reason_1:
            trn_result.Put_out_Reason_1=self.put_out_reason_1
            updateFields.append('Put_out_Reason_1')   
        if self.put_out_rider_2:
            trn_result.Put_out_rider_2=self.put_out_rider_2
            updateFields.append('Put_out_rider_2')   
        if self.put_out_reason_2:
            trn_result.Put_out_Reason_2=self.put_out_reason_2
            updateFields.append('Put_out_Reason_2')   
        if self.put_out_rider_3:
            trn_result.Put_out_rider_3=self.put_out_rider_3
            updateFields.append('Put_out_rider_3')   
        if self.put_out_reason_3:
            trn_result.Put_out_Reason_3=self.put_out_reason_3
            updateFields.append('Put_out_Reason_3')   
        if self.put_out_rider_4:
            trn_result.Put_out_rider_4=self.put_out_rider_4
            updateFields.append('Put_out_rider_4')   
        if self.put_out_reason_4:
            trn_result.Put_out_Reason_4=self.put_out_reason_4
            updateFields.append('Put_out_Reason_4')   
        if self.put_out_rider_5:
            trn_result.Put_out_rider_5=self.put_out_rider_5
            updateFields.append('Put_out_rider_5')   
        if self.put_out_reason_5:
            trn_result.Put_out_Reason_5=self.put_out_reason_5
            updateFields.append('Put_out_Reason_5')   
        if self.runway_status_code:
            trn_result.Runway_status_code=self.runway_status_code
            updateFields.append('Runway_status_code')   
        if self.track_conditions:
            trn_result.Track_conditions=self.track_conditions
            updateFields.append('Track_conditions')   
        if self.reserve :
            trn_result.Reserve=self.reserve
            updateFields.append('Reserve')   
        trn_result.save(update_fields=updateFields)

    def insert_or_update_Trn_Result(self, name):
        try:
            # ファイル読み込み　データセット
            file = open(name,'r',encoding='shift_jis')
            for line in file: 
                
                # Q:何度も連打すると何故かうまく行かない。A:PollingObserver使用する。
                self.init_trn_result()
                
                self.setDatData(line)
                
                break            
            file.close()

            # DB　ファイル登録
            with transaction.atomic():
                # レース結果データレコード
                Trn_Result(Classification=self.classification, Data_type=self.data_type, Track_code=self.track_code, Track_name=self.track_name \
                , Date_AD=self.date_ad, First_day_of_the_event=self.first_day_of_the_event, Race_No=self.race_No, Race_distance=self.race_distance \
                , Betting_type_3=self.betting_type_3, Trifecta_On_sale=self.trifecta_on_sale, Betting_type_5=self.betting_type_5, Trio_On_sale=self.trio_on_sale).save()            
    
                # 空白チェックして実体があるカラムは更新
                self.update_trn_results(Trn_Result.objects.get(id=Trn_Result.objects.all().aggregate(Max('id')).get('id__max')))

                # 選手成績テーブル
                self.insert_or_update_trn_rider_results(self.trn_rider_results_line)

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)

    # ファイル作成時のイベント
    def on_created(self, event):
        filepath = event.src_path
        filename_result_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,resultData ,filename_result_record))
        # 監視元のフォルダパスを生成

        print('%s created Start' % filename_result_record)
        # ファイル読み込み
        
        self.insert_or_update_Trn_Result(name)
        
        print('%s created End' % filename_result_record)

    # ファイル変更時のイベント
    def on_modified(self, event):
        filepath = event.src_path
        filename_result_record = os.path.basename(filepath)
        print('%s changed' % filename_result_record)

    # ファイル削除時のイベント
    def on_deleted(self, event):
        filepath = event.src_path
        filename_result_record = os.path.basename(filepath)
        print('%s deleted' % filename_result_record)

    # ファイル移動時のイベント
    def on_moved(self, event):
        filepath = event.src_path
        filename_result_record = os.path.basename(filepath)

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base,resultData ,filename_result_record))    
        print('%s moved Start' % filename_result_record)
        # ファイル読み込み
        #!/usr/bin/python
        # -*- coding: utf-8 -*-
        self.insert_or_update_Trn_Result(name)

        print('%s moved End' % filename_result_record)

# コマンド実行の確認
class Command(BaseCommand):

    # python manage.py help XXXXXで表示されるメッセージ
    help = 'ファイルを監視してDBに登録する。'

    '''与えられた引数を受け取る'''
    def add_arguments(self, parser):
        # 今回はresultという名前で取得する。（引数は最低でも1個, int型）
        parser.add_argument('command_id', nargs='+', type=int)


    """受け取った引数を登録する"""
    def handle(self, *args, **options):
        # ファイル監視の開始
        # レース結果データレコード（mmddhhmmss0000JRR2.dat） 3: レース結果データレコード
        # J 以外固定
        # ・ファイル名称末尾８桁の“J”は場コード（1～6）、“RR”はレース No.（01～12）となります。 
        # 監視対象ディレクトリを指定する
        if resultID in options['command_id']:
            base_trn_Result = os.path.dirname(os.path.abspath(__file__))
            base = os.path.normpath(os.path.join(base_trn_Result,resultData))
            target_dir = os.path.expanduser(base)
            event_handler = FileChangeHandler(target_file_result_record)
            observer = PollingObserver()
            observer.schedule(event_handler, target_dir, recursive=go_recursively)# recursive再帰的
            observer.start()
        else:
            raise ValueError("command_id エラー")

        # 処理が終了しないようスリープを挟んで無限ループ
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
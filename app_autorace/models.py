from django.db import models
from django.db.models import * 
from django.utils import timezone

#---------DBマスターテーブル---------

#システム状態
class Tran_Systemstatus(Model):
    Environment = ForeignKey('Mst_Environment', verbose_name='実行環境',on_delete=PROTECT) #実行環境管理マスタ
    Unyou_date = DateField(verbose_name='運用日') #運用日
    Operationmode = ForeignKey('Mst_Operationmode',verbose_name='運用モード', on_delete=PROTECT)  #運用モード管理マスタ
    Daily_func_time = TimeField(verbose_name='日替わり設定時刻') #日替わり設定時刻
    Daily_func_prev_time = TimeField(verbose_name='日替わり前回実行時刻') #日替わり前回実行時刻
    Daily_func_prev_type = IntegerField(verbose_name='日替わり前回実行タイプ') #日替わり前回実行タイプ

    class Meta:
        verbose_name_plural = '#システム状態'
    
    def __str__(self):
        return str(self.Environment)
    
    def setState(self, opemode):
        self.Operationmode = opemode
        self.save()        #　変更したらセーブする！
        pass

#運用モード管理
class Mst_Operationmode(Model):
    Operationmode_code =  IntegerField(verbose_name='運用モード')
    Operationmode_name = CharField(verbose_name='運用モード表記', max_length=15) # オフライン/オンライン/マスタ編集中/日時処理中/～～マスタ編集中・・・

    class Meta:
       verbose_name_plural = '#運用管理'

    def __str__(self):
        return self.Operationmode_name

#実行環境管理
class Mst_Environment(Model):
    Environment_code =  IntegerField(verbose_name='実行環境')
    Environment_name = CharField(verbose_name='実行環境表記', max_length=15) #本番系/開発系

    class Meta:
       verbose_name_plural = '#実行環境管理'

    def __str__(self):
        return str(self.Environment_name)

#場名マスタ
class Mst_Race_track(Model):
    Track_code = CharField('コード', blank=True, null=True, max_length=1)
    Track_name = CharField('正式名', blank=True, null=True, max_length=10)
    shortened_3 = CharField('３字', blank=True, null=True, max_length=6)
    shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '場名マスタ'

    def __str__(self):
        return self.Track_name

#記念マスタ
class Mst_Commemorative_Race(Model):
    Commemorative_code = CharField('コード', blank=True, null=True, max_length=1)
    Commemorative_name = CharField('正式名', blank=True, null=True, max_length=40)
    shortened_2 = CharField('２字', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '記念マスタ'

    def __str__(self):
        return self.Commemorative_name

#特別記念マスタ
class Mst_Special_Commemorative_Race(Model):
    Special_commemorative_code = CharField('コード', blank=True, null=True, max_length=2)
    Special_commemorative_name = CharField('正式名', blank=True, null=True, max_length=60)
    Appear_index = CharField('表示順', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '特別記念マスタ'

    def __str__(self):
        return self.Special_commemorative_name

#種類マスタ
class Mst_Handicap_Open(Model):
    Handicap_Open_code = CharField('コード', blank=True, null=True, max_length=1)
    Handicap_Open_name = CharField('正式名', blank=True, null=True, max_length=20)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '種類マスタ'

    def __str__(self):
        return self.Handicap_Open_name

#級マスタ
class Mst_Player_class(Model):
    Rider_class_code = CharField('コード', blank=True, null=True, max_length=1)
    Rider_class_name = CharField('正式名', blank=True, null=True, max_length=6)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '級マスタ'

    def __str__(self):
        return self.Rider_class_name

#車級マスタ
class Mst_Auto_class(Model):
    Race_car_classification_code = CharField('コード', blank=True, null=True, max_length=1)
    Race_car_classification_name = CharField('正式名', blank=True, null=True, max_length=10)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '車級マスタ'

    def __str__(self):
        return self.Race_car_classification_name

#異常区分マスタ
class Mst_Accident_type(Model):
    Accident_code = CharField('コード', blank=True, null=True, max_length=1)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)
    Shortened_2 = CharField('２字', blank=True, null=True, max_length=4)
    Accident_name = CharField('正式名', blank=True, null=True, max_length=20)
    Appear_index = CharField('表示順', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '異常区分マスタ'

    def __str__(self):
        return self.Accident_name

#状況マスタ
class Mst_Race_status(Model):
    Race_situation_code = CharField('コード', blank=True, null=True, max_length=1)
    Race_situation_name = CharField('正式名', blank=True, null=True, max_length=20)

    class Meta:
        verbose_name_plural = '状況マスタ'

    def __str__(self):
        return self.Race_situation_name

#異常発走マスタ
class Mst_Illegal_start(Model):
    Illegal_start_code = CharField('コード', blank=True, null=True, max_length=1)
    Illegal_start_name = CharField('正式名', blank=True, null=True, max_length=20)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '異常発走マスタ'

    def __str__(self):
        return self.Illegal_start_name

#被妨害マスタ
class Mst_Disturbed(Model):
    Disturbed_code = CharField('コード', blank=True, null=True, max_length=1)
    Disturbed_name = CharField('正式名', blank=True, null=True, max_length=60)

    class Meta:
        verbose_name_plural = '被妨害マスタ'

    def __str__(self):
        return self.Disturbed_name

#発売状況マスタ
class Mst_Release_status(Model):
    Release_status_code = CharField('コード', blank=True, null=True, max_length=1)
    Release_status_name = CharField('正式名', blank=True, null=True, max_length=60)

    class Meta:
        verbose_name_plural = '発売状況マスタ'

    def __str__(self):
        return self.Release_status_name

#返還理由マスタ
class Mst_Putout_Reason(Model):
    Put_out_Reason_code = CharField('コード', blank=True, null=True, max_length=1)
    Shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '返還理由マスタ'

    def __str__(self):
        return self.Shortened_1

#売場名マスタ
class Mst_Outside_track(Model):
    Mst_Outside_track_code = CharField('コード', blank=True, null=True, max_length=1)
    Mst_Outside_track_name = CharField('正式名', blank=True, null=True, max_length=10)
    shortened_3 = CharField('３字', blank=True, null=True, max_length=6)
    shortened_1 = CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '売場名マスタ'

    def __str__(self):
        return self.Mst_Outside_track_name

#---------DBトランザクションテーブル---------

#スケジュール
class Trn_Schedule(Model):
    Cllasification = CharField('区分', blank=True, null=True, max_length=1)
    Data_type = CharField('データ種別', blank=True, null=True ,max_length=1)
    Send_date = CharField('送信日', blank=True, null=True, max_length=8)
    Race_date_1 = CharField('競争年月日１', blank=True, null=True, max_length=8)
    Outside_1 = CharField('場外売場情報１', blank=True, null=True, max_length=1)
    Track_code1_1 = CharField('場コード１＿１', blank=True, null=True, max_length=1)
    races_1_1 = CharField('レース数１＿１', blank=True, null=True, max_length=2)
    Track_code1_2 = CharField('場コード１＿２', blank=True, null=True, max_length=1)
    races_1_2 = CharField('レース数１＿２', blank=True, null=True, max_length=2)
    Track_code1_3 = CharField('場コード１＿３', blank=True, null=True, max_length=1)
    races_1_3 = CharField('レース数１＿３', blank=True, null=True, max_length=2)
    Track_code1_4 = CharField('場コード１＿４', blank=True, null=True, max_length=1)
    races_1_4 = CharField('レース数１＿４', blank=True, null=True, max_length=2)
    Track_code1_5 = CharField('場コード１＿５', blank=True, null=True, max_length=1)
    races_1_5 = CharField('レース数１＿５', blank=True, null=True, max_length=2)
    Track_code1_6 = CharField('場コード１＿６', blank=True, null=True, max_length=1)
    races_1_6 = CharField('レース数１＿６', blank=True, null=True, max_length=2)
    Race_date_2 = CharField('競争年月日２', blank=True, null=True, max_length=8)
    Outside_2 = CharField('場外売場情報２', blank=True, null=True, max_length=1)
    Track_code2_1 = CharField('場コード２＿１', blank=True, null=True, max_length=1)
    races_2_1 = CharField('レース数２＿１', blank=True, null=True, max_length=2)
    Track_code2_2 = CharField('場コード２＿２', blank=True, null=True, max_length=1)
    races_2_2 = CharField('レース数２＿２', blank=True, null=True, max_length=2)
    Track_code2_3 = CharField('場コード２＿３', blank=True, null=True, max_length=1)
    races_2_3 = CharField('レース数２＿３', blank=True, null=True, max_length=2)
    Track_code2_4 = CharField('場コード２＿４', blank=True, null=True, max_length=1)
    races_2_4 = CharField('レース数２＿４', blank=True, null=True, max_length=2)
    Track_code2_5 = CharField('場コード２＿５', blank=True, null=True, max_length=1)
    races_2_5 = CharField('レース数２＿５', blank=True, null=True, max_length=2)
    Track_code2_6 = CharField('場コード２＿６', blank=True, null=True, max_length=1)
    races_2_6 = CharField('レース数２＿６', blank=True, null=True, max_length=2)
    Race_date_3 = CharField('競争年月日３', blank=True, null=True, max_length=8)
    Outside_3 = CharField('場外売場情報３', blank=True, null=True, max_length=1)
    Track_code3_1 = CharField('場コード３＿１', blank=True, null=True, max_length=1)
    races_3_1 = CharField('レース数３＿１', blank=True, null=True, max_length=2)
    Track_code3_2 = CharField('場コード３＿２', blank=True, null=True, max_length=1)
    races_3_2 = CharField('レース数３＿２', blank=True, null=True, max_length=2)
    Track_code3_3 = CharField('場コード３＿３', blank=True, null=True, max_length=1)
    races_3_3 = CharField('レース数３＿３', blank=True, null=True, max_length=2)
    Track_code3_4 = CharField('場コード３＿４', blank=True, null=True, max_length=1)
    races_3_4 = CharField('レース数３＿４', blank=True, null=True, max_length=2)
    Track_code3_5 = CharField('場コード３＿５', blank=True, null=True, max_length=1)
    races_3_5 = CharField('レース数３＿５', blank=True, null=True, max_length=2)
    Track_code3_6 = CharField('場コード３＿６', blank=True, null=True, max_length=1)
    races_3_6 = CharField('レース数３＿６', blank=True, null=True, max_length=2)
    Top_30_prizes = CharField('賞金上位３０傑', blank=True, null=True, max_length=1)

    class Meta:
        verbose_name_plural = '【固定長】スケジュール'

#番組編成データレコード
class Trn_Program(Model):
    Classification = CharField('区分', blank=True, null=True, max_length=1)
    Data_type = CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = CharField('場コード', blank=True, null=True ,max_length=1)
    Track_name = CharField('場名', blank=True, null=True ,max_length=6)
    Date_AD = CharField('開催日（西暦）', blank=True, null=True ,max_length=8)
    Date_Japanese_calendar = CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = CharField('記念コード', blank=True, null=True, max_length=1)
    Special_commemorative_code = CharField('特別記念コード', blank=True, null=True, max_length=2)
    Race_No = CharField('レース№', blank=True, null=True, max_length=2)
    Race_name = CharField('レース名称', blank=True, null=True, max_length=26)
    Race_distance = CharField('競走距離', blank=True, null=True, max_length=4)
    Scheduled_start_time = CharField('発送予定時刻', blank=True, null=True, max_length=5)
    Participation = CharField('車立て数', blank=True, null=True, max_length=1)
    Race_Prize_Amount = CharField('レース賞金額', blank=True, null=True, max_length=9)
    Handicap_Open_code = CharField('ハンデ・オープン戦', blank=True, null=True, max_length=1)
    Voting_code = CharField('投票場コード', blank=True, null=True, max_length=2)
    Win_Ave_Totaling_Date = CharField('勝率集計日', blank=True, null=True, max_length=8)
    Totaling_date = CharField('通算成績集計日', blank=True, null=True, max_length=8)
    Reserve = CharField('予備', blank=True, null=True, max_length=124)
    class Meta:
        verbose_name_plural = '【固定長】番組編成データレコード'

#出走選手テーブル
class Trn_Running_list(Model):
    Track_code = CharField('場コード', blank=True, null=True, max_length=1)
    Date_AD = CharField('開催日（西暦）', blank=True, null=True, max_length=8)
    Race_No = CharField('レース№', blank=True, null=True, max_length=2)
    Bracket_No =  CharField('連勝番号', blank=True, null=True, max_length=1)
    Rider_No = CharField('車番', blank=True, null=True, max_length=1)
    Rider_code = CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_code = CharField('ＬＧコード', blank=True, null=True, max_length=1)
    LG_name = CharField('ＬＧ名', blank=True, null=True, max_length=6)
    Nickname = CharField('呼名', blank=True, null=True, max_length=12)
    Rider_class_code = CharField('選手級別', blank=True, null=True, max_length=1)
    Race_car_classification_code = CharField('競走車級別', blank=True, null=True, max_length=1)
    Handicap = CharField('ハンデ', blank=True, null=True, max_length=3)
    Last_run_4 = CharField('直近前々々々走', blank=True, null=True, max_length=2)
    Last_run_3 = CharField('直近前々々走', blank=True, null=True, max_length=2)
    Last_run_2 = CharField('直近前々走', blank=True, null=True, max_length=2)
    Last_run_1 = CharField('直近前走', blank=True, null=True, max_length=2)
    Last_run_4_Track = CharField('直近前々々々走出走場', blank=True, null=True, max_length=1)
    Last_run_3_Track = CharField('直近前々々走出走場', blank=True, null=True, max_length=1)
    Last_run_2_Track = CharField('直近前々走出走場', blank=True, null=True, max_length=1)
    Last_run_1_Track = CharField('直近前走出走場', blank=True, null=True, max_length=1)
    Last_run_time = CharField('直近前走タイム', blank=True, null=True, max_length=4)
    Avg_time = CharField('平均タイム', blank=True, null=True, max_length=4)
    Highest_time = CharField('最高タイム', blank=True, null=True, max_length=4)
    Best_time_Track = CharField('最高タイム場所', blank=True, null=True, max_length=6)
    Rider_birthplace = CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = CharField('年齢', blank=True, null=True, max_length=2)
    By_period = CharField('期別', blank=True, null=True, max_length=2)
    Avg_win_1 = CharField('単勝率', blank=True, null=True, max_length=4)
    Avg_win_2 = CharField('連勝率', blank=True, null=True, max_length=4)
    Avg_win_3 = CharField('複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_goodrunway = CharField('良走路単勝率', blank=True, null=True, max_length=4)
    Avg_win_2_goodrunway = CharField('良走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_goodrunway = CharField('良走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_Wetrunway = CharField('雨走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_2_Wetrunway = CharField('雨走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_Wetrunway = CharField('雨走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_ohter = CharField('その他走路単勝率', blank=True, null=True, max_length=4)
    Avg_win_2_ohter = CharField('その他走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_ohter = CharField('その他走路複勝率', blank=True, null=True, max_length=4)
    Last_1_test_run_time = CharField('過去１走試走タイム', blank=True, null=True, max_length=4)
    Last_1_time = CharField('過去１走競走タイム', blank=True, null=True, max_length=4)
    Last_1_lap_time = CharField('過去１走周回タイム', blank=True, null=True, max_length=4)
    Last_1_run = CharField('過去１走着', blank=True, null=True, max_length=2)
    Last_1_Track = CharField('過去１走場', blank=True, null=True, max_length=1)
    Last_1_ST = CharField('過去１走ＳＴ', blank=True, null=True, max_length=2)
    Last_1_Handicap = CharField('過去１走ハンデ', blank=True, null=True, max_length=3)
    Last_1_track_condition = CharField('過去１走走路状況', blank=True, null=True, max_length=2)
    Last_2_test_run_time = CharField('過去２走試走タイム', blank=True, null=True, max_length=4)
    Last_2_time = CharField('過去２走競走タイム', blank=True, null=True, max_length=4)
    Last_2_lap_time = CharField('過去２走周回タイム', blank=True, null=True, max_length=4)
    Last_2_run = CharField('過去２走着', blank=True, null=True, max_length=2)
    Last_2_Track = CharField('過去２走場', blank=True, null=True, max_length=1)
    Last_2_ST = CharField('過去２走ＳＴ', blank=True, null=True, max_length=2)
    Last_2_Handicap = CharField('過去２走ハンデ', blank=True, null=True, max_length=3)
    Last_2_track_condition = CharField('過去２走走路状況', blank=True, null=True, max_length=2)
    Last_3_test_run_time = CharField('過去３走試走タイム', blank=True, null=True, max_length=4)
    Last_3_time = CharField('過去３走競走タイム', blank=True, null=True, max_length=4)
    Last_3_lap_time = CharField('過去３走周回タイム', blank=True, null=True, max_length=4)
    Last_3_run = CharField('過去３走着', blank=True, null=True, max_length=2)
    Last_3_Track = CharField('過去３走場', blank=True, null=True, max_length=1)
    Last_3_ST = CharField('過去３走ＳＴ', blank=True, null=True, max_length=2)
    Last_3_Handicap = CharField('過去３走ハンデ', blank=True, null=True, max_length=3)
    Last_3_track_condition = CharField('過去３走走路状況', blank=True, null=True, max_length=2)
    Last_4_test_run_time = CharField('過去４走試走タイム', blank=True, null=True, max_length=4)
    Last_4_time = CharField('過去４走競走タイム', blank=True, null=True, max_length=4)
    Last_4_lap_time = CharField('過去４走周回タイム', blank=True, null=True, max_length=4)
    Last_4_run = CharField('過去４走着', blank=True, null=True, max_length=2)
    Last_4_Track = CharField('過去４走場', blank=True, null=True, max_length=1)
    Last_4_ST = CharField('過去４走ＳＴ', blank=True, null=True, max_length=2)
    Last_4_Handicap = CharField('過去４走ハンデ', blank=True, null=True, max_length=3)
    Last_4_track_condition = CharField('過去４走走路状況', blank=True, null=True, max_length=2)
    Last_5_test_run_time = CharField('過去５走試走タイム', blank=True, null=True, max_length=4)
    Last_5_time = CharField('過去５走競走タイム', blank=True, null=True, max_length=4)
    Last_5_lap_time = CharField('過去５走周回タイム', blank=True, null=True, max_length=4)
    Last_5_run = CharField('過去５走着', blank=True, null=True, max_length=2)
    Last_5_Track = CharField('過去５走場', blank=True, null=True, max_length=1)
    Last_5_ST = CharField('過去５走ＳＴ', blank=True, null=True, max_length=2)
    Last_5_Handicap = CharField('過去５走ハンデ', blank=True, null=True, max_length=3)
    Last_5_track_condition = CharField('過去５走走路状況', blank=True, null=True, max_length=2)
    Last_6_test_run_time = CharField('過去６走試走タイム', blank=True, null=True, max_length=4)
    Last_6_time = CharField('過去６走競走タイム', blank=True, null=True, max_length=4)
    Last_6_lap_time = CharField('過去６走周回タイム', blank=True, null=True, max_length=4)
    Last_6_run = CharField('過去６走着', blank=True, null=True, max_length=2)
    Last_6_Track = CharField('過去６走場', blank=True, null=True, max_length=1)
    Last_6_ST = CharField('過去６走ＳＴ', blank=True, null=True, max_length=2)
    Last_6_Handicap = CharField('過去６走ハンデ', blank=True, null=True, max_length=3)
    Last_6_track_condition = CharField('過去６走走路状況', blank=True, null=True, max_length=2)
    Last_7_test_run_time = CharField('過去７走試走タイム', blank=True, null=True, max_length=4)
    Last_7_time = CharField('過去７走競走タイム', blank=True, null=True, max_length=4)
    Last_7_lap_time = CharField('過去７走周回タイム', blank=True, null=True, max_length=4)
    Last_7_run = CharField('過去７走着', blank=True, null=True, max_length=2)
    Last_7_Track = CharField('過去７走場', blank=True, null=True, max_length=1)
    Last_7_ST = CharField('過去７走ＳＴ', blank=True, null=True, max_length=2)
    Last_7_Handicap = CharField('過去７走ハンデ', blank=True, null=True, max_length=3)
    Last_7_track_condition = CharField('過去７走走路状況', blank=True, null=True, max_length=2)
    Last_8_test_run_time = CharField('過去８走試走タイム', blank=True, null=True, max_length=4)
    Last_8_time = CharField('過去８走競走タイム', blank=True, null=True, max_length=4)
    Last_8_lap_time = CharField('過去８走周回タイム', blank=True, null=True, max_length=4)
    Last_8_run = CharField('過去８走着', blank=True, null=True, max_length=2)
    Last_8_Track = CharField('過去８走場', blank=True, null=True, max_length=1)
    Last_8_ST = CharField('過去８走ＳＴ', blank=True, null=True, max_length=2)
    Last_8_Handicap = CharField('過去８走ハンデ', blank=True, null=True, max_length=3)
    Last_8_track_condition = CharField('過去８走走路状況', blank=True, null=True, max_length=2)
    Last_9_test_run_time = CharField('過去９走試走タイム', blank=True, null=True, max_length=4)
    Last_9_time = CharField('過去９走競走タイム', blank=True, null=True, max_length=4)
    Last_9_lap_time = CharField('過去９走周回タイム', blank=True, null=True, max_length=4)
    Last_9_run = CharField('過去９走着', blank=True, null=True, max_length=2)
    Last_9_Track = CharField('過去９走場', blank=True, null=True, max_length=1)
    Last_9_ST = CharField('過去９走ＳＴ', blank=True, null=True, max_length=2)
    Last_9_Handicap = CharField('過去９走ハンデ', blank=True, null=True, max_length=3)
    Last_9_track_condition = CharField('過去９走走路状況', blank=True, null=True, max_length=2)
    Last_10_test_run_time = CharField('過去１０走試走タイム', blank=True, null=True, max_length=4)
    Last_10_time = CharField('過去１０走競走タイム', blank=True, null=True, max_length=4)
    Last_10_lap_time = CharField('過去１０走周回タイム', blank=True, null=True, max_length=4)
    Last_10_run = CharField('過去１０走着', blank=True, null=True, max_length=2)
    Last_10_Track = CharField('過去１０走場', blank=True, null=True, max_length=1)
    Last_10_ST = CharField('過去１０走ＳＴ', blank=True, null=True, max_length=2)
    Last_10_Handicap = CharField('過去１０走ハンデ', blank=True, null=True, max_length=3)
    Last_10_track_condition = CharField('過去１０走走路状況', blank=True, null=True, max_length=2)
    Total_V = CharField('通算Ｖ数', blank=True, null=True, max_length=4)
    Total_1st = CharField('１着回数', blank=True, null=True, max_length=4)
    Total_2nd = CharField('２着回数', blank=True, null=True, max_length=4)
    Total_3rd = CharField('３着回数', blank=True, null=True, max_length=4)
    Total_other = CharField('着外回数', blank=True, null=True, max_length=5)

    class Meta:
        verbose_name_plural = '【固定長】番組編成・出走選手テーブル'

#レース結果データレコード
class Trn_Result(Model):
    Classification = CharField('区分', blank=True, null=True, max_length=1)
    Data_type = CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = CharField('場コード', blank=True, null=True ,max_length=1)
    Track_name = CharField('場名', blank=True, null=True ,max_length=6)
    Date_AD = CharField('開催日（西暦）', blank=True, null=True, max_length=8)
    Date_Japanese_calendar = CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = CharField('記念コード', blank=True, null=True, max_length=1)
    Special_commemorative_code = CharField('特別記念コード', blank=True, null=True, max_length=2)
    Net_sales_day = CharField('当日純売上金額', blank=True, null=True, max_length=14)
    Net_sales_period = CharField('当該節純売上金額', blank=True, null=True, max_length=14)
    Net_sales_held = CharField('当該回純売上金額', blank=True, null=True, max_length=14)
    visitors_day = CharField('当日入場者数', blank=True, null=True, max_length=7)
    visitors_period = CharField('当該節入場者数', blank=True, null=True, max_length=7)
    visitors_held = CharField('当該回入場者数', blank=True, null=True, max_length=7)
    Race_No = CharField('レース№', blank=True, null=True, max_length=2)
    Race_name = CharField('レース名称', blank=True, null=True, max_length=26)
    Race_distance = CharField('競走距離', blank=True, null=True, max_length=4)
    Participant_No = CharField('車立て数', blank=True, null=True, max_length=1)
    Race_Approved = CharField('不成立コード', blank=True, null=True, max_length=1)
    Race_postponed = CharField('順延フラグ', blank=True, null=True, max_length=1)
    Handicap_Open = CharField('ハンデ・オープン戦', blank=True, null=True, max_length=1)
    Race_Sales = CharField('当該レース売上金額', blank=True, null=True, max_length=13)
    Race_Pay_back = CharField('当該レース返還金額', blank=True, null=True, max_length=13)
    Win_prize = CharField('一着賞金', blank=True, null=True, max_length=8)
    Voting_code = CharField('投票場コード', blank=True, null=True, max_length=2)
    Exacta_No_1 = CharField('連単組番１', blank=True, null=True, max_length=3)
    Exacta_1 = CharField('連単払戻金額１', blank=True, null=True, max_length=7)
    Exacta_pick_1 = CharField('連単勝車人気１', blank=True, null=True, max_length=2)
    Exacta_No_2 = CharField('連単組番２', blank=True, null=True, max_length=3)
    Exacta_2 = CharField('連単払戻金額２', blank=True, null=True, max_length=7)
    Exacta_pick_2 = CharField('連単勝車人気２', blank=True, null=True, max_length=2)
    Quinella_No_1 = CharField('連複組番１', blank=True, null=True, max_length=3)
    Quinella_1 = CharField('連複払戻金額１', blank=True, null=True, max_length=7)
    Quinella_pick_1 = CharField('連複勝車人気１', blank=True, null=True, max_length=2)
    Quinella_No_2 = CharField('連複組番２', blank=True, null=True, max_length=3)
    Quinella_2 = CharField('連複払戻金額２', blank=True, null=True, max_length=7)
    Quinella_pick_2 = CharField('連複勝車人気２', blank=True, null=True, max_length=2)
    Betting_type_3 = CharField('賭式区分３', blank=True, null=True, max_length=1)
    Trifecta_On_sale = CharField('発売有無３', blank=True, null=True, max_length=1)
    Trifecta_approved = CharField('不成立３', blank=True, null=True, max_length=1)
    Trifecta_No_1 = CharField('組番３＿１', blank=True, null=True, max_length=5)
    Trifecta_No_2 = CharField('組番３＿２', blank=True, null=True, max_length=5)
    Trifecta_No_3 = CharField('組番３＿３', blank=True, null=True, max_length=5)
    Trifecta_No_4 = CharField('組番３＿４', blank=True, null=True, max_length=5)
    Trifecta_1 = CharField('払戻金３＿１', blank=True, null=True, max_length=7)
    Trifecta_2 = CharField('払戻金３＿２', blank=True, null=True, max_length=7)
    Trifecta_3 = CharField('払戻金３＿３', blank=True, null=True, max_length=7)
    Trifecta_4 = CharField('払戻金３＿４', blank=True, null=True, max_length=7)
    Trifecta_pick_1 = CharField('人気３＿１', blank=True, null=True, max_length=3)
    Trifecta_pick_2 = CharField('人気３＿２', blank=True, null=True, max_length=3)
    Trifecta_pick_3 = CharField('人気３＿３', blank=True, null=True, max_length=3)
    Trifecta_pick_4 = CharField('人気３＿４', blank=True, null=True, max_length=3)
    Betting_type_4 = CharField('賭式区分４', blank=True, null=True, max_length=1)
    Wide_On_sale = CharField('発売有無４', blank=True, null=True, max_length=1)
    Wide_approved_1 = CharField('不成立４＿１', blank=True, null=True, max_length=1)
    Wide_approved_2 = CharField('不成立４＿２', blank=True, null=True, max_length=1)
    Wide_approved_3 = CharField('不成立４＿３', blank=True, null=True, max_length=1)
    Wide_No_1 = CharField('組番４＿１', blank=True, null=True, max_length=3)
    Wide_No_2 = CharField('組番４＿２', blank=True, null=True, max_length=3)
    Wide_No_3 = CharField('組番４＿３', blank=True, null=True, max_length=3)
    Wide_No_4 = CharField('組番４＿４', blank=True, null=True, max_length=3)
    Wide_No_5 = CharField('組番４＿５', blank=True, null=True, max_length=3)
    Wide_1 = CharField('払戻金４＿１', blank=True, null=True, max_length=7)
    Wide_2 = CharField('払戻金４＿２', blank=True, null=True, max_length=7)
    Wide_3 = CharField('払戻金４＿３', blank=True, null=True, max_length=7)
    Wide_4 = CharField('払戻金４＿４', blank=True, null=True, max_length=7)
    Wide_5 = CharField('払戻金４＿５', blank=True, null=True, max_length=7)
    Wide_pick_1 = CharField('人気４＿１', blank=True, null=True, max_length=7)
    Wide_pick_2 = CharField('人気４＿２', blank=True, null=True, max_length=3)
    Wide_pick_3 = CharField('人気４＿３', blank=True, null=True, max_length=3)
    Wide_pick_4 = CharField('人気４＿４', blank=True, null=True, max_length=3)
    Wide_pick_5 = CharField('人気４＿５', blank=True, null=True, max_length=3)
    Betting_type_5 = CharField('賭式区分５', blank=True, null=True, max_length=1)
    Trio_On_sale = CharField('発売有無５', blank=True, null=True, max_length=1)
    Trio_approved = CharField('不成立５', blank=True, null=True, max_length=1)
    Trio_No_1 = CharField('組番５＿１', blank=True, null=True, max_length=5)
    Trio_No_2 = CharField('組番５＿２', blank=True, null=True, max_length=5)
    Trio_No_3 = CharField('組番５＿３', blank=True, null=True, max_length=5)
    Trio_No_4 = CharField('組番５＿４', blank=True, null=True, max_length=5)
    Trio_1 = CharField('払戻金５＿１', blank=True, null=True, max_length=7)
    Trio_2 = CharField('払戻金５＿２', blank=True, null=True, max_length=7)
    Trio_3 = CharField('払戻金５＿３', blank=True, null=True, max_length=7)
    Trio_4 = CharField('払戻金５＿４', blank=True, null=True, max_length=7)
    Trio_pick_1 = CharField('人気５＿１', blank=True, null=True, max_length=3)
    Trio_pick_2 = CharField('人気５＿２', blank=True, null=True, max_length=3)
    Trio_pick_3 = CharField('人気５＿３', blank=True, null=True, max_length=3)
    Trio_pick_4 = CharField('人気５＿４', blank=True, null=True, max_length=3)
    Put_out_rider_1 = CharField('返還選手名１', blank=True, null=True, max_length=6)
    Put_out_Reason_1 = CharField('返還理由１', blank=True, null=True, max_length=1)
    Put_out_rider_2 = CharField('返還選手名２', blank=True, null=True, max_length=6)
    Put_out_Reason_2 = CharField('返還理由２', blank=True, null=True, max_length=1)
    Put_out_rider_3 = CharField('返還選手名３', blank=True, null=True, max_length=6)
    Put_out_Reason_3 = CharField('返還理由３', blank=True, null=True, max_length=1)
    Put_out_rider_4 = CharField('返還選手名４', blank=True, null=True, max_length=6)
    Put_out_Reason_4 = CharField('返還理由４', blank=True, null=True, max_length=1)
    Put_out_rider_5 = CharField('返還選手名５', blank=True, null=True, max_length=6)
    Put_out_Reason_5 = CharField('返還理由５', blank=True, null=True, max_length=1)
    Runway_status_code = CharField('走路状況コード', blank=True, null=True, max_length=1)
    Track_conditions = CharField('走路状況', blank=True, null=True, max_length=2)
    Reserve = CharField('予備', blank=True, null=True, max_length=793)

    class Meta:
        verbose_name_plural = '【固定長】レース結果データレコード'

#選手成績テーブル
class Trn_Rider_results(Model):
    Track_code = CharField('場コード', blank=True, null=True, max_length=1)
    Date_AD = CharField('開催日（西暦）', blank=True, null=True, max_length=8)
    Race_No = CharField('レース№', blank=True, null=True, max_length=2)
    Bracket_No =  CharField('連勝番号', blank=True, null=True, max_length=1)
    Rider_No = CharField('車番', blank=True, null=True, max_length=1)
    Rider_code = CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_name = CharField('ＬＧ名', blank=True, null=True, max_length=6)
    LG_code = CharField('ＬＧコード', blank=True, null=True, max_length=1)
    Nickname = CharField('呼名', blank=True, null=True, max_length=12)
    Rider_birthplace = CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = CharField('年齢', blank=True, null=True, max_length=2)
    By_period = CharField('期別', blank=True, null=True, max_length=2)
    Handicap = CharField('ハンデ', blank=True, null=True, max_length=3)
    Result = CharField('着', blank=True, null=True, max_length=1)
    Accident_code = CharField('事故コード', blank=True, null=True, max_length=2)
    Accident_name = CharField('事故名称', blank=True, null=True, max_length=6)
    Illegal_start_code = CharField('異常発走コード', blank=True, null=True, max_length=1)
    Disturbed_code = CharField('被妨害コード', blank=True, null=True, max_length=1)
    Test_run_time = CharField('試走タイム', blank=True, null=True, max_length=4)
    Race_time = CharField('競走タイム', blank=True, null=True, max_length=4)
    Minute_second = CharField('分秒', blank=True, null=True, max_length=4)
    Start_timing = CharField('スタートタイミング', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '【固定長】レース結果・選手成績テーブル'

#場外売場情報
class Trn_Outside_track(Model):
    Cllasification = CharField('区分', blank=True, null=True, max_length=1)
    Data_type = CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = CharField('場コード', blank=True, null=True ,max_length=1)
    Track_name = CharField('場名', blank=True, null=True ,max_length=6)
    Date_AD = CharField('開催日（西暦）', blank=True, null=True ,max_length=8)
    Date_Japanese_calendar = CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = CharField('記念コード', blank=True, null=True, max_length=1)
    Special_commemorative_code = CharField('特別記念コード', blank=True, null=True, max_length=2)

    OTB_code_1 = CharField('売場コード＿１', blank=True, null=True, max_length=1)
    OTB_1 = CharField('売場名＿１', blank=True, null=True, max_length=6)
    OTB_Classification_1 = CharField('売場区分＿１', blank=True, null=True, max_length=1)
    Held_Classification_1 = CharField('開催区分＿１', blank=True, null=True, max_length=1)
    Note_code_1 = CharField('注釈コード＿１', blank=True, null=True, max_length=2)
    race_1_1 = CharField('レース１＿１', blank=True, null=True, max_length=1)
    race_2_1 = CharField('レース２＿１', blank=True, null=True, max_length=1)
    race_3_1 = CharField('レース３＿１', blank=True, null=True, max_length=1)
    race_4_1 = CharField('レース４＿１', blank=True, null=True, max_length=1)
    race_5_1 = CharField('レース５＿１', blank=True, null=True, max_length=1)
    race_6_1 = CharField('レース６＿１', blank=True, null=True, max_length=1)
    race_7_1 = CharField('レース７＿１', blank=True, null=True, max_length=1)
    race_8_1 = CharField('レース８＿１', blank=True, null=True, max_length=1)
    race_9_1 = CharField('レース９＿１', blank=True, null=True, max_length=1)
    race_10_1 = CharField('レース１０＿１', blank=True, null=True, max_length=1)
    race_11_1 = CharField('レース１１＿１', blank=True, null=True, max_length=1)
    race_12_1 = CharField('レース１２＿１', blank=True, null=True, max_length=1)

    OTB_code_2 = CharField('売場コード＿２', blank=True, null=True, max_length=1)
    OTB_2 = CharField('売場名＿２', blank=True, null=True, max_length=6)
    OTB_Classification_2 = CharField('売場区分＿２', blank=True, null=True, max_length=1)
    Held_Classification_2 = CharField('開催区分＿２', blank=True, null=True, max_length=1)
    Note_code_2 = CharField('注釈コード＿２', blank=True, null=True, max_length=2)
    race_1_2 = CharField('レース１＿２', blank=True, null=True, max_length=1)
    race_2_2 = CharField('レース２＿２', blank=True, null=True, max_length=1)
    race_3_2 = CharField('レース３＿２', blank=True, null=True, max_length=1)
    race_4_2 = CharField('レース４＿２', blank=True, null=True, max_length=1)
    race_5_2 = CharField('レース５＿２', blank=True, null=True, max_length=1)
    race_6_2 = CharField('レース６＿２', blank=True, null=True, max_length=1)
    race_7_2 = CharField('レース７＿２', blank=True, null=True, max_length=1)
    race_8_2 = CharField('レース８＿２', blank=True, null=True, max_length=1)
    race_9_2 = CharField('レース９＿２', blank=True, null=True, max_length=1)
    race_10_2 = CharField('レース１０＿２', blank=True, null=True, max_length=1)
    race_11_2 = CharField('レース１１＿２', blank=True, null=True, max_length=1)
    race_12_2 = CharField('レース１２＿２', blank=True, null=True, max_length=1)

    OTB_code_3 = CharField('売場コード＿３', blank=True, null=True, max_length=1)
    OTB_3 = CharField('売場名＿３', blank=True, null=True, max_length=6)
    OTB_Classification_3 = CharField('売場区分＿３', blank=True, null=True, max_length=1)
    Held_Classification_3 = CharField('開催区分＿３', blank=True, null=True, max_length=1)
    Note_code_3 = CharField('注釈コード＿３', blank=True, null=True, max_length=2)
    race_1_3 = CharField('レース１＿３', blank=True, null=True, max_length=1)
    race_2_3 = CharField('レース２＿３', blank=True, null=True, max_length=1)
    race_3_3 = CharField('レース３＿３', blank=True, null=True, max_length=1)
    race_4_3 = CharField('レース４＿３', blank=True, null=True, max_length=1)
    race_5_3 = CharField('レース５＿３', blank=True, null=True, max_length=1)
    race_6_3 = CharField('レース６＿３', blank=True, null=True, max_length=1)
    race_7_3 = CharField('レース７＿３', blank=True, null=True, max_length=1)
    race_8_3 = CharField('レース８＿３', blank=True, null=True, max_length=1)
    race_9_3 = CharField('レース９＿３', blank=True, null=True, max_length=1)
    race_10_3 = CharField('レース１０＿３', blank=True, null=True, max_length=1)
    race_11_3 = CharField('レース１１＿３', blank=True, null=True, max_length=1)
    race_12_3 = CharField('レース１２＿３', blank=True, null=True, max_length=1)

    OTB_code_4 = CharField('売場コード＿４', blank=True, null=True, max_length=1)
    OTB_4 = CharField('売場名＿４', blank=True, null=True, max_length=6)
    OTB_Classification_4 = CharField('売場区分＿４', blank=True, null=True, max_length=1)
    Held_Classification_4 = CharField('開催区分＿４', blank=True, null=True, max_length=1)
    Note_code_4 = CharField('注釈コード＿４', blank=True, null=True, max_length=2)
    race_1_4 = CharField('レース１＿４', blank=True, null=True, max_length=1)
    race_2_4 = CharField('レース２＿４', blank=True, null=True, max_length=1)
    race_3_4 = CharField('レース３＿４', blank=True, null=True, max_length=1)
    race_4_4 = CharField('レース４＿４', blank=True, null=True, max_length=1)
    race_5_4 = CharField('レース５＿４', blank=True, null=True, max_length=1)
    race_6_4 = CharField('レース６＿４', blank=True, null=True, max_length=1)
    race_7_4 = CharField('レース７＿４', blank=True, null=True, max_length=1)
    race_8_4 = CharField('レース８＿４', blank=True, null=True, max_length=1)
    race_9_4 = CharField('レース９＿４', blank=True, null=True, max_length=1)
    race_10_4 = CharField('レース１０＿４', blank=True, null=True, max_length=1)
    race_11_4 = CharField('レース１１＿４', blank=True, null=True, max_length=1)
    race_12_4 = CharField('レース１２＿４', blank=True, null=True, max_length=1)

    OTB_code_5 = CharField('売場コード＿５', blank=True, null=True, max_length=1)
    OTB_5 = CharField('売場名＿５', blank=True, null=True, max_length=6)
    OTB_Classification_5 = CharField('売場区分＿５', blank=True, null=True, max_length=1)
    Held_Classification_5 = CharField('開催区分＿５', blank=True, null=True, max_length=1)
    Note_code_5 = CharField('注釈コード＿５', blank=True, null=True, max_length=2)
    race_1_5 = CharField('レース１＿５', blank=True, null=True, max_length=1)
    race_2_5 = CharField('レース２＿５', blank=True, null=True, max_length=1)
    race_3_5 = CharField('レース３＿５', blank=True, null=True, max_length=1)
    race_4_5 = CharField('レース４＿５', blank=True, null=True, max_length=1)
    race_5_5 = CharField('レース５＿５', blank=True, null=True, max_length=1)
    race_6_5 = CharField('レース６＿５', blank=True, null=True, max_length=1)
    race_7_5 = CharField('レース７＿５', blank=True, null=True, max_length=1)
    race_8_5 = CharField('レース８＿５', blank=True, null=True, max_length=1)
    race_9_5 = CharField('レース９＿５', blank=True, null=True, max_length=1)
    race_10_5 = CharField('レース１０＿５', blank=True, null=True, max_length=1)
    race_11_5 = CharField('レース１１＿５', blank=True, null=True, max_length=1)
    race_12_5 = CharField('レース１２＿５', blank=True, null=True, max_length=1)

    OTB_code_6 = CharField('売場コード＿６', blank=True, null=True, max_length=1)
    OTB_6 = CharField('売場名＿６', blank=True, null=True, max_length=6)
    OTB_Classification_6 = CharField('売場区分＿６', blank=True, null=True, max_length=1)
    Held_Classification_6 = CharField('開催区分＿６', blank=True, null=True, max_length=1)
    Note_code_6 = CharField('注釈コード＿６', blank=True, null=True, max_length=2)
    race_1_6 = CharField('レース１＿６', blank=True, null=True, max_length=1)
    race_2_6 = CharField('レース２＿６', blank=True, null=True, max_length=1)
    race_3_6 = CharField('レース３＿６', blank=True, null=True, max_length=1)
    race_4_6 = CharField('レース４＿６', blank=True, null=True, max_length=1)
    race_5_6 = CharField('レース５＿６', blank=True, null=True, max_length=1)
    race_6_6 = CharField('レース６＿６', blank=True, null=True, max_length=1)
    race_7_6 = CharField('レース７＿６', blank=True, null=True, max_length=1)
    race_8_6 = CharField('レース８＿６', blank=True, null=True, max_length=1)
    race_9_6 = CharField('レース９＿６', blank=True, null=True, max_length=1)
    race_10_6 = CharField('レース１０＿６', blank=True, null=True, max_length=1)
    race_11_6 = CharField('レース１１＿６', blank=True, null=True, max_length=1)
    race_12_6 = CharField('レース１２＿６', blank=True, null=True, max_length=1)

    OTB_code_7 = CharField('売場コード＿７', blank=True, null=True, max_length=1)
    OTB_7 = CharField('売場名＿７', blank=True, null=True, max_length=6)
    OTB_Classification_7 = CharField('売場区分＿７', blank=True, null=True, max_length=1)
    Held_Classification_7 = CharField('開催区分＿７', blank=True, null=True, max_length=1)
    Note_code_7 = CharField('注釈コード＿７', blank=True, null=True, max_length=2)
    race_1_7 = CharField('レース１＿７', blank=True, null=True, max_length=1)
    race_2_7 = CharField('レース２＿７', blank=True, null=True, max_length=1)
    race_3_7 = CharField('レース３＿７', blank=True, null=True, max_length=1)
    race_4_7 = CharField('レース４＿７', blank=True, null=True, max_length=1)
    race_5_7 = CharField('レース５＿７', blank=True, null=True, max_length=1)
    race_6_7 = CharField('レース６＿７', blank=True, null=True, max_length=1)
    race_7_7 = CharField('レース７＿７', blank=True, null=True, max_length=1)
    race_8_7 = CharField('レース８＿７', blank=True, null=True, max_length=1)
    race_9_7 = CharField('レース９＿７', blank=True, null=True, max_length=1)
    race_10_7 = CharField('レース１０＿７', blank=True, null=True, max_length=1)
    race_11_7 = CharField('レース１１＿７', blank=True, null=True, max_length=1)
    race_12_7 = CharField('レース１２＿７', blank=True, null=True, max_length=1)

    OTB_code_8 = CharField('売場コード＿８', blank=True, null=True, max_length=1)
    OTB_8 = CharField('売場名＿８', blank=True, null=True, max_length=6)
    OTB_Classification_8 = CharField('売場区分＿８', blank=True, null=True, max_length=1)
    Held_Classification_8 = CharField('開催区分＿８', blank=True, null=True, max_length=1)
    Note_code_8 = CharField('注釈コード＿８', blank=True, null=True, max_length=2)
    race_1_8 = CharField('レース１＿８', blank=True, null=True, max_length=1)
    race_2_8 = CharField('レース２＿８', blank=True, null=True, max_length=1)
    race_3_8 = CharField('レース３＿８', blank=True, null=True, max_length=1)
    race_4_8 = CharField('レース４＿８', blank=True, null=True, max_length=1)
    race_5_8 = CharField('レース５＿８', blank=True, null=True, max_length=1)
    race_6_8 = CharField('レース６＿８', blank=True, null=True, max_length=1)
    race_7_8 = CharField('レース７＿８', blank=True, null=True, max_length=1)
    race_8_8 = CharField('レース８＿８', blank=True, null=True, max_length=1)
    race_9_8 = CharField('レース９＿８', blank=True, null=True, max_length=1)
    race_10_8 = CharField('レース１０＿８', blank=True, null=True, max_length=1)
    race_11_8 = CharField('レース１１＿８', blank=True, null=True, max_length=1)
    race_12_8 = CharField('レース１２＿８', blank=True, null=True, max_length=1)

    OTB_code_9 = CharField('売場コード＿９', blank=True, null=True, max_length=1)
    OTB_9 = CharField('売場名＿９', blank=True, null=True, max_length=6)
    OTB_Classification_9 = CharField('売場区分＿９', blank=True, null=True, max_length=1)
    Held_Classification_9 = CharField('開催区分＿９', blank=True, null=True, max_length=1)
    Note_code_9 = CharField('注釈コード＿９', blank=True, null=True, max_length=2)
    race_1_9 = CharField('レース１＿９', blank=True, null=True, max_length=1)
    race_2_9 = CharField('レース２＿９', blank=True, null=True, max_length=1)
    race_3_9 = CharField('レース３＿９', blank=True, null=True, max_length=1)
    race_4_9 = CharField('レース４＿９', blank=True, null=True, max_length=1)
    race_5_9 = CharField('レース５＿９', blank=True, null=True, max_length=1)
    race_6_9 = CharField('レース６＿９', blank=True, null=True, max_length=1)
    race_7_9 = CharField('レース７＿９', blank=True, null=True, max_length=1)
    race_8_9 = CharField('レース８＿９', blank=True, null=True, max_length=1)
    race_9_9 = CharField('レース９＿９', blank=True, null=True, max_length=1)
    race_10_9 = CharField('レース１０＿９', blank=True, null=True, max_length=1)
    race_11_9 = CharField('レース１１＿９', blank=True, null=True, max_length=1)
    race_12_9 = CharField('レース１２＿９', blank=True, null=True, max_length=1)

    OTB_code_10 = CharField('売場コード＿１０', blank=True, null=True, max_length=1)
    OTB_10 = CharField('売場名＿１０', blank=True, null=True, max_length=6)
    OTB_Classification_10 = CharField('売場区分＿１０', blank=True, null=True, max_length=1)
    Held_Classification_10 = CharField('開催区分＿１０', blank=True, null=True, max_length=1)
    Note_code_10 = CharField('注釈コード＿１０', blank=True, null=True, max_length=2)
    race_1_10 = CharField('レース１＿１０', blank=True, null=True, max_length=1)
    race_2_10 = CharField('レース２＿１０', blank=True, null=True, max_length=1)
    race_3_10 = CharField('レース３＿１０', blank=True, null=True, max_length=1)
    race_4_10 = CharField('レース４＿１０', blank=True, null=True, max_length=1)
    race_5_10 = CharField('レース５＿１０', blank=True, null=True, max_length=1)
    race_6_10 = CharField('レース６＿１０', blank=True, null=True, max_length=1)
    race_7_10 = CharField('レース７＿１０', blank=True, null=True, max_length=1)
    race_8_10 = CharField('レース８＿１０', blank=True, null=True, max_length=1)
    race_9_10 = CharField('レース９＿１０', blank=True, null=True, max_length=1)
    race_10_10 = CharField('レース１０＿１０', blank=True, null=True, max_length=1)
    race_11_10 = CharField('レース１１＿１０', blank=True, null=True, max_length=1)
    race_12_10 = CharField('レース１２＿１０', blank=True, null=True, max_length=1)

    OTB_code_11 = CharField('売場コード＿１１', blank=True, null=True, max_length=1)
    OTB_11 = CharField('売場名＿１１', blank=True, null=True, max_length=6)
    OTB_Classification_11 = CharField('売場区分＿１１', blank=True, null=True, max_length=1)
    Held_Classification_11 = CharField('開催区分＿１１', blank=True, null=True, max_length=1)
    Note_code_11 = CharField('注釈コード＿１１', blank=True, null=True, max_length=2)
    race_1_11 = CharField('レース１＿１１', blank=True, null=True, max_length=1)
    race_2_11 = CharField('レース２＿１１', blank=True, null=True, max_length=1)
    race_3_11 = CharField('レース３＿１１', blank=True, null=True, max_length=1)
    race_4_11 = CharField('レース４＿１１', blank=True, null=True, max_length=1)
    race_5_11 = CharField('レース５＿１１', blank=True, null=True, max_length=1)
    race_6_11 = CharField('レース６＿１１', blank=True, null=True, max_length=1)
    race_7_11 = CharField('レース７＿１１', blank=True, null=True, max_length=1)
    race_8_11 = CharField('レース８＿１１', blank=True, null=True, max_length=1)
    race_9_11 = CharField('レース９＿１１', blank=True, null=True, max_length=1)
    race_10_11 = CharField('レース１０＿１１', blank=True, null=True, max_length=1)
    race_11_11 = CharField('レース１１＿１１', blank=True, null=True, max_length=1)
    race_12_11 = CharField('レース１２＿１１', blank=True, null=True, max_length=1)

    OTB_code_12 = CharField('売場コード＿１２', blank=True, null=True, max_length=1)
    OTB_12 = CharField('売場名＿１２', blank=True, null=True, max_length=6)
    OTB_Classification_12 = CharField('売場区分＿１２', blank=True, null=True, max_length=1)
    Held_Classification_12 = CharField('開催区分＿１２', blank=True, null=True, max_length=1)
    Note_code_12 = CharField('注釈コード＿１２', blank=True, null=True, max_length=2)
    race_1_12 = CharField('レース１＿１２', blank=True, null=True, max_length=1)
    race_2_12 = CharField('レース２＿１２', blank=True, null=True, max_length=1)
    race_3_12 = CharField('レース３＿１２', blank=True, null=True, max_length=1)
    race_4_12 = CharField('レース４＿１２', blank=True, null=True, max_length=1)
    race_5_12 = CharField('レース５＿１２', blank=True, null=True, max_length=1)
    race_6_12 = CharField('レース６＿１２', blank=True, null=True, max_length=1)
    race_7_12 = CharField('レース７＿１２', blank=True, null=True, max_length=1)
    race_8_12 = CharField('レース８＿１２', blank=True, null=True, max_length=1)
    race_9_12 = CharField('レース９＿１２', blank=True, null=True, max_length=1)
    race_10_12 = CharField('レース１０＿１２', blank=True, null=True, max_length=1)
    race_11_12 = CharField('レース１１＿１２', blank=True, null=True, max_length=1)
    race_12_12 = CharField('レース１２＿１２', blank=True, null=True, max_length=1)

    OTB_code_13 = CharField('売場コード＿１３', blank=True, null=True, max_length=1)
    OTB_13 = CharField('売場名＿１３', blank=True, null=True, max_length=6)
    OTB_Classification_13 = CharField('売場区分＿１３', blank=True, null=True, max_length=1)
    Held_Classification_13 = CharField('開催区分＿１３', blank=True, null=True, max_length=1)
    Note_code_13 = CharField('注釈コード＿１３', blank=True, null=True, max_length=2)
    race_1_13 = CharField('レース１＿１３', blank=True, null=True, max_length=1)
    race_2_13 = CharField('レース２＿１３', blank=True, null=True, max_length=1)
    race_3_13 = CharField('レース３＿１３', blank=True, null=True, max_length=1)
    race_4_13 = CharField('レース４＿１３', blank=True, null=True, max_length=1)
    race_5_13 = CharField('レース５＿１３', blank=True, null=True, max_length=1)
    race_6_13 = CharField('レース６＿１３', blank=True, null=True, max_length=1)
    race_7_13 = CharField('レース７＿１３', blank=True, null=True, max_length=1)
    race_8_13 = CharField('レース８＿１３', blank=True, null=True, max_length=1)
    race_9_13 = CharField('レース９＿１３', blank=True, null=True, max_length=1)
    race_10_13 = CharField('レース１０＿１３', blank=True, null=True, max_length=1)
    race_11_13 = CharField('レース１１＿１３', blank=True, null=True, max_length=1)
    race_12_13 = CharField('レース１２＿１３', blank=True, null=True, max_length=1)

    OTB_code_14 = CharField('売場コード＿１４', blank=True, null=True, max_length=1)
    OTB_14 = CharField('売場名＿１４', blank=True, null=True, max_length=6)
    OTB_Classification_14 = CharField('売場区分＿１４', blank=True, null=True, max_length=1)
    Held_Classification_14 = CharField('開催区分＿１４', blank=True, null=True, max_length=1)
    Note_code_14 = CharField('注釈コード＿１４', blank=True, null=True, max_length=2)
    race_1_14 = CharField('レース１＿１４', blank=True, null=True, max_length=1)
    race_2_14 = CharField('レース２＿１４', blank=True, null=True, max_length=1)
    race_3_14 = CharField('レース３＿１４', blank=True, null=True, max_length=1)
    race_4_14 = CharField('レース４＿１４', blank=True, null=True, max_length=1)
    race_5_14 = CharField('レース５＿１４', blank=True, null=True, max_length=1)
    race_6_14 = CharField('レース６＿１４', blank=True, null=True, max_length=1)
    race_7_14 = CharField('レース７＿１４', blank=True, null=True, max_length=1)
    race_8_14 = CharField('レース８＿１４', blank=True, null=True, max_length=1)
    race_9_14 = CharField('レース９＿１４', blank=True, null=True, max_length=1)
    race_10_14 = CharField('レース１０＿１４', blank=True, null=True, max_length=1)
    race_11_14 = CharField('レース１１＿１４', blank=True, null=True, max_length=1)
    race_12_14 = CharField('レース１２＿１４', blank=True, null=True, max_length=1)

    OTB_code_15 = CharField('売場コード＿１５', blank=True, null=True, max_length=1)
    OTB_15 = CharField('売場名＿１５', blank=True, null=True, max_length=6)
    OTB_Classification_15 = CharField('売場区分＿１５', blank=True, null=True, max_length=1)
    Held_Classification_15 = CharField('開催区分＿１５', blank=True, null=True, max_length=1)
    Note_code_15 = CharField('注釈コード＿１５', blank=True, null=True, max_length=2)
    race_1_15 = CharField('レース１＿１５', blank=True, null=True, max_length=1)
    race_2_15 = CharField('レース２＿１５', blank=True, null=True, max_length=1)
    race_3_15 = CharField('レース３＿１５', blank=True, null=True, max_length=1)
    race_4_15 = CharField('レース４＿１５', blank=True, null=True, max_length=1)
    race_5_15 = CharField('レース５＿１５', blank=True, null=True, max_length=1)
    race_6_15 = CharField('レース６＿１５', blank=True, null=True, max_length=1)
    race_7_15 = CharField('レース７＿１５', blank=True, null=True, max_length=1)
    race_8_15 = CharField('レース８＿１５', blank=True, null=True, max_length=1)
    race_9_15 = CharField('レース９＿１５', blank=True, null=True, max_length=1)
    race_10_15 = CharField('レース１０＿１５', blank=True, null=True, max_length=1)
    race_11_15 = CharField('レース１１＿１５', blank=True, null=True, max_length=1)
    race_12_15 = CharField('レース１２＿１５', blank=True, null=True, max_length=1)

    OTB_code_16 = CharField('売場コード＿１６', blank=True, null=True, max_length=1)
    OTB_16 = CharField('売場名＿１６', blank=True, null=True, max_length=6)
    OTB_Classification_16 = CharField('売場区分＿１６', blank=True, null=True, max_length=1)
    Held_Classification_16 = CharField('開催区分＿１６', blank=True, null=True, max_length=1)
    Note_code_16 = CharField('注釈コード＿１６', blank=True, null=True, max_length=2)
    race_1_16 = CharField('レース１＿１６', blank=True, null=True, max_length=1)
    race_2_16 = CharField('レース２＿１６', blank=True, null=True, max_length=1)
    race_3_16 = CharField('レース３＿１６', blank=True, null=True, max_length=1)
    race_4_16 = CharField('レース４＿１６', blank=True, null=True, max_length=1)
    race_5_16 = CharField('レース５＿１６', blank=True, null=True, max_length=1)
    race_6_16 = CharField('レース６＿１６', blank=True, null=True, max_length=1)
    race_7_16 = CharField('レース７＿１６', blank=True, null=True, max_length=1)
    race_8_16 = CharField('レース８＿１６', blank=True, null=True, max_length=1)
    race_9_16 = CharField('レース９＿１６', blank=True, null=True, max_length=1)
    race_10_16 = CharField('レース１０＿１６', blank=True, null=True, max_length=1)
    race_11_16 = CharField('レース１１＿１６', blank=True, null=True, max_length=1)
    race_12_16 = CharField('レース１２＿１６', blank=True, null=True, max_length=1)

    OTB_code_17 = CharField('売場コード＿１７', blank=True, null=True, max_length=1)
    OTB_17 = CharField('売場名＿１７', blank=True, null=True, max_length=6)
    OTB_Classification_17 = CharField('売場区分＿１７', blank=True, null=True, max_length=1)
    Held_Classification_17 = CharField('開催区分＿１７', blank=True, null=True, max_length=1)
    Note_code_17 = CharField('注釈コード＿１７', blank=True, null=True, max_length=2)
    race_1_17 = CharField('レース１＿１７', blank=True, null=True, max_length=1)
    race_2_17 = CharField('レース２＿１７', blank=True, null=True, max_length=1)
    race_3_17 = CharField('レース３＿１７', blank=True, null=True, max_length=1)
    race_4_17 = CharField('レース４＿１７', blank=True, null=True, max_length=1)
    race_5_17 = CharField('レース５＿１７', blank=True, null=True, max_length=1)
    race_6_17 = CharField('レース６＿１７', blank=True, null=True, max_length=1)
    race_7_17 = CharField('レース７＿１７', blank=True, null=True, max_length=1)
    race_8_17 = CharField('レース８＿１７', blank=True, null=True, max_length=1)
    race_9_17 = CharField('レース９＿１７', blank=True, null=True, max_length=1)
    race_10_17 = CharField('レース１０＿１７', blank=True, null=True, max_length=1)
    race_11_17 = CharField('レース１１＿１７', blank=True, null=True, max_length=1)
    race_12_17 = CharField('レース１２＿１７', blank=True, null=True, max_length=1)

    OTB_code_18 = CharField('売場コード＿１８', blank=True, null=True, max_length=1)
    OTB_18 = CharField('売場名＿１８', blank=True, null=True, max_length=6)
    OTB_Classification_18 = CharField('売場区分＿１８', blank=True, null=True, max_length=1)
    Held_Classification_18 = CharField('開催区分＿１８', blank=True, null=True, max_length=1)
    Note_code_18 = CharField('注釈コード＿１８', blank=True, null=True, max_length=2)
    race_1_18 = CharField('レース１＿１８', blank=True, null=True, max_length=1)
    race_2_18 = CharField('レース２＿１８', blank=True, null=True, max_length=1)
    race_3_18 = CharField('レース３＿１８', blank=True, null=True, max_length=1)
    race_4_18 = CharField('レース４＿１８', blank=True, null=True, max_length=1)
    race_5_18 = CharField('レース５＿１８', blank=True, null=True, max_length=1)
    race_6_18 = CharField('レース６＿１８', blank=True, null=True, max_length=1)
    race_7_18 = CharField('レース７＿１８', blank=True, null=True, max_length=1)
    race_8_18 = CharField('レース８＿１８', blank=True, null=True, max_length=1)
    race_9_18 = CharField('レース９＿１８', blank=True, null=True, max_length=1)
    race_10_18 = CharField('レース１０＿１８', blank=True, null=True, max_length=1)
    race_11_18 = CharField('レース１１＿１８', blank=True, null=True, max_length=1)
    race_12_18 = CharField('レース１２＿１８', blank=True, null=True, max_length=1)

    OTB_code_19 = CharField('売場コード＿１９', blank=True, null=True, max_length=1)
    OTB_19 = CharField('売場名＿１９', blank=True, null=True, max_length=6)
    OTB_Classification_19 = CharField('売場区分＿１９', blank=True, null=True, max_length=1)
    Held_Classification_19 = CharField('開催区分＿１９', blank=True, null=True, max_length=1)
    Note_code_19 = CharField('注釈コード＿１９', blank=True, null=True, max_length=2)
    race_1_19 = CharField('レース１＿１９', blank=True, null=True, max_length=1)
    race_2_19 = CharField('レース２＿１９', blank=True, null=True, max_length=1)
    race_3_19 = CharField('レース３＿１９', blank=True, null=True, max_length=1)
    race_4_19 = CharField('レース４＿１９', blank=True, null=True, max_length=1)
    race_5_19 = CharField('レース５＿１９', blank=True, null=True, max_length=1)
    race_6_19 = CharField('レース６＿１９', blank=True, null=True, max_length=1)
    race_7_19 = CharField('レース７＿１９', blank=True, null=True, max_length=1)
    race_8_19 = CharField('レース８＿１９', blank=True, null=True, max_length=1)
    race_9_19 = CharField('レース９＿１９', blank=True, null=True, max_length=1)
    race_10_19 = CharField('レース１０＿１９', blank=True, null=True, max_length=1)
    race_11_19 = CharField('レース１１＿１９', blank=True, null=True, max_length=1)
    race_12_19 = CharField('レース１２＿１９', blank=True, null=True, max_length=1)

    OTB_code_20 = CharField('売場コード＿２０', blank=True, null=True, max_length=1)
    OTB_20 = CharField('売場名＿２０', blank=True, null=True, max_length=6)
    OTB_Classification_20 = CharField('売場区分＿２０', blank=True, null=True, max_length=1)
    Held_Classification_20 = CharField('開催区分＿２０', blank=True, null=True, max_length=1)
    Note_code_20 = CharField('注釈コード＿２０', blank=True, null=True, max_length=2)
    race_1_20 = CharField('レース１＿２０', blank=True, null=True, max_length=1)
    race_2_20 = CharField('レース２＿２０', blank=True, null=True, max_length=1)
    race_3_20 = CharField('レース３＿２０', blank=True, null=True, max_length=1)
    race_4_20 = CharField('レース４＿２０', blank=True, null=True, max_length=1)
    race_5_20 = CharField('レース５＿２０', blank=True, null=True, max_length=1)
    race_6_20 = CharField('レース６＿２０', blank=True, null=True, max_length=1)
    race_7_20 = CharField('レース７＿２０', blank=True, null=True, max_length=1)
    race_8_20 = CharField('レース８＿２０', blank=True, null=True, max_length=1)
    race_9_20 = CharField('レース９＿２０', blank=True, null=True, max_length=1)
    race_10_20 = CharField('レース１０＿２０', blank=True, null=True, max_length=1)
    race_11_20 = CharField('レース１１＿２０', blank=True, null=True, max_length=1)
    race_12_20 = CharField('レース１２＿２０', blank=True, null=True, max_length=1)

    class Meta:
        verbose_name_plural = '【固定長】場外売場情報'

#選手取得賞金上位３０位レコード
class Trn_Top_30_Prize(Model):
    Cllasification = CharField('区分', blank=True, null=True, max_length=1)
    Data_type = CharField('データ種別', blank=True, null=True ,max_length=1)
    Send_date = CharField('送信日', blank=True, null=True, max_length=8)
    Totaling_date = CharField('集計日', blank=True, null=True, max_length=8)
    Ranking = CharField('順位', blank=True, null=True, max_length=2)
    Rider_code = CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_code = CharField('ＬＧコード', blank=True, null=True, max_length=1)
    LG_name = CharField('ＬＧ名', blank=True, null=True, max_length=6)
    Rider_class_code = CharField('選手級別', blank=True, null=True, max_length=1)
    By_period = CharField('期別', blank=True, null=True, max_length=2)
    Rider_birthplace = CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = CharField('年齢', blank=True, null=True, max_length=2)
    Prize = CharField('取得賞金', blank=True, null=True, max_length=12)

    class Meta:
        verbose_name_plural = '【固定長】選手取得賞金上位３０位レコード'

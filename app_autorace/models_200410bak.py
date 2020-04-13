from django.db import models
from django.utils import timezone

#---------DBマスターテーブル---------

#場名マスタ
class Mst_Race_track(models.Model):
    Track_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Track_name = models.CharField('正式名', blank=True, null=True, max_length=10)
    shortened_3 = models.CharField('３字', blank=True, null=True, max_length=6)
    shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '場名マスタ'

    def __str__(self):
        return self.Track_name

#記念マスタ
class Mst_Commemorative_Race(models.Model):
    Commemorative_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Commemorative_name = models.CharField('正式名', blank=True, null=True, max_length=40)
    shortened_2 = models.CharField('２字', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '記念マスタ'

    def __str__(self):
        return self.Commemorative_name

#特別記念マスタ
class Mst_Special_Commemorative_Race(models.Model):
    Special_commemorative_code = models.CharField('コード', blank=True, null=True, max_length=2)
    Special_commemorative_name = models.CharField('正式名', blank=True, null=True, max_length=60)
    Appear_index = models.CharField('表示順', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '特別記念マスタ'

    def __str__(self):
        return self.Special_commemorative_name

#種類マスタ
class Mst_Handicap_Open(models.Model):
    Handicap_Open_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Handicap_Open_name = models.CharField('正式名', blank=True, null=True, max_length=20)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '種類マスタ'

    def __str__(self):
        return self.Handicap_Open_name

#級マスタ
class Mst_Player_class(models.Model):
    Rider_class_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Rider_class_name = models.CharField('正式名', blank=True, null=True, max_length=6)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '級マスタ'

    def __str__(self):
        return self.Rider_class_name

#車級マスタ
class Mst_Auto_class(models.Model):
    Race_car_classification_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Race_car_classification_name = models.CharField('正式名', blank=True, null=True, max_length=10)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '車級マスタ'

    def __str__(self):
        return self.Race_car_classification_name

#異常区分マスタ
class Mst_Accident_type(models.Model):
    Accident_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)
    Shortened_2 = models.CharField('２字', blank=True, null=True, max_length=4)
    Accident_name = models.CharField('正式名', blank=True, null=True, max_length=20)
    Appear_index = models.CharField('表示順', blank=True, null=True, max_length=4)

    class Meta:
        verbose_name_plural = '異常区分マスタ'

    def __str__(self):
        return self.Accident_name

#状況マスタ
class Mst_Race_status(models.Model):
    Race_situation_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Race_situation_name = models.CharField('正式名', blank=True, null=True, max_length=20)

    class Meta:
        verbose_name_plural = '状況マスタ'

    def __str__(self):
        return self.Race_situation_name

#異常発走マスタ
class Mst_Illegal_start(models.Model):
    Illegal_start_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Illegal_start_name = models.CharField('正式名', blank=True, null=True, max_length=20)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '異常発走マスタ'

    def __str__(self):
        return self.Illegal_start_name

#被妨害マスタ
class Mst_Disturbed(models.Model):
    Disturbed_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Disturbed_name = models.CharField('正式名', blank=True, null=True, max_length=60)

    class Meta:
        verbose_name_plural = '被妨害マスタ'

    def __str__(self):
        return self.Disturbed_name

#発売状況マスタ
class Mst_Release_status(models.Model):
    Release_status_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Release_status_name = models.CharField('正式名', blank=True, null=True, max_length=60)

    class Meta:
        verbose_name_plural = '発売状況マスタ'

    def __str__(self):
        return self.Release_status_name

#返還理由マスタ
class Mst_Putout_Reason(models.Model):
    Put_out_Reason_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '返還理由マスタ'

    def __str__(self):
        return self.Shortened_1

#売場名マスタ
class Mst_Outside_track(models.Model):
    Mst_Outside_track_code = models.CharField('コード', blank=True, null=True, max_length=1)
    Mst_Outside_track_name = models.CharField('正式名', blank=True, null=True, max_length=10)
    shortened_3 = models.CharField('３字', blank=True, null=True, max_length=6)
    shortened_1 = models.CharField('１字', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '売場名マスタ'

    def __str__(self):
        return self.Mst_Outside_track_name

#---------DBトランテーブル---------

#スケジュール
class Trn_Schedule(models.Model):
    Cllasification = models.CharField('区分', blank=True, null=True, max_length=1)
    Data_type = models.CharField('データ種別', blank=True, null=True ,max_length=1)
    Send_date = models.CharField('送信日', blank=True, null=True, max_length=1)
    Race_date_1 = models.CharField('競争年月日１', blank=True, null=True, max_length=8)
    Outside_1 = models.CharField('場外売場情報１', blank=True, null=True, max_length=1)
    Track_code1_1 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_1', blank=True, null=True, max_length=1)
    races_1_1 = models.IntegerField('レース数１＿１', blank=True, null=True)
    Track_code1_2 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_2', blank=True, null=True, max_length=1)
    races_1_2 = models.IntegerField('レース数１＿２', blank=True, null=True)
    Track_code1_3 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_3', blank=True, null=True, max_length=1)
    races_1_3 = models.IntegerField('レース数１＿３', blank=True, null=True)
    Track_code1_4 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_4', blank=True, null=True, max_length=1)
    races_1_4 = models.IntegerField('レース数１＿４', blank=True, null=True)
    Track_code1_5 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_5', blank=True, null=True, max_length=1)
    races_1_5 = models.IntegerField('レース数１＿５', blank=True, null=True)
    Track_code1_6 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack1_6', blank=True, null=True, max_length=1)
    races_1_6 = models.IntegerField('レース数１＿６', blank=True, null=True)
    Race_date_2 = models.CharField('競争年月日２', blank=True, null=True, max_length=8)
    Outside_2 = models.CharField('場外売場情報２', blank=True, null=True, max_length=1)
    Track_code2_1 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_1', blank=True, null=True, max_length=1)
    races_2_1 = models.IntegerField('レース数２＿１', blank=True, null=True)
    Track_code2_2 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_2', blank=True, null=True, max_length=1)
    races_2_2 = models.IntegerField('レース数２＿２', blank=True, null=True)
    Track_code2_3 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_3', blank=True, null=True, max_length=1)
    races_2_3 = models.IntegerField('レース数２＿３', blank=True, null=True)
    Track_code2_4 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_4', blank=True, null=True, max_length=1)
    races_2_4 = models.IntegerField('レース数２＿４', blank=True, null=True)
    Track_code2_5 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_5', blank=True, null=True, max_length=1)
    races_2_5 = models.IntegerField('レース数２＿５', blank=True, null=True)
    Track_code2_6 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack2_6', blank=True, null=True, max_length=1)
    races_2_6 = models.IntegerField('レース数２＿６', blank=True, null=True)
    Race_date_3 = models.CharField('競争年月日３', blank=True, null=True, max_length=8)
    Outside_3 = models.CharField('場外売場情報３', blank=True, null=True, max_length=1)
    Track_code3_1 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_1', blank=True, null=True, max_length=1)
    races_3_1 = models.IntegerField('レース数３＿１', blank=True, null=True)
    Track_code3_2 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_2', blank=True, null=True, max_length=1)
    races_3_2 = models.IntegerField('レース数３＿２', blank=True, null=True)
    Track_code3_3 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_3', blank=True, null=True, max_length=1)
    races_3_3 = models.IntegerField('レース数３＿３', blank=True, null=True)
    Track_code3_4 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_4', blank=True, null=True, max_length=1)
    races_3_4 = models.IntegerField('レース数３＿４', blank=True, null=True)
    Track_code3_5 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_5', blank=True, null=True, max_length=1)
    races_3_5 = models.IntegerField('レース数３＿５', blank=True, null=True)
    Track_code3_6 = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'TRack3_6', blank=True, null=True, max_length=1)
    races_3_6 = models.IntegerField('レース数３＿６', blank=True, null=True)
    Top_30_prizes = models.CharField('賞金上位３０傑', blank=True, null=True, max_length=1)

    class Meta:
        verbose_name_plural = 'スケジュール'

#番組編成データレコード
class Trn_Program(models.Model):
    Classification = models.CharField('区分', blank=True, null=True, max_length=1)
    Data_type = models.CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Date_AD = models.DateField('開催日（西暦）', blank=True, null=True, max_length=8)
    Date_Japanese_calendar = models.CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = models.CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = models.CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = models.CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = models.CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = models.ForeignKey('Mst_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Special_commemorative_code = models.ForeignKey('Mst_Special_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=2)
    Race_No = models.IntegerField('レース№', blank=True, null=True)
    Race_name = models.CharField('レース名称', blank=True, null=True, max_length=26)
    Race_distance = models.IntegerField('競走距離', blank=True, null=True)
    Scheduled_start_time = models.CharField('発送予定時刻', blank=True, null=True, max_length=5)
    Participation = models.IntegerField('車立て数', blank=True, null=True)
    Race_Prize_Amount = models.IntegerField('レース賞金額', blank=True, null=True)
    Handicap_Open_code = models.ForeignKey('Mst_Handicap_Open', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Voting_code = models.CharField('投票場コード', blank=True, null=True, max_length=2)
    Win_Ave_Totaling_Date = models.DateField('勝率集計日', blank=True, null=True, max_length=8)
    Totaling_date = models.DateField('通算成績集計日', blank=True, null=True, max_length=8)

    class Meta:
        verbose_name_plural = '番組編成データレコード'

#出走選手テーブル
class Trn_Running_list(models.Model):
    Track_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Date_AD = models.DateField('開催日（西暦）', blank=True, null=True, max_length=8)
    Race_No = models.IntegerField('レース№', blank=True, null=True)
    Bracket_No =  models.IntegerField('連勝番号', blank=True, null=True)
    Rider_No = models.IntegerField('車番', blank=True, null=True)
    Rider_code = models.CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = models.CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = models.CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = models.CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_name = models.CharField('ＬＧ名', blank=True, null=True, max_length=6)
    LG_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'LG_code_Running_list', blank=True, null=True, max_length=1)
    Nickname = models.CharField('呼名', blank=True, null=True, max_length=12)
    Rider_class_code = models.ForeignKey('Mst_Player_class', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Race_car_classification_code = models.ForeignKey('Mst_Auto_class', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Handicap = models.CharField('ハンデ', blank=True, null=True, max_length=3)
    Last_run_4 = models.CharField('直近前々々々走', blank=True, null=True, max_length=2)
    Last_run_3 = models.CharField('直近前々々走', blank=True, null=True, max_length=2)
    Last_run_2 = models.CharField('直近前々走', blank=True, null=True, max_length=2)
    Last_run_1 = models.CharField('直近前走', blank=True, null=True, max_length=2)
    Last_run_4_Track = models.CharField('直近前々々々走出走場', blank=True, null=True, max_length=1)
    Last_run_3_Track = models.CharField('直近前々々走出走場', blank=True, null=True, max_length=1)
    Last_run_2_Track = models.CharField('直近前々走出走場', blank=True, null=True, max_length=1)
    Last_run_1_Track = models.CharField('直近前走出走場', blank=True, null=True, max_length=1)
    Last_run_time = models.CharField('直近前走タイム', blank=True, null=True, max_length=4)
    Avg_time = models.CharField('平均タイム', blank=True, null=True, max_length=4)
    Highest_time = models.CharField('最高タイム', blank=True, null=True, max_length=4)
    Best_time_Track = models.CharField('最高タイム場所', blank=True, null=True, max_length=6)
    Rider_birthplace = models.CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = models.IntegerField('年齢', blank=True, null=True)
    By_period = models.CharField('期別', blank=True, null=True, max_length=2)
    Avg_win_1 = models.CharField('単勝率', blank=True, null=True, max_length=4)
    Avg_win_2 = models.CharField('連勝率', blank=True, null=True, max_length=4)
    Avg_win_3 = models.CharField('複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_goodrunway = models.CharField('良走路単勝率', blank=True, null=True, max_length=4)
    Avg_win_2_goodrunway = models.CharField('良走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_goodrunway = models.CharField('良走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_Wetrunway = models.CharField('雨走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_2_Wetrunway = models.CharField('雨走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_Wetrunway = models.CharField('雨走路複勝率', blank=True, null=True, max_length=4)
    Avg_win_1_ohter = models.CharField('その他走路単勝率', blank=True, null=True, max_length=4)
    Avg_win_2_ohter = models.CharField('その他走路連勝率', blank=True, null=True, max_length=4)
    Avg_win_3_ohter = models.CharField('その他走路複勝率', blank=True, null=True, max_length=4)
    Last_1_test_run_time = models.CharField('過去１走試走タイム', blank=True, null=True, max_length=4)
    Last_1_time = models.CharField('過去１走競走タイム', blank=True, null=True, max_length=4)
    Last_1_lap_time = models.CharField('過去１走周回タイム', blank=True, null=True, max_length=4)
    Last_1_run = models.CharField('過去１走着', blank=True, null=True, max_length=2)
    Last_1_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_1_Track', blank=True, null=True, max_length=1)
    Last_1_ST = models.CharField('過去１走ＳＴ', blank=True, null=True, max_length=2)
    Last_1_Handicap = models.CharField('過去１走ハンデ', blank=True, null=True, max_length=3)
    Last_1_track_condition = models.CharField('過去１走走路状況', blank=True, null=True, max_length=2)
    Last_2_test_run_time = models.CharField('過去２走試走タイム', blank=True, null=True, max_length=4)
    Last_2_time = models.CharField('過去２走競走タイム', blank=True, null=True, max_length=4)
    Last_2_lap_time = models.CharField('過去２走周回タイム', blank=True, null=True, max_length=4)
    Last_2_run = models.CharField('過去２走着', blank=True, null=True, max_length=2)
    Last_2_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_2_Track', blank=True, null=True, max_length=1)
    Last_2_ST = models.CharField('過去２走ＳＴ', blank=True, null=True, max_length=2)
    Last_2_Handicap = models.CharField('過去２走ハンデ', blank=True, null=True, max_length=3)
    Last_2_track_condition = models.CharField('過去２走走路状況', blank=True, null=True, max_length=2)
    Last_3_test_run_time = models.CharField('過去３走試走タイム', blank=True, null=True, max_length=4)
    Last_3_time = models.CharField('過去３走競走タイム', blank=True, null=True, max_length=4)
    Last_3_lap_time = models.CharField('過去３走周回タイム', blank=True, null=True, max_length=4)
    Last_3_run = models.CharField('過去３走着', blank=True, null=True, max_length=2)
    Last_3_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_3_Track', blank=True, null=True, max_length=1)
    Last_3_ST = models.CharField('過去３走ＳＴ', blank=True, null=True, max_length=2)
    Last_3_Handicap = models.CharField('過去３走ハンデ', blank=True, null=True, max_length=3)
    Last_3_track_condition = models.CharField('過去３走走路状況', blank=True, null=True, max_length=2)
    Last_4_test_run_time = models.CharField('過去４走試走タイム', blank=True, null=True, max_length=4)
    Last_4_time = models.CharField('過去４走競走タイム', blank=True, null=True, max_length=4)
    Last_4_lap_time = models.CharField('過去４走周回タイム', blank=True, null=True, max_length=4)
    Last_4_run = models.CharField('過去４走着', blank=True, null=True, max_length=2)
    Last_4_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_4_Track', blank=True, null=True, max_length=1)
    Last_4_ST = models.CharField('過去４走ＳＴ', blank=True, null=True, max_length=2)
    Last_4_Handicap = models.CharField('過去４走ハンデ', blank=True, null=True, max_length=3)
    Last_4_track_condition = models.CharField('過去４走走路状況', blank=True, null=True, max_length=2)
    Last_5_test_run_time = models.CharField('過去５走試走タイム', blank=True, null=True, max_length=4)
    Last_5_time = models.CharField('過去５走競走タイム', blank=True, null=True, max_length=4)
    Last_5_lap_time = models.CharField('過去５走周回タイム', blank=True, null=True, max_length=4)
    Last_5_run = models.CharField('過去５走着', blank=True, null=True, max_length=2)
    Last_5_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_5_Track', blank=True, null=True, max_length=1)
    Last_5_ST = models.CharField('過去５走ＳＴ', blank=True, null=True, max_length=2)
    Last_5_Handicap = models.CharField('過去５走ハンデ', blank=True, null=True, max_length=3)
    Last_5_track_condition = models.CharField('過去５走走路状況', blank=True, null=True, max_length=2)
    Last_6_test_run_time = models.CharField('過去６走試走タイム', blank=True, null=True, max_length=4)
    Last_6_time = models.CharField('過去６走競走タイム', blank=True, null=True, max_length=4)
    Last_6_lap_time = models.CharField('過去６走周回タイム', blank=True, null=True, max_length=4)
    Last_6_run = models.CharField('過去６走着', blank=True, null=True, max_length=2)
    Last_6_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_6_Track', blank=True, null=True, max_length=1)
    Last_6_ST = models.CharField('過去６走ＳＴ', blank=True, null=True, max_length=2)
    Last_6_Handicap = models.CharField('過去６走ハンデ', blank=True, null=True, max_length=3)
    Last_6_track_condition = models.CharField('過去６走走路状況', blank=True, null=True, max_length=2)
    Last_7_test_run_time = models.CharField('過去７走試走タイム', blank=True, null=True, max_length=4)
    Last_7_time = models.CharField('過去７走競走タイム', blank=True, null=True, max_length=4)
    Last_7_lap_time = models.CharField('過去７走周回タイム', blank=True, null=True, max_length=4)
    Last_7_run = models.CharField('過去７走着', blank=True, null=True, max_length=2)
    Last_7_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_7_Track', blank=True, null=True, max_length=1)
    Last_7_ST = models.CharField('過去７走ＳＴ', blank=True, null=True, max_length=2)
    Last_7_Handicap = models.CharField('過去７走ハンデ', blank=True, null=True, max_length=3)
    Last_7_track_condition = models.CharField('過去７走走路状況', blank=True, null=True, max_length=2)
    Last_8_test_run_time = models.CharField('過去８走試走タイム', blank=True, null=True, max_length=4)
    Last_8_time = models.CharField('過去８走競走タイム', blank=True, null=True, max_length=4)
    Last_8_lap_time = models.CharField('過去８走周回タイム', blank=True, null=True, max_length=4)
    Last_8_run = models.CharField('過去８走着', blank=True, null=True, max_length=2)
    Last_8_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_8_Track', blank=True, null=True, max_length=1)
    Last_8_ST = models.CharField('過去８走ＳＴ', blank=True, null=True, max_length=2)
    Last_8_Handicap = models.CharField('過去８走ハンデ', blank=True, null=True, max_length=3)
    Last_8_track_condition = models.CharField('過去８走走路状況', blank=True, null=True, max_length=2)
    Last_9_test_run_time = models.CharField('過去９走試走タイム', blank=True, null=True, max_length=4)
    Last_9_time = models.CharField('過去９走競走タイム', blank=True, null=True, max_length=4)
    Last_9_lap_time = models.CharField('過去９走周回タイム', blank=True, null=True, max_length=4)
    Last_9_run = models.CharField('過去９走着', blank=True, null=True, max_length=2)
    Last_9_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_9_Track', blank=True, null=True, max_length=1)
    Last_9_ST = models.CharField('過去９走ＳＴ', blank=True, null=True, max_length=2)
    Last_9_Handicap = models.CharField('過去９走ハンデ', blank=True, null=True, max_length=3)
    Last_9_track_condition = models.CharField('過去９走走路状況', blank=True, null=True, max_length=2)
    Last_10_test_run_time = models.CharField('過去１０走試走タイム', blank=True, null=True, max_length=4)
    Last_10_time = models.CharField('過去１０走競走タイム', blank=True, null=True, max_length=4)
    Last_10_lap_time = models.CharField('過去１０走周回タイム', blank=True, null=True, max_length=4)
    Last_10_run = models.CharField('過去１０走着', blank=True, null=True, max_length=2)
    Last_10_Track = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'Last_10_Track', blank=True, null=True, max_length=1)
    Last_10_ST = models.CharField('過去１０走ＳＴ', blank=True, null=True, max_length=2)
    Last_10_Handicap = models.CharField('過去１０走ハンデ', blank=True, null=True, max_length=3)
    Last_10_track_condition = models.CharField('過去１０走走路状況', blank=True, null=True, max_length=2)
    Total_V = models.IntegerField('通算Ｖ数', blank=True, null=True)
    Total_1st = models.IntegerField('１着回数', blank=True, null=True)
    Total_2nd = models.IntegerField('２着回数', blank=True, null=True)
    Total_3rd = models.IntegerField('３着回数', blank=True, null=True)
    Total_other = models.IntegerField('着外回数', blank=True, null=True)

    class Meta:
        verbose_name_plural = '出走選手テーブル'

#レース結果データレコード
class Trn_Result(models.Model):
    Classification = models.CharField('区分', blank=True, null=True, max_length=1)
    Data_type = models.CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Track_name = models.CharField('場名', blank=True, null=True ,max_length=6)
    Date_AD = models.DateField('開催日（西暦）', blank=True, null=True, max_length=8)
    Date_Japanese_calendar = models.CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = models.CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = models.CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = models.CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = models.CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = models.ForeignKey('Mst_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Special_commemorative_code = models.ForeignKey('Mst_Special_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=2)
    Net_sales_day = models.IntegerField('当日純売上金額', blank=True, null=True)
    Net_sales_period = models.IntegerField('当該節純売上金額', blank=True, null=True)
    Net_sales_held = models.IntegerField('当該回純売上金額', blank=True, null=True)
    visitors_day = models.IntegerField('当日入場者数', blank=True, null=True)
    visitors_period = models.IntegerField('当該節入場者数', blank=True, null=True)
    visitors_held = models.IntegerField('当該回入場者数', blank=True, null=True)
    Race_No = models.IntegerField('レース№', blank=True, null=True)
    Race_name = models.CharField('レース名称', blank=True, null=True, max_length=26)
    Race_distance = models.IntegerField('競走距離', blank=True, null=True)
    Participant_No = models.IntegerField('車立て数', blank=True, null=True)
    Race_Approved = models.CharField('不成立コード', blank=True, null=True, max_length=1)
    Race_postponed = models.ForeignKey('Mst_Race_status', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Handicap_Open = models.ForeignKey('Mst_Handicap_Open', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Race_Sales = models.IntegerField('当該レース売上金額', blank=True, null=True)
    Race_Pay_back = models.IntegerField('当該レース返還金額', blank=True, null=True)
    Win_prize = models.IntegerField('一着賞金', blank=True, null=True)
    Voting_code = models.CharField('投票場コード', blank=True, null=True, max_length=2)
    Exacta_No_1 = models.CharField('連単組番１', blank=True, null=True, max_length=3)
    Exacta_1 = models.IntegerField('連単払戻金額１', blank=True, null=True)
    Exacta_pick_1 = models.IntegerField('連単勝車人気１', blank=True, null=True)
    Exacta_No_2 = models.CharField('連単組番２', blank=True, null=True, max_length=3)
    Exacta_2 = models.IntegerField('連単払戻金額２', blank=True, null=True)
    Exacta_pick_2 = models.IntegerField('連単勝車人気２', blank=True, null=True)
    Quinella_No_1 = models.CharField('連複組番１', blank=True, null=True, max_length=3)
    Quinella_1 = models.IntegerField('連複払戻金額１', blank=True, null=True)
    Quinella_pick_1 = models.IntegerField('連複勝車人気１', blank=True, null=True)
    Quinella_No_2 = models.CharField('連複組番２', blank=True, null=True, max_length=3)
    Quinella_2 = models.IntegerField('連複払戻金額２', blank=True, null=True)
    Quinella_pick_2 = models.IntegerField('連複勝車人気２', blank=True, null=True)
    Betting_type_3 = models.CharField('賭式区分３', blank=True, null=True, max_length=1)
    Trifecta_On_sale = models.CharField('発売有無３', blank=True, null=True, max_length=1)
    Trifecta_approved = models.CharField('不成立３', blank=True, null=True, max_length=1)
    Trifecta_No_1 = models.CharField('組番３＿１', blank=True, null=True, max_length=5)
    Trifecta_1 = models.IntegerField('払戻金３＿１', blank=True, null=True)
    Trifecta_pick_1 = models.IntegerField('人気３＿１', blank=True, null=True)
    Trifecta_No_2 = models.CharField('組番３＿２', blank=True, null=True, max_length=5)
    Trifecta_2 = models.IntegerField('払戻金３＿２', blank=True, null=True)
    Trifecta_pick_2 = models.IntegerField('人気３＿２', blank=True, null=True)
    Trifecta_No_3 = models.CharField('組番３＿３', blank=True, null=True, max_length=5)
    Trifecta_3 = models.IntegerField('払戻金３＿３', blank=True, null=True)
    Trifecta_pick_3 = models.IntegerField('人気３＿３', blank=True, null=True)
    Betting_type_4 = models.CharField('賭式区分４', blank=True, null=True, max_length=1)
    Wide_On_sale = models.CharField('発売有無４', blank=True, null=True, max_length=1)
    Wide_approved = models.CharField('不成立４', blank=True, null=True, max_length=1)
    Wide_No_1 = models.CharField('組番４＿１', blank=True, null=True, max_length=3)
    Wide_1 = models.IntegerField('払戻金４＿１', blank=True, null=True)
    Wide_pick_1 = models.IntegerField('人気４＿１', blank=True, null=True)
    Wide_No_2 = models.CharField('組番４＿２', blank=True, null=True, max_length=3)
    Wide_2 = models.IntegerField('払戻金４＿２', blank=True, null=True)
    Wide_pick_2 = models.IntegerField('人気４＿２', blank=True, null=True)
    Wide_No_3 = models.CharField('組番４＿３', blank=True, null=True, max_length=3)
    Wide_3 = models.IntegerField('払戻金４＿３', blank=True, null=True)
    Wide_pick_3 = models.IntegerField('人気４＿３', blank=True, null=True)
    Wide_No_4 = models.CharField('組番４＿４', blank=True, null=True, max_length=3)
    Wide_4 = models.IntegerField('払戻金４＿４', blank=True, null=True)
    Wide_pick_4 = models.IntegerField('人気４＿４', blank=True, null=True)
    Wide_No_5 = models.CharField('組番４＿５', blank=True, null=True, max_length=3)
    Wide_5 = models.IntegerField('払戻金４＿５', blank=True, null=True)
    Wide_pick_5 = models.IntegerField('人気４＿５', blank=True, null=True)
    Betting_type_5 = models.CharField('賭式区分５', blank=True, null=True, max_length=1)
    Trio_On_sale = models.CharField('発売有無５', blank=True, null=True, max_length=1)
    Trio_approved = models.CharField('不成立５', blank=True, null=True, max_length=1)
    Trio_No_1 = models.CharField('組番５＿１', blank=True, null=True, max_length=5)
    Trio_1 = models.IntegerField('払戻金５＿１', blank=True, null=True)
    Trio_pick_1 = models.IntegerField('人気５＿１', blank=True, null=True)
    Trio_No_2 = models.CharField('組番５＿２', blank=True, null=True, max_length=5)
    Trio_2 = models.IntegerField('払戻金５＿２', blank=True, null=True)
    Trio_pick_2 = models.IntegerField('人気５＿２', blank=True, null=True)
    Trio_No_3 = models.CharField('組番５＿３', blank=True, null=True, max_length=5)
    Trio_3 = models.IntegerField('払戻金５＿３', blank=True, null=True)
    Trio_pick_3 = models.IntegerField('人気５＿３', blank=True, null=True)
    Trio_No_4 = models.CharField('組番５＿４', blank=True, null=True, max_length=5)
    Trio_4 = models.IntegerField('払戻金５＿４', blank=True, null=True)
    Trio_pick_4 = models.IntegerField('人気５＿４', blank=True, null=True)
    Put_out_rider_1 = models.CharField('返還選手名１', blank=True, null=True, max_length=6)
    Put_out_Reason_1 = models.CharField('返還理由１', blank=True, null=True, max_length=1)
    Put_out_rider_2 = models.CharField('返還選手名２', blank=True, null=True, max_length=6)
    Put_out_Reason_2 = models.CharField('返還理由２', blank=True, null=True, max_length=1)
    Put_out_rider_3 = models.CharField('返還選手名３', blank=True, null=True, max_length=6)
    Put_out_Reason_3 = models.CharField('返還理由３', blank=True, null=True, max_length=1)
    Put_out_rider_4 = models.CharField('返還選手名４', blank=True, null=True, max_length=6)
    Put_out_Reason_4 = models.CharField('返還理由４', blank=True, null=True, max_length=1)
    Put_out_rider_5 = models.CharField('返還選手名５', blank=True, null=True, max_length=6)
    Put_out_Reason_5 = models.CharField('返還理由５', blank=True, null=True, max_length=1)
    Runway_status_code = models.CharField('走路状況コード', blank=True, null=True, max_length=1)
    Track_conditions = models.CharField('走路状況', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = 'レース結果データレコード'

#選手成績テーブル
class Trn_Rider_results(models.Model):
    Track_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Date_AD = models.DateField('開催日（西暦）', blank=True, null=True, max_length=8)
    Race_No = models.IntegerField('レース№', blank=True, null=True)
    Bracket_No =  models.IntegerField('連勝番号', blank=True, null=True)
    Rider_No = models.IntegerField('車番', blank=True, null=True)
    Rider_code = models.CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = models.CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = models.CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = models.CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_name = models.CharField('ＬＧ名', blank=True, null=True, max_length=6)
    LG_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, related_name = 'LG_code_Rider_results', blank=True, null=True, max_length=1)
    Nickname = models.CharField('呼名', blank=True, null=True, max_length=12)
    Rider_birthplace = models.CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = models.IntegerField('年齢', blank=True, null=True)
    By_period = models.CharField('期別', blank=True, null=True, max_length=2)
    Handicap = models.CharField('ハンデ', blank=True, null=True, max_length=3)
    Result = models.CharField('着', blank=True, null=True, max_length=1)
    Accident_code = models.CharField('事故コード', blank=True, null=True, max_length=2)
    Accident_name = models.CharField('事故名称', blank=True, null=True, max_length=6)
    Illegal_start_code = models.CharField('異常発走コード', blank=True, null=True, max_length=1)
    Disturbed_code = models.CharField('被妨害コード', blank=True, null=True, max_length=1)
    Test_run_time = models.CharField('試走タイム', blank=True, null=True, max_length=4)
    Race_time = models.CharField('競走タイム', blank=True, null=True, max_length=4)
    Minute_second = models.CharField('分秒', blank=True, null=True, max_length=4)
    Start_timing = models.CharField('スタートタイミング', blank=True, null=True, max_length=2)

    class Meta:
        verbose_name_plural = '選手成績テーブル'

#場外売場情報
class Trn_Outside_track(models.Model):
    Cllasification = models.CharField('区分', blank=True, null=True, max_length=1)
    Data_type = models.CharField('データ種別', blank=True, null=True ,max_length=1)
    Track_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Track_name = models.CharField('場名', blank=True, null=True ,max_length=6)
    Date_AD = models.DateField('開催日（西暦）', blank=True, null=True, max_length=8)
    Date_Japanese_calendar = models.CharField('開催日（和暦）', blank=True, null=True, max_length=22)
    Held_day = models.CharField('開催回日目', blank=True, null=True, max_length=28)
    Period_days = models.CharField('節日数', blank=True, null=True, max_length=8)
    Event_name = models.CharField('開催名称', blank=True, null=True, max_length=40)
    First_day_of_the_event = models.CharField('開催初日', blank=True, null=True, max_length=8)
    Commemorative_code = models.ForeignKey('Mst_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Special_commemorative_code = models.ForeignKey('Mst_Special_Commemorative_Race', on_delete=models.CASCADE, blank=True, null=True, max_length=2)
    OTB_code = models.ForeignKey('Mst_Outside_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    OTB = models.CharField('売場名', blank=True, null=True, max_length=6)
    OTB_Classification = models.CharField('売場区分', blank=True, null=True, max_length=1)
    Held_Classification = models.CharField('開催区分', blank=True, null=True, max_length=1)
    Note_code = models.ForeignKey('Mst_Release_status', on_delete=models.CASCADE, blank=True, null=True, max_length=2)
    race_1 = models.CharField('レース１', blank=True, null=True, max_length=1)
    race_2 = models.CharField('レース２', blank=True, null=True, max_length=1)
    race_3 = models.CharField('レース３', blank=True, null=True, max_length=1)
    race_4 = models.CharField('レース４', blank=True, null=True, max_length=1)
    race_5 = models.CharField('レース５', blank=True, null=True, max_length=1)
    race_6 = models.CharField('レース６', blank=True, null=True, max_length=1)
    race_7 = models.CharField('レース７', blank=True, null=True, max_length=1)
    race_8 = models.CharField('レース８', blank=True, null=True, max_length=1)
    race_9 = models.CharField('レース９', blank=True, null=True, max_length=1)
    race_10 = models.CharField('レース１０', blank=True, null=True, max_length=1)
    race_11 = models.CharField('レース１１', blank=True, null=True, max_length=1)
    race_12 = models.CharField('レース１２', blank=True, null=True, max_length=1)

    class Meta:
        verbose_name_plural = '場外売場情報'

#選手取得賞金上位３０位レコード
class Trn_Top_30_Prize(models.Model):
    Cllasification = models.CharField('区分', blank=True, null=True, max_length=1)
    Data_type = models.CharField('データ種別', blank=True, null=True ,max_length=1)
    Send_date = models.CharField('送信日', blank=True, null=True, max_length=8)
    Totaling_date = models.CharField('集計日', blank=True, null=True, max_length=8)
    Ranking = models.CharField('順位', blank=True, null=True, max_length=2)
    Rider_code = models.CharField('選手コード', blank=True, null=True, max_length=4)
    Rider_full_name = models.CharField('選手名（フルネーム）', blank=True, null=True, max_length=16)
    Rider_shortened_3_name = models.CharField('選手名（短縮３文字）', blank=True, null=True, max_length=6)
    Rider_shortened_4_name = models.CharField('選手名（短縮４文字）', blank=True, null=True, max_length=8)
    LG_name = models.CharField('ＬＧ名', blank=True, null=True, max_length=6)
    LG_code = models.ForeignKey('Mst_Race_track', on_delete=models.CASCADE, blank=True, null=True, max_length=1)
    Rider_class_code = models.CharField('選手級別', blank=True, null=True, max_length=1)
    By_period = models.CharField('期別', blank=True, null=True, max_length=2)
    Rider_birthplace = models.CharField('選手出身地', blank=True, null=True, max_length=6)
    Rider_Age = models.IntegerField('年齢', blank=True, null=True)
    Prize = models.IntegerField('取得賞金', blank=True, null=True)

    class Meta:
        verbose_name_plural = '選手取得賞金上位３０位レコード'

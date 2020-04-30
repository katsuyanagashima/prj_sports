from django.db.models import *
from django.utils import timezone


# --------------------------------------------------------------------------------------------------
# システム状態
class Tran_Systemstatus(Model):
    Event_date = IntegerField(verbose_name='開催年月', blank=True, null=True)
    CurrentBasho = ForeignKey('Mst_Basho', on_delete=CASCADE)
    #SystemStatus =   CharField(verbose_name='運用モード表記', max_length=10, blank=True, null=True)
    SystemStatus = ForeignKey('Mst_Operationmode', on_delete=CASCADE, blank=True, null=True)
    TorikumiDate = ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name='torikumi')
    MatchDate = ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name='match')
    First_date = DateField(verbose_name='初日年月日')
    Banzuke_date = DateField(verbose_name='番付発表日')
    Age_calcu_reference_date = DateField(verbose_name='年齢算出基準日')

    class Meta:
        verbose_name_plural = '#システム状態'

    def __str__(self):
        return str(self.Event_date)

# --------------------------------------------------------------------------------------------------
# 01:新番付資料
class Tran_Banzuke_forecast(Model):
    Sys_status = ForeignKey('Tran_Systemstatus', on_delete=CASCADE)  # システム状態の開催年月
    Rikishi = ForeignKey('Mst_Rikishi', on_delete=CASCADE, related_name='rikishi')  # 力士マスタ
    #Join_code =  IntegerField(verbose_name='参加区分', blank=True, null=True)
    Class_code = ForeignKey('Mst_Class', on_delete=CASCADE)  # 階級マスタ
    #Eastwest_code =  ForeignKey('Mst_Eastwest', on_delete=CASCADE) #東西マスタ
    #Lifetime_chii = ForeignKey('Mst_Lifetime_statusinfo', on_delete=CASCADE, related_name='Lifetime_chii', blank=True, null=True)  # 生涯地位情報
    Banzuke_rank = IntegerField(verbose_name='番付順位', blank=True, null=True)
    #Haridashi =  IntegerField(verbose_name='張付区分', blank=True, null=True)
    Banzuke_no = IntegerField(verbose_name='番付通番', blank=True, null=True)
    #Lifetime_result = ForeignKey('Mst_Lifetime_result', on_delete=CASCADE, related_name='Lifetime_result', blank=True, null=True)  # 生涯成績マスタ
    #Lifetime_award = ForeignKey('Mst_Lifetime_award', on_delete=CASCADE, related_name='Lifetime_award', blank=True, null=True)  # 生涯受賞回数マスタ
    #Appear_code =  IntegerField(verbose_name='新再降区分', blank=True, null=True)
    #Demoted_rank =  IntegerField(verbose_name='昇降順位', blank=True, null=True)

    class Meta:
        verbose_name_plural = '*【NewsML】01:新番付資料'

    def __str__(self):
        return str(self.Rikishi)


# 02-05:番付
class Tran_Banzuke(Model):
    Sys_status = ForeignKey('Tran_Systemstatus', on_delete=CASCADE)  # システム状態の開催年月
    Rikishi = ForeignKey('Mst_Rikishi', on_delete=CASCADE)  # 力士マスタ
    Join_code = IntegerField(verbose_name='参加区分', blank=True, null=True)
    Class_code = ForeignKey('Mst_Class', on_delete=CASCADE)  # 階級マスタ
    Eastwest_code = ForeignKey('Mst_Eastwest', on_delete=CASCADE)  # 東西マスタ
    Lifetime_chii = ForeignKey('Mst_Lifetime_statusinfo', on_delete=CASCADE, related_name='Lifetime_chiis', blank=True, null=True)  # 生涯地位情報
    Banzuke_rank = IntegerField(verbose_name='番付順位', blank=True, null=True)
    Haridashi = IntegerField(verbose_name='張付区分', blank=True, null=True)
    Banzuke_no = IntegerField(verbose_name='番付通番', blank=True, null=True)
    Appear_code = IntegerField(verbose_name='新再降区分', blank=True, null=True)
    Lifetime_result = ForeignKey('Mst_Lifetime_result', on_delete=CASCADE, related_name='Lifetime_results', blank=True, null=True)  # 生涯成績マスタ
    Lifetime_award = ForeignKey('Mst_Lifetime_award', on_delete=CASCADE, related_name='Lifetime_awards', blank=True, null=True)  # 生涯受賞回数マスタ
    #Appear_code =  IntegerField(verbose_name='新再降区分', blank=True, null=True)　
    Demoted_rank = IntegerField(verbose_name='昇降順位', blank=True, null=True)

    class Meta:
        verbose_name_plural = '*【NewsML】02-05:番付'

    def __str__(self):
        return str(self.Rikishi)


# --------------------------------------------------------------------------------------------------
# 階級上位力士
# 場所切り替え時に（初日の前に）全レコードを削除する
#
class Tran_TopClassRikishi(Model):
    Class_code = ForeignKey('Mst_Class', verbose_name='階級', on_delete=CASCADE)  # 階級コード
    Yearmonth = IntegerField(verbose_name='開催年月西暦')  # ６桁数字
    Nichime_code = ForeignKey('Mst_Nichime', verbose_name='日目', on_delete=CASCADE)  # 日目コード
    LossCount = PositiveIntegerField(verbose_name='負け数', blank=True, null=True)
    WinCount = PositiveIntegerField(verbose_name='勝ち数', blank=True, null=True)

    class Meta:
        verbose_name_plural = '*階級上位力士'
        unique_together = ('Class_code', 'Nichime_code')

    def __str__(self):
        return str(self.Class_code)


# --------------------------------------------------------------------------------------------------
# 優勝・三賞入力
#
class Tran_YushoSansho(Model):
    Rikishi = ForeignKey('Mst_Rikishi', verbose_name='力士名', on_delete=PROTECT)
    Yearmonth = IntegerField(verbose_name='開催年月西暦')  # ６桁数字
    Nichime_code = ForeignKey('Mst_Nichime', verbose_name='日目', on_delete=CASCADE)
    Class_code = ForeignKey('Mst_Class', verbose_name='階級', on_delete=CASCADE)
    Yusho_flg = BooleanField(verbose_name='優勝区分', blank=False, null=False, default=False)
    Shukunsho_flg = BooleanField(verbose_name='殊勲賞区分', blank=False, null=False, default=False)
    Kantosho_flg = BooleanField(verbose_name='敢闘賞区分', blank=False, null=False, default=False)
    Ginosho_flg = BooleanField(verbose_name='技能賞区分', blank=False, null=False, default=False)
    # 過去の優勝・三賞力士を保存する必要がある？
    #  保存する場合は、入力された日目を残す？

    class Meta:
        verbose_name_plural = '*優勝・三賞入力'
        unique_together = ('Rikishi', 'Yearmonth', 'Nichime_code', 'Class_code')

    def __str__(self):
        return str(self.Rikishi)

# --------------------------------------------------------------------------------------------------
# NewsMLステータス
#
class Tran_NewsMLStatus(Model):
    content_id =  CharField(verbose_name='製品ID', max_length=23, blank=True, null=True)
    status = IntegerField(verbose_name='状態', blank=True, null=True) 
    revised = IntegerField(verbose_name='修正回数', blank=True, null=True) 
    delivery_flag = BooleanField(verbose_name='配信済フラグ', blank=True, null=True) 
    premiss_date = DateField(verbose_name='運用日付', blank=True, null=True) 
    create_date = DateTimeField(verbose_name='レコード作成日時', auto_now_add=True, blank=True, null=True)
    update_date = DateTimeField(verbose_name='レコード更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'NewsMLステータス'
    
        def __str__(self):
            return str(self.content_id)

# --------------------------------------------------------------------------------------------------
# MQシーケンス
#
class Tran_MQ_sequense(Model):
    sequense =  IntegerField(verbose_name='シーケンス番号', blank=True, null=True)
    create_date = DateTimeField(verbose_name='レコード作成日時', auto_now_add=True, blank=True, null=True)
    update_date = DateTimeField(verbose_name='レコード更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'MQステータス'
    
        def __str__(self):
            return str(self.sequense)


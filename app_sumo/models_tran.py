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
    Rikishi = ForeignKey('Mst_Rikishi', on_delete=CASCADE)  # 力士マスタ
    #Join_code =  IntegerField(verbose_name='参加区分', blank=True, null=True)
    Class_code = ForeignKey('Mst_Class', on_delete=CASCADE)  # 階級マスタ
    #Eastwest_code =  ForeignKey('Mst_Eastwest', on_delete=CASCADE) #東西マスタ
    Chii_code = ForeignKey('Mst_Chii', on_delete=CASCADE)  # 地位マスタ
    Banzuke_rank = IntegerField(verbose_name='番付順位', blank=True, null=True)
    #Haridashi =  IntegerField(verbose_name='張付区分', blank=True, null=True)
    Banzuke_no = IntegerField(verbose_name='番付通番', blank=True, null=True)

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
    Chii_code = ForeignKey('Mst_Chii', on_delete=CASCADE)  # 地位マスタ
    Banzuke_rank = IntegerField(verbose_name='番付順位', blank=True, null=True)
    Haridashi = IntegerField(verbose_name='張付区分', blank=True, null=True)
    Banzuke_no = IntegerField(verbose_name='番付通番', blank=True, null=True)
    Appear_code = IntegerField(verbose_name='新再降区分', blank=True, null=True)
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

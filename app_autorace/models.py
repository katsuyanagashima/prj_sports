from django.db import models
from django.utils import timezone

class systemstatus(models.Model):
    sys_status = models.IntegerField('状態', blank=True, null=True)
    sys_display = models.CharField('表示用', blank=True, max_length=10)
    sys_updated = models.DateTimeField('更新日時', auto_now=True, null=True)

    class Meta:
        verbose_name_plural = '運用状態'

    def __str__(self):
        return self.sys_display

class csvtest1(models.Model):
    no = models.IntegerField('番号', blank=True, null=True)
    name = models.CharField('名前', blank=True, max_length=100)

    class Meta:
        verbose_name_plural = 'CSVテスト１'

    def __unicode__(self):
        return(self.name)

    def __str__(self):
        return self.name

class auto_schedule(models.Model):
    kind = models.CharField('区分', blank=True, max_length=1)
    kindofdata = models.CharField('データ種別', blank=True, max_length=1)
    dateofsend = models.IntegerField('送信日', blank=True, null=True)
    dateofrace1 = models.CharField('競争年月日1', blank=True, max_length=8)
    placeofrace1 = models.CharField('場外発売情報1', blank=True, max_length=1)
    place_code1_1 = models.CharField('場コード1_1', blank=True, max_length=1)
    numberofrace1_1 = models.IntegerField('レース数1_1', blank=True, null=True)
    place_code1_2 = models.CharField('場コード1_2', blank=True, max_length=1)
    numberofrace1_2 = models.CharField('レース数1_2', blank=True, null=True, max_length=2)
    place_code1_3 = models.CharField('場コード1_3', blank=True, max_length=1)
    numberofrace1_3 = models.CharField('レース数1_3', blank=True, null=True, max_length=2)
    place_code1_4 = models.CharField('場コード1_4', blank=True, max_length=1)
    numberofrace1_4 = models.CharField('レース数1_4', blank=True, null=True, max_length=2)
    place_code1_5 = models.CharField('場コード1_5', blank=True, max_length=1)
    numberofrace1_5 = models.CharField('レース数1_5', blank=True, null=True, max_length=2)
    place_code1_6 = models.CharField('場コード1_6', blank=True, max_length=1)
    numberofrace1_6 = models.CharField('レース数1_6', blank=True, null=True, max_length=2)
    dateofrace2 = models.CharField('競争年月日2', blank=True, max_length=8)
    placeofrace2 = models.CharField('場外発売情報2', blank=True, max_length=1)
    place_code2_1 = models.CharField('場コード2_1', blank=True, max_length=1)
    numberofrace2_1 = models.CharField('レース数2_1', blank=True, null=True, max_length=2)
    place_code2_2 = models.CharField('場コード2_2', blank=True, max_length=1)
    numberofrace2_2 = models.CharField('レース数2_2', blank=True, null=True, max_length=2)
    place_code2_3 = models.CharField('場コード2_3', blank=True, max_length=11)
    numberofrace2_3 = models.CharField('レース数2_3', blank=True, null=True, max_length=2)
    place_code2_4 = models.CharField('場コード2_4', blank=True, max_length=1)
    numberofrace2_4 = models.CharField('レース数2_4', blank=True, null=True, max_length=2)
    place_code2_5 = models.CharField('場コード2_5', blank=True, max_length=1)
    numberofrace2_5 = models.CharField('レース数2_5', blank=True, null=True, max_length=2)
    place_code2_6 = models.CharField('場コード2_6', blank=True, max_length=1)
    numberofrace2_6 = models.CharField('レース数2_6', blank=True, null=True, max_length=2)
    dateofrace3 = models.CharField('競争年月日3', blank=True, max_length=8)
    placeofrace3= models.CharField('場外発売情報3', blank=True, max_length=1)
    place_code3_1 = models.CharField('場コード3_1', blank=True, max_length=1)
    numberofrace3_1 = models.CharField('レース数3_1', blank=True, null=True, max_length=2)
    place_code3_2 = models.CharField('場コード3_2', blank=True, max_length=1)
    numberofrace3_2 = models.CharField('レース数3_2', blank=True, null=True, max_length=2)
    place_code3_3 = models.CharField('場コード3_3', blank=True, max_length=1)
    numberofrace3_3 = models.CharField('レース数3_3', blank=True, null=True, max_length=2)
    place_code3_4 = models.CharField('場コード3_4', blank=True, max_length=1)
    numberofrace3_4 = models.CharField('レース数3_4', blank=True, null=True, max_length=2)
    place_code3_5 = models.CharField('場コード3_5', blank=True, max_length=1)
    numberofrace3_5 = models.CharField('レース数3_5', blank=True, null=True, max_length=2)
    place_code3_6 = models.CharField('場コード3_6', blank=True, max_length=1)
    numberofrace3_6 = models.CharField('レース数3_6', blank=True, null=True, max_length=2)
    prize30 = models.CharField('賞金上位30', blank=True, max_length=1)

    class Meta:
        verbose_name_plural = 'スケジュールレコード'

    def __str__(self):
        return self.dateofrace1

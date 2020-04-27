from django.db import models
from django.db.models import * 
from django.utils import timezone

#CSV取り込み用に分離したテーブルをインポート
from .models_fixedlength import *

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

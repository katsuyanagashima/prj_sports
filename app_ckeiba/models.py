from django.db import models
from django.db.models import * 

#システム状態
class Tran_Systemstatus(Model):
    Unyou_date = DateField(verbose_name='運用日')
    SystemStatus = ForeignKey('Mst_Operationmode', on_delete=PROTECT) #ステータス管理マスタ 
    class Meta:
        verbose_name_plural = '#システム状態'
    
    def __str__(self):
        return str(self.Unyou_date)
    
    def setState(self, state):
        self.SystemStatus = state
        self.save()        #　変更したらセーブする！
        pass

#ステータス管理
class Mst_Operationmode(Model):
    Operationmode_code =  IntegerField(verbose_name='運用モード')
    Operationmode_name = CharField(verbose_name='運用モード表記', max_length=15)

    class Meta:
       verbose_name_plural = '#運用管理'

    def __str__(self):
        return str(self.Operationmode_code)

#競馬場マスタ
class Mst_Jou(Model):
    Jou_code = IntegerField(verbose_name='競馬場コード')
    Jou_name = CharField(verbose_name='正式名', max_length=20) #大井競馬場
    Jou_seisekiA = CharField(verbose_name='成績Ａ用', max_length=5) #大
    Jou_3char = CharField(verbose_name='３字略称', max_length=3) #大井△
    Jou_banei = BooleanField(verbose_name='ばんえいフラグ') #false
    Jou_1corner = CharField(verbose_name='１コーナー名称', max_length=5, blank=True, null=True) #１△角
    Jou_2corner = CharField(verbose_name='２コーナー名称', max_length=5, blank=True, null=True) #２△角
    Jou_3corner = CharField(verbose_name='３コーナー名称', max_length=5, blank=True, null=True) #３△角
    Jou_4corner = CharField(verbose_name='４コーナー名称', max_length=5, blank=True, null=True) #４△角
    
    class Meta:
        verbose_name_plural = '競馬場マスタ'

    def __str__(self):
        return self.Jou_name

#グレードマスタ
class Mst_Grade(Model):
    Grade_code = IntegerField(verbose_name='グレード区分')
    Grade_name = CharField(verbose_name='グレード名称', max_length=5)

    class Meta:
        verbose_name_plural = 'グレードマスタ'

    def __str__(self):
        return self.Grade_name
        
#品種年齢区分マスタ
class Mst_Breed_age(Model):
    Breed_age_code = IntegerField(verbose_name='品種年齢区分')
    Breed_age_name = CharField(verbose_name='競走種別用名称', max_length=10) #混合３・４歳
    Breed_age_age_name = CharField(verbose_name='馬齢条件用名称', max_length=10) #３・４歳
    Breed_age_breed_name = CharField(verbose_name='品種年齢名称', max_length=10) #混合
    
    class Meta:
        verbose_name_plural = '品種年齢区分マスタ'

    def __str__(self):
        return self.Breed_age_name

#天候マスタ
class Mst_Weather(Model):
    Weather_code = IntegerField(verbose_name='天候コード')
    Weather_name = CharField(verbose_name='天候名称', max_length=5) #晴
    
    class Meta:
        verbose_name_plural = '天候マスタ'

    def __str__(self):
        return self.Weather_name

#着差マスタ
class Mst_Margin(Model):
    Margin_code = IntegerField(verbose_name='着差コード')
    Margin_name = CharField(verbose_name='着差名称', max_length=5) #１△
    
    class Meta:
        verbose_name_plural = '着差マスタ'

    def __str__(self):
        return self.Margin_name
        
#差マスタ
class Mst_Bigmargin(Model):
    Bigmargin_code = IntegerField(verbose_name='差コード')
    Bigmargin_name = CharField(verbose_name='差名称', max_length=5)  #大差
    Bigmargin_display_name = CharField(verbose_name='画面表示用名称', max_length=5, blank=True)  #＝
    
    class Meta:
        verbose_name_plural = '差マスタ'

    def __str__(self):
        return self.Bigmargin_name
                
#事故種類マスタ
class Mst_Accident_type(Model):
    Accident_type_code = IntegerField(verbose_name='事故種類コード')
    Accident_type_name = CharField(verbose_name='事故種類名称', max_length=15)  #競走不成立
    Accident_type_priority = IntegerField(verbose_name='優先順位', blank=True)  #0
    
    class Meta:
        verbose_name_plural = '事故種類マスタ'

    def __str__(self):
        return self.Accident_type_name
                        
#事故理由マスタ
class Mst_Accident_reason(Model):
    Accident_reason_code = IntegerField(verbose_name='事故理由コード')
    Accident_reason_name = CharField(verbose_name='事故理由名称', max_length=15)  #進路妨害
    class Meta:
        verbose_name_plural = '事故理由マスタ'

    def __str__(self):
        return self.Accident_reason_name

#性別マスタ
class Mst_Sex(Model):
    Sex_code = IntegerField(verbose_name='性別コード')
    Sex_name = CharField(verbose_name='性別名称', max_length=2)  #牡
    Sex_sub = CharField(verbose_name='性別備考', max_length=5, blank=True)  #雄馬
    class Meta:
        verbose_name_plural = '性別マスタ'

    def __str__(self):
        return self.Sex_name

#所属場マスタ
class Mst_Affiliation(Model):
    Affiliation_code = IntegerField(verbose_name='所属場コード')
    Affiliation_name = CharField(verbose_name='所属場名称（正式名）', max_length=10)  #北海道
    Affiliation_1char = CharField(verbose_name='所属場名称（1字）', max_length=1)  #北
    class Meta:
        verbose_name_plural = '所属場マスタ'

    def __str__(self):
        return self.Affiliation_name

#中央交流区マスタ
class Mst_MixJRA(Model):
    MixJRA_code = IntegerField(verbose_name='中央交流区コード')
    MixJRA_name = CharField(verbose_name='交流区分名称', max_length=15)  #指定交流
    MixJRA_1char = IntegerField(verbose_name='配信区分コード')  #2
    class Meta:
        verbose_name_plural = '中央交流区マスタ'

    def __str__(self):
        return self.MixJRA_name

#芝・ダート区分マスタ
class Mst_Turf_dirt(Model):
    Turf_dirt_code = IntegerField(verbose_name='芝・ダート区分コード')
    Turf_dirt_name = CharField(verbose_name='芝区分名称', max_length=15)  #ダート
    class Meta:
        verbose_name_plural = '芝・ダート区分マスタ'

    def __str__(self):
        return self.Turf_dirt_name

#コース区分マスタ
class Mst_Course(Model):
    Course_code = IntegerField(verbose_name='コース区分コード')
    Course_name = CharField(verbose_name='コース区分名称', max_length=15)  #外コース
    class Meta:
        verbose_name_plural = 'コース区分マスタ'

    def __str__(self):
        return self.Course_name

#回り区分マスタ
class Mst_Rotation(Model):
    Rotation_code = IntegerField(verbose_name='回り区分コード')
    Rotation_name = CharField(verbose_name='回り区分名称', max_length=5)  #右
    class Meta:
        verbose_name_plural = '回り区分マスタ'

    def __str__(self):
        return self.Rotation_name

#ナイター区分マスタ
class Mst_Night_race(Model):
    Night_race_code = BooleanField(verbose_name='ナイター区分コード') #false：実施しない　true：実施
    Night_race_name = CharField(verbose_name='ナイター区分名称', max_length=5)  #昼
    class Meta:
        verbose_name_plural = 'ナイター区分マスタ'

    def __str__(self):
        return self.Night_race_name
        
#負担重量区分マスタ
class Mst_Handicap(Model):
    Handicap_code = IntegerField(verbose_name='負担重量区分コード') 
    Handicap_name = CharField(verbose_name='負担重量区分名称', max_length=5)  #ハンデ
    class Meta:
        verbose_name_plural = '負担重量区分マスタ'

    def __str__(self):
        return self.Handicap_name

#馬場状態マスタ
class Mst_Baba(Model):
    Baba_code = IntegerField(verbose_name='馬場状態コード') 
    Baba_name = CharField(verbose_name='馬場状態名称', max_length=5)  #良
    class Meta:
        verbose_name_plural = '馬場状態マスタ'

    def __str__(self):
        return self.Baba_name

#騎手変更理由マスタ
class Mst_Jockey_change(Model):
    Jockey_change_code = IntegerField(verbose_name='騎手変更理由コード') 
    Jockey_change_name = CharField(verbose_name='騎手変更理由名称', max_length=25)  #公正保持
    class Meta:
        verbose_name_plural = '騎手変更理由マスタ'

    def __str__(self):
        return self.Jockey_change_name

#事象マスタ
class Mst_Matter(Model):
    Matter_code = IntegerField(verbose_name='事象コード') 
    Matter_name = CharField(verbose_name='事象名称', max_length=15)  #事故
    class Meta:
        verbose_name_plural = '事象マスタ'

    def __str__(self):
        return self.Matter_name

#対象者マスタ
class Mst_Target_person(Model):
    Target_person_code = IntegerField(verbose_name='対象者コード') 
    Target_person_name = CharField(verbose_name='対象者名称', max_length=15)  #馬主
    class Meta:
        verbose_name_plural = '対象者マスタ'

    def __str__(self):
        return self.Target_person_name7
        
#競走種類マスタ
class Mst_Race_type(Model):
    Race_type_code = IntegerField(verbose_name='競走種類コード') 
    Race_type_name = CharField(verbose_name='競走種類名称', max_length=15)  #重賞
    Race_type_deliverytype = IntegerField(verbose_name='配信区分')  #3
    class Meta:
        verbose_name_plural = '競走種類マスタ'

    def __str__(self):
        return self.Race_type_name

# ここまでデータ系マスタ

# ここから配信系マスタ

#配信社マスタ
class Mst_Company(Model):
    Company_code = IntegerField(verbose_name='配信社コード') 
    Company_name = CharField(verbose_name='配信社名称', max_length=5)  #道新
    Company_block = BooleanField(verbose_name='ブロック指定フラグ')  #true
    Company_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】配信社マスタ'

    def __str__(self):
        return self.Company_name
        
#通常配信先マスタ
class Mst_Haishin(Model):
    Jou_code = ForeignKey('Mst_Jou',verbose_name='競馬場コード', on_delete=CASCADE) #競馬場マスタ 
    Haishin_racekaku = CharField(verbose_name='レース格', max_length=5) 
    Haishin_haishinsaki = CharField(verbose_name='配信先', max_length=5) 
    Haishin_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】通常配信先マスタ'

    def __str__(self):
        return self.Haishin_racekaku

#期間限定配信先マスタ
class Mst_Haishin_gentei(Model):
    Company_code = ForeignKey('Mst_Company',verbose_name='配信社コード', on_delete=CASCADE) #配信社コード 配信社マスタ 
    Jou_code = ForeignKey('Mst_Jou',verbose_name='競馬場コード', on_delete=CASCADE) #競馬場コード 競馬場マスタ 
    Haishin_gentei_start = CharField(verbose_name='開始日時', max_length=20) 
    Haishin_gentei_end = CharField(verbose_name='終了日時', max_length=20) 
    Haishin_gentei_start_race = CharField(verbose_name='開始R', max_length=5) 
    Haishin_gentei_end_race = CharField(verbose_name='終了R', max_length=5) 
    Haishin_gentei_file_name = CharField(verbose_name='ファイル名', max_length=15) 
    Haishin_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】期間限定配信先マスタ'

    def __str__(self):
        return self.Haishin_gentei_file_name
            
#プリンタ出力先マスタ
class Mst_Printer(Model):
    Printer_kei = IntegerField(verbose_name='系') 
    Printer_output = CharField(verbose_name='出力系', max_length=5) 
    Haishin_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】プリンタ出力先マスタ'

    def __str__(self):
        return self.Printer_output

# ここまで配信系マスタ

# ここからスケジュール系マスタ

#開催日割
class Mst_Kaisai_Hiwari(Model):
    Kaisai_Hiwari_date = DateField(verbose_name='開催日割')  
    class Meta:
        verbose_name_plural = '【スケジュール系】開催日割'

    def __str__(self):
        return self.Kaisai_Hiwari_date
        
#本日施行情報
class Mst_Honjitu_Shikou(Model):
    Honjitu_Shikou_date = DateField(verbose_name='本日施行情報')  
    class Meta:
        verbose_name_plural = '【スケジュール系】本日施行情報'

    def __str__(self):
        return self.Honjitu_Shikou_date

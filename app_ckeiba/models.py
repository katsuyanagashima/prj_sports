from django.db import models
from django.db.models import * 

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
        return str(self.Operationmode_name)


#実行環境管理
class Mst_Environment(Model):
    Environment_code =  IntegerField(verbose_name='実行環境')
    Environment_name = CharField(verbose_name='実行環境表記', max_length=15) #本番系/開発系

    class Meta:
       verbose_name_plural = '#実行環境管理'

    def __str__(self):
        return str(self.Environment_name)

#競馬場マスタ
class Mst_Jou(Model):
    Jou_code = IntegerField(verbose_name='競馬場コード')
    Jou_name = CharField(verbose_name='正式名', max_length=20) #大井競馬場
    Jou_seisekiA = CharField(verbose_name='成績Ａ用', max_length=1) #大
    Jou_3char = CharField(verbose_name='３字略称', max_length=3) #大井△
    Jou_banei = BooleanField(verbose_name='ばんえいフラグ') #false
    Group = CharField(verbose_name='グループ', max_length=5, blank=True, null=True)
    Group_priority = IntegerField(verbose_name='グループ優先', blank=True, null=True)
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
    Grade_code = CharField(verbose_name='グレード区分', max_length=2)
    Grade_name = CharField(verbose_name='グレード名称', max_length=4)
    Send_class = CharField(verbose_name='配信区分', max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'グレードマスタ'

    def __str__(self):
        return self.Grade_name
        
#品種年齢区分マスタ
class Mst_Breed_age(Model):
    Breed_age_code = IntegerField(verbose_name='品種年齢区分')
    Name_for_race_type = CharField(verbose_name='競走種別用名称', max_length=10, blank=True, null=True) #混合３・４歳
    Name_for_horse_age_condition = CharField(verbose_name='馬齢条件用名称', max_length=10, blank=True, null=True) #３・４歳
    Breed_age_name = CharField(verbose_name='品種年齢名称', max_length=10, blank=True, null=True) #混合
    
    class Meta:
        verbose_name_plural = '品種年齢区分マスタ'

    def __str__(self):
        return self.Name_for_race_type

#天候マスタ
class Mst_Weather(Model):
    Weather_code = IntegerField(verbose_name='天候コード')
    Weather_name = CharField(verbose_name='天候名称', max_length=5, blank=True, null=True) #晴
    
    class Meta:
        verbose_name_plural = '天候マスタ'

    def __str__(self):
        return self.Weather_name

#着差マスタ
class Mst_Margin(Model):
    Margin_code = IntegerField(verbose_name='着差コード')
    Margin_name = CharField(verbose_name='着差名称(通常）', max_length=10, blank=True, null=True) #１△
    Margin_convert = CharField(verbose_name='着差名称(変換)', max_length=10, blank=True, null=True) 
    
    class Meta:
        verbose_name_plural = '着差マスタ'

    def __str__(self):
        return self.Margin_name
        
#差マスタ
class Mst_Difference(Model):
    Differnce_code = IntegerField(verbose_name='差コード')
    Differnce_name = CharField(verbose_name='差名称', max_length=5, blank=True, null=True)  #大差
    Differnce_display = CharField(verbose_name='画面表示用名称', max_length=5, blank=True, null=True)  #＝
    
    class Meta:
        verbose_name_plural = '差マスタ'

    def __str__(self):
        return self.Differnce_name
                
#事故種類マスタ
class Mst_Accident_type(Model):
    Accident_type_code = IntegerField(verbose_name='事故種類コード')
    Accident_type_name = CharField(verbose_name='事故種類名称', max_length=15, blank=True, null=True)  #競走不成立
    Fulltag_all = CharField(verbose_name='フルタグＡＬＬ', max_length=15, blank=True, null=True)
    Priority = IntegerField(verbose_name='優先順位', blank=True, null=True) #0
    Accident_class = IntegerField(verbose_name='異常区分設定フラグ', blank=True, null=True) 
    
    
    class Meta:
        verbose_name_plural = '事故種類マスタ'

    def __str__(self):
        return self.Accident_type_name
                        
#事故理由マスタ
class Mst_Accident_reason(Model):
    Accident_reason_code = IntegerField(verbose_name='事故理由コード')
    Accident_reason_name = CharField(verbose_name='事故理由名称', max_length=15, blank=True, null=True)  #進路妨害
    Accident_class = IntegerField(verbose_name='異常区分設定フラグ', blank=True, null=True) 

    class Meta:
        verbose_name_plural = '事故理由マスタ'

    def __str__(self):
        return self.Accident_reason_name

#性別マスタ
class Mst_Gender(Model):
    Horse_gender_code = IntegerField(verbose_name='性別コード')
    Horse_gender = CharField(verbose_name='性別名称', max_length=2, blank=True, null=True)  #牡
    Remarks = CharField(verbose_name='備考', max_length=5, blank=True, null=True)  #雄馬
    class Meta:
        verbose_name_plural = '性別マスタ'

    def __str__(self):
        return self.Horse_gender

#所属場マスタ
class Mst_Belonging(Model):
    Belonging_code = IntegerField(verbose_name='所属場コード')
    Belonging = CharField(verbose_name='所属場名称（正式名）', max_length=10, blank=True, null=True)  #北海道
    Belonging_1char = CharField(verbose_name='所属場名称（1字）', max_length=1, blank=True, null=True)  #北
    class Meta:
        verbose_name_plural = '所属場マスタ'

    def __str__(self):
        return self.Belonging

#中央交流区分マスタ
class Mst_JRA_exchanges(Model):
    JRA_exchanges_code = IntegerField(verbose_name='中央交流区コード')
    JRA_exchanges = CharField(verbose_name='交流区分名称', max_length=10, blank=True, null=True)  #指定交流
    Send_classification = IntegerField(verbose_name='配信区分コード', blank=True, null=True)  #2
    class Meta:
        verbose_name_plural = '中央交流区分マスタ'

    def __str__(self):
        return self.JRA_exchanges

#芝・ダート区分マスタ
class Mst_Turf_dirt_class(Model):
    Turf_dirt_code = IntegerField(verbose_name='芝・ダート区分コード')
    Turf_dirt_name = CharField(verbose_name='芝区分名称', max_length=5, blank=True, null=True)  #ダート
    class Meta:
        verbose_name_plural = '芝・ダート区分マスタ'

    def __str__(self):
        return self.Turf_dirt_name

#コース区分マスタ
class Mst_Course_class(Model):
    Course_class_code = IntegerField(verbose_name='コース区分コード')
    Course_class_name = CharField(verbose_name='コース区分名称', max_length=5, blank=True, null=True)  #外コース
    class Meta:
        verbose_name_plural = 'コース区分マスタ'

    def __str__(self):
        return self.Course_class_name

#回り区分マスタ
class Mst_Clockwise_class(Model):
    CW_or_CCW_code = IntegerField(verbose_name='回り区分コード')
    CW_or_CCW = CharField(verbose_name='回り区分名称', max_length=5, blank=True, null=True)  #右
    class Meta:
        verbose_name_plural = '回り区分マスタ'

    def __str__(self):
        return self.CW_or_CCW

#ナイター区分マスタ
class Mst_Night_race_class(Model):
    Night_race_code = IntegerField(verbose_name='ナイター区分コード') #0：実施しない　1：実施
    Night_race_name = CharField(verbose_name='ナイター区分名称', max_length=5, blank=True, null=True)  
    class Meta:
        verbose_name_plural = 'ナイター区分マスタ'

    def __str__(self):
        return self.Night_race_name
        
#負担重量区分マスタ
class Mst_Handicap(Model):
    Handicap_code = IntegerField(verbose_name='負担重量区分コード') 
    Handicap_name = CharField(verbose_name='負担重量区分名称', max_length=5, blank=True, null=True)  #ハンデ
    Weight_shortend = CharField(verbose_name='設定値', max_length=5, blank=True, null=True) 
    class Meta:
        verbose_name_plural = '負担重量区分マスタ'

    def __str__(self):
        return self.Handicap_name

#馬場状態マスタ
class Mst_Track_condition(Model):
    Track_condition_code = IntegerField(verbose_name='馬場状態コード') 
    Track_condition_name = CharField(verbose_name='馬場状態名称', max_length=5, blank=True, null=True)  #良
    class Meta:
        verbose_name_plural = '馬場状態マスタ'

    def __str__(self):
        return self.Track_condition_name

#騎手変更理由マスタ
class Mst_Jockey_changed_reason(Model):
    Jockey_changed_reason_code = IntegerField(verbose_name='騎手変更理由コード') 
    Jockey_changed_reason_name = CharField(verbose_name='騎手変更理由名称', max_length=10, blank=True, null=True)  #公正保持
    class Meta:
        verbose_name_plural = '騎手変更理由マスタ'

    def __str__(self):
        return self.Jockey_changed_reason_name

#事象マスタ
class Mst_Matter(Model):
    Matter_code = IntegerField(verbose_name='事象コード') 
    Matter_name = CharField(verbose_name='事象名称', max_length=10, blank=True, null=True)  #事故
    class Meta:
        verbose_name_plural = '事象マスタ'

    def __str__(self):
        return self.Matter_name

#対象者マスタ
class Mst_Target_person(Model):
    Target_person_code = IntegerField(verbose_name='対象者コード') 
    Target_person_name = CharField(verbose_name='対象者名称', max_length=10, blank=True, null=True)  #馬主
    class Meta:
        verbose_name_plural = '対象者マスタ'

    def __str__(self):
        return self.Target_person_name
        
#競走種類マスタ
class Mst_Race_type(Model):
    Race_type_code = IntegerField(verbose_name='競走種類コード') 
    Race_type_name = CharField(verbose_name='競走種類名称', max_length=10, blank=True, null=True)  #重賞
    Race_type_deliverytype = IntegerField(verbose_name='配信区分')  #3
    class Meta:
        verbose_name_plural = '競走種類マスタ'

    def __str__(self):
        return self.Race_type_name

# ここまでデータ系マスタ

# ここから配信系マスタ

#配信社マスタ
class Mst_Haishinsha(Model):
    Haishinsha_code = IntegerField(verbose_name='配信社コード') 
    Haishinsha_name = CharField(verbose_name='配信社名称', max_length=10)  #北海道新聞
    Haishinsha_2char_name = CharField(verbose_name='配信社名称', max_length=2, blank=True, null=True)  #道新
    Haishinsha_block = IntegerField(verbose_name='ブロック指定フラグ', blank=True, null=True)  
    Haishinsha_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】配信社マスタ'

    def __str__(self):
        return self.Haishinsha_name
        
#通常配信先マスタ
class Mst_Haishinsaki_Nomal(Model):
    Jou_code = ForeignKey('Mst_Jou',verbose_name='競馬場コード', on_delete=CASCADE) #競馬場マスタ 
    Haishin_racekaku = CharField(verbose_name='レース格', max_length=5, blank=True, null=True) 
    Haishinsha_code = ForeignKey('Mst_Haishinsha',verbose_name='配信先', on_delete=CASCADE) #配信社コード 配信社マスタ 
    Haishin_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】通常配信先マスタ'

    def __str__(self):
        return self.Haishin_racekaku

#期間限定配信先マスタ
class Mst_Haishinsaki_Limited(Model):
    Haishinsha_code = ForeignKey('Mst_Haishinsha',verbose_name='配信社コード', on_delete=CASCADE) #配信社コード 配信社マスタ 
    Jou_code = ForeignKey('Mst_Jou',verbose_name='競馬場コード', on_delete=CASCADE) #競馬場コード 競馬場マスタ 
    Start_date = DateField(verbose_name='開始日時') 
    End_date = DateField(verbose_name='終了日時') 
    Start_race = IntegerField(verbose_name='開始R') 
    End_race = IntegerField(verbose_name='終了R') 
    File_name = CharField(verbose_name='ファイル名', max_length=30, blank=True, null=True) 
    Haishin_limited_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】期間限定配信先マスタ'

    def __str__(self):
        return self.Haishin_gentei_file_name
            
#プリンタ出力先マスタ
class Mst_Printer(Model):
    Printer_kei = IntegerField(verbose_name='系') 
    Printer_output = CharField(verbose_name='出力系', max_length=5) 
    Printer_yobi = CharField(verbose_name='予備', max_length=30, blank=True, null=True)
    class Meta:
        verbose_name_plural = '【配信系】プリンタ出力先マスタ'

    def __str__(self):
        return self.Printer_output

# ここまで配信系マスタ

# ここからスケジュール系マスタ

#開催日割
# まだ未完成。とりあえずつくった。
class Mst_Kaisai_Hiwari(Model):
    Kaisai_Hiwari_date = DateField(verbose_name='開催日割')  
    class Meta:
        verbose_name_plural = '【スケジュール系】開催日割'

    def __str__(self):
        return self.Kaisai_Hiwari_date
        
#本日施行情報
# まだ未完成。とりあえずつくった。
class Mst_Honjitu_Shikou(Model):
    Honjitu_Shikou_date = DateField(verbose_name='本日施行情報')  
    class Meta:
        verbose_name_plural = '【スケジュール系】本日施行情報'

    def __str__(self):
        return self.Honjitu_Shikou_date

#その他

#修正句マスタ
class Mst_Fix_annotation(Model):
    content_id = CharField(verbose_name='製品ID', max_length=64) 
    tag_name = CharField(verbose_name='タグ名', max_length=64) 
    fix_tag_annotation = CharField(verbose_name='修正名', max_length=64)
    parent_tag_name = IntegerField(verbose_name='親タグID') 
    priority = IntegerField(verbose_name='優先順位') 
    create_date = DateField(verbose_name='レコード作成日') 
    update_date = DateField(verbose_name='レコード更新日') 
    class Meta:
        verbose_name_plural = '修正句マスタ'

    def __str__(self):
        return self.content_id

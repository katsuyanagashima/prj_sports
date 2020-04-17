from django.db import models
from django.db.models import * 

# 各種マスタ

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

#競馬場マスタ
class Mst_Jou(Model):
    Jou_code = IntegerField(verbose_name='競馬場コード', unique=True)
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
    Grade_code = CharField(verbose_name='グレード区分', max_length=2, unique=True)
    Grade_name = CharField(verbose_name='グレード名称', max_length=4)
    Send_class = CharField(verbose_name='配信区分', max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'グレードマスタ'

    def __str__(self):
        return self.Grade_name
        
#品種年齢区分マスタ
class Mst_Breed_age(Model):
    Breed_age_code = IntegerField(verbose_name='品種年齢区分', unique=True)
    Name_for_race_type = CharField(verbose_name='競走種別用名称', max_length=10, blank=True, null=True) #混合３・４歳
    Name_for_horse_age_condition = CharField(verbose_name='馬齢条件用名称', max_length=10, blank=True, null=True) #３・４歳
    Breed_age_name = CharField(verbose_name='品種年齢名称', max_length=10, blank=True, null=True) #混合
    
    class Meta:
        verbose_name_plural = '品種年齢区分マスタ'

    def __str__(self):
        return self.Name_for_race_type

#天候マスタ
class Mst_Weather(Model):
    Weather_code = IntegerField(verbose_name='天候コード', unique=True)
    Weather_name = CharField(verbose_name='天候名称', max_length=5, blank=True, null=True) #晴
    
    class Meta:
        verbose_name_plural = '天候マスタ'

    def __str__(self):
        return self.Weather_name

#着差マスタ
class Mst_Margin(Model):
    Margin_code = IntegerField(verbose_name='着差コード', unique=True)
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
    Accident_type_code = IntegerField(verbose_name='事故種類コード', unique=True)
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
    Accident_reason_code = IntegerField(verbose_name='事故理由コード', unique=True)
    Accident_reason_name = CharField(verbose_name='事故理由名称', max_length=15, blank=True, null=True)  #進路妨害
    Accident_class = IntegerField(verbose_name='異常区分設定フラグ', blank=True, null=True) 

    class Meta:
        verbose_name_plural = '事故理由マスタ'

    def __str__(self):
        return self.Accident_reason_name

#性別マスタ
class Mst_Gender(Model):
    Horse_gender_code = IntegerField(verbose_name='性別コード', unique=True)
    Horse_gender = CharField(verbose_name='性別名称', max_length=2, blank=True, null=True)  #牡
    Remarks = CharField(verbose_name='備考', max_length=5, blank=True, null=True)  #雄馬
    class Meta:
        verbose_name_plural = '性別マスタ'

    def __str__(self):
        return self.Horse_gender

#所属場マスタ
class Mst_Belonging(Model):
    Belonging_code = IntegerField(verbose_name='所属場コード', unique=True)
    Belonging = CharField(verbose_name='所属場名称（正式名）', max_length=10, blank=True, null=True)  #北海道
    Belonging_1char = CharField(verbose_name='所属場名称（1字）', max_length=1, blank=True, null=True)  #北
    class Meta:
        verbose_name_plural = '所属場マスタ'

    def __str__(self):
        return self.Belonging

#中央交流区分マスタ
class Mst_JRA_exchanges(Model):
    JRA_exchanges_code = IntegerField(verbose_name='中央交流区コード', unique=True)
    JRA_exchanges = CharField(verbose_name='交流区分名称', max_length=10, blank=True, null=True)  #指定交流
    Send_classification = IntegerField(verbose_name='配信区分コード', blank=True, null=True)  #2
    class Meta:
        verbose_name_plural = '中央交流区分マスタ'

    def __str__(self):
        return self.JRA_exchanges

#芝・ダート区分マスタ
class Mst_Turf_dirt_class(Model):
    Turf_dirt_code = IntegerField(verbose_name='芝・ダート区分コード', unique=True)
    Turf_dirt_name = CharField(verbose_name='芝区分名称', max_length=5, blank=True, null=True)  #ダート
    class Meta:
        verbose_name_plural = '芝・ダート区分マスタ'

    def __str__(self):
        return self.Turf_dirt_name

#コース区分マスタ
class Mst_Course_class(Model):
    Course_class_code = IntegerField(verbose_name='コース区分コード', unique=True)
    Course_class_name = CharField(verbose_name='コース区分名称', max_length=5, blank=True, null=True)  #外コース
    class Meta:
        verbose_name_plural = 'コース区分マスタ'

    def __str__(self):
        return self.Course_class_name

#回り区分マスタ
class Mst_Clockwise_class(Model):
    CW_or_CCW_code = IntegerField(verbose_name='回り区分コード', unique=True)
    CW_or_CCW = CharField(verbose_name='回り区分名称', max_length=5, blank=True, null=True)  #右
    class Meta:
        verbose_name_plural = '回り区分マスタ'

    def __str__(self):
        return self.CW_or_CCW

#ナイター区分マスタ
class Mst_Night_race_class(Model):
    Night_race_code = IntegerField(verbose_name='ナイター区分コード', unique=True) #0：実施しない　1：実施
    Night_race_name = CharField(verbose_name='ナイター区分名称', max_length=5, blank=True, null=True)  
    class Meta:
        verbose_name_plural = 'ナイター区分マスタ'

    def __str__(self):
        return self.Night_race_name
        
#負担重量区分マスタ
class Mst_Handicap(Model):
    Handicap_code = IntegerField(verbose_name='負担重量区分コード', unique=True) 
    Handicap_name = CharField(verbose_name='負担重量区分名称', max_length=5, blank=True, null=True)  #ハンデ
    Weight_shortend = CharField(verbose_name='設定値', max_length=5, blank=True, null=True) 
    class Meta:
        verbose_name_plural = '負担重量区分マスタ'

    def __str__(self):
        return self.Handicap_name

#馬場状態マスタ
class Mst_Track_condition(Model):
    Track_condition_code = IntegerField(verbose_name='馬場状態コード', unique=True) 
    Track_condition_name = CharField(verbose_name='馬場状態名称', max_length=5, blank=True, null=True)  #良
    class Meta:
        verbose_name_plural = '馬場状態マスタ'

    def __str__(self):
        return self.Track_condition_name

#騎手変更理由マスタ
class Mst_Jockey_changed_reason(Model):
    Jockey_changed_reason_code = IntegerField(verbose_name='騎手変更理由コード', unique=True) 
    Jockey_changed_reason_name = CharField(verbose_name='騎手変更理由名称', max_length=10, blank=True, null=True)  #公正保持
    class Meta:
        verbose_name_plural = '騎手変更理由マスタ'

    def __str__(self):
        return self.Jockey_changed_reason_name

#事象マスタ
class Mst_Matter(Model):
    Matter_code = IntegerField(verbose_name='事象コード', unique=True) 
    Matter_name = CharField(verbose_name='事象名称', max_length=10, blank=True, null=True)  #事故
    class Meta:
        verbose_name_plural = '事象マスタ'

    def __str__(self):
        return self.Matter_name

#対象者マスタ
class Mst_Target_person(Model):
    Target_person_code = IntegerField(verbose_name='対象者コード', unique=True) 
    Target_person_name = CharField(verbose_name='対象者名称', max_length=10, blank=True, null=True)  #馬主
    class Meta:
        verbose_name_plural = '対象者マスタ'

    def __str__(self):
        return self.Target_person_name
        
#競走種類マスタ
class Mst_Race_type(Model):
    Race_type_code = IntegerField(verbose_name='競走種類コード', unique=True) 
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



# ここから中間DB

# 【中間DB】出走表
class Md_Shussouhyou(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "shussouhyou")  #競馬場マスタ
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')

    # 競走年月日
    ck_kyounichi = DateField(verbose_name='競走年月日')
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')

    # レース情報
    rebangou = IntegerField(verbose_name='レース番号')
    shubetsu = ForeignKey('Mst_Breed_age', verbose_name='競争種別', on_delete=CASCADE, related_name = "shubetu")  #品種年齢区分マスタ
    tokusouhonsuu = IntegerField(verbose_name='特別競争本題回数')
    tokusoumeihon = CharField(verbose_name='特別競争名本題', max_length=100, blank=True, null=True)
    tokusoumeifuku = CharField(verbose_name='特別競争名副題', max_length=100, blank=True, null=True)
    ck_fukusyoumei = CharField(verbose_name='副賞名', max_length=100, blank=True, null=True) #複数ある場合繰り返すかリスト化する必要あり
    guredo = ForeignKey('Mst_Grade', verbose_name='グレード', on_delete=CASCADE, blank=True, null=True)  #グレードマスタ
    md_kyousousyu = ForeignKey('Mst_Race_type', verbose_name='競争種類コード', on_delete=CASCADE)  #競走種類マスタ
    ck_chuokouryu = ForeignKey('Mst_JRA_exchanges', verbose_name='中央交流区分', on_delete=CASCADE)  #中央交流区分マスタ
    kyori = IntegerField(verbose_name='競争距離')

    # トラック情報
    ck_shibadat = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE)  #芝・ダート区分マスタ
    ck_naigai = ForeignKey('Mst_Course_class', verbose_name='コース区分', on_delete=CASCADE)  #コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class', verbose_name='回り区分', on_delete=CASCADE)  #回り区分マスタ
    ck_naita  = ForeignKey('Mst_Night_race_class', verbose_name='ナイター区分', on_delete=CASCADE)  #ナイター区分マスタ
    ck_shokin1 = IntegerField(verbose_name='1着賞金')
    ck_shokin2 = IntegerField(verbose_name='2着賞金')
    ck_shokin3 = IntegerField(verbose_name='3着賞金')
    ck_shokin4 = IntegerField(verbose_name='4着賞金')
    ck_shokin5 = IntegerField(verbose_name='5着賞金')
    refun = IntegerField(verbose_name='レコードタイム分')
    rebyo = IntegerField(verbose_name='レコードタイム秒')
    remiri = IntegerField(verbose_name='レコードタイムミリ')
    rekobamei = CharField(verbose_name='レコード馬名', max_length=10, blank=True, null=True)
    shusuu = IntegerField(verbose_name='出走頭数')
    hassoujikoku = TimeField(verbose_name='発送時刻')
    bareijouken = ForeignKey('Mst_Breed_age', verbose_name='競争種別', on_delete=CASCADE, related_name = "barei")    #品種年齢区分マスタ。もう取得してる競走種別用名称から馬齢条件用名称を取得？
    ck_shikaku = CharField(verbose_name='レコード馬名', max_length=10, blank=True, null=True) #複数ある場合繰り返すかリスト化する必要あり
    ck_rkaku = CharField(verbose_name='レース格', max_length=10, blank=True, null=True) #複数ある場合繰り返すかリスト化する必要あり
    ck_rkumi = CharField(verbose_name='レース組', max_length=10, blank=True, null=True) #複数ある場合繰り返すかリスト化する必要あり
    jyuuryoushubetsu = ForeignKey('Mst_Handicap', verbose_name='負担重量区分', on_delete=CASCADE)  #負担重量区分マスタ


    # 出走馬。最大16頭立て
    shussouba1 = ForeignKey('Md_Shussouba', verbose_name='出走馬1', on_delete=CASCADE, related_name = "umaban_1", blank=True, null=True)  #出走馬マスタ
    shussouba2 = ForeignKey('Md_Shussouba', verbose_name='出走馬2', on_delete=CASCADE, related_name = "umaban_2", blank=True, null=True)  #出走馬マスタ
    shussouba3 = ForeignKey('Md_Shussouba', verbose_name='出走馬3', on_delete=CASCADE, related_name = "umaban_3", blank=True, null=True)  #出走馬マスタ
    shussouba4 = ForeignKey('Md_Shussouba', verbose_name='出走馬4', on_delete=CASCADE, related_name = "umaban_4", blank=True, null=True)  #出走馬マスタ
    shussouba5 = ForeignKey('Md_Shussouba', verbose_name='出走馬5', on_delete=CASCADE, related_name = "umaban_5", blank=True, null=True)  #出走馬マスタ
    shussouba6 = ForeignKey('Md_Shussouba', verbose_name='出走馬6', on_delete=CASCADE, related_name = "umaban_6", blank=True, null=True)  #出走馬マスタ
    shussouba7 = ForeignKey('Md_Shussouba', verbose_name='出走馬7', on_delete=CASCADE, related_name = "umaban_7", blank=True, null=True)  #出走馬マスタ
    shussouba8 = ForeignKey('Md_Shussouba', verbose_name='出走馬8', on_delete=CASCADE, related_name = "umaban_8", blank=True, null=True)  #出走馬マスタ
    shussouba9 = ForeignKey('Md_Shussouba', verbose_name='出走馬9', on_delete=CASCADE, related_name = "umaban_9", blank=True, null=True)  #出走馬マスタ
    shussouba10 = ForeignKey('Md_Shussouba', verbose_name='出走馬10', on_delete=CASCADE, related_name = "umaban_10", blank=True, null=True)  #出走馬マスタ
    shussouba11 = ForeignKey('Md_Shussouba', verbose_name='出走馬11', on_delete=CASCADE, related_name = "umaban_11", blank=True, null=True)  #出走馬マスタ
    shussouba12 = ForeignKey('Md_Shussouba', verbose_name='出走馬12', on_delete=CASCADE, related_name = "umaban_12", blank=True, null=True)  #出走馬マスタ
    shussouba13 = ForeignKey('Md_Shussouba', verbose_name='出走馬13', on_delete=CASCADE, related_name = "umaban_13", blank=True, null=True)  #出走馬マスタ
    shussouba14 = ForeignKey('Md_Shussouba', verbose_name='出走馬14', on_delete=CASCADE, related_name = "umaban_14", blank=True, null=True)  #出走馬マスタ
    shussouba15 = ForeignKey('Md_Shussouba', verbose_name='出走馬15', on_delete=CASCADE, related_name = "umaban_15", blank=True, null=True)  #出走馬マスタ
    shussouba16 = ForeignKey('Md_Shussouba', verbose_name='出走馬16', on_delete=CASCADE, related_name = "umaban_16", blank=True, null=True)  #出走馬マスタ
    
    class Meta:
        verbose_name_plural = '【中間DB】出走表'

    def __str__(self):
        return self.joumei


# 出走馬情報（最大16頭立ての前提。）
class Md_Shussouba(Model):

    #リレーション用の情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "shussouba")  #競馬場マスタ
    ck_kyounichi = DateField(verbose_name='競走年月日')
    rebangou = IntegerField(verbose_name='レース番号')


    # 馬情報
    waku = IntegerField(verbose_name='枠番')
    uma = IntegerField(verbose_name='馬番')
    ck_boiro = CharField(verbose_name='帽色', max_length=10)
    fujuu = IntegerField(verbose_name='負担重量', blank=True, null=True)
    ck_sekijuu = IntegerField(verbose_name='積載重量', blank=True, null=True)
    seibetsu = ForeignKey('Mst_Gender', verbose_name='性別', on_delete=CASCADE)  #性別マスタ
    bamei = CharField(verbose_name='馬名', max_length=10, blank=True, null=True)
    kyuubamei = CharField(verbose_name='旧馬名', max_length=10, blank=True, null=True)
    barei = IntegerField(verbose_name='馬齢')
    ck_keiro = CharField(verbose_name='毛色', max_length=10, blank=True, null=True)
    ck_chichi = CharField(verbose_name='父名', max_length=10, blank=True, null=True)
    ck_haha = CharField(verbose_name='母名', max_length=10, blank=True, null=True)
    ck_hahachichi = CharField(verbose_name='母の父名', max_length=10, blank=True, null=True)
    ck_banushi = CharField(verbose_name='馬主名', max_length=30, blank=True, null=True)
    ck_seisansya = CharField(verbose_name='生産牧場名', max_length=30, blank=True, null=True)
    ck_umasyozoku = ForeignKey('Mst_Belonging', verbose_name='所属場', on_delete=CASCADE , related_name = "uma_shozoku")  #所属場マスタ
    ck_kakutokuskin = IntegerField(verbose_name='収得賞金')

    # 騎手情報
    kimei = CharField(verbose_name='騎手名', max_length=30)
    kimei_sei = CharField(verbose_name='騎手名_姓', max_length=20, blank=True, null=True)
    kimei_mei = CharField(verbose_name='騎手名_名', max_length=20, blank=True, null=True)
    ck_kisyozoku = ForeignKey('Mst_Belonging', verbose_name='騎手所属場', on_delete=CASCADE , related_name = "kishu_shozoku")  #所属場マスタ
    ck_kimnbangou = IntegerField(verbose_name='騎手免許番号')
    ck_kizen_1chaku = IntegerField(verbose_name='騎手成績 1着')
    ck_kizen_2chaku = IntegerField(verbose_name='騎手成績 2着')
    ck_kizen_3chaku = IntegerField(verbose_name='騎手成績 3着')
    ck_kizen_chakugai = IntegerField(verbose_name='騎手成績 着外')
    mikubun = IntegerField(verbose_name='見習区分')

    # 調教師情報
    choumei = CharField(verbose_name='調教師名', max_length=30)
    choumei_sei = CharField(verbose_name='調教師名_姓', max_length=20, blank=True, null=True)
    choumei_mei = CharField(verbose_name='調教師名_名', max_length=20, blank=True, null=True)

    # 距離別成績
    ck_tan_1chaku = IntegerField(verbose_name='短距離 1着')
    ck_tan_2chaku = IntegerField(verbose_name='短距離 2着')
    ck_tan_3chaku = IntegerField(verbose_name='短距離 3着')
    ck_tan_chakugai = IntegerField(verbose_name='短距離 着外')
    ck_tyuu_1chaku = IntegerField(verbose_name='中距離 1着')
    ck_tyuu_2chaku = IntegerField(verbose_name='中距離 2着')
    ck_tyuu_3chaku = IntegerField(verbose_name='中距離 3着')
    ck_tyuu_chakugai = IntegerField(verbose_name='中距離 着外')
    ck_tyou_1chaku = IntegerField(verbose_name='長距離 1着')
    ck_tyou_2chaku = IntegerField(verbose_name='長距離 2着')
    ck_tyou_3chaku = IntegerField(verbose_name='長距離 3着')
    ck_tyou_chakugai = IntegerField(verbose_name='長距離 着外')

    # 着別成績
    ck_zen_1chaku = IntegerField(verbose_name='全成績 1着')
    ck_zen_2chaku = IntegerField(verbose_name='全成績 2着')
    ck_zen_3chaku = IntegerField(verbose_name='全成績 3着')
    ck_zen_chakugai = IntegerField(verbose_name='全成績 着外')
    ck_migid_1chaku = IntegerField(verbose_name='右回りダート成績 1着')
    ck_migid_2chaku = IntegerField(verbose_name='右回りダート成績 2着')
    ck_migid_3chaku = IntegerField(verbose_name='右回りダート成績 3着')
    ck_migid_chakugai = IntegerField(verbose_name='右回りダート成績 着外')
    ck_hidarid_1chaku = IntegerField(verbose_name='左回りダート成績 1着')
    ck_hidarid_2chaku = IntegerField(verbose_name='左回りダート成績 2着')
    ck_hidarid_3chaku = IntegerField(verbose_name='左回りダート成績 3着')
    ck_hidarid_chakugai = IntegerField(verbose_name='左回りダート成績 着外')
    ck_jyou_1chaku = IntegerField(verbose_name='該当競馬場芝orダート成績 1着')
    ck_jyou_2chaku = IntegerField(verbose_name='該当競馬場芝orダート成績 2着')
    ck_jyou_3chaku = IntegerField(verbose_name='該当競馬場芝orダート成績 3着')
    ck_jyou_chakugai = IntegerField(verbose_name='該当競馬場芝orダート成績 着外')

    #過去成績
    kakoseiseki1 = ForeignKey('Md_Shussouba_kako', verbose_name='過去成績1', on_delete=CASCADE, related_name = "kako_1")  #過去成績マスタ
    kakoseiseki2 = ForeignKey('Md_Shussouba_kako', verbose_name='過去成績2', on_delete=CASCADE, related_name = "kako_2")  #過去成績マスタ
    kakoseiseki3 = ForeignKey('Md_Shussouba_kako', verbose_name='過去成績3', on_delete=CASCADE, related_name = "kako_3")  #過去成績マスタ
    kakoseiseki4 = ForeignKey('Md_Shussouba_kako', verbose_name='過去成績4', on_delete=CASCADE, related_name = "kako_4")  #過去成績マスタ
    kakoseiseki5 = ForeignKey('Md_Shussouba_kako', verbose_name='過去成績5', on_delete=CASCADE, related_name = "kako_5")  #過去成績マスタ

    
    class Meta:
        verbose_name_plural = '【中間DB】出走表_出走馬'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou)+'R ' + str(self.uma) +'番 ' + str(self.bamei)

    # 過去成績 5回分繰り返す
class Md_Shussouba_kako(Model):

    #リレーション用の情報
    bamei = CharField(verbose_name='馬名', max_length=10, blank=True, null=True)

    # 出走日付
    ck_kkhiduke = DateField(verbose_name='出走日付')
    # 開催場情報
    ck_kkjoumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "shussouba_kako")  #競馬場マスタ
    ck_kktenkou = ForeignKey('Mst_Weather', verbose_name='天候マスタ', on_delete=CASCADE)  #天候マスタ
    ck_kkbajou = ForeignKey('Mst_Track_condition', verbose_name='馬場状態マスタ', on_delete=CASCADE)  #馬場状態マスタ
    ck_kkbasui = IntegerField(verbose_name='馬場水分')
    # レース情報
    ck_kknaita = ForeignKey('Mst_Night_race_class', verbose_name='ナイター区分マスタ', on_delete=CASCADE)  #ナイター区分マスタ
    ck_kkshubetsu = ForeignKey('Mst_Breed_age', verbose_name='品種年齢区分マスタ', on_delete=CASCADE , related_name = "kako")  #品種年齢区分マスタ
    ck_kkrmei = CharField(verbose_name='レース名称', max_length=50, blank=True, null=True)
    ck_kkshikaku = CharField(verbose_name='競争資格条件', max_length=30, blank=True, null=True) # 複数ある場合、,で区切る
    ck_kkrkaku = CharField(verbose_name='レース格', max_length=20, blank=True, null=True) # 複数ある場合、,で区切る
    ck_kkrkumi = CharField(verbose_name='レース組', max_length=20, blank=True, null=True) # 複数ある場合、,で区切る
    ck_kkguredo = ForeignKey('Mst_Grade', verbose_name='グレードマスタ', on_delete=CASCADE)  #グレードマスタ
    ck_kkkyori = IntegerField(verbose_name='競争距離')
    # トラック情報
    ck_shibadat = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE)  #芝・ダート区分マスタ
    ck_naigai = ForeignKey('Mst_Course_class', verbose_name='コース区分', on_delete=CASCADE)  #コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class', verbose_name='回り区分', on_delete=CASCADE)  #回り区分マスタ

    ck_kkshusuu = IntegerField(verbose_name='出走頭数')
    # 出走馬成績情報
    ck_kkjuni = IntegerField(verbose_name='順位')
    ck_kknyujuni = IntegerField(verbose_name='入選順位')
    ck_kkwaku = IntegerField(verbose_name='枠番')
    ck_kkuma = IntegerField(verbose_name='馬番')
    ck_kkfujuu = IntegerField(verbose_name='負担重量')
    ck_kksekijuu = IntegerField(verbose_name='積載重量')
    ck_kkgenkigou = CharField(verbose_name='減量記号', max_length=3, blank=True, null=True)
    ck_kkkimei = CharField(verbose_name='騎手名（３字略）', max_length=3, blank=True, null=True)
    ck_kktime = IntegerField(verbose_name='タイム')
    ck_kkaiteuma = CharField(verbose_name='相手馬名', max_length=10, blank=True, null=True)
    ck_kktimesa = IntegerField(verbose_name='タイム差')
    ck_kkjikosyu = ForeignKey('Mst_Accident_type', verbose_name='事故種類コード', on_delete=CASCADE)  #事故種類マスタ
    ck_kkjikoriyuu = ForeignKey('Mst_Accident_reason', verbose_name='事故理由コード', on_delete=CASCADE)  #事故理由マスタ
    ck_kkkojuni = CharField(verbose_name='コーナー通過順', max_length=20, blank=True, null=True) #-で区切る　例：3-4-4-5
    ck_kka3ha = IntegerField(verbose_name='上がり３ハロン')
    ck_kkbajuu = IntegerField(verbose_name='馬体重')
    ck_kktannin = IntegerField(verbose_name='単勝人気')

    class Meta:
        verbose_name_plural = '【中間DB】出走表_出走馬_過去成績'

    def __str__(self):
        return str(self.bamei) + ' ' + str(self.ck_kkhiduke)

# 【中間DB】入場人員
class Md_Nyujo(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "nyujo")  #競馬場マスタ
    tounyuujinin = IntegerField(verbose_name='当日入場人員')

    class Meta:
        verbose_name_plural = '【中間DB】入場人員'

    def __str__(self):
        return str(self.tounyuujinin)

# 【中間DB】売上金
class Md_Uriagekin(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "uriage")  #競馬場マスタ
    touuriage = IntegerField(verbose_name='当日売上')

    class Meta:
        verbose_name_plural = '【中間DB】売上金'

    def __str__(self):
        return str(self.touuriage)

# 【中間DB】成績・払戻
class Md_Seiseki_Haraimodoshi(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "seiseki_haraimodoshi")  #競馬場マスタ
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')

    # 競走年月日
    ck_kyounichi = DateField(verbose_name='競走年月日')
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')

    #当日情報
    tenkou = ForeignKey('Mst_Weather', verbose_name='天候マスタ', on_delete=CASCADE)  #天候マスタ
    md_bajyou = ForeignKey('Mst_Track_condition', verbose_name='馬場状態マスタ', on_delete=CASCADE)  #馬場状態マスタ
    md_sibada = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE, related_name = "tojitsu")  #芝・ダート区分マスタ
    ck_babamizu = IntegerField(verbose_name='馬場水分')

    #レース情報
    rebangou = IntegerField(verbose_name='レース番号')
    shubetsu = ForeignKey('Mst_Breed_age', verbose_name='競争種別', on_delete=CASCADE, related_name = "seiseki_shubetu")  #品種年齢区分マスタ
    tokusouhonsuu = IntegerField(verbose_name='特別競争本題回数')
    tokusoumeihon = CharField(verbose_name='特別競争名本題', max_length=100, blank=True, null=True)
    tokusoumeifuku = CharField(verbose_name='特別競争名副題', max_length=100, blank=True, null=True)
    ck_fukusyoumei = CharField(verbose_name='副賞名', max_length=100, blank=True, null=True) #複数ある場合繰り返すかリスト化する必要あり
    guredo = ForeignKey('Mst_Grade', verbose_name='グレード', on_delete=CASCADE, blank=True, null=True)  #グレードマスタ
    md_kyousousyu = ForeignKey('Mst_Race_type', verbose_name='競争種類コード', on_delete=CASCADE)  #競走種類マスタ
    ck_chuokouryu = ForeignKey('Mst_JRA_exchanges', verbose_name='中央交流区分', on_delete=CASCADE)  #中央交流区分マスタ
    kyori = IntegerField(verbose_name='競争距離')

    #トラック情報
    ck_shibadat = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE, related_name = "track")  #芝・ダート区分マスタ
    ck_naigai = ForeignKey('Mst_Course_class', verbose_name='コース区分', on_delete=CASCADE)  #コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class', verbose_name='回り区分', on_delete=CASCADE)  #回り区分マスタ
    ck_kknaita = ForeignKey('Mst_Night_race_class', verbose_name='ナイター区分マスタ', on_delete=CASCADE)  #ナイター区分マスタ

    ck_shokin1 = IntegerField(verbose_name='1着賞金')
    ck_shokin2 = IntegerField(verbose_name='2着賞金')
    ck_shokin3 = IntegerField(verbose_name='3着賞金')
    ck_shokin4 = IntegerField(verbose_name='4着賞金')
    ck_shokin5 = IntegerField(verbose_name='5着賞金')
    shusuu = IntegerField(verbose_name='出走頭数')
    jyoukenjouhou1 = CharField(verbose_name='競争条件１情報', max_length=30, blank=True, null=True)

    #競争条件情報
    bareijouken = ForeignKey('Mst_Breed_age', verbose_name='競争種別', on_delete=CASCADE, related_name="seiseki_barei")  #品種年齢区分マスタ
    ck_shikaku = CharField(verbose_name='競争資格条件', max_length=30, blank=True, null=True) # 複数ある場合、,で区切る
    ck_rkaku = CharField(verbose_name='レース格', max_length=20, blank=True, null=True) # 複数ある場合、,で区切る
    ck_rkumi = CharField(verbose_name='レース組', max_length=20, blank=True, null=True)  # 複数ある場合、,で区切る
    jyuuryoushubetsu = ForeignKey('Mst_Handicap', verbose_name='負担重量区分', on_delete=CASCADE)  #負担重量区分マスタ

    # 成績情報。最大16頭立て
    seiseki1 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績1', on_delete=CASCADE, related_name = "umaban_1", blank=True, null=True)  #成績マスタ
    seiseki2 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績2', on_delete=CASCADE, related_name = "umaban_2", blank=True, null=True)  #成績マスタ
    seiseki3 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績3', on_delete=CASCADE, related_name = "umaban_3", blank=True, null=True)  #成績マスタ
    seiseki4 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績4', on_delete=CASCADE, related_name = "umaban_4", blank=True, null=True)  #成績マスタ
    seiseki5 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績5', on_delete=CASCADE, related_name = "umaban_5", blank=True, null=True)  #成績マスタ
    seiseki6 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績6', on_delete=CASCADE, related_name = "umaban_6", blank=True, null=True)  #成績マスタ
    seiseki7 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績7', on_delete=CASCADE, related_name = "umaban_7", blank=True, null=True)  #成績マスタ
    seiseki8 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績8', on_delete=CASCADE, related_name = "umaban_8", blank=True, null=True)  #成績マスタ
    seiseki9 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績9', on_delete=CASCADE, related_name = "umaban_9", blank=True, null=True)  #成績マスタ
    seiseki10 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績10', on_delete=CASCADE, related_name = "umaban_10", blank=True, null=True)  #成績マスタ
    seiseki11 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績11', on_delete=CASCADE, related_name = "umaban_11", blank=True, null=True)  #成績マスタ
    seiseki12 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績12', on_delete=CASCADE, related_name = "umaban_12", blank=True, null=True)  #成績マスタ
    seiseki13 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績13', on_delete=CASCADE, related_name = "umaban_13", blank=True, null=True)  #成績マスタ
    seiseki14 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績14', on_delete=CASCADE, related_name = "umaban_14", blank=True, null=True)  #成績マスタ
    seiseki15 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績15', on_delete=CASCADE, related_name = "umaban_15", blank=True, null=True)  #成績マスタ
    seiseki16 = ForeignKey('Md_Seiseki_Haraimodoshi_seiseki', verbose_name='出走馬成績16', on_delete=CASCADE, related_name = "umaban_16", blank=True, null=True)  #成績マスタ
    
    # 払戻情報
    # 単勝払戻情報
    tanharajyoukyou = IntegerField(verbose_name='単勝払戻状況')
    tankumijoukyou = IntegerField(verbose_name='単勝組番状況')
    tansaki = IntegerField(verbose_name='単勝先番')
    tanharakin = IntegerField(verbose_name='単勝払戻金')
    tantounin = IntegerField(verbose_name='単勝投票人気')

    # 複勝払戻情報
    fukuharajoukyou = IntegerField(verbose_name='複勝払戻状況')
    fukukumijoukyou = IntegerField(verbose_name='複勝組番状況')
    fukusaki = IntegerField(verbose_name='複勝先番')
    tanharakin = IntegerField(verbose_name='複勝払戻金')
    fukuharakin = IntegerField(verbose_name='複勝投票人気')

    # 枠連複払戻情報
    wakupukuharajoukyou = IntegerField(verbose_name='枠連複払戻状況')
    wakupukukumijoukyou = IntegerField(verbose_name='枠連複組番状況')
    wakupukusaki = IntegerField(verbose_name='枠連複先番')
    wakupukuato = IntegerField(verbose_name='枠連複後番')
    wakupukuharakin = IntegerField(verbose_name='枠連複払戻金')
    wakupukutounin = IntegerField(verbose_name='枠連複投票人気')

    # 枠連単払戻情報
    ck_wakutanharajoukyou = IntegerField(verbose_name='枠連単払戻状況')
    ck_wakutankumijoukyou = IntegerField(verbose_name='枠連単組番状況')
    ck_wakutansaki = IntegerField(verbose_name='枠連単先番')
    ck_wakutanato = IntegerField(verbose_name='枠連単後番')
    ck_wakutanharakin = IntegerField(verbose_name='枠連単払戻金')
    ck_wakutantounin = IntegerField(verbose_name='枠連単投票人気')

    
    # 馬連複払戻情報
    umapukuharajoukyou = IntegerField(verbose_name='馬連複払戻状況')
    umapukukumijoukyou = IntegerField(verbose_name='馬連複組番状況')
    umapukusaki = IntegerField(verbose_name='馬連複先番')
    umapukuato = IntegerField(verbose_name='馬連複後番')
    umapukuharakin = IntegerField(verbose_name='馬連複払戻金')
    umapukutounin = IntegerField(verbose_name='馬連複投票人気')

    # 馬連単払戻情報
    umatanharajoukyou = IntegerField(verbose_name='馬連単払戻状況')
    umatankumijoukyou = IntegerField(verbose_name='馬連単組番状況')
    umatansaki = IntegerField(verbose_name='馬連単先番')
    umatanato = IntegerField(verbose_name='馬連単後番')
    umatanharakin = IntegerField(verbose_name='馬連単払戻金')
    umatantounin = IntegerField(verbose_name='馬連単投票人気')

    
    # 三連複複払戻情報
    sanpukuharajoukyou = IntegerField(verbose_name='三連複払戻状況')
    sanpukukumijoukyou = IntegerField(verbose_name='三連複組番状況')
    sanpukusaki = IntegerField(verbose_name='三連複先番')
    sanpukunaka = IntegerField(verbose_name='三連複中番')
    sanpukuato = IntegerField(verbose_name='三連複後番')
    sanpukuharakin = IntegerField(verbose_name='三連複払戻金')
    sanpukutounin = IntegerField(verbose_name='三連複投票人気')

    # 三連単払戻情報
    santanharajoukyou = IntegerField(verbose_name='三連単払戻状況')
    santankumijoukyou = IntegerField(verbose_name='三連単組番状況')
    santansaki = IntegerField(verbose_name='三連単先番')
    santannaka = IntegerField(verbose_name='三連単中番')
    santanato = IntegerField(verbose_name='三連単後番')
    santanharakin = IntegerField(verbose_name='三連単払戻金')
    santantounin = IntegerField(verbose_name='三連単投票人気')

    # ワイド払戻情報
    waharajoukyou = IntegerField(verbose_name='ワイド払戻状況')
    wakumijoukyou = IntegerField(verbose_name='ワイド組番状況')
    wasaki = IntegerField(verbose_name='ワイド先番')
    waato = IntegerField(verbose_name='ワイド後番')
    waharakin = IntegerField(verbose_name='ワイド払戻金')
    watounin = IntegerField(verbose_name='ワイド投票人気')

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou)+'R'


# 【中間DB】成績・払戻_成績
class Md_Seiseki_Haraimodoshi_seiseki(Model):

    #リレーション用の情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "seiseki")  #競馬場マスタ
    ck_kyounichi = DateField(verbose_name='競走年月日')
    rebangou = IntegerField(verbose_name='レース番号')

    #着順情報
    juni = IntegerField(verbose_name='順位')
    nyuusenjuni = IntegerField(verbose_name='入線順位')
    waku = IntegerField(verbose_name='枠番')
    uma = IntegerField(verbose_name='馬番')
    ck_boiro = CharField(verbose_name='帽色', max_length=10)
    bamei = CharField(verbose_name='馬名', max_length=10, blank=True, null=True)
    seibetsu = ForeignKey('Mst_Gender', verbose_name='性別', on_delete=CASCADE)  #性別マスタ
    barei = IntegerField(verbose_name='馬齢')
    fujuu = IntegerField(verbose_name='負担重量', blank=True, null=True)
    ck_sekijuu = IntegerField(verbose_name='積載重量', blank=True, null=True)

    kimei = CharField(verbose_name='騎手名', max_length=30)
    kimei_sei = CharField(verbose_name='騎手名_姓', max_length=20, blank=True, null=True)
    kimei_mei = CharField(verbose_name='騎手名_名', max_length=20, blank=True, null=True)
    ck_kimnbangou = IntegerField(verbose_name='騎手免許番号')
    mikubun = IntegerField(verbose_name='見習区分')
    md_genkigou = CharField(verbose_name='減量記号', max_length=3, blank=True, null=True)

    ck_maekimei = CharField(verbose_name='変更前騎手名', max_length=30)
    kimei_sei = CharField(verbose_name='変更前騎手名_姓', max_length=20, blank=True, null=True)
    kimei_mei = CharField(verbose_name='変更前騎手名_名', max_length=20, blank=True, null=True)

    ck_maekimnbangou = IntegerField(verbose_name='変更前騎手免許番号')
    ck_maemikubun = IntegerField(verbose_name='変更前騎手見習区分')
    ck_henriyuu = ForeignKey('Mst_Jockey_changed_reason', verbose_name='騎手変更理由', on_delete=CASCADE)  #騎手変更理由マスタ

    # タイム
    fun = IntegerField(verbose_name='分')
    byo = IntegerField(verbose_name='秒')
    miri = IntegerField(verbose_name='ミリ')
    reko = CharField(verbose_name='レコード', max_length=5, blank=True, null=True)

    #着差情報
    sa = ForeignKey('Mst_Margin', verbose_name='着差', on_delete=CASCADE)  #着差マスタ
    md_doutyaku = IntegerField(verbose_name='同着区分')
    sareigai = ForeignKey('Mst_Accident_type', verbose_name='着差例外', on_delete=CASCADE, related_name="chakusa_reigai")  #事故種類マスタ
    ck_jikosyu = ForeignKey('Mst_Accident_type', verbose_name='事故種別', on_delete=CASCADE, related_name="jiko_shubetu")  #事故種類マスタ
    ck_jikoriyuu = ForeignKey('Mst_Accident_reason', verbose_name='事故理由', on_delete=CASCADE)  #事故理由マスタ
    bajuu = IntegerField(verbose_name='馬体重')
    bajuuzougen = IntegerField(verbose_name='馬体重増減')
    choumei = CharField(verbose_name='調教師名', max_length=30)
    choumei_sei = CharField(verbose_name='調教師名_姓', max_length=20, blank=True, null=True)
    choumei_mei = CharField(verbose_name='調教師名_名', max_length=20, blank=True, null=True)
    ikubunnai = ForeignKey('Mst_Accident_type', verbose_name='異常区分内容', on_delete=CASCADE, related_name="ijou_kubun")  #事故種類マスタ

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_成績'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou)+'R ' + str(self.juni) +'着 ' + str(self.bamei)


# 【中間DB】コーナー・ラップ
class Md_Corner_Rap(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "corner_rap")  #競馬場マスタ
    kainichime = IntegerField(verbose_name='開催日目')

    #競争年月日
    ck_kyounichi = DateField(verbose_name='競走年月日')
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    rebangou = IntegerField(verbose_name='レース番号')

    #１着馬情報 最大３頭（同着を考慮）
    chaku1uma_1 = IntegerField(verbose_name='１着馬番')
    chaku1uma_2 = IntegerField(verbose_name='１着馬番(同着)')
    chaku1uma_3 = IntegerField(verbose_name='１着馬番(同着)(同着)   ')


    a4ha = IntegerField(verbose_name='上がり４ハロン')
    a3ha = IntegerField(verbose_name='上がり３ハロン')
    #ハロンラップタイム ハロン数分、繰り返す(,でつなげて格納？)
    ta = IntegerField(verbose_name='タイム')

    #コーナー順位情報　※先頭馬番がグループの場合は、馬番が若い番号を設定。
    kosentouuma = IntegerField(verbose_name='コーナー先頭馬番')
    #コーナー詳細
    koshousai_sa = IntegerField(verbose_name='差')
    #集団
    shuudan_sa = IntegerField(verbose_name='馬番')

    class Meta:
        verbose_name_plural = '【中間DB】コーナー・ラップ'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou) + 'R'
        
# 【中間DB】上がり
class Md_Agari(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "agari")  #競馬場マスタ
    kainichime = IntegerField(verbose_name='開催日目')

    #競争年月日
    ck_kyounichi = DateField(verbose_name='競走年月日')
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')

    #レース名
    rebangou = IntegerField(verbose_name='レース番号')

    # 馬情報
    uma = IntegerField(verbose_name='馬番')
    bamei = CharField(verbose_name='馬名', max_length=10)
    a3hakei = IntegerField(verbose_name='上がり３ハロン計')

    class Meta:
        verbose_name_plural = '【中間DB】上がり'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou) + 'R'

# 【中間DB】通信文
class Md_Tshuushinbun(Model):
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード', on_delete=CASCADE, related_name = "tsushinbun")  #競馬場マスタ
    kainichime = IntegerField(verbose_name='開催日目')

    #競争年月日
    ck_kyounichi = DateField(verbose_name='競走年月日')
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')

    #レース名
    rebangou = IntegerField(verbose_name='レース番号')
    
    # 付加文書内容
    ck_jishou = ForeignKey('Mst_Matter', verbose_name='事象', on_delete=CASCADE)  #事象マスタ
    ck_taishousya = ForeignKey('Mst_Target_person', verbose_name='対象者', on_delete=CASCADE)  #対象者マスタ
    uma = IntegerField(verbose_name='馬番')
    ck_jisyoumei = CharField(verbose_name='事象名', max_length=10)
    kijinai = CharField(verbose_name='記事内容', max_length=200)

    class Meta:
        verbose_name_plural = '【中間DB】通信文'

    def __str__(self):
        return str(self.ck_kyounichi) + str(self.joumei) + str(self.rebangou) + 'R'



# ここかCSV取り込み

# -------------------------------------------
#開催日割_BA7
class Schedule_BA7(models.Model):
    Data_ID = models.CharField(verbose_name="電文ID", max_length=3, null=True)
    held_year = models.CharField(verbose_name="開催年度", max_length=4, null=True)
    Organizer_times = models.CharField(verbose_name="主催者回次", max_length=2, null=True)
    Track_times = models.CharField(verbose_name="競馬場回次", max_length=2, null=True)
    Organizer_code = models.CharField(verbose_name="主催者コード", max_length=2, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Schedule_BA7_Jou_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_code = models.CharField(verbose_name="開催区分", max_length=1, null=True)
    Night_game_code = models.ForeignKey("Mst_Night_race_class", to_field="Night_race_code", related_name="Schedule_BA7_Night_game_code", on_delete=models.DO_NOTHING, verbose_name="ナイター開催区分", max_length=1, null=True)
    Dates = models.CharField(verbose_name="開催日数", max_length=1, null=True)
    Date_1 = models.CharField(verbose_name="開催年月日１", max_length=8, null=True)
    Day_code_1 = models.CharField(verbose_name="曜日コード１", max_length=2, null=True)
    Races_1 = models.CharField(verbose_name="レース数１", max_length=2, null=True)
    Postpone_date_1_1 = models.CharField(verbose_name="代替競走年月日１＿１", max_length=8, null=True)
    Postpone_day_code_1_1 = models.CharField(verbose_name="代替曜日コード１＿１", max_length=2, null=True)
    Postpone_start_1_1 = models.CharField(verbose_name="代替レース開始番号１＿１", max_length=2, null=True)
    Postpone_date_1_2 = models.CharField(verbose_name="代替競走年月日１＿２", max_length=8, null=True)
    Postpone_day_code_1_2 = models.CharField(verbose_name="代替曜日コード１＿２", max_length=2, null=True)
    Postpone_start_1_2 = models.CharField(verbose_name="代替レース開始番号１＿２", max_length=2, null=True)
    Date_2 = models.CharField(verbose_name="開催年月日２", max_length=8, null=True)
    Day_code_2 = models.CharField(verbose_name="曜日コード２", max_length=2, null=True)
    Races_2 = models.CharField(verbose_name="レース数２", max_length=2, null=True)
    Postpone_date_2_1 = models.CharField(verbose_name="代替競走年月日２＿１", max_length=8, null=True)
    Postpone_day_code_2_1 = models.CharField(verbose_name="代替曜日コード２＿１", max_length=2, null=True)
    Postpone_start_2_1 = models.CharField(verbose_name="代替レース開始番号２＿１", max_length=2, null=True)
    Postpone_date_2_2 = models.CharField(verbose_name="代替競走年月日２＿２", max_length=8, null=True)
    Postpone_day_code_2_2 = models.CharField(verbose_name="代替曜日コード２＿２", max_length=2, null=True)
    Postpone_start_2_2 = models.CharField(verbose_name="代替レース開始番号２＿２", max_length=2, null=True)
    Date_3 = models.CharField(verbose_name="開催年月日３", max_length=8, null=True)
    Day_code_3 = models.CharField(verbose_name="曜日コード３", max_length=2, null=True)
    Races_3 = models.CharField(verbose_name="レース数３", max_length=2, null=True)
    Postpone_date_3_1 = models.CharField(verbose_name="代替競走年月日３＿１", max_length=8, null=True)
    Postpone_day_code_3_1 = models.CharField(verbose_name="代替曜日コード３＿１", max_length=2, null=True)
    Postpone_start_3_1 = models.CharField(verbose_name="代替レース開始番号３＿１", max_length=2, null=True)
    Postpone_date_3_2 = models.CharField(verbose_name="代替競走年月日３＿２", max_length=8, null=True)
    Postpone_day_code_3_2 = models.CharField(verbose_name="代替曜日コード３＿２", max_length=2, null=True)
    Postpone_start_3_2 = models.CharField(verbose_name="代替レース開始番号３＿２", max_length=2, null=True)
    Date_4 = models.CharField(verbose_name="開催年月日４", max_length=8, null=True)
    Day_code_4 = models.CharField(verbose_name="曜日コード４", max_length=2, null=True)
    Races_4 = models.CharField(verbose_name="レース数４", max_length=2, null=True)
    Postpone_date_4_1 = models.CharField(verbose_name="代替競走年月日４＿１", max_length=8, null=True)
    Postpone_day_code_4_1 = models.CharField(verbose_name="代替曜日コード４＿１", max_length=2, null=True)
    Postpone_start_4_1 = models.CharField(verbose_name="代替レース開始番号４＿１", max_length=2, null=True)
    Postpone_date_4_2 = models.CharField(verbose_name="代替競走年月日４＿２", max_length=8, null=True)
    Postpone_day_code_4_2 = models.CharField(verbose_name="代替曜日コード４＿２", max_length=2, null=True)
    Postpone_start_4_2 = models.CharField(verbose_name="代替レース開始番号４＿２", max_length=2, null=True)
    Date_5 = models.CharField(verbose_name="開催年月日５", max_length=8, null=True)
    Day_code_5 = models.CharField(verbose_name="曜日コード５", max_length=2, null=True)
    Races_5 = models.CharField(verbose_name="レース数５", max_length=2, null=True)
    Postpone_date_5_1 = models.CharField(verbose_name="代替競走年月日５＿１", max_length=8, null=True)
    Postpone_day_code_5_1 = models.CharField(verbose_name="代替曜日コード５＿１", max_length=2, null=True)
    Postpone_start_5_1 = models.CharField(verbose_name="代替レース開始番号５＿１", max_length=2, null=True)
    Postpone_date_5_2 = models.CharField(verbose_name="代替競走年月日５＿２", max_length=8, null=True)
    Postpone_day_code_5_2 = models.CharField(verbose_name="代替曜日コード５＿２", max_length=2, null=True)
    Postpone_start_5_2 = models.CharField(verbose_name="代替レース開始番号５＿２", max_length=2, null=True)
    Date_6 = models.CharField(verbose_name="開催年月日６", max_length=8, null=True)
    Day_code_6 = models.CharField(verbose_name="曜日コード６", max_length=2, null=True)
    Races_6 = models.CharField(verbose_name="レース数６", max_length=2, null=True)
    Postpone_date_6_1 = models.CharField(verbose_name="代替競走年月日６＿１", max_length=8, null=True)
    Postpone_day_code_6_1 = models.CharField(verbose_name="代替曜日コード６＿１", max_length=2, null=True)
    Postpone_start_6_1 = models.CharField(verbose_name="代替レース開始番号６＿１", max_length=2, null=True)
    Postpone_date_6_2 = models.CharField(verbose_name="代替競走年月日６＿２", max_length=8, null=True)
    Postpone_day_code_6_2 = models.CharField(verbose_name="代替曜日コード６＿２", max_length=2, null=True)
    Postpone_start_6_2 = models.CharField(verbose_name="代替レース開始番号６＿２", max_length=2, null=True)

    class Meta:
        verbose_name_plural = '【CSV】開催日割_BA7'

    #本日施行情報ファイル_INI
class Trn_Enforcement_information_today_INI(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Enforcement_information_today_INI_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_day = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Track_times = models.CharField(verbose_name="競馬場回次", max_length=2, null=True)
    Races = models.CharField(verbose_name="施行レース数", max_length=2, null=True)

    class Meta:
        verbose_name_plural = '【CSV】本日施行情報_INI'

#出馬表Ａ_SUA
class Trn_Running_list_A_SUA(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Organizer_times = models.CharField(verbose_name="主催者回次", max_length=2, null=True)
    Track_times = models.CharField(verbose_name="競馬場回次", max_length=2, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Running_list_A_SUA_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Track_name = models.CharField(verbose_name="競馬場名称", max_length=4, null=True)
    Track_name_shortened = models.CharField(verbose_name="競馬場略称", max_length=2, null=True)
    Organizer_code = models.CharField(verbose_name="主催者コード", max_length=2, null=True)
    Organizer_name = models.CharField(verbose_name="主催者名称", max_length=10, null=True)
    Held_day = models.CharField(verbose_name="開催曜日", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Win_sale = models.CharField(verbose_name="単勝実施区分名", max_length=4, null=True)
    Place_sale = models.CharField(verbose_name="複勝実施区分名", max_length=4, null=True)
    Bracketquinella_sale = models.CharField(verbose_name="枠連複実施区分名", max_length=5, null=True)
    bracketexacta_sale = models.CharField(verbose_name="枠連単実施区分名", max_length=5, null=True)
    Quinella_sale = models.CharField(verbose_name="馬連複実施区分名", max_length=5, null=True)
    Exacta_sale = models.CharField(verbose_name="馬連単実施区分名", max_length=5, null=True)
    Race_type_code = models.ForeignKey("Mst_Race_type", to_field="Race_type_code", related_name="Trn_Running_list_A_SUA_Race_type_code", on_delete=models.DO_NOTHING, verbose_name="競走種類コード", max_length=1, null=True)
    Race_type_name = models.CharField(verbose_name="競走種類名称", max_length=3, null=True)
    Breed_age_code = models.ForeignKey("Mst_Breed_age", to_field="Breed_age_code", related_name="Trn_Running_list_A_SUA_Breed_age_code", on_delete=models.DO_NOTHING, verbose_name="品種年齢区分", max_length=2, null=True)
    Breed_age_name = models.CharField(verbose_name="品種年齢区分名称", max_length=7, null=True)
    Weight_code = models.ForeignKey("Mst_Handicap", to_field="Handicap_code", related_name="Trn_Running_list_A_SUA_Weight_code", on_delete=models.DO_NOTHING, verbose_name="負担重量区分", max_length=2, null=True)
    Weight_name = models.CharField(verbose_name="負担重量区分名称", max_length=3, null=True)
    Male_weight = models.CharField(verbose_name="雄負担重量", max_length=3, null=True)
    Female_weight = models.CharField(verbose_name="雌負担重量", max_length=3, null=True)
    Race_times = models.CharField(verbose_name="レース回次", max_length=2, null=True)
    Race_name = models.CharField(verbose_name="レース名称", max_length=40, null=True)
    Additional_name = models.CharField(verbose_name="付加名称", max_length=40, null=True)
    JRA_exchanges_code = models.ForeignKey("Mst_JRA_exchanges", to_field="JRA_exchanges_code", related_name="Trn_Running_list_A_SUA_JRA_exchanges_code", on_delete=models.DO_NOTHING, verbose_name="中央交流区分", max_length=1, null=True)
    Race_code = models.CharField(verbose_name="レースコード", max_length=4, null=True)
    Certified_race_code = models.CharField(verbose_name="認定競走区分", max_length=1, null=True)
    Grade_code = models.ForeignKey("Mst_Grade", to_field="Grade_code", related_name="Trn_Running_list_A_SUA_Grade_code", on_delete=models.DO_NOTHING, verbose_name="グレード区分", max_length=2, null=True)
    Grade_name = models.CharField(verbose_name="グレード区分名称", max_length=3, null=True)
    Night_race_code = models.ForeignKey("Mst_Night_race_class", to_field="Night_race_code", related_name="Trn_Running_list_A_SUA_Night_race_code", on_delete=models.DO_NOTHING, verbose_name="ナイターレース区分", max_length=1, null=True)
    Prize_money_1 = models.CharField(verbose_name="本賞金１", max_length=9, null=True)
    Prize_money_2 = models.CharField(verbose_name="本賞金２", max_length=9, null=True)
    Prize_money_3 = models.CharField(verbose_name="本賞金３", max_length=9, null=True)
    Prize_money_4 = models.CharField(verbose_name="本賞金４", max_length=9, null=True)
    Main_prize_5 = models.CharField(verbose_name="本賞金５", max_length=9, null=True)
    Additional_prize_1 = models.CharField(verbose_name="付加賞金１", max_length=9, null=True)
    Additional_prize_2 = models.CharField(verbose_name="付加賞金２", max_length=9, null=True)
    Additional_prize_3 = models.CharField(verbose_name="付加賞金３", max_length=9, null=True)
    Additional_prize_4 = models.CharField(verbose_name="付加賞金４", max_length=9, null=True)
    Additional_prize_5 = models.CharField(verbose_name="付加賞金５", max_length=9, null=True)
    Supplementary_prize_1 = models.CharField(verbose_name="副賞名１", max_length=20, null=True)
    Supplementary_prize_2 = models.CharField(verbose_name="副賞名２", max_length=20, null=True)
    Supplementary_prize_3 = models.CharField(verbose_name="副賞名３", max_length=20, null=True)
    Supplementary_prize_4 = models.CharField(verbose_name="副賞名４", max_length=20, null=True)
    Supplementary_prize_5 = models.CharField(verbose_name="副賞名５", max_length=20, null=True)
    Supplementary_prize_6 = models.CharField(verbose_name="副賞名６", max_length=20, null=True)
    Supplementary_prize_7 = models.CharField(verbose_name="副賞名７", max_length=20, null=True)
    Supplementary_prize_8 = models.CharField(verbose_name="副賞名８", max_length=20, null=True)
    Supplementary_prize_9 = models.CharField(verbose_name="副賞名９", max_length=20, null=True)
    Supplementary_prize_10 = models.CharField(verbose_name="副賞名１０", max_length=20, null=True)
    Supplementary_prize_11 = models.CharField(verbose_name="副賞名１１", max_length=20, null=True)
    Supplementary_prize_12 = models.CharField(verbose_name="副賞名１２", max_length=20, null=True)
    Supplementary_Award_13 = models.CharField(verbose_name="副賞名１３", max_length=20, null=True)
    Supplementary_prize_14 = models.CharField(verbose_name="副賞名１４", max_length=20, null=True)
    Supplementary_prize_15 = models.CharField(verbose_name="副賞名１５", max_length=20, null=True)
    Organizer_total_races = models.CharField(verbose_name="主催者通算競走番号", max_length=4, null=True)
    Scheduled_participation = models.CharField(verbose_name="出走予定頭数", max_length=2, null=True)
    Race_qualification_1 = models.CharField(verbose_name="競走資格条件１", max_length=4, null=True)
    Race_qualification_2 = models.CharField(verbose_name="競走資格条件２", max_length=8, null=True)
    Race_qualification_3 = models.CharField(verbose_name="競走資格条件３", max_length=8, null=True)
    Race_rank_1 = models.CharField(verbose_name="レース格１", max_length=2, null=True)
    Race_rank_2 = models.CharField(verbose_name="レース格２", max_length=4, null=True)
    Race_group_1 = models.CharField(verbose_name="レース組１", max_length=2, null=True)
    Race_group_2 = models.CharField(verbose_name="レース組２", max_length=4, null=True)
    Prize_amount_1 = models.CharField(verbose_name="賞金額１", max_length=9, null=True)
    Under_1 = models.CharField(verbose_name="文字１", max_length=2, null=True)
    Prize_amount_2 = models.CharField(verbose_name="賞金額２", max_length=9, null=True)
    Under_2 = models.CharField(verbose_name="文字２", max_length=2, null=True)
    Saddling_enclosure_time = models.CharField(verbose_name="装鞍所引付時刻", max_length=4, null=True)
    Start_time = models.CharField(verbose_name="発走時刻", max_length=4, null=True)
    Race_Distance = models.CharField(verbose_name="距離", max_length=4, null=True)
    Turf_dirt_code = models.ForeignKey("Mst_Turf_dirt_class", to_field="Turf_dirt_code", related_name="Trn_Running_list_A_SUA_Turf_dirt_code", on_delete=models.DO_NOTHING, verbose_name="芝ダート区分", max_length=1, null=True)
    Turf_Dart_name = models.CharField(verbose_name="芝ダート区分名称", max_length=3, null=True)
    Inner_outer_code = models.ForeignKey("Mst_Course_class", to_field="Course_class_code", related_name="Trn_Running_list_A_SUA_Inner_outer_code", on_delete=models.DO_NOTHING, verbose_name="内外コース区分", max_length=1, null=True)
    Inner_outer_name = models.CharField(verbose_name="内外コース区分名称", max_length=4, null=True)
    CW_or_CCW_code = models.ForeignKey("Mst_Clockwise_class", to_field="CW_or_CCW_code", related_name="Trn_Running_list_A_SUA_CW_or_CCW_code", on_delete=models.DO_NOTHING, verbose_name="回り区分", max_length=1, null=True)
    Weather_code = models.ForeignKey("Mst_Weather", to_field="Weather_code", related_name="Trn_Running_list_A_SUA_Weather_code", on_delete=models.DO_NOTHING, verbose_name="天候コード", max_length=1, null=True)
    Weather_name = models.CharField(verbose_name="天候名称", max_length=2, null=True)
    Track_condition_code = models.ForeignKey("Mst_Track_condition", to_field="Track_condition_code", related_name="Trn_Running_list_A_SUA_Track_condition_code", on_delete=models.DO_NOTHING, verbose_name="馬場状態コード", max_length=1, null=True)
    Track_condition_name = models.CharField(verbose_name="馬場状態名称", max_length=2, null=True)
    Track_moisture = models.CharField(verbose_name="馬場水分", max_length=3, null=True)
    Night_lighting = models.CharField(verbose_name="ナイタ照明点灯開始レース", max_length=2, null=True)
    Record_time = models.CharField(verbose_name="レコードタイム", max_length=4, null=True)
    Record_era = models.CharField(verbose_name="レコード年号", max_length=1, null=True)
    Record_race_date_JP = models.CharField(verbose_name="レコード競走年月日和暦", max_length=6, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Weight = models.CharField(verbose_name="負担重量", max_length=3, null=True)
    Jockey_name = models.CharField(verbose_name="騎手氏名", max_length=15, null=True)

    class Meta:
        verbose_name_plural = '【CSV】出馬表Ａ_SUA'

#出馬表Ｂ_SUB
class Trn_Running_list_B_SUB(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Running_list_B_SUB_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Bracket_No = models.CharField(verbose_name="枠番", max_length=2, null=True)
    Hat_color = models.CharField(verbose_name="帽色", max_length=1, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Horse_registration_No = models.CharField(verbose_name="馬登録番号", max_length=10, null=True)
    Horse_invitation_code = models.CharField(verbose_name="馬招待区分", max_length=1, null=True)
    Horse_classification = models.CharField(verbose_name="馬区分", max_length=1, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Horse_gender_code = models.ForeignKey("Mst_Gender", to_field="Horse_gender_code", related_name="Trn_Running_list_B_SUB_Horse_gender_code", on_delete=models.DO_NOTHING, verbose_name="馬性別コード", max_length=2, null=True)
    Horse_birth_date = models.CharField(verbose_name="馬生年月日", max_length=8, null=True)
    Horse_age = models.CharField(verbose_name="馬齢", max_length=2, null=True)
    Coat_color = models.CharField(verbose_name="毛色", max_length=3, null=True)
    Horse_name_change = models.CharField(verbose_name="馬名変更種類名", max_length=1, null=True)
    Old_horse_name = models.CharField(verbose_name="旧馬名", max_length=9, null=True)
    Horce_belonging_code = models.ForeignKey("Mst_Belonging", to_field="Belonging_code", related_name="Trn_Running_list_B_SUB_Horce_belonging_code", on_delete=models.DO_NOTHING, verbose_name="所属場コード", max_length=2, null=True)
    Location_code = models.CharField(verbose_name="所在地コード", max_length=2, null=True)
    Birth_pref = models.CharField(verbose_name="産地県名", max_length=4, null=True)
    Birth_town = models.CharField(verbose_name="産地町名", max_length=12, null=True)
    Breeder_name = models.CharField(verbose_name="生産者氏名", max_length=20, null=True)
    Arab_blood_volume = models.CharField(verbose_name="アラブ血量", max_length=5, null=True)
    Breed_name = models.CharField(verbose_name="品種名", max_length=3, null=True)
    Sire_breed_name = models.CharField(verbose_name="父品種名", max_length=3, null=True)
    Sire_name = models.CharField(verbose_name="父馬名", max_length=30, null=True)
    Mare_breed_name = models.CharField(verbose_name="母品種名", max_length=3, null=True)
    Mare_horse = models.CharField(verbose_name="母馬名", max_length=30, null=True)
    BroodMareSire_breed_name = models.CharField(verbose_name="母父品種名", max_length=3, null=True)
    BroodMareSire_name = models.CharField(verbose_name="母父馬名", max_length=30, null=True)
    Previous_horse_weight = models.CharField(verbose_name="前走馬体重", max_length=4, null=True)
    Case = models.CharField(verbose_name="格", max_length=2, null=True)
    Program_prize_money = models.CharField(verbose_name="番組賞金", max_length=11, null=True)
    Last_race_date = models.CharField(verbose_name="最終出走年月日", max_length=8, null=True)
    Weight = models.CharField(verbose_name="負担重量", max_length=3, null=True)
    Carry_weight = models.CharField(verbose_name="積載重量", max_length=5, null=True)
    Owner_Registration_No = models.CharField(verbose_name="馬主登録番号", max_length=10, null=True)
    Horse_owner_name = models.CharField(verbose_name="馬主氏名", max_length=30, null=True)
    Trainer_license_No = models.CharField(verbose_name="調教師免許番号", max_length=6, null=True)
    Trainer_name = models.CharField(verbose_name="調教師氏名", max_length=10, null=True)
    Trainer_shortened = models.CharField(verbose_name="調教師略名", max_length=3, null=True)
    Jockey_license_No = models.CharField(verbose_name="騎手免許番号", max_length=6, null=True)
    Jockey_name = models.CharField(verbose_name="騎手氏名", max_length=10, null=True)
    Jockey_shortened = models.CharField(verbose_name="騎手略名", max_length=3, null=True)
    Weight_handicap = models.CharField(verbose_name="減量重量", max_length=3, null=True)
    Weight_handicap_symbol = models.CharField(verbose_name="減量重量記号", max_length=1, null=True)
    Jockey_belong_stable = models.CharField(verbose_name="騎手所属厩舎名", max_length=3, null=True)
    Jockey_invitation_code = models.CharField(verbose_name="騎手招待区分", max_length=1, null=True)
    Jockey_invitation_name = models.CharField(verbose_name="騎手招待区分名称", max_length=1, null=True)
    Jockey_belonging_code = models.ForeignKey("Mst_Belonging", to_field="Belonging_code", related_name="Trn_Running_list_B_SUB_Jockey_belonging_code", on_delete=models.DO_NOTHING, verbose_name="騎手所属場コード", max_length=2, null=True)
    Jockey_location_code = models.CharField(verbose_name="騎手所在地コード", max_length=2, null=True)

    class Meta:
        verbose_name_plural = '【CSV】出馬表Ｂ_SUB'

#出馬表Ｃ_SUC
class Trn_Running_list_C_SUC(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Running_list_C_SUC_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=18, null=True)
    Run_history_classification = models.CharField(verbose_name="出走履歴区分", max_length=1, null=True)
    JRA_exchanges_code = models.ForeignKey("Mst_JRA_exchanges", to_field="JRA_exchanges_code", related_name="Trn_Running_list_C_SUC_JRA_exchanges_code", on_delete=models.DO_NOTHING, verbose_name="中央交流区分", max_length=1, null=True)
    Track_code = models.CharField(verbose_name="競馬場名称", max_length=4, null=True)
    Track_name_shortened = models.CharField(verbose_name="競馬場略名", max_length=3, null=True)
    Track_times = models.CharField(verbose_name="競馬場回次", max_length=2, null=True)
    Race_type_code = models.ForeignKey("Mst_Race_type", to_field="Race_type_code", related_name="Trn_Running_list_C_SUC_Race_type_code", on_delete=models.DO_NOTHING, verbose_name="競走種類コード", max_length=1, null=True)
    Race_Distance = models.CharField(verbose_name="距離", max_length=4, null=True)
    Night_race_code = models.ForeignKey("Mst_Night_race_class", to_field="Night_race_code", related_name="Trn_Running_list_C_SUC_Night_race_code", on_delete=models.DO_NOTHING, verbose_name="ナイターレース区分", max_length=1, null=True)
    Breed_age_code = models.ForeignKey("Mst_Breed_age", to_field="Breed_age_code", related_name="Trn_Running_list_C_SUC_Breed_age_code", on_delete=models.DO_NOTHING, verbose_name="品種年齢区分", max_length=2, null=True)
    Race_times = models.CharField(verbose_name="レース回次", max_length=3, null=True)
    Race_name = models.CharField(verbose_name="レース名称", max_length=40, null=True)
    Grade_code = models.ForeignKey("Mst_Grade", to_field="Grade_code", related_name="Trn_Running_list_C_SUC_Grade_code", on_delete=models.DO_NOTHING, verbose_name="グレード区分", max_length=2, null=True)
    Race_qualification_1 = models.CharField(verbose_name="競走資格条件１", max_length=4, null=True)
    Race_qualification_2 = models.CharField(verbose_name="競走資格条件２", max_length=4, null=True)
    Race_qualification_3 = models.CharField(verbose_name="競走資格条件３", max_length=4, null=True)
    Race_rank_1 = models.CharField(verbose_name="レース格１", max_length=2, null=True)
    Race_rank_2 = models.CharField(verbose_name="レース格２", max_length=2, null=True)
    Race_group_1 = models.CharField(verbose_name="レース組１", max_length=2, null=True)
    Race_group_2 = models.CharField(verbose_name="レース組２", max_length=2, null=True)
    Prize_amount_1 = models.CharField(verbose_name="賞金額１", max_length=9, null=True)
    Under_1 = models.CharField(verbose_name="文字１", max_length=2, null=True)
    Prize_amount_2 = models.CharField(verbose_name="賞金額２", max_length=9, null=True)
    Under_2 = models.CharField(verbose_name="文字２", max_length=2, null=True)
    Weather_code = models.ForeignKey("Mst_Weather", to_field="Weather_code", related_name="Trn_Running_list_C_SUC_Weather_code", on_delete=models.DO_NOTHING, verbose_name="天候コード", max_length=1, null=True)
    Weather_name = models.CharField(verbose_name="天候名称", max_length=2, null=True)
    Track_condition_code = models.ForeignKey("Mst_Track_condition", to_field="Track_condition_code", related_name="Trn_Running_list_C_SUC_Track_condition_code", on_delete=models.DO_NOTHING, verbose_name="馬場状態コード", max_length=1, null=True)
    Track_condition_name = models.CharField(verbose_name="馬場状態名称", max_length=2, null=True)
    Track_moisture = models.CharField(verbose_name="馬場水分", max_length=3, null=True)
    Turf_dirt_code = models.CharField(verbose_name="芝ダート区分", max_length=1, null=True)
    Turf_Dart_name = models.CharField(verbose_name="芝ダート区分名称", max_length=3, null=True)
    Inner_outer_code = models.ForeignKey("Mst_Course_class", to_field="Course_class_code", related_name="Trn_Running_list_C_SUC_Inner_outer_code", on_delete=models.DO_NOTHING, verbose_name="内外コース区分", max_length=1, null=True)
    Inner_outer_name = models.CharField(verbose_name="内外コース区分名称", max_length=4, null=True)
    CW_or_CCW_code = models.ForeignKey("Mst_Clockwise_class", to_field="CW_or_CCW_code", related_name="Trn_Running_list_C_SUC_CW_or_CCW_code", on_delete=models.DO_NOTHING, verbose_name="回り区分", max_length=1, null=True)
    Participation = models.CharField(verbose_name="出走頭数", max_length=2, null=True)
    Horse_gender_code = models.ForeignKey("Mst_Gender", to_field="Horse_gender_code", related_name="Trn_Running_list_C_SUC_Horse_gender_code", on_delete=models.DO_NOTHING, verbose_name="性別コード", max_length=1, null=True)
    Bracket_No = models.CharField(verbose_name="枠番", max_length=2, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Horse_weight = models.CharField(verbose_name="馬体重", max_length=4, null=True)
    Weight = models.CharField(verbose_name="負担重量", max_length=3, null=True)
    Carry_weight = models.CharField(verbose_name="積載重量", max_length=5, null=True)
    Trainer_license_No = models.CharField(verbose_name="調教師免許番号", max_length=6, null=True)
    Trainer_shortened = models.CharField(verbose_name="調教師略名", max_length=3, null=True)
    Jockey_license_No = models.CharField(verbose_name="騎手免許番号", max_length=6, null=True)
    Jockey_shortened = models.CharField(verbose_name="騎手略名", max_length=3, null=True)
    Weight_handicap = models.CharField(verbose_name="減量後重量", max_length=3, null=True)
    Weight_handicap_symbol = models.CharField(verbose_name="減量重量記号", max_length=1, null=True)
    Result = models.CharField(verbose_name="着", max_length=2, null=True)
    Margin_code_1 = models.ForeignKey("Mst_Margin", to_field="Margin_code", related_name="Trn_Running_list_C_SUC_Margin_code_1", on_delete=models.DO_NOTHING, verbose_name="着差コード１", max_length=2, null=True)
    Margin_1 = models.CharField(verbose_name="着差１", max_length=4, null=True)
    Margin_code_2 = models.ForeignKey("Mst_Margin", to_field="Margin_code", related_name="Trn_Running_list_C_SUC_Margin_code_2", on_delete=models.DO_NOTHING, verbose_name="着差コード２", max_length=2, null=True)
    Margin_2 = models.CharField(verbose_name="着差２", max_length=4, null=True)
    Margin_code_3 = models.ForeignKey("Mst_Margin", to_field="Margin_code", related_name="Trn_Running_list_C_SUC_Margin_code_3", on_delete=models.DO_NOTHING, verbose_name="着差コード３", max_length=2, null=True)
    Margin_3 = models.CharField(verbose_name="着差３", max_length=4, null=True)
    Deadheat_code = models.CharField(verbose_name="同着区分", max_length=1, null=True)
    Finish_time = models.CharField(verbose_name="タイム", max_length=4, null=True)
    Finish_line_result = models.CharField(verbose_name="入線着", max_length=2, null=True)
    Accident_code = models.ForeignKey("Mst_Accident_type", to_field="Accident_type_code", related_name="Trn_Running_list_C_SUC_Accident_code", on_delete=models.DO_NOTHING, verbose_name="事故種類コード", max_length=2, null=True)
    Accident_name = models.CharField(verbose_name="事故種類名称", max_length=5, null=True)
    Accident_reason_code = models.ForeignKey("Mst_Accident_reason", to_field="Accident_reason_code", related_name="Trn_Running_list_C_SUC_Accident_reason_code", on_delete=models.DO_NOTHING, verbose_name="事故理由コード", max_length=2, null=True)
    Accident_reason_name = models.CharField(verbose_name="事故理由名称", max_length=7, null=True)
    Prize_money = models.CharField(verbose_name="本賞金", max_length=9, null=True)
    Additional_prize = models.CharField(verbose_name="付加賞金", max_length=9, null=True)
    Corner_passing_rank_1 = models.CharField(verbose_name="コーナー通過順位１", max_length=2, null=True)
    Corner_passing_rank_2 = models.CharField(verbose_name="コーナー通過順位２", max_length=2, null=True)
    Corner_passing_rank_3 = models.CharField(verbose_name="コーナー通過順位３", max_length=2, null=True)
    Corner_passing_rank_4 = models.CharField(verbose_name="コーナー通過順位４", max_length=2, null=True)
    Corner_passing_rank_5 = models.CharField(verbose_name="コーナー通過順位５", max_length=2, null=True)
    Corner_passing_rank_6 = models.CharField(verbose_name="コーナー通過順位６", max_length=2, null=True)
    Corner_passing_rank_7 = models.CharField(verbose_name="コーナー通過順位７", max_length=2, null=True)
    Corner_passing_rank_8 = models.CharField(verbose_name="コーナー通過順位８", max_length=2, null=True)
    Last_3furlong = models.CharField(verbose_name="上がり３ハロン", max_length=3, null=True)
    Win_Pic = models.CharField(verbose_name="人気度", max_length=2, null=True)
    Winner_finish_time = models.CharField(verbose_name="相手馬タイム", max_length=4, null=True)
    Winner = models.CharField(verbose_name="相手馬名", max_length=18, null=True)

    class Meta:
        verbose_name_plural = '【CSV】出馬表Ｃ_SUC'

#出馬表Ｄ_SUD
class Trn_Running_list_D_SUD(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Jockey_shortened = models.CharField(verbose_name="騎手略名", max_length=3, null=True)
    Stats_win = models.CharField(verbose_name="着別成績（全成績１着）", max_length=3, null=True)
    Stats_2nd = models.CharField(verbose_name="着別成績（全成績２着）", max_length=3, null=True)
    Stats_3rd = models.CharField(verbose_name="着別成績（全成績３着）", max_length=3, null=True)
    Stats_other = models.CharField(verbose_name="着別成績（全成績着外）", max_length=3, null=True)
    Stats_CCW_dirt_win = models.CharField(verbose_name="着別成績（左回りダート１着）", max_length=3, null=True)
    Stats_CCW_dirt_2nd = models.CharField(verbose_name="着別成績（左回りダート２着）", max_length=3, null=True)
    Stats_CCW_dirt_3rd = models.CharField(verbose_name="着別成績（左回りダート３着）", max_length=3, null=True)
    Stats_CCW_dirt_other = models.CharField(verbose_name="着別成績（左回りダート着外）", max_length=3, null=True)
    Stats_CW_dirt_win = models.CharField(verbose_name="着別成績（右回りダート１着）", max_length=3, null=True)
    Stats_CW_dirt_2nd = models.CharField(verbose_name="着別成績（右回りダート２着）", max_length=3, null=True)
    Stats_CW_dirt_3rd = models.CharField(verbose_name="着別成績（右回りダート３着）", max_length=3, null=True)
    Stats_CW_dirt_other = models.CharField(verbose_name="着別成績（右回りダート着外）", max_length=3, null=True)
    Stats_track_win = models.CharField(verbose_name="該当競馬場芝ｏｒダート成績１着", max_length=3, null=True)
    Stats_track_2nd = models.CharField(verbose_name="該当競馬場芝ｏｒダート成績２着", max_length=3, null=True)
    Stats_track_3rd = models.CharField(verbose_name="該当競馬場芝ｏｒダート成績３着", max_length=3, null=True)
    Stats_track_other = models.CharField(verbose_name="該当競馬場芝ｏｒダート成績着外", max_length=3, null=True)
    Stats_short_distance_win = models.CharField(verbose_name="短距離成績１着", max_length=3, null=True)
    Stats_short_distance_2nd = models.CharField(verbose_name="短距離成績２着", max_length=3, null=True)
    Stats_short_distance_3rd = models.CharField(verbose_name="短距離成績３着", max_length=3, null=True)
    Stats_short_distance_other = models.CharField(verbose_name="短距離成績着外", max_length=3, null=True)
    Stats_middle_distance_win = models.CharField(verbose_name="中距離成績１着", max_length=3, null=True)
    Stats_middle_distance_2nd = models.CharField(verbose_name="中距離成績２着", max_length=3, null=True)
    Stats_middle_distance_3rd = models.CharField(verbose_name="中距離成績３着", max_length=3, null=True)
    Stats_middle_distance_other = models.CharField(verbose_name="中距離成績着外", max_length=3, null=True)
    Stats_long_distance_win = models.CharField(verbose_name="長距離成績１着", max_length=3, null=True)
    Stats_long_distance_2nd = models.CharField(verbose_name="長距離成績２着", max_length=3, null=True)
    Stats_long_distance_3rd = models.CharField(verbose_name="長距離成績３着", max_length=3, null=True)
    Stats_long_distance_other = models.CharField(verbose_name="長距離成績着外", max_length=3, null=True)
    Stats_jockey_win = models.CharField(verbose_name="騎乗騎手成績１着", max_length=3, null=True)
    Stats_jockey_2nd = models.CharField(verbose_name="騎乗騎手成績２着", max_length=3, null=True)
    Stats_jockey_3rd = models.CharField(verbose_name="騎乗騎手成績３着", max_length=3, null=True)
    Stats_jockey_other = models.CharField(verbose_name="騎乗騎手成績着外", max_length=3, null=True)
    
    class Meta:
        verbose_name_plural = '【CSV】出馬表Ｄ_SUD'

#出馬表Ｅ_SUE
class Trn_Running_list_E_SUE(models.Model):
    Data_ID = models.CharField(verbose_name="電文ID", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Track_code = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Held_times = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Running_list_E_SUE_Held_times", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Race_No = models.CharField(verbose_name="距離", max_length=4, null=True)
    Turf_dirt_code = models.ForeignKey("Mst_Turf_dirt_class", to_field="Turf_dirt_code", related_name="Trn_Running_list_E_SUE_Turf_dirt_code", on_delete=models.DO_NOTHING, verbose_name="芝ダート区分", max_length=1, null=True)
    Track_condition_code = models.ForeignKey("Mst_Track_condition", to_field="Track_condition_code", related_name="Trn_Running_list_E_SUE_Track_condition_code", on_delete=models.DO_NOTHING, verbose_name="馬場状態コード", max_length=1, null=True)
    Stats_track_win = models.CharField(verbose_name="１着回数", max_length=3, null=True)
    Stats_track_2nd = models.CharField(verbose_name="２着回数", max_length=3, null=True)
    Stats_track_3rd = models.CharField(verbose_name="３着回数", max_length=3, null=True)
    Stats_track_other = models.CharField(verbose_name="着外回数", max_length=3, null=True)
    Earned_prize_money = models.CharField(verbose_name="収得賞金", max_length=10, null=True)
    Best_time = models.CharField(verbose_name="最高タイム", max_length=4, null=True)
        
    class Meta:
        verbose_name_plural = '【CSV】出馬表Ｅ_SUE'

#取消除外_SU1
class Trn_Cancellation_exclusion_SU1(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Cancellation_exclusion_SU1_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Trainer_license_No = models.CharField(verbose_name="調教師免許番号", max_length=6, null=True)
    Trainer_name = models.CharField(verbose_name="調教師氏名", max_length=10, null=True)
    Accident_code = models.ForeignKey("Mst_Accident_type", to_field="Accident_type_code", related_name="Trn_Cancellation_exclusion_SU1_Accident_code", on_delete=models.DO_NOTHING, verbose_name="事故種類コード", max_length=2, null=True)
    Accident_name = models.CharField(verbose_name="事故種類名称", max_length=5, null=True)
    Accident_reason_code = models.ForeignKey("Mst_Accident_reason", to_field="Accident_reason_code", related_name="Trn_Cancellation_exclusion_SU1_Accident_reason_code", on_delete=models.DO_NOTHING, verbose_name="事故理由コード", max_length=2, null=True)
    Accident_reason_name = models.CharField(verbose_name="事故理由名称", max_length=7, null=True)

    class Meta:
        verbose_name_plural = '【CSV】取消除外_SU1'

#騎乗変更_SU3
class Trn_Change_riding_SU3(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Change_riding_SU3_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Horse_name = models.CharField(verbose_name="馬名", max_length=9, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Weight = models.CharField(verbose_name="負担重量", max_length=3, null=True)
    Carry_weight = models.CharField(verbose_name="積載重量", max_length=5, null=True)
    Jockey_license_No = models.CharField(verbose_name="騎手免許番号", max_length=6, null=True)
    Jockey_name = models.CharField(verbose_name="騎手氏名", max_length=10, null=True)
    Jockey_shortened = models.CharField(verbose_name="騎手略名", max_length=3, null=True)
    Weight_handicap = models.CharField(verbose_name="減量重量", max_length=2, null=True)
    Weight_handicap_symbol = models.CharField(verbose_name="減量重量記号", max_length=1, null=True)
    Jockey_belong_stable = models.CharField(verbose_name="騎手所属厩舎名", max_length=3, null=True)
    Jockey_invitation_code = models.CharField(verbose_name="騎手招待区分", max_length=1, null=True)
    Jockey_belonging_code = models.ForeignKey("Mst_Belonging", to_field="Belonging_code", related_name="Trn_Change_riding_SU3_Jockey_belonging_code", on_delete=models.DO_NOTHING, verbose_name="騎手所属場コード", max_length=2, null=True)
    Jockey_location_code = models.CharField(verbose_name="騎手所在地コード", max_length=2, null=True)
    Jockey_license_No_1 = models.CharField(verbose_name="変更騎手免許番号１", max_length=6, null=True)
    Jockey_name_1 = models.CharField(verbose_name="変更騎手氏名１", max_length=10, null=True)
    Jockey_shortened_1 = models.CharField(verbose_name="変更騎手略名１", max_length=3, null=True)
    Weight_handicap_1 = models.CharField(verbose_name="変更減量重量１", max_length=2, null=True)
    Weight_handicap_symbol_1 = models.CharField(verbose_name="変更減量重量記号１", max_length=1, null=True)
    Jockey_changed_reason_code_1 = models.ForeignKey("Mst_Jockey_changed_reason", to_field="Jockey_changed_reason_code", related_name="Trn_Change_riding_SU3_Jockey_changed_reason_code_1", on_delete=models.DO_NOTHING, verbose_name="騎手変更理由コード１", max_length=2, null=True)
    Jockey_changed_reason_name_1 = models.CharField(verbose_name="騎手変更理由名称１", max_length=4, null=True)
    Jockey_belong_stable_1 = models.CharField(verbose_name="変更騎手所属厩舎名１", max_length=3, null=True)
    Jockey_invitation_code_1 = models.CharField(verbose_name="変更騎手招待区分１", max_length=1, null=True)
    Jockey_belonging_code_1 = models.ForeignKey("Mst_Belonging", to_field="Belonging_code", related_name="Trn_Change_riding_SU3_Jockey_belonging_code_1", on_delete=models.DO_NOTHING, verbose_name="変更騎手所属場コード１", max_length=2, null=True)
    Jockey_location_code_1 = models.CharField(verbose_name="変更騎手所在地コード１", max_length=2, null=True)
    Jockey_license_No_2 = models.CharField(verbose_name="変更騎手免許番号２", max_length=6, null=True)
    Jockey_name_2 = models.CharField(verbose_name="変更騎手氏名２", max_length=10, null=True)
    Jockey_shortened_2 = models.CharField(verbose_name="変更騎手略名２", max_length=3, null=True)
    Weight_handicap_2 = models.CharField(verbose_name="変更減量重量２", max_length=2, null=True)
    Weight_handicap_symbol_2 = models.CharField(verbose_name="変更減量重量記号２", max_length=1, null=True)
    Jockey_changed_reason_code_2 = models.ForeignKey("Mst_Jockey_changed_reason", to_field="Jockey_changed_reason_code", related_name="Trn_Change_riding_SU3_Jockey_changed_reason_code_2", on_delete=models.DO_NOTHING, verbose_name="騎手変更理由コード２", max_length=2, null=True)
    Jockey_changed_reason_name_2 = models.CharField(verbose_name="騎手変更理由名称２", max_length=4, null=True)
    Jockey_belong_stable_2 = models.CharField(verbose_name="変更騎手所属厩舎名２", max_length=3, null=True)
    Jockey_invitation_code_2 = models.CharField(verbose_name="変更騎手招待区分２", max_length=1, null=True)
    Jockey_belonging_code_2 = models.ForeignKey("Mst_Belonging", to_field="Belonging_code", related_name="Trn_Change_riding_SU3_Jockey_belonging_code_2", on_delete=models.DO_NOTHING, verbose_name="変更騎手所属場コード２", max_length=2, null=True)
    Jockey_location_code_2 = models.CharField(verbose_name="変更騎手所在地コード２", max_length=2, null=True)

    class Meta:
        verbose_name_plural = '【CSV】騎乗変更_SU3'

#コーナ通過順_BA2
class Trn_Corner_passing_order_BA2(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Corner_passing_order_BA2_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Track_name = models.CharField(verbose_name="競馬場名称", max_length=4, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Corner_name_1 = models.CharField(verbose_name="コーナ名称１", max_length=8, null=True)
    Corner_passing_rank_1 = models.CharField(verbose_name="コーナ通過順１", max_length=55, null=True)
    Corner_name_2 = models.CharField(verbose_name="コーナ名称２", max_length=8, null=True)
    Corner_passing_rank_2 = models.CharField(verbose_name="コーナ通過順２", max_length=55, null=True)
    Corner_name_3 = models.CharField(verbose_name="コーナ名称３", max_length=8, null=True)
    Corner_passing_rank_3 = models.CharField(verbose_name="コーナ通過順３", max_length=55, null=True)
    Corner_name_4 = models.CharField(verbose_name="コーナ名称４", max_length=8, null=True)
    Corner_passing_rank_4 = models.CharField(verbose_name="コーナ通過順４", max_length=55, null=True)
    Corner_name_5 = models.CharField(verbose_name="コーナ名称５", max_length=8, null=True)
    Corner_passing_rank_5 = models.CharField(verbose_name="コーナ通過順５", max_length=55, null=True)
    Corner_name_6 = models.CharField(verbose_name="コーナ名称６", max_length=8, null=True)
    Corner_passing_rank_6 = models.CharField(verbose_name="コーナ通過順６", max_length=55, null=True)
    Corner_name_7 = models.CharField(verbose_name="コーナ名称７", max_length=8, null=True)
    Corner_passing_rank_7 = models.CharField(verbose_name="コーナ通過順７", max_length=55, null=True)
    Corner_name_8 = models.CharField(verbose_name="コーナ名称８", max_length=8, null=True)
    Corner_passing_rank_8 = models.CharField(verbose_name="コーナ通過順８", max_length=55, null=True)

    class Meta:
        verbose_name_plural = '【CSV】コーナ通過順_BA2'

#ハロンタイム_BA3
class Trn_Fallon_time_BA3(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Fallon_time_BA3_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Track_name = models.CharField(verbose_name="競馬場名称", max_length=4, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Furlong_time_1 = models.CharField(verbose_name="ハロンタイム１", max_length=3, null=True)
    Furlong_time_2 = models.CharField(verbose_name="ハロンタイム２", max_length=3, null=True)
    Furlong_time_3 = models.CharField(verbose_name="ハロンタイム３", max_length=3, null=True)
    Furlong_time_4 = models.CharField(verbose_name="ハロンタイム４", max_length=3, null=True)
    Furlong_time_5 = models.CharField(verbose_name="ハロンタイム５", max_length=3, null=True)
    Furlong_time_6 = models.CharField(verbose_name="ハロンタイム６", max_length=3, null=True)
    Furlong_time_7 = models.CharField(verbose_name="ハロンタイム７", max_length=3, null=True)
    Furlong_time_8 = models.CharField(verbose_name="ハロンタイム８", max_length=3, null=True)
    Furlong_time_9 = models.CharField(verbose_name="ハロンタイム９", max_length=3, null=True)
    Furlong_time_10 = models.CharField(verbose_name="ハロンタイム１０", max_length=3, null=True)
    Furlong_time_11 = models.CharField(verbose_name="ハロンタイム１１", max_length=3, null=True)
    Furlong_time_12 = models.CharField(verbose_name="ハロンタイム１２", max_length=3, null=True)
    Furlong_time_13 = models.CharField(verbose_name="ハロンタイム１３", max_length=3, null=True)
    Furlong_time_14 = models.CharField(verbose_name="ハロンタイム１４", max_length=3, null=True)
    Furlong_time_15 = models.CharField(verbose_name="ハロンタイム１５", max_length=3, null=True)
    Last_3furlong = models.CharField(verbose_name="上がり３ハロン", max_length=3, null=True)
    Last_4furlong = models.CharField(verbose_name="上がり４ハロン", max_length=3, null=True)

    class Meta:
        verbose_name_plural = '【CSV】ハロンタイム_BA3'

#上がり３ハロン_BA4
class Last_3_Fallon_BA4(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Last_3_Fallon_BA4_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Track_name = models.CharField(verbose_name="競馬場名称", max_length=4, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Last_3furlong_1 = models.CharField(verbose_name="上がり３ハロン１", max_length=3, null=True)
    Last_3furlong_2 = models.CharField(verbose_name="上がり３ハロン２", max_length=3, null=True)
    Last_3furlong_3 = models.CharField(verbose_name="上がり３ハロン３", max_length=3, null=True)
    Last_3furlong_4 = models.CharField(verbose_name="上がり３ハロン４", max_length=3, null=True)
    Last_3furlong_5 = models.CharField(verbose_name="上がり３ハロン５", max_length=3, null=True)
    Last_3furlong_6 = models.CharField(verbose_name="上がり３ハロン６", max_length=3, null=True)
    Last_3furlong_7 = models.CharField(verbose_name="上がり３ハロン７", max_length=3, null=True)
    Last_3furlong_8 = models.CharField(verbose_name="上がり３ハロン８", max_length=3, null=True)
    Last_3furlong_9 = models.CharField(verbose_name="上がり３ハロン９", max_length=3, null=True)
    Last_3furlong_10 = models.CharField(verbose_name="上がり３ハロン１０", max_length=3, null=True)
    Last_3furlong_11 = models.CharField(verbose_name="上がり３ハロン１１", max_length=3, null=True)
    Last_3furlong_12 = models.CharField(verbose_name="上がり３ハロン１２", max_length=3, null=True)
    Last_3furlong_13 = models.CharField(verbose_name="上がり３ハロン１３", max_length=3, null=True)
    Last_3furlong_14 = models.CharField(verbose_name="上がり３ハロン１４", max_length=3, null=True)
    Last_3furlong_15 = models.CharField(verbose_name="上がり３ハロン１５", max_length=3, null=True)
    Last_3furlong_16 = models.CharField(verbose_name="上がり３ハロン１６", max_length=3, null=True)

    class Meta:
        verbose_name_plural = '【CSV】上がり３ハロン_BA4'

#入場人員_BA5
class Trn_Visitors_BA5(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Visitors_BA5_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Paid_visitors = models.CharField(verbose_name="有料入場人員", max_length=6, null=True)
    Free_visitors = models.CharField(verbose_name="無料入場人員", max_length=6, null=True)

    class Meta:
        verbose_name_plural = '【CSV】入場人員_BA5'

#付加文書_BU1
class Trn_Attached_document_BU1(models.Model):
    Data_ID = models.CharField(verbose_name="電文ＩＤ", max_length=3, null=True)
    Race_date = models.CharField(verbose_name="競走年月日", max_length=8, null=True)
    Track_code = models.ForeignKey("Mst_Jou", to_field="Jou_code", related_name="Trn_Attached_document_BU1_Track_code", on_delete=models.DO_NOTHING, verbose_name="競馬場コード", max_length=2, null=True)
    Held_times = models.CharField(verbose_name="開催日次", max_length=1, null=True)
    Race_No = models.CharField(verbose_name="レース番号", max_length=2, null=True)
    Output_order = models.CharField(verbose_name="出力順", max_length=2, null=True)
    Event_code = models.ForeignKey("Mst_Matter", to_field="Matter_code", related_name="Trn_Attached_document_BU1_Event_code", on_delete=models.DO_NOTHING, verbose_name="事象", max_length=1, null=True)
    Accident_type_order = models.CharField(verbose_name="事故種類入力順", max_length=2, null=True)
    Target_person = models.ForeignKey("Mst_Target_person", to_field="Target_person_code", related_name="Trn_Attached_document_BU1_Target_person", on_delete=models.DO_NOTHING, verbose_name="対象者", max_length=2, null=True)
    Horse_No = models.CharField(verbose_name="馬番", max_length=2, null=True)
    Event_name = models.CharField(verbose_name="事象名", max_length=7, null=True)
    Attached_document_1 = models.CharField(verbose_name="レース付加文書１", max_length=30, null=True)
    Attached_document_2 = models.CharField(verbose_name="レース付加文書２", max_length=30, null=True)
    Attached_document_3 = models.CharField(verbose_name="レース付加文書３", max_length=30, null=True)
    Attached_document_4 = models.CharField(verbose_name="レース付加文書４", max_length=30, null=True)
    Attached_document_5 = models.CharField(verbose_name="レース付加文書５", max_length=30, null=True)
    Attached_document_6 = models.CharField(verbose_name="レース付加文書６", max_length=30, null=True)
    Attached_document_7 = models.CharField(verbose_name="レース付加文書７", max_length=30, null=True)
    Attached_document_8 = models.CharField(verbose_name="レース付加文書８", max_length=30, null=True)
    Attached_document_9 = models.CharField(verbose_name="レース付加文書９", max_length=30, null=True)
    Attached_document_10 = models.CharField(verbose_name="レース付加文書１０", max_length=30, null=True)
    Attached_document_11 = models.CharField(verbose_name="レース付加文書１１", max_length=30, null=True)
    Attached_document_12 = models.CharField(verbose_name="レース付加文書１２", max_length=30, null=True)
    Attached_document_13 = models.CharField(verbose_name="レース付加文書１３", max_length=30, null=True)
    Attached_document_14 = models.CharField(verbose_name="レース付加文書１４", max_length=30, null=True)
    Attached_document_15 = models.CharField(verbose_name="レース付加文書１５", max_length=30, null=True)
    Attached_document_16 = models.CharField(verbose_name="レース付加文書１６", max_length=30, null=True)

    class Meta:
        verbose_name_plural = '【CSV】付加文書_BU1'

from django.db.models import *
from django.utils import timezone

#トランザクション系の分離したテーブルをインポート
from .models_tran import *

# 前と後ろの空白除去の設定を変更し、空白が来ても登録される自作CharField
class NonStrippingCharField(CharField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""
    def __init__(self, verbose_name, max_length, blank=True, *args, **kwargs):
        kwargs['verbose_name'] = verbose_name
        kwargs['max_length'] = max_length
        kwargs['blank'] = blank
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingCharField, self).formfield(**kwargs)


#力士マスタ
class Mst_Rikishi(Model):
    Rikishi_code = IntegerField(verbose_name="力士コード")
    Rikishi_name_kanji_official = CharField(verbose_name="正式力士名漢字", max_length=10, blank=True)
    Rikishi_name_kanji_kana = CharField(verbose_name="正式力士名かな", max_length=20, blank=True)
    Rikishi_name_Kanji_2char = NonStrippingCharField("２文字力士名漢字", 4)
    Rikishi_name_Kanji_3char = NonStrippingCharField("３文字力士名漢字", 6)
    Rikishi_name_Kanji_4char = NonStrippingCharField("４文字力士名漢字", 8)
    Rikishi_name_jikai_code_official = CharField(verbose_name="正式力士名字解コード配列", max_length=20, blank=True)
    Rikishi_name_jikai_code_2char = CharField(verbose_name="２文字力士名字解コード配列", max_length=8, blank=True)
    Rikishi_name_jikai_code_3char = CharField(verbose_name="３文字力士名字解コード配列", max_length=12, blank=True)
    Rikishi_name_jikai_code_4char = CharField(verbose_name="４文字力士名字解コード配列", max_length=16, blank=True)
    Heya_code = ForeignKey('Mst_Heya', on_delete=CASCADE) #部屋マスタ
    OCR_rikishi_name_Kanji = CharField(verbose_name="OCR用力士名漢字", max_length=10, blank=True)
    Real_name = CharField(verbose_name="本名", max_length=20, blank=True)
    Date_of_birth = DateField(verbose_name="生年月日西暦", blank=True)
    Hometown_code_1 = ForeignKey('Mst_Hometown', on_delete=CASCADE, related_name = 'hometown1', blank=True, null=True) #出身地名マスタ
    Hometown_details_1 = CharField(verbose_name="出身地詳細１", max_length=64, blank=True)
    Hometown_details_abbr1_2char = CharField(verbose_name="出身地詳細２文字略称１", max_length=4, blank=True)
    Hometown_details_abbr1_3char = CharField(verbose_name="出身地詳細３文字略称１", max_length=6, blank=True)
    Hometown_code_2 = ForeignKey('Mst_Hometown', on_delete=CASCADE, related_name = 'hometown2', blank=True, null=True) #出身地名マスタ
    Hometown_details_2 = CharField(verbose_name="出身地詳細２", max_length=64, blank=True)
    Hometown_details_abbr2_2char = CharField(verbose_name="出身地詳細２文字略称２", max_length=4, blank=True)
    Hometown_details_abbr2_3char = CharField(verbose_name="出身地詳細３文字略称２", max_length=6, blank=True)
    Alien_classification = BooleanField(verbose_name="外国人区分")
    Height = IntegerField(verbose_name="身長", blank=True, null=True)
    Weight = IntegerField(verbose_name="体重", blank=True, null=True)
    Last_weight = IntegerField(verbose_name="前回体重", blank=True, null=True)
    Hatsudohyou_year = IntegerField(verbose_name="初土俵年", blank=True, null=True)
    Hatsubasho_code = ForeignKey('Mst_Basho', on_delete=CASCADE, related_name = 'hatsubasyo', blank=True, null=True) #場所マスタ
    Tukedashi_class_code = ForeignKey('Mst_Class', on_delete=CASCADE, blank=True, null=True) #階級マスタ
    Tukedashi_class = BooleanField(verbose_name="付出区分")
    Tukedashi_maime = IntegerField(verbose_name="付出枚目", blank=True, null=True)
    Rikishi_attrib_class = ForeignKey('Mst_Rikishistatus', on_delete=CASCADE, blank=True, null=True) #力士状態マスタ
    Retired_year_AD = IntegerField(verbose_name="引退年月西暦", blank=True, null=True)
    Retirebasho_code = ForeignKey('Mst_Basho', on_delete=CASCADE, related_name = 'retirement', blank=True, null=True) #場所マスタ
    Day_of_retirement = ForeignKey('Mst_Nichime', on_delete=CASCADE, blank=True, null=True) #日目マスタ
    Hometown_details_Municipality_1 = CharField(verbose_name="出身地詳細市町村１", max_length=66, blank=True)
    Hometown_details_Municipality_2 = CharField(verbose_name="出身地詳細市町村２", max_length=66, blank=True)

    class Meta:
        verbose_name_plural = '力士マスタ'

    # def clean(self, value):
    #      if value is not None:
    #          value = value.strip()
    #      return super(Mst_Rikishi, self).clean(value)
        
    def __str__(self):
        return self.Rikishi_name_kanji_official
    


#力士状態マスタ
class Mst_Rikishistatus(Model):
    Rikishistatus_code = IntegerField(verbose_name='状態コード')
    Rikishistatus_name = CharField(verbose_name='状態名称', max_length=5)

    class Meta:
        verbose_name_plural = '力士状態マスタ'

    def __str__(self):
        return self.Rikishistatus_name

#改名履歴マスタ
class Mst_Rename_history(Model):
    Yearmonth = IntegerField(verbose_name='年月西暦', blank=True, null=True)
    Rikishi_code = ForeignKey('Mst_Rikishi', on_delete=CASCADE, blank=True, null=True)
    Rikishi_name_kanji = CharField(verbose_name='改名前力士名漢字', max_length=10, blank=True, null=True)
    Rikishi_name_kana =  CharField(verbose_name='力士名かな', max_length=20, blank=True, null=True)
    Rikishi_name_2char = NonStrippingCharField("２文字力士名漢字", 4)
    Rikishi_name_3char = NonStrippingCharField("３文字力士名漢字", 6)
    Rikishi_name_4char = NonStrippingCharField("４文字力士名漢字", 8)
    Rikishi_name_jikai_code_official = CharField(verbose_name="正式力士名字解コード配列", max_length=20, blank=True, null=True)
    Rikishi_name_jikai_code_2char = CharField(verbose_name="２文字力士名字解コード配列", max_length=8, blank=True, null=True)
    Rikishi_name_jikai_code_3char = CharField(verbose_name="３文字力士名字解コード配列", max_length=12, blank=True, null=True)
    Rikishi_name_jikai_code_4char = CharField(verbose_name="４文字力士名字解コード配列", max_length=16, blank=True, null=True)

    class Meta:
        verbose_name_plural = '改名履歴マスタ'

    def __str__(self):
        return self.Rikishi_name_kanji

#場所マスタ
class Mst_Basho(Model):
    Basho_code = IntegerField(verbose_name='場所コード')
    Basho_kanji = CharField(verbose_name='場所名漢字', max_length=10)
    Basho_kana = CharField(verbose_name='場所名かな', max_length=20)
    Basho_month = IntegerField(verbose_name='月')
    Basho_1char = CharField(verbose_name='１文字略称', max_length=2, blank=True)
    Basho_symbol = CharField(verbose_name='１文字記号', max_length=2, blank=True)
    Weight_measure_category = IntegerField(verbose_name='体重測定区分', blank=True, null=True)

    class Meta:
        verbose_name_plural = '場所マスタ'

    def __str__(self):
        return self.Basho_kanji

#部屋マスタ
class Mst_Heya(Model):
    Heya_code = IntegerField(verbose_name='部屋コード')
    Heya_official_kanji = CharField(verbose_name='正式名称漢字', max_length=10)
    Heya_official_kana = CharField(verbose_name='正式名称かな', max_length=20)
    Heya_kanji_2char = CharField(verbose_name='２文字部屋名漢字', max_length=4)
    Heya_kanji_3char = CharField(verbose_name='３文字部屋名漢字', max_length=6)
    Heya_kanji_2char_jikai = CharField(verbose_name='２文字部屋名字解コード配列', max_length=8, blank=True)
    Heya_kanji_3char_jikai = CharField(verbose_name='３文字部屋名字解コード配列', max_length=12, blank=True)

    class Meta:
        verbose_name_plural = '部屋マスタ'

    def __str__(self):
        return self.Heya_official_kanji

#決まり手マスタ
class Mst_Kimarite(Model):
    Heya_code = IntegerField(verbose_name='決まり手コード')
    Kimarite_name = CharField(verbose_name='決まり手名称', max_length=32)
    Kimarite_abbr_5char = CharField(verbose_name='決まり手５文字略称', max_length=10)
    Display_order = IntegerField(verbose_name='表示順')
    Opponent_kimarite_code = IntegerField(verbose_name='相手決まり手コード')

    class Meta:
        verbose_name_plural = '決まり手マスタ'

    def __str__(self):
        return self.Kimarite_name

#階級マスタ
class Mst_Class(Model):
    Class_code = IntegerField(verbose_name='階級コード')
    Class_name_kanji = CharField(verbose_name='階級名漢字', max_length=10)
    Class_name_kana = CharField(verbose_name='階級名かな', max_length=20)
    Class_name_1char = CharField(verbose_name='１文字略称', max_length=2)
    Class_name_3char = CharField(verbose_name='３文字名称', max_length=6)
    Banzuke_1char = CharField(verbose_name='階級番付１文字略称', max_length=2)
    Class_name1 = CharField(verbose_name='名称１', max_length=20, blank=True)
    Class_name2 = CharField(verbose_name='名称２', max_length=20, blank=True)
    Class_name3 = CharField(verbose_name='名称３', max_length=20, blank=True)

    class Meta:
        verbose_name_plural = '階級マスタ'

    def __str__(self):
        return self.Class_name_kanji

#地位マスタ
class Mst_Chii(Model):
    Chii_code = IntegerField(verbose_name='地位コード')
    Chii_kanji = CharField(verbose_name='地位名漢字', max_length=10)
    Chii_kana = CharField(verbose_name='地位名かな', max_length=20)
    Chii_2char = CharField(verbose_name='２文字略称', max_length=4)
    Chii_3char = CharField(verbose_name='３文字名称', max_length=6)
    Chii_name1 = CharField(verbose_name='名称１', max_length=20, blank=True)
    Chii_name2 = CharField(verbose_name='名称２', max_length=20, blank=True)
    Chii_name3 = CharField(verbose_name='名称３', max_length=20, blank=True)
    Sort_code = IntegerField(verbose_name='ソートコード', blank=True, null=True)

    class Meta:
        verbose_name_plural = '地位マスタ'

    def __str__(self):
        return self.Chii_kanji

#受賞区分マスタ
class Mst_Award_category(Model):
    Award_category_code = IntegerField(verbose_name='受賞コード')
    Award_category_kanji = CharField(verbose_name='受賞名漢字', max_length=10)
    Award_category_kana = CharField(verbose_name='受賞名かな', max_length=20)
    Award_category_name1 = CharField(verbose_name='名称１', max_length=10, blank=True)
    Award_category_name2 = CharField(verbose_name='名称２', max_length=10, blank=True)
    Award_category_name3 = CharField(verbose_name='名称３', max_length=10, blank=True)

    class Meta:
        verbose_name_plural = '受賞区分マスタ'

    def __str__(self):
        return self.Award_category_kanji


#出身地名マスタ
class Mst_Hometown(Model):
    Hometown_code = IntegerField(verbose_name='出身地コード')
    Country_prefecture_kanji = CharField(verbose_name='国・都道府県名漢字', max_length=20)
    Country_prefecture_kana = CharField(verbose_name='国・都道府県名かな', max_length=40)
    Country_prefecture_2char = CharField(verbose_name='２文字略称', max_length=4)
    Country_prefecture_3char = CharField(verbose_name='３文字略称', max_length=6)

    class Meta:
        verbose_name_plural = '出身地マスタ'

    def __str__(self):
        return self.Country_prefecture_kanji


#生涯受賞回数マスタ
# class Mst_Lifetime_award(Model):
#    BAward_code = CharField(verbose_name='受賞コード', max_length=2)
#    Rikishi_code = ForeignKey(Mst_Rikishi, on_delete=CASCADE) #力士マスタ
#    Class_code = ForeignKey(Mst_Class, on_delete=CASCADE) #階級マスタ
#    Award_count = IntegerField(verbose_name='受賞回数')


#開催マスタ
class Mst_Event(Model):
    Event_date = IntegerField(verbose_name='開催年月')
    Basho_code = ForeignKey('Mst_Basho', on_delete=CASCADE)
    Torikumi_nichime_code = ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name = 'torikumi_nichime')
    Shoubu_nichime_code = ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name = 'shoubu_nichime')
    Frist_date = DateField(verbose_name='初日年月日')
    Banzuke_date = DateField(verbose_name='番付発表日')
    Age_calcu_reference_date = DateField(verbose_name='年齢算出基準日')

    class Meta:
        verbose_name_plural = '（システム状態に移行したので削除）開催マスタ'


#日目マスタ
class Mst_Nichime(Model):
    Nichime_code = IntegerField(verbose_name='日目コード')
    Nichime_name = CharField(verbose_name='日目名称', max_length=6)
    Touzai_division = ForeignKey('Mst_Eastwest', on_delete=CASCADE, blank=True, null=True) #東西マスタ
    Nichime_3char = CharField(verbose_name='３文字略称', max_length=10, blank=True)
    Nichime_4char = CharField(verbose_name='４文字略称', max_length=10, blank=True)

    class Meta:
        verbose_name_plural = '日目マスタ'

    def __str__(self):
        return self.Nichime_name

#東西マスタ
class Mst_Eastwest(Model):
    Eastwest_code = IntegerField(verbose_name='東西コード')
    Eastwest_name = CharField(verbose_name='東西名称', max_length=2)

    class Meta:
        verbose_name_plural = '東西マスタ'

    def __str__(self):
        return self.Eastwest_name

#生涯地位情報
class Mst_Lifetime_statusinfo(Model):
    Rikishi_code = ForeignKey(Mst_Rikishi, on_delete=CASCADE) #力士マスタ
    Chii_code = ForeignKey(Mst_Chii, on_delete=CASCADE) #地位マスタ

    class Meta:
        verbose_name_plural = '生涯地位情報'

    def __str__(self):
        return str(self.Chii_code)

#生涯成績マスタ
class Mst_Lifetime_result(Model):
    Rikishi_code = ForeignKey(Mst_Rikishi, on_delete=CASCADE) #力士マスタ
    Class_code =  ForeignKey(Mst_Class, on_delete=CASCADE) #階級マスタ
    Totalbasho = IntegerField(verbose_name='通算出場場所回数')
    Totalwins = IntegerField(verbose_name='通算勝ち回数')
    Totalloss = IntegerField(verbose_name='通算負け回数')
    Totalkyuujou = IntegerField(verbose_name='通算休場回数')
    Totalties = IntegerField(verbose_name='通算分け回数')
    Totalgivekinboshi = IntegerField(verbose_name='通算与金星回数')
    Totalgetkinboshi = IntegerField(verbose_name='通算奪金星回数')
    Highestchii_code = ForeignKey(Mst_Chii, on_delete=CASCADE) #地位マスタ
    Highestorder = IntegerField(verbose_name='最高順位', blank=True, null=True)
    Touzai_division = ForeignKey(Mst_Eastwest, on_delete=CASCADE, blank=True, null=True) #東西マスタ
    Maxsticking = IntegerField(verbose_name='最高張付')
    Overallwinrate = FloatField(verbose_name='通算勝率')
    Overallwinrate_yasumimake = FloatField(verbose_name='通算勝率（休を負）')
    Maxcontinuousplayed = IntegerField(verbose_name='最高連続出場回数', blank=True, null=True)
    Currentcontinuosplayed = IntegerField(verbose_name='現連続出場回数', blank=True, null=True)
    Numberofreignedbasho = IntegerField(verbose_name='在位場所数', blank=True, null=True)

    class Meta:
        verbose_name_plural = '生涯成績マスタ'

    def __str__(self):
        return str(self.Rikishi_code)

#生涯受賞回数マスタ
class Mst_Lifetime_award(Model):
    Award_category_code = ForeignKey(Mst_Award_category, on_delete=CASCADE) #受賞区分マスタ
    Rikishi_code = ForeignKey(Mst_Rikishi, on_delete=CASCADE) #力士マスタ
    Numberofaward = IntegerField(verbose_name='受賞回数')

    class Meta:
        verbose_name_plural = '生涯受賞回数マスタ'


#勝負情報
class Mst_Gameinfo(Model):
    Game_category = IntegerField(verbose_name='勝負区分')
    Kimarite_code =  ForeignKey('Mst_Kimarite', on_delete=CASCADE) #決まり手マスタ
    Game_mark = CharField(verbose_name='勝負マーク', max_length=2, blank=True)
    Game_mark2 = CharField(verbose_name='勝負マーク２', max_length=2, blank=True)
    Cumulative_class = IntegerField(verbose_name='累積区分', blank=True, null=True)
    Participation_division = IntegerField(verbose_name='出場区分', blank=True, null=True)
    Opponent_category = IntegerField(verbose_name='相手勝負区分', blank=True, null=True)
    Screendisplay_category = IntegerField(verbose_name='画面表示区分', blank=True, null=True)
    Screendisplay_string = CharField(verbose_name='画面表示文字列', max_length=40, blank=True)
    Name1 = CharField(verbose_name='名称１', max_length=20, blank=True)
    Name2 = CharField(verbose_name='名称２', max_length=20, blank=True)
    Name3 = CharField(verbose_name='名称３', max_length=20, blank=True)

    class Meta:
        verbose_name_plural = '勝負情報'

#電文種別
class Mst_KindofNewsML(Model):
    Content_code =  IntegerField(verbose_name='電文種別コード', blank=True, null=True)
    ContentName = CharField(verbose_name='電文種別名称', max_length=32, blank=True, null=True)
    Group_code =  IntegerField(verbose_name='グループＩＤ', blank=True, null=True)
    NewsMLNo = CharField(verbose_name='NewsML種別コード', max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = '電文種別'

    def __str__(self):
        return str(self.ContentName)

#運用管理
class Mst_Operationmode(Model):
    Operationmode_code =  IntegerField(verbose_name='運用モード', blank=True, null=True)
    Operationmode_name = CharField(verbose_name='運用モード表記', max_length=10, blank=True, null=True)

    class Meta:
       verbose_name_plural = '運用管理'

    def __str__(self):
        return str(self.Operationmode_name)

#都道府県マスタ
class Mst_Prefectures(Model):
    Prefectures_code =  IntegerField(verbose_name='都道府県コード', blank=True, null=True)
    Prefectures_name = CharField(verbose_name='名称', max_length=10, blank=True, null=True)

    class Meta:
       verbose_name_plural = '都道府県'

    def __str__(self):
        return str(self.Prefectures_name)

#配信コードマスタ
class Mst_Delivery(Model):
    Delivery_code =  IntegerField(verbose_name='配信コード', blank=True, null=True)
    Delivery_name = CharField(verbose_name='配信名称', max_length=10, blank=True, null=True)
    Individual_address =  IntegerField(verbose_name='個別指定', blank=True, null=True)

    class Meta:
       verbose_name_plural = '配信コードマスタ'

    def __str__(self):
        return str(self.Delivery_name)

#副ヘッタマスタ
class Mst_SubHeader(Model):
    Content_code =  ForeignKey('Mst_KindofNewsML', on_delete=CASCADE, blank=True, null=True) #電文種別マスタ
    Makecontent_code = IntegerField(verbose_name='作成種別コード', blank=True, null=True) 
    Prefectures_code =  ForeignKey('Mst_Prefectures', on_delete=CASCADE, blank=True, null=True) #都道府県マスタ
    Nichime_code =  ForeignKey('Mst_Nichime', on_delete=CASCADE, blank=True, null=True) #日目マスタ
    Delivery_code =  ForeignKey('Mst_Delivery', on_delete=CASCADE, blank=True, null=True) #配信コードマスタ

    class Meta:
        verbose_name_plural = '副ヘッタマスタ'
    
        def __str__(self):
            return str(self.Content_code)

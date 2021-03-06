from django.db import models
from django.utils import timezone

class Eventinfo(models.Model):
    taikai_text = models.CharField(max_length=200)
#    taikai_date = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.taikai_text

class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_name_formal = models.CharField(max_length=200, blank=True)
    player_name_formal3 = models.CharField(max_length=200, blank=True)
    player_name_yomi = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')
 
    def __str__(self):
        return self.player_name
    
class Waza(models.Model):
    waza_name = models.CharField(max_length=200)
    waza_name_formal = models.CharField(max_length=200, blank=True)
    waza_name_formal7 = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published')
 
    def __str__(self):
        return self.waza_name

class Outcome(models.Model):
    mark = models.CharField(max_length=200)
    winloss = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.mark

class Match(models.Model):
    player1 = models.ForeignKey('Player', related_name='rikishi_1', on_delete=models.CASCADE)
 #   player1winloss = models.IntegerField(blank=True)
    player1win = models.IntegerField(blank=True, default='0')
    player1loss = models.IntegerField(blank=True, default='0')
    player1tie = models.IntegerField(blank=True, default='0')
    player1absence = models.IntegerField(blank=True, default='0')
    outcome1 = models.ForeignKey('Outcome', related_name='rikishi_1', on_delete=models.CASCADE)
    waza = models.ForeignKey(Waza, on_delete=models.CASCADE)
    outcome2 = models.ForeignKey('Outcome', related_name='rikishi_2', on_delete=models.CASCADE)
    player2 = models.ForeignKey('Player', related_name='rikishi_2', on_delete=models.CASCADE)
 #   player2winloss = models.IntegerField(blank=True)
    player2win = models.IntegerField(blank=True, default='0')
    player2loss = models.IntegerField(blank=True, default='0')
    player2absence = models.IntegerField(blank=True, default='0')
    player2tie = models.IntegerField(blank=True, default='0')
#    pub_date = models.DateTimeField('date published')
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str('%s - %s' % (self.player1, self.player2))

class Memo(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)


# CSVの検証
class PostCsv(models.Model):
    player_name = models.CharField(max_length=200)
    player_name_formal = models.CharField(max_length=200, blank=True)
    player_name_formal3 = models.CharField(max_length=200, blank=True)
    player_name_yomi = models.CharField(max_length=200, blank=True)


# ---------------------------------------------------------------------------------------------------------
#力士マスタ
class Mst_Rikishi(models.Model):
    Rikishi_code = models.IntegerField(verbose_name="力士コード")
    Rikishi_name_kanji_official = models.CharField(verbose_name="正式力士名漢字", max_length=10, blank=True)
    Rikishi_name_kanji_kana = models.CharField(verbose_name="正式力士名かな", max_length=20, blank=True)
    Rikishi_name_Kanji_2char = models.CharField(verbose_name="２文字力士名漢字", max_length=4, blank=True)
    Rikishi_name_Kanji_3char = models.CharField(verbose_name="３文字力士名漢字", max_length=6, blank=True)
    Rikishi_name_Kanji_4char = models.CharField(verbose_name="４文字力士名漢字", max_length=8, blank=True)
    Rikishi_name_jikai_code_official = models.CharField(verbose_name="正式力士名字解コード配列", max_length=20, blank=True)
    Rikishi_name_jikai_code_2char = models.CharField(verbose_name="２文字力士名字解コード配列", max_length=8, blank=True)
    Rikishi_name_jikai_code_3char = models.CharField(verbose_name="３文字力士名字解コード配列", max_length=12, blank=True)
    Rikishi_name_jikai_code_4char = models.CharField(verbose_name="４文字力士名字解コード配列", max_length=16, blank=True)
    Heya_code = models.ForeignKey('Mst_Heya', on_delete=models.CASCADE) #部屋マスタ
    OCR_rikishi_name_Kanji = models.CharField(verbose_name="OCR用力士名漢字", max_length=10, blank=True)
    Real_name = models.CharField(verbose_name="本名", max_length=20, blank=True)
    Date_of_birth = models.DateField(verbose_name="生年月日西暦", blank=True)   
    Hometown_code_1 = models.ForeignKey('Mst_Hometown', on_delete=models.CASCADE, related_name = 'hometown1', blank=True, null=True) #出身地名マスタ
    Hometown_details_1 = models.CharField(verbose_name="出身地詳細１", max_length=64, blank=True)
    Hometown_details_abbr1_2char = models.CharField(verbose_name="出身地詳細２文字略称１", max_length=4, blank=True)
    Hometown_details_abbr1_3char = models.CharField(verbose_name="出身地詳細３文字略称１", max_length=6, blank=True)
    Hometown_code_2 = models.ForeignKey('Mst_Hometown', on_delete=models.CASCADE, related_name = 'hometown2', blank=True, null=True) #出身地名マスタ
    Hometown_details_2 = models.CharField(verbose_name="出身地詳細２", max_length=64, blank=True)
    Hometown_details_abbr2_2char = models.CharField(verbose_name="出身地詳細２文字略称２", max_length=4, blank=True)
    Hometown_details_abbr2_3char = models.CharField(verbose_name="出身地詳細３文字略称２", max_length=6, blank=True)
    Alien_classification = models.BooleanField(verbose_name="外国人区分")
    Height = models.IntegerField(verbose_name="身長", blank=True, null=True)
    Weight = models.IntegerField(verbose_name="体重", blank=True, null=True)
    Last_weight = models.IntegerField(verbose_name="前回体重", blank=True, null=True)
    Hatsudohyou_year = models.IntegerField(verbose_name="初土俵年", blank=True, null=True)
    Hatsubasho_code = models.ForeignKey('Mst_Basho', on_delete=models.CASCADE, related_name = 'hatsubasyo', blank=True, null=True) #場所マスタ
    Tukedashi_class_code = models.ForeignKey('Mst_Class', on_delete=models.CASCADE, blank=True, null=True) #階級マスタ
    Tukedashi_class = models.BooleanField(verbose_name="付出区分")
    Tukedashi_maime = models.IntegerField(verbose_name="付出枚目", blank=True, null=True)
    Rikishi_attrib_class = models.ForeignKey('Mst_Rikishistatus', on_delete=models.CASCADE, blank=True, null=True) #力士状態マスタ
    Retired_year_AD = models.IntegerField(verbose_name="引退年月西暦", blank=True, null=True)
    Retirebasho_code = models.ForeignKey('Mst_Basho', on_delete=models.CASCADE, related_name = 'retirement', blank=True, null=True) #場所マスタ
    Day_of_retirement = models.ForeignKey('Mst_Nichime', on_delete=models.CASCADE, blank=True, null=True) #日目マスタ
    Hometown_details_Municipality_1 = models.CharField(verbose_name="出身地詳細市町村１", max_length=66, blank=True)
    Hometown_details_Municipality_2 = models.CharField(verbose_name="出身地詳細市町村２", max_length=66, blank=True)

    class Meta:
        verbose_name_plural = '力士マスタ'
    
    def __str__(self):
        return self.Rikishi_name_kanji_official

#力士状態マスタ
class Mst_Rikishistatus(models.Model):
    Rikishistatus_code = models.IntegerField(verbose_name='状態コード')
    Rikishistatus_name = models.CharField(verbose_name='状態名称', max_length=5)

    class Meta:
        verbose_name_plural = '力士状態マスタ'
    
    def __str__(self):
        return self.Rikishistatus_name

#場所マスタ
class Mst_Basho(models.Model):
    Basho_code = models.IntegerField(verbose_name='場所コード')
    Basho_kanji = models.CharField(verbose_name='場所名漢字', max_length=10)
    Bashi_kana = models.CharField(verbose_name='場所名かな', max_length=20)
    Basho_month = models.IntegerField(verbose_name='月')
    Bashi_1char = models.CharField(verbose_name='１文字略称', max_length=2, blank=True)
    Basho_symbol = models.CharField(verbose_name='１文字記号', max_length=2, blank=True)
    Weight_measure_category = models.IntegerField(verbose_name='体重測定区分', blank=True, null=True)

    class Meta:
        verbose_name_plural = '場所マスタ'
    
    def __str__(self):
        return self.Basho_kanji

#部屋マスタ
class Mst_Heya(models.Model):
    Heya_code = models.IntegerField(verbose_name='部屋コード')
    Heya_official_kanji = models.CharField(verbose_name='正式名称漢字', max_length=10)
    Heya_official_kana = models.CharField(verbose_name='正式名称かな', max_length=20)
    Heya_kanji_2char = models.CharField(verbose_name='２文字部屋名漢字', max_length=4)
    Heya_kanji_3char = models.CharField(verbose_name='３文字部屋名漢字', max_length=6)
    Heya_kanji_2char_jikai = models.CharField(verbose_name='２文字部屋名字解コード配列', max_length=8, blank=True)
    Heya_kanji_3char_jikai = models.CharField(verbose_name='３文字部屋名字解コード配列', max_length=12, blank=True)

    class Meta:
        verbose_name_plural = '部屋マスタ'
    
    def __str__(self):
        return self.Heya_official_kanji

#決まり手マスタ
class Mst_Kimarite(models.Model):
    Heya_code = models.IntegerField(verbose_name='決まり手コード')
    Kimarite_name = models.CharField(verbose_name='決まり手名称', max_length=32)
    Kimarite_abbr_5char = models.CharField(verbose_name='決まり手５文字略称', max_length=10)
    Display_order = models.IntegerField(verbose_name='表示順')
    Opponent_kimarite_code = models.IntegerField(verbose_name='相手決まり手コード')

    class Meta:
        verbose_name_plural = '決まり手マスタ'
    
    def __str__(self):
        return self.Kimarite_name

#階級マスタ
class Mst_Class(models.Model):
    Class_code = models.IntegerField(verbose_name='階級コード')
    Class_name_kanji = models.CharField(verbose_name='階級名漢字', max_length=10)
    Class_name_kana = models.CharField(verbose_name='階級名かな', max_length=20)
    Class_name_1char = models.CharField(verbose_name='１文字略称', max_length=2)
    Class_name_3char = models.CharField(verbose_name='３文字名称', max_length=6)
    Banzuke_1char = models.CharField(verbose_name='階級番付１文字略称', max_length=2)
    Class_name1 = models.CharField(verbose_name='名称１', max_length=20, blank=True)
    Class_name2 = models.CharField(verbose_name='名称２', max_length=20, blank=True)
    Class_name3 = models.CharField(verbose_name='名称３', max_length=20, blank=True)

    class Meta:
        verbose_name_plural = '階級マスタ'
    
    def __str__(self):
        return self.Class_name_kanji

#地位マスタ
class Mst_Chii(models.Model):
    Chii_code = models.IntegerField(verbose_name='地位コード')
    Chii_kanji = models.CharField(verbose_name='地位名漢字', max_length=10)
    Chii_kana = models.CharField(verbose_name='地位名かな', max_length=20)
    Chii_2char = models.CharField(verbose_name='２文字略称', max_length=4)
    Chii_3char = models.CharField(verbose_name='３文字名称', max_length=6)
    Chii_name1 = models.CharField(verbose_name='名称１', max_length=20, blank=True)
    Chii_name2 = models.CharField(verbose_name='名称２', max_length=20, blank=True)
    Chii_name3 = models.CharField(verbose_name='名称３', max_length=20, blank=True)

    class Meta:
        verbose_name_plural = '地位マスタ'
    
    def __str__(self):
        return self.Chii_kanji

#受賞区分マスタ
class Mst_Award_category(models.Model):
    Award_category_code = models.IntegerField(verbose_name='受賞コード')
    Award_category_kanji = models.CharField(verbose_name='受賞名漢字', max_length=10)
    Award_category_kana = models.CharField(verbose_name='受賞名かな', max_length=20)
    Award_category_name1 = models.CharField(verbose_name='名称１', max_length=10, blank=True)
    Award_category_name2 = models.CharField(verbose_name='名称２', max_length=10, blank=True)
    Award_category_name3 = models.CharField(verbose_name='名称３', max_length=10, blank=True)

    class Meta:
        verbose_name_plural = '受賞区分マスタ'
    
    def __str__(self):
        return self.Award_category_kanji


#出身地名マスタ
class Mst_Hometown(models.Model):
    Hometown_code = models.IntegerField(verbose_name='出身地コード')
    Country_prefecture_kanji = models.CharField(verbose_name='国・都道府県名漢字', max_length=20)
    Country_prefecture_kana = models.CharField(verbose_name='国・都道府県名かな', max_length=40)
    Country_prefecture_2char = models.CharField(verbose_name='２文字略称', max_length=4)
    Country_prefecture_3char = models.CharField(verbose_name='３文字略称', max_length=6)

    class Meta:
        verbose_name_plural = '出身地マスタ'
    
    def __str__(self):
        return self.Country_prefecture_kanji


#生涯受賞回数マスタ
# class Mst_Lifetime_award(models.Model):
#    BAward_code = models.CharField(verbose_name='受賞コード', max_length=2)
#    Rikishi_code = models.ForeignKey(Mst_Rikishi, on_delete=models.CASCADE) #力士マスタ
#    Class_code = models.ForeignKey(Mst_Class, on_delete=models.CASCADE) #階級マスタ
#    Award_count = models.IntegerField(verbose_name='受賞回数')

#開催マスタ
class Mst_Event(models.Model):
    Event_date = models.IntegerField(verbose_name='開催年月')
    Basho_code = models.ForeignKey('Mst_Basho', on_delete=models.CASCADE)
    Torikumi_nichime_code = models.ForeignKey('Mst_Nichime', on_delete=models.CASCADE, related_name = 'torikumi_nichime')
    Shoubu_nichime_code = models.ForeignKey('Mst_Nichime', on_delete=models.CASCADE, related_name = 'shoubu_nichime')
    Frist_date = models.DateField(verbose_name='初日年月日')
    Banzuke_date = models.DateField(verbose_name='番付発表日')
    Age_calcu_reference_date = models.DateField(verbose_name='年齢算出基準日')

    class Meta:
        verbose_name_plural = '開催マスタ'


#日目マスタ
class Mst_Nichime(models.Model):
    Nicime_code = models.IntegerField(verbose_name='日目コード')
    Nicime_name = models.CharField(verbose_name='日目名称', max_length=6)
    Touzai_division = models.ForeignKey('Mst_Eastwest', on_delete=models.CASCADE, blank=True, null=True) #東西マスタ 
    Nicime_3char = models.CharField(verbose_name='３文字略称', max_length=10, blank=True)
    Nicime_4char = models.CharField(verbose_name='４文字略称', max_length=10, blank=True)
 
    class Meta:
        verbose_name_plural = '日目マスタ'

    def __str__(self):
        return self.Nicime_name

#東西マスタ
class Mst_Eastwest(models.Model):
    Eastwest_code = models.IntegerField(verbose_name='東西コード')
    Eastwest_name = models.CharField(verbose_name='東西名称', max_length=2)

    class Meta:
        verbose_name_plural = '東西マスタ'
    
    def __str__(self):
        return self.Eastwest_name



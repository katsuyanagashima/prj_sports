from django.db.models import * 
from django.utils import timezone

#力士マスタ
class Mst_Rikishi(Model):
    Rikishi_code = IntegerField(verbose_name="力士コード")
    Rikishi_name_kanji_official = CharField(verbose_name="正式力士名漢字", max_length=10, blank=True)
    Rikishi_name_kanji_kana = CharField(verbose_name="正式力士名かな", max_length=20, blank=True)
    Rikishi_name_Kanji_2char = CharField(verbose_name="２文字力士名漢字", max_length=4, blank=True)
    Rikishi_name_Kanji_3char = CharField(verbose_name="３文字力士名漢字", max_length=6, blank=True)
    Rikishi_name_Kanji_4char = CharField(verbose_name="４文字力士名漢字", max_length=8, blank=True)
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

#場所マスタ
class Mst_Basho(Model):
    Basho_code = IntegerField(verbose_name='場所コード')
    Basho_kanji = CharField(verbose_name='場所名漢字', max_length=10)
    Bashi_kana = CharField(verbose_name='場所名かな', max_length=20)
    Basho_month = IntegerField(verbose_name='月')
    Bashi_1char = CharField(verbose_name='１文字略称', max_length=2, blank=True)
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
    Nicime_code = IntegerField(verbose_name='日目コード')
    Nicime_name = CharField(verbose_name='日目名称', max_length=6)
    Touzai_division = ForeignKey('Mst_Eastwest', on_delete=CASCADE, blank=True, null=True) #東西マスタ
    Nicime_3char = CharField(verbose_name='３文字略称', max_length=10, blank=True)
    Nicime_4char = CharField(verbose_name='４文字略称', max_length=10, blank=True)

    class Meta:
        verbose_name_plural = '日目マスタ'

    def __str__(self):
        return self.Nicime_name

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
    Totalgetkinboshi = IntegerField(verbose_name='通算与金星回数')
    Totalgivekinboshi = IntegerField(verbose_name='通算奪金星回数')
    Highestchii_code = ForeignKey(Mst_Chii, on_delete=CASCADE) #地位マスタ
    Highestorder = IntegerField(verbose_name='最高順位')
    Touzai_division = ForeignKey(Mst_Eastwest, on_delete=CASCADE) #東西マスタ
    Maxsticking = IntegerField(verbose_name='最高張付')
    Overallwinrate = IntegerField(verbose_name='通算勝率')
    Overallwinrate_yasumimake = IntegerField(verbose_name='通算勝率（休を負）')
    Maxcontinuousplayed = IntegerField(verbose_name='最高連続出場回数')
    Currentcontinuosplayed = IntegerField(verbose_name='現連続出場回数')
    Numberofreignedbasho = IntegerField(verbose_name='在位場所数')

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

# --------------------------------------------------------------------------------------------------
#システム状態
class Tran_Systemstatus(Model):
    Event_date =  IntegerField(verbose_name='開催年月', blank=True, null=True)
    CurrentBasho =  ForeignKey('Mst_Basho', on_delete=CASCADE)
    SystemStatus =  ForeignKey('Mst_Operationmode', on_delete=CASCADE, blank=True, null=True) 
    TorikumiDate =  ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name = 'torikumi')
    MatchDate =  ForeignKey('Mst_Nichime', on_delete=CASCADE, related_name = 'match')
    Frist_date = DateField(verbose_name='初日年月日')
    Banzuke_date = DateField(verbose_name='番付発表日')
    Age_calcu_reference_date = DateField(verbose_name='年齢算出基準日')

    class Meta:
        verbose_name_plural = '#システム状態'
    
    def __str__(self):
        return str(self.Event_date)

# --------------------------------------------------------------------------------------------------
#番付明細　NewsML作成（01:新番付資料）
# 
class Tran_Banzuke(Model):
    Event_date =  ForeignKey('Tran_Systemstatus', on_delete=CASCADE) #システム状態の開催年月
    RikishiId =  ForeignKey('Mst_Rikishi', on_delete=CASCADE) #力士マスタ
    Join_code =  IntegerField(verbose_name='参加区分', blank=True, null=True)
    Class_code =  ForeignKey('Mst_Class', on_delete=CASCADE) #階級マスタ
    Eastwest_code =  ForeignKey('Mst_Eastwest', on_delete=CASCADE) #東西マスタ
    Chii_code =  ForeignKey('Mst_Chii', on_delete=CASCADE) #地位マスタ
    Banzuke_rank =  IntegerField(verbose_name='番付順位', blank=True, null=True)
    Haridashi =  IntegerField(verbose_name='張付区分', blank=True, null=True)
    Banzuke_no =  IntegerField(verbose_name='番付通番', blank=True, null=True)
    Appear_code =  IntegerField(verbose_name='新再降区分', blank=True, null=True)
 #   Appear_code =  IntegerField(verbose_name='新再降区分', blank=True, null=True)　
    Demoted_rank =  IntegerField(verbose_name='昇降順位', blank=True, null=True)

    class Meta:
        verbose_name_plural = '*番付明細　NewsML作成（01:新番付資料）'

    def __str__(self):
        return str(self.RikishiId)	

#以下、モックアップ用

# class Eventinfo(Model):
#     taikai_text = CharField(max_length=200)
# #    taikai_date = CharField(max_length=200)
#     pub_date = DateTimeField('date published')

#     class Meta:
#         verbose_name_plural = 'イベント'

# class Player(Model):
#     player_name = CharField(max_length=200)
#     player_name_formal = CharField(max_length=200, blank=True)
#     player_name_formal3 = CharField(max_length=200, blank=True)
#     player_name_yomi = CharField(max_length=200, blank=True)
#     pub_date = DateTimeField('date published')

#     class Meta:
#         verbose_name_plural = '選手'

# class Waza(Model):
#     waza_name = CharField(max_length=200)
#     waza_name_formal = CharField(max_length=200, blank=True)
#     waza_name_formal7 = CharField(max_length=200, blank=True)
#     pub_date = DateTimeField('date published')

#     class Meta:
#         verbose_name_plural = '技'
#     def __str__(self):
#         return self.waza_name

# class Outcome(Model):
#     mark = CharField(max_length=200)
#     winloss = CharField(max_length=200)
#     pub_date = DateTimeField('date published')

#     class Meta:
#         verbose_name_plural = '勝負'
#     def __str__(self):
#         return self.mark

# class Match(Model):
#     player1 = ForeignKey('Player', related_name='rikishi_1', on_delete=CASCADE)
#  #   player1winloss = IntegerField(blank=True)
#     player1win = IntegerField(blank=True, default='0')
#     player1loss = IntegerField(blank=True, default='0')
#     player1tie = IntegerField(blank=True, default='0')
#     player1absence = IntegerField(blank=True, default='0')
#     outcome1 = ForeignKey('Outcome', related_name='rikishi_1', on_delete=CASCADE)
#     waza = ForeignKey(Waza, on_delete=CASCADE)
#     outcome2 = ForeignKey('Outcome', related_name='rikishi_2', on_delete=CASCADE)
#     player2 = ForeignKey('Player', related_name='rikishi_2', on_delete=CASCADE)
#  #   player2winloss = IntegerField(blank=True)
#     player2win = IntegerField(blank=True, default='0')
#     player2loss = IntegerField(blank=True, default='0')
#     player2absence = IntegerField(blank=True, default='0')
#     player2tie = IntegerField(blank=True, default='0')
# #    pub_date = DateTimeField('date published')
#     pub_date = DateTimeField(default=timezone.now)

#     class Meta:
#         verbose_name_plural = '試合'
#     # def __str__(self):
#     #     return str('%s - %s' % (self.player1, self.player2))


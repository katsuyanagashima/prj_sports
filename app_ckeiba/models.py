from django.db import models
from django.db.models import *
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import *
# CSV取り込み用に分離したテーブルをインポート
from .models_csv import *


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#                                                               【マスタ】　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# システム状態
class Tran_Systemstatus(Model):
    Environment = ForeignKey(
        'Mst_Environment', verbose_name='実行環境', on_delete=PROTECT)  # 実行環境管理マスタ
    Unyou_date = DateField(verbose_name='運用日')  # 運用日
    Operationmode = ForeignKey(
        'Mst_Operationmode', verbose_name='運用モード', on_delete=PROTECT)  # 運用モード管理マスタ
    Daily_func_time = TimeField(verbose_name='日替わり設定時刻')  # 日替わり設定時刻
    Daily_func_prev_time = TimeField(verbose_name='日替わり前回実行時刻')  # 日替わり前回実行時刻
    Daily_func_prev_type = IntegerField(
        verbose_name='日替わり前回実行タイプ')  # 日替わり前回実行タイプ

    class Meta:
        verbose_name_plural = '#システム状態'

    def __str__(self):
        return str(self.Environment)

    def setState(self, opemode):
        self.Operationmode = opemode
        self.save()  # 　変更したらセーブする！
        pass

# 運用モード管理


class Mst_Operationmode(Model):
    Operationmode_code = IntegerField(verbose_name='運用モード')
    # オフライン/オンライン/マスタ編集中/日時処理中/～～マスタ編集中・・・
    Operationmode_name = CharField(verbose_name='運用モード表記', max_length=15)

    class Meta:
        verbose_name_plural = '#運用管理'

    def __str__(self):
        return self.Operationmode_name


# 実行環境管理
class Mst_Environment(Model):
    Environment_code = IntegerField(verbose_name='実行環境')
    Environment_name = CharField(
        verbose_name='実行環境表記', max_length=15)  # 本番系/開発系

    class Meta:
        verbose_name_plural = '#実行環境管理'

    def __str__(self):
        return str(self.Environment_name)

# 競馬場マスタ


class Mst_Jou(Model):
    Jou_code = IntegerField(verbose_name='競馬場コード', unique=True)
    Jou_name = CharField(verbose_name='正式名', max_length=20)  # 大井競馬場
    Jou_seisekiA = CharField(verbose_name='成績Ａ用', max_length=1)  # 大
    Jou_3char = CharField(verbose_name='３字略称', max_length=3)  # 大井△
    Jou_banei = BooleanField(verbose_name='ばんえいフラグ')  # false
    Group = CharField(verbose_name='グループ', max_length=5, blank=True, null=True)
    Group_priority = IntegerField(verbose_name='グループ優先', blank=True, null=True)
    Jou_1corner = CharField(verbose_name='１コーナー名称',
                            max_length=5, blank=True, null=True)  # １△角
    Jou_2corner = CharField(verbose_name='２コーナー名称',
                            max_length=5, blank=True, null=True)  # ２△角
    Jou_3corner = CharField(verbose_name='３コーナー名称',
                            max_length=5, blank=True, null=True)  # ３△角
    Jou_4corner = CharField(verbose_name='４コーナー名称',
                            max_length=5, blank=True, null=True)  # ４△角

    class Meta:
        verbose_name_plural = '競馬場マスタ'

    # NewsML生成時用の、正式名と３文字略称、ばんえいフラグ取得関数
    def getJoudata(joucode):
        if type('joucode') is int:
            jou_data = get_object_or_404(Mst_Jou, Jou_code=joucode)
        elif type('joucode') is str:
            jou_data = get_list_or_404(Mst_Jou, Jou_name=joucode)[0]
        else:
            return none

        jou_3char = jou_data.Jou_3char
        # ３字略称は、△を全角スペースに変換する
        jou_3char_trans = jou_3char.translate(str.maketrans({"△": "　"}))
        return jou_data.Jou_name, jou_3char_trans, jou_data.Jou_banei

    def __str__(self):
        return self.Jou_name

# グレードマスタ


class Mst_Grade(Model):
    Grade_code = CharField(verbose_name='グレード区分', max_length=2, unique=True)
    Grade_name = CharField(verbose_name='グレード名称', max_length=4)
    Send_class = CharField(verbose_name='配信区分',
                           max_length=4, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'グレードマスタ'

    def __str__(self):
        return self.Grade_name

# 品種年齢区分マスタ


class Mst_Breed_age(Model):
    Breed_age_code = IntegerField(verbose_name='品種年齢区分', unique=True)
    Name_for_race_type = CharField(
        verbose_name='競走種別用名称', max_length=10, blank=True, null=True)  # 混合３・４歳
    Name_for_horse_age_condition = CharField(
        verbose_name='馬齢条件用名称', max_length=10, blank=True, null=True)  # ３・４歳
    Breed_age_name = CharField(
        verbose_name='品種年齢名称', max_length=10, blank=True, null=True)  # 混合

    class Meta:
        verbose_name_plural = '品種年齢区分マスタ'

    # NewsML生成時用の、競走種別用名称から馬齢条件用名称を取得する関数
    def getBareiJouken(Name_for_race_type):
        ba_instance = get_list_or_404(
            Mst_Breed_age, Name_for_race_type=Name_for_race_type)[0]
        return ba_instance.Name_for_horse_age_condition

    def __str__(self):
        return self.Name_for_race_type

# 天候マスタ


class Mst_Weather(Model):
    Weather_code = IntegerField(verbose_name='天候コード', unique=True)
    Weather_name = CharField(
        verbose_name='天候名称', max_length=5, blank=True, null=True)  # 晴

    class Meta:
        verbose_name_plural = '天候マスタ'

    def __str__(self):
        return self.Weather_name

# 着差マスタ


class Mst_Margin(Model):
    Margin_code = IntegerField(verbose_name='着差コード', unique=True)
    Margin_name = CharField(
        verbose_name='着差名称(通常）', max_length=10, blank=True, null=True)  # １△
    Margin_convert = CharField(
        verbose_name='着差名称(変換)', max_length=10, blank=True, null=True)

    class Meta:
        verbose_name_plural = '着差マスタ'

    def __str__(self):
        return self.Margin_name

# 差マスタ


class Mst_Difference(Model):
    Differnce_code = IntegerField(verbose_name='差コード')
    Differnce_name = CharField(
        verbose_name='差名称', max_length=5, blank=True, null=True)  # 大差
    Differnce_display = CharField(
        verbose_name='画面表示用名称', max_length=5, blank=True, null=True)  # ＝

    class Meta:
        verbose_name_plural = '差マスタ'

    def __str__(self):
        return self.Differnce_name

# 事故種類マスタ


class Mst_Accident_type(Model):
    Accident_type_code = IntegerField(verbose_name='事故種類コード', unique=True)
    # Accident_type_code = IntegerField(verbose_name='事故種類コード', unique=True)
    Accident_type_name = CharField(
        verbose_name='事故種類名称', max_length=15, blank=True, null=True)  # 競走不成立
    Fulltag_all = CharField(verbose_name='フルタグＡＬＬ',
                            max_length=15, blank=True, null=True)
    Priority = IntegerField(verbose_name='優先順位', blank=True, null=True)  # 0
    Accident_class = IntegerField(
        verbose_name='異常区分設定フラグ', blank=True, null=True)

    class Meta:
        verbose_name_plural = '事故種類マスタ'

    def __str__(self):
        return self.Accident_type_name

# 事故理由マスタ


class Mst_Accident_reason(Model):
    Accident_reason_code = IntegerField(verbose_name='事故理由コード', unique=True)
    Accident_reason_name = CharField(
        verbose_name='事故理由名称', max_length=15, blank=True, null=True)  # 進路妨害
    Accident_class = IntegerField(
        verbose_name='異常区分設定フラグ', blank=True, null=True)

    class Meta:
        verbose_name_plural = '事故理由マスタ'

    def __str__(self):
        return self.Accident_reason_name

# 性別マスタ


class Mst_Gender(Model):
    Horse_gender_code = IntegerField(verbose_name='性別コード', unique=True)
    Horse_gender = CharField(
        verbose_name='性別名称', max_length=2, blank=True, null=True)  # 牡
    Remarks = CharField(verbose_name='備考', max_length=5,
                        blank=True, null=True)  # 雄馬

    class Meta:
        verbose_name_plural = '性別マスタ'

    def __str__(self):
        return self.Horse_gender

# 所属場マスタ
class Mst_Belonging(Model):
    Belonging_code = IntegerField(verbose_name='所属場コード', unique=True)
    Belonging = CharField(verbose_name='所属場名称（正式名）',
                          max_length=10, blank=True, null=True)  # 北海道
    Belonging_1char = CharField(
        verbose_name='所属場名称（1字）', max_length=1, blank=True, null=True)  # 北

    class Meta:
        verbose_name_plural = '所属場マスタ'
    
    # NewsML生成時用の、所属場名称（正式名）から所属場名称（1字）を取得する関数
    def getBelonging_1char(Belonging):
        be_instance = get_list_or_404(
            Mst_Belonging, Belonging=Belonging)[0]
        return be_instance.Belonging_1char

    def __str__(self):
        return self.Belonging

# 中央交流区分マスタ


class Mst_JRA_exchanges(Model):
    JRA_exchanges_code = IntegerField(verbose_name='中央交流区コード', unique=True)
    JRA_exchanges = CharField(verbose_name='交流区分名称',
                              max_length=10, blank=True, null=True)  # 指定交流
    Send_classification = IntegerField(
        verbose_name='配信区分コード', blank=True, null=True)  # 2

    class Meta:
        verbose_name_plural = '中央交流区分マスタ'

    def __str__(self):
        return self.JRA_exchanges

# 芝・ダート区分マスタ


class Mst_Turf_dirt_class(Model):
    Turf_dirt_code = IntegerField(verbose_name='芝・ダート区分コード', unique=True)
    Turf_dirt_name = CharField(
        verbose_name='芝区分名称', max_length=5, blank=True, null=True)  # ダート

    class Meta:
        verbose_name_plural = '芝・ダート区分マスタ'

    def __str__(self):
        return self.Turf_dirt_name

# コース区分マスタ


class Mst_Course_class(Model):
    Course_class_code = IntegerField(verbose_name='コース区分コード', unique=True)
    Course_class_name = CharField(
        verbose_name='コース区分名称', max_length=5, blank=True, null=True)  # 外コース

    class Meta:
        verbose_name_plural = 'コース区分マスタ'

    def __str__(self):
        return self.Course_class_name

# 回り区分マスタ


class Mst_Clockwise_class(Model):
    CW_or_CCW_code = IntegerField(verbose_name='回り区分コード', unique=True)
    CW_or_CCW = CharField(verbose_name='回り区分名称',
                          max_length=5, blank=True, null=True)  # 右

    class Meta:
        verbose_name_plural = '回り区分マスタ'

    def __str__(self):
        return self.CW_or_CCW

# ナイター区分マスタ


class Mst_Night_race_class(Model):
    Night_race_code = IntegerField(
        verbose_name='ナイター区分コード', unique=True)  # 0：実施しない　1：実施
    Night_race_name = CharField(
        verbose_name='ナイター区分名称', max_length=5, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ナイター区分マスタ'

    def __str__(self):
        return self.Night_race_name

# 負担重量区分マスタ


class Mst_Handicap(Model):
    Handicap_code = IntegerField(verbose_name='負担重量区分コード', unique=True)
    Handicap_name = CharField(verbose_name='負担重量区分名称',
                              max_length=5, blank=True, null=True)  # ハンデ
    Weight_shortend = CharField(
        verbose_name='設定値', max_length=5, blank=True, null=True)

    class Meta:
        verbose_name_plural = '負担重量区分マスタ'

    def __str__(self):
        return self.Handicap_name

# 馬場状態マスタ


class Mst_Track_condition(Model):
    Track_condition_code = IntegerField(verbose_name='馬場状態コード', unique=True)
    Track_condition_name = CharField(
        verbose_name='馬場状態名称', max_length=5, blank=True, null=True)  # 良

    class Meta:
        verbose_name_plural = '馬場状態マスタ'

    def __str__(self):
        return self.Track_condition_name

# 騎手変更理由マスタ


class Mst_Jockey_changed_reason(Model):
    Jockey_changed_reason_code = IntegerField(
        verbose_name='騎手変更理由コード', unique=True)
    Jockey_changed_reason_name = CharField(
        verbose_name='騎手変更理由名称', max_length=10, blank=True, null=True)  # 公正保持

    class Meta:
        verbose_name_plural = '騎手変更理由マスタ'

    def __str__(self):
        return self.Jockey_changed_reason_name

# 事象マスタ


class Mst_Matter(Model):
    Matter_code = IntegerField(verbose_name='事象コード', unique=True)
    Matter_name = CharField(verbose_name='事象名称',
                            max_length=10, blank=True, null=True)  # 事故

    class Meta:
        verbose_name_plural = '事象マスタ'

    def __str__(self):
        return self.Matter_name

# 対象者マスタ


class Mst_Target_person(Model):
    Target_person_code = IntegerField(verbose_name='対象者コード', unique=True)
    Target_person_name = CharField(
        verbose_name='対象者名称', max_length=10, blank=True, null=True)  # 馬主

    class Meta:
        verbose_name_plural = '対象者マスタ'

    def __str__(self):
        return self.Target_person_name

# 競走種類マスタ


class Mst_Race_type(Model):
    Race_type_code = IntegerField(verbose_name='競走種類コード', unique=True)
    Race_type_name = CharField(
        verbose_name='競走種類名称', max_length=10, blank=True, null=True)  # 重賞
    Race_type_deliverytype = IntegerField(verbose_name='配信区分')  # 3

    class Meta:
        verbose_name_plural = '競走種類マスタ'

    def __str__(self):
        return self.Race_type_name

# ここまでデータ系マスタ

# ここから配信系マスタ

# 配信社マスタ


class Mst_Haishinsha(Model):
    Haishinsha_code = IntegerField(verbose_name='配信社コード')
    Haishinsha_name = CharField(verbose_name='配信社名称', max_length=10)  # 北海道新聞
    Haishinsha_2char_name = CharField(
        verbose_name='配信社名称2文字', max_length=2, blank=True, null=True)  # 道新
    Haishinsha_block = IntegerField(
        verbose_name='ブロック指定フラグ', blank=True, null=True)
    Haishinsha_yobi = CharField(
        verbose_name='予備', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = '【配信系】配信社マスタ'

    def __str__(self):
        return self.Haishinsha_name

# 通常配信先マスタ


class Mst_Haishinsaki_Nomal(Model):
    Jou_code = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                          on_delete=CASCADE)  # 競馬場マスタ
    Haishin_racekaku = CharField(
        verbose_name='レース格', max_length=5, blank=True, null=True)
    Haishinsha_code = ForeignKey(
        'Mst_Haishinsha', verbose_name='配信先', on_delete=CASCADE)  # 配信社コード 配信社マスタ
    Haishin_yobi = CharField(
        verbose_name='予備', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = '【配信系】通常配信先マスタ'

    def __str__(self):
        return self.Haishin_racekaku

# 期間限定配信先マスタ


class Mst_Haishinsaki_Limited(Model):
    Haishinsha_code = ForeignKey(
        'Mst_Haishinsha', verbose_name='配信社コード', on_delete=CASCADE)  # 配信社コード 配信社マスタ
    Jou_code = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                          on_delete=CASCADE)  # 競馬場コード 競馬場マスタ
    Start_date = DateField(verbose_name='開始日時')
    End_date = DateField(verbose_name='終了日時')
    Start_race = IntegerField(verbose_name='開始R')
    End_race = IntegerField(verbose_name='終了R')
    File_name = CharField(verbose_name='ファイル名',
                          max_length=30, blank=True, null=True)
    Haishin_limited_yobi = CharField(
        verbose_name='予備', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = '【配信系】期間限定配信先マスタ'

    def __str__(self):
        return self.Haishin_gentei_file_name

# プリンタ出力先マスタ


class Mst_Printer(Model):
    Printer_kei = IntegerField(verbose_name='系')
    Printer_output = CharField(verbose_name='出力系', max_length=5)
    Printer_yobi = CharField(
        verbose_name='予備', max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = '【配信系】プリンタ出力先マスタ'

    def __str__(self):
        return self.Printer_output

# ここまで配信系マスタ

# ここからスケジュール系マスタ

# 開催日割
# まだ未完成。とりあえずつくった。


class Mst_Kaisai_Hiwari(Model):
    Kaisai_Hiwari_date = DateField(verbose_name='開催日割')

    class Meta:
        verbose_name_plural = '【スケジュール系】開催日割'

    def __str__(self):
        return self.Kaisai_Hiwari_date

# 本日施行情報
# まだ未完成。とりあえずつくった。


class Mst_Honjitu_Shikou(Model):
    Honjitu_Shikou_date = DateField(verbose_name='本日施行情報')

    class Meta:
        verbose_name_plural = '【スケジュール系】本日施行情報'

    def __str__(self):
        return self.Honjitu_Shikou_date

# その他

# 修正句マスタ


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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#                                                               【中間DB】　　  　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# 【中間DB】出走表
class Md_Shussouhyou(Model):

    # 基本情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                        on_delete=CASCADE, related_name="shussouhyou")  # 競馬場マスタ
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')
    rebangou = IntegerField(verbose_name='レース番号')
    shubetsu = ForeignKey('Mst_Breed_age', verbose_name='競争種別',
                          on_delete=CASCADE, related_name="shubetu")  # 品種年齢区分マスタ
    tokusouhonsuu = IntegerField(verbose_name='特別競争本題回数')
    tokusoumeihon = CharField(verbose_name='特別競争名本題',
                              max_length=100, blank=True, null=True)
    tokusoumeifuku = CharField(
        verbose_name='特別競争名副題', max_length=100, blank=True, null=True)

    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_fukusyoumei = CharField(
        verbose_name='副賞名', max_length=400, blank=True, null=True)

    guredo = ForeignKey('Mst_Grade', verbose_name='グレード',
                        on_delete=CASCADE, blank=True, null=True)  # グレードマスタ
    md_kyousousyu = ForeignKey('Mst_Race_type', verbose_name='競争種類コード',
                               on_delete=CASCADE, blank=True, null=True)  # 競走種類マスタ
    ck_chuokouryu = ForeignKey('Mst_JRA_exchanges', verbose_name='中央交流区分',
                               on_delete=CASCADE, blank=True, null=True)  # 中央交流区分マスタ
    kyori = IntegerField(verbose_name='競争距離', blank=True, null=True)

    # トラック情報
    ck_shibadat = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分',
                             on_delete=CASCADE, blank=True, null=True)  # 芝・ダート区分マスタ
    ck_naigai = ForeignKey('Mst_Course_class', verbose_name='コース区分',
                           on_delete=CASCADE, blank=True, null=True)  # コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class', verbose_name='回り区分',
                           on_delete=CASCADE, blank=True, null=True)  # 回り区分マスタ
    ck_naita = ForeignKey('Mst_Night_race_class', verbose_name='ナイター区分',
                          on_delete=CASCADE, blank=True, null=True)  # ナイター区分マスタ
    ck_shokin1 = IntegerField(verbose_name='1着賞金', blank=True, null=True)
    ck_shokin2 = IntegerField(verbose_name='2着賞金', blank=True, null=True)
    ck_shokin3 = IntegerField(verbose_name='3着賞金', blank=True, null=True)
    ck_shokin4 = IntegerField(verbose_name='4着賞金', blank=True, null=True)
    ck_shokin5 = IntegerField(verbose_name='5着賞金', blank=True, null=True)
    ck_rekobi = IntegerField(verbose_name='レコード発生年月日',
                             blank=True, null=True)  # 追加 例：19800918
    refun = IntegerField(verbose_name='レコードタイム分', blank=True, null=True)
    rebyo = IntegerField(verbose_name='レコードタイム秒', blank=True, null=True)
    remiri = IntegerField(verbose_name='レコードタイムミリ', blank=True, null=True)
    ck_rekokimei = CharField(verbose_name='レコード騎手名',
                             max_length=10, blank=True, null=True)  # 追加
    ck_rekofujyuu = IntegerField(
        verbose_name='レコード負担重量', blank=True, null=True)  # 追加
    rekobamei = CharField(verbose_name='レコード馬名',
                          max_length=10, blank=True, null=True)
    shusuu = IntegerField(verbose_name='出走頭数', blank=True, null=True)
    hji = IntegerField(verbose_name='発送時刻（時）', blank=True, null=True)
    hfun = IntegerField(verbose_name='発送時刻（分）', blank=True, null=True)
    # 品種年齢区分マスタ。競走種別用名称からしか選択できないので、NewsML生成時にマスタから馬齢条件用名称を取得する。
    # bareijouken = ForeignKey('Mst_Breed_age', verbose_name='競争種別', on_delete=CASCADE, related_name="barei")

    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_shikaku = CharField(verbose_name='競争資格',
                           max_length=10, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_rkaku = CharField(verbose_name='レース格',
                         max_length=10, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_rkumi = CharField(verbose_name='レース組',
                         max_length=10, blank=True, null=True)

    jyuuryoushubetsu = ForeignKey(
        'Mst_Handicap', verbose_name='負担重量区分', on_delete=CASCADE, blank=True, null=True)  # 負担重量区分マスタ

    class Meta:
        verbose_name_plural = '【中間DB】出走表'

    def __str__(self):
        return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/'+str(self.ck_kyouhi)+str(self.joumei) + str(self.rebangou)+'R'


# 出走馬情報（最大16頭立ての前提。）
class Md_Shussouhyou_shussouba(Model):

    # 出走表外部キー
    shussouhyou = ForeignKey('Md_Shussouhyou', verbose_name='出走表',
                             on_delete=CASCADE, related_name="shussouba")  # 【中間DB】出走表

    # 馬情報
    waku = IntegerField(verbose_name='枠番')
    uma = IntegerField(verbose_name='馬番')
    ck_boiro = CharField(verbose_name='帽色', max_length=10)
    fujuu = DecimalField(verbose_name='負担重量',max_digits=5,
                         decimal_places=1, blank=True, null=True)
    ck_sekijuu = IntegerField(verbose_name='積載重量', blank=True, null=True)
    seibetsu = ForeignKey('Mst_Gender', verbose_name='性別',
                          on_delete=CASCADE)  # 性別マスタ
    bamei = CharField(verbose_name='馬名', max_length=10, blank=True, null=True)
    kyuubamei = CharField(verbose_name='旧馬名',
                          max_length=10, blank=True, null=True)
    barei = IntegerField(verbose_name='馬齢')
    ck_keiro = CharField(verbose_name='毛色', max_length=10,
                         blank=True, null=True)
    ck_chichi = CharField(
        verbose_name='父名', max_length=10, blank=True, null=True)
    ck_haha = CharField(verbose_name='母名', max_length=10,
                        blank=True, null=True)
    ck_hahachichi = CharField(
        verbose_name='母の父名', max_length=10, blank=True, null=True)
    ck_banushi = CharField(
        verbose_name='馬主名', max_length=30, blank=True, null=True)
    ck_seisansya = CharField(verbose_name='生産牧場名',
                             max_length=30, blank=True, null=True)
    ck_umasyozoku = ForeignKey('Mst_Belonging', verbose_name='所属場',
                               on_delete=CASCADE, related_name="uma_shozoku")  # 所属場マスタ
    ck_kakutokuskin = IntegerField(verbose_name='収得賞金')

    # 出走取り消し情報
    ck_jikosyu = ForeignKey('Mst_Accident_type', verbose_name='事故種別',
                            on_delete=CASCADE, related_name="shuusouba")  # 事故種類マスタ
    ck_jikoriyuu = ForeignKey('Mst_Accident_reason', verbose_name='事故理由',
                              on_delete=CASCADE, related_name="shuusouba")  # 事故理由マスタ

    # 騎手情報
    kimei = CharField(verbose_name='騎手名', max_length=3)
    kimei_sei = CharField(verbose_name='騎手名_姓',
                          max_length=20, blank=True, null=True)
    kimei_mei = CharField(verbose_name='騎手名_名',
                          max_length=20, blank=True, null=True)
    ck_kisyozoku = ForeignKey('Mst_Belonging', verbose_name='騎手所属場',
                              on_delete=CASCADE, related_name="kishu_shozoku")  # 所属場マスタ
    ck_kimnbangou = IntegerField(verbose_name='騎手免許番号')
    ck_kizen_1chaku = IntegerField(verbose_name='騎手成績 1着')
    ck_kizen_2chaku = IntegerField(verbose_name='騎手成績 2着')
    ck_kizen_3chaku = IntegerField(verbose_name='騎手成績 3着')
    ck_kizen_chakugai = IntegerField(verbose_name='騎手成績 着外')
    mikubun = IntegerField(verbose_name='見習区分')

    # 騎手変更情報
    ck_henriyuu = ForeignKey('Mst_Jockey_changed_reason', verbose_name='騎手変更理由',
                             on_delete=CASCADE, blank=True, null=True)  # 騎手変更理由マスタ
    ck_maekimei = CharField(verbose_name='変更前騎手名',
                            max_length=30, blank=True, null=True)
    ck_henmaefujuu = DecimalField(
        verbose_name='変更前負担重量',max_digits=5, decimal_places=1, blank=True, null=True)
    ck_henmaesekijuu = IntegerField(
        verbose_name='変更前積載重量', blank=True, null=True)

    # 調教師情報
    choumei = CharField(verbose_name='調教師名', max_length=30)
    choumei_sei = CharField(verbose_name='調教師名_姓',
                            max_length=20, blank=True, null=True)
    choumei_mei = CharField(verbose_name='調教師名_名',
                            max_length=20, blank=True, null=True)

    # 距離別成績
    ck_tan_1chaku = IntegerField(verbose_name='短距離 1着', blank=True, null=True)
    ck_tan_2chaku = IntegerField(verbose_name='短距離 2着', blank=True, null=True)
    ck_tan_3chaku = IntegerField(verbose_name='短距離 3着', blank=True, null=True)
    ck_tan_chakugai = IntegerField(
        verbose_name='短距離 着外', blank=True, null=True)
    ck_tyuu_1chaku = IntegerField(verbose_name='中距離 1着', blank=True, null=True)
    ck_tyuu_2chaku = IntegerField(verbose_name='中距離 2着', blank=True, null=True)
    ck_tyuu_3chaku = IntegerField(verbose_name='中距離 3着', blank=True, null=True)
    ck_tyuu_chakugai = IntegerField(
        verbose_name='中距離 着外', blank=True, null=True)
    ck_tyou_1chaku = IntegerField(verbose_name='長距離 1着', blank=True, null=True)
    ck_tyou_2chaku = IntegerField(verbose_name='長距離 2着', blank=True, null=True)
    ck_tyou_3chaku = IntegerField(verbose_name='長距離 3着', blank=True, null=True)
    ck_tyou_chakugai = IntegerField(
        verbose_name='長距離 着外', blank=True, null=True)

    # 場別距離別累計成績(距離別コース別成績)
    # Md_Shussouhyou_shussouba_ruikei に外だし

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

    ck_omo_1chaku = IntegerField(verbose_name='重と不良馬場成績 1着')
    ck_omo_2chaku = IntegerField(verbose_name='重と不良馬場成績 2着')
    ck_omo_3chaku = IntegerField(verbose_name='重と不良馬場成績 3着')
    ck_omo_chakugai = IntegerField(verbose_name='重と不良馬場成績 着外')

    ck_omo_1chaku_shiba = IntegerField(verbose_name='重と不良馬場成績_芝 1着')
    ck_omo_2chaku_shiba = IntegerField(verbose_name='重と不良馬場成績_芝 2着')
    ck_omo_3chaku_shiba = IntegerField(verbose_name='重と不良馬場成績_芝 3着')
    ck_omo_chakugai_shiba = IntegerField(verbose_name='重と不良馬場成績_芝 着外')

    class Meta:
        verbose_name_plural = '【中間DB】出走表_出走馬'

    def __str__(self):
        return str(self.shussouhyou) + str(self.uma) + '番 ' + str(self.bamei)

    # 場別距離別累計成績
class Md_Shussouhyou_shussouba_ruikei(Model):

    # 出走馬外部キー
    shussouba = ForeignKey('Md_Shussouhyou_shussouba', verbose_name='出走馬',
                           on_delete=CASCADE, related_name="shussouba_ruikei")  # 【中間DB】出走表_出走馬

    ck_ruijoumei = ForeignKey('Mst_Jou', verbose_name='累計競馬場名',
                              on_delete=CASCADE, related_name="rukei", blank=True, null=True)  # 競馬場マスタ

    ck_ruikyori = IntegerField(verbose_name='累計距離', blank=True, null=True)

    ck_ruishibadat = ForeignKey(
        'Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE, blank=True, null=True)  # 芝・ダート区分マスタ

    ck_ruibajru = ForeignKey('Mst_Track_condition', verbose_name='該当馬最高タイム_馬場状態',
                             on_delete=CASCADE, related_name="kyoribetsu_tougai", blank=True, null=True)  # 馬場状態マスタ
    ck_kkbasui = DecimalField(verbose_name='馬場水分（ばんえい）',max_digits=5,decimal_places=1, blank=True, null=True)

    ck_ruikai_1chaku = IntegerField(
        verbose_name='累計回数 1着', blank=True, null=True)
    ck_ruikai_2chaku = IntegerField(
        verbose_name='累計回数 2着', blank=True, null=True)
    ck_ruikai_3chaku = IntegerField(
        verbose_name='累計回数 3着', blank=True, null=True)
    ck_ruikai_chakugai = IntegerField(
        verbose_name='累計回数 着外', blank=True, null=True)
    ck_ruirekuta = IntegerField(
        verbose_name='累計最高タイム', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】出走表_出走馬_場別距離別累計成績'

    def __str__(self):
        return str(self.shussouba) + ' ' + str(self.ck_ruijoumei) + ' ' + str(self.ck_ruishibadat) + ' ' + str(self.ck_ruikyori) + 'm'

    # 過去成績 5回分繰り返す
class Md_Shussouhyou_shussouba_5seiseki(Model):

    # 出走馬外部キー
    shussouba = ForeignKey('Md_Shussouhyou_shussouba', verbose_name='出走馬',
                           on_delete=CASCADE, related_name="shussouba_kako")  # 【中間DB】出走表_出走馬

    # 出走日付
    ck_kkhiduke = DateField(verbose_name='出走日付')
    # 開催場情報
    ck_kkjoumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                             on_delete=CASCADE, related_name="shussouba_kako")  # 競馬場マスタ
    ck_kktenkou = ForeignKey(
        'Mst_Weather', verbose_name='天候マスタ', on_delete=CASCADE)  # 天候マスタ
    ck_kkbajou = ForeignKey(
        'Mst_Track_condition', verbose_name='馬場状態マスタ', on_delete=CASCADE, blank=True, null=True)  # 馬場状態マスタ
    ck_kkbasui = DecimalField(verbose_name='馬場水分（ばんえい）',max_digits=5,
                         decimal_places=1, blank=True, null=True)
    # レース情報
    ck_kknaita = ForeignKey(
        'Mst_Night_race_class', verbose_name='ナイター区分マスタ', on_delete=CASCADE)  # ナイター区分マスタ
    ck_kkshubetsu = ForeignKey('Mst_Breed_age', verbose_name='品種年齢区分マスタ',
                               on_delete=CASCADE, related_name="kako")  # 品種年齢区分マスタ
    ck_kkrmei = CharField(verbose_name='レース名称',
                          max_length=50, blank=True, null=True)

    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_kkshikaku = CharField(verbose_name='競争資格条件',
                             max_length=30, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_kkrkaku = CharField(verbose_name='レース格',
                           max_length=20, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_kkrkumi = CharField(verbose_name='レース組',
                           max_length=20, blank=True, null=True)

    ck_kkguredo = ForeignKey(
        'Mst_Grade', verbose_name='グレードマスタ', on_delete=CASCADE)  # グレードマスタ
    ck_kkkyori = IntegerField(verbose_name='競争距離')
    # トラック情報
    ck_shibadat = ForeignKey(
        'Mst_Turf_dirt_class', verbose_name='芝・ダート区分', on_delete=CASCADE)  # 芝・ダート区分マスタ
    ck_naigai = ForeignKey(
        'Mst_Course_class', verbose_name='コース区分', on_delete=CASCADE)  # コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class',
                           verbose_name='回り区分', on_delete=CASCADE)  # 回り区分マスタ

    ck_kkshusuu = IntegerField(verbose_name='出走頭数')
    # 出走馬成績情報
    ck_kkjuni = IntegerField(verbose_name='順位')
    ck_kknyujuni = IntegerField(verbose_name='入選順位')
    ck_kkwaku = IntegerField(verbose_name='枠番')
    ck_kkuma = IntegerField(verbose_name='馬番')
    ck_kkfujuu = IntegerField(verbose_name='負担重量')
    ck_kksekijuu = IntegerField(verbose_name='積載重量')
    ck_kkgenkigou = CharField(
        verbose_name='減量記号', max_length=3, blank=True, null=True)
    ck_kkkimei = CharField(verbose_name='騎手名（３字略）',
                           max_length=3, blank=True, null=True)
    ck_kktime = IntegerField(verbose_name='タイム')
    ck_kkaiteuma = CharField(
        verbose_name='相手馬名', max_length=10, blank=True, null=True)
    ck_kktimesa = IntegerField(verbose_name='タイム差')
    ck_kkjikosyu = ForeignKey(
        'Mst_Accident_type', verbose_name='事故種類コード', on_delete=CASCADE)  # 事故種類マスタ
    ck_kkjikoriyuu = ForeignKey(
        'Mst_Accident_reason', verbose_name='事故理由コード', on_delete=CASCADE)  # 事故理由マスタ
    ck_kkkojuni = CharField(
        verbose_name='コーナー通過順', max_length=20, blank=True, null=True)  # -で区切る　例：3-4-4-5
    ck_kka3ha = IntegerField(verbose_name='上がり３ハロン', blank=True, null=True)
    ck_kkbajuu = IntegerField(verbose_name='馬体重', blank=True, null=True)
    ck_kktannin = IntegerField(verbose_name='単勝人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】出走表_出走馬_過去成績'

    def __str__(self):
        return str(self.shussouba) + ' ' + str(self.ck_kkhiduke)


# ======================================================================================================================


# # 【中間DB】入場人員 →【中間DB】場当日情報に統合
# class Md_Nyujo(Model):
#     # 基本情報
#     joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
#                         on_delete=CASCADE, related_name="nyujo")  # 競馬場マスタ
#     ck_kyounen = IntegerField(verbose_name='年')
#     ck_kyoutuki = IntegerField(verbose_name='月')
#     ck_kyouhi = IntegerField(verbose_name='日')
#     kaisuu = IntegerField(verbose_name='回数')
#     kainichime = IntegerField(verbose_name='開催日目')

#     tounyuujinin = IntegerField(verbose_name='当日入場人員')

#     class Meta:
#         verbose_name_plural = '【中間DB】入場人員'

#     def __str__(self):
#         return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei) + str(self.tounyuujinin)


# # ======================================================================================================================


# # 【中間DB】売上金 →【中間DB】場当日情報に統合
# class Md_Uriagekin(Model):
#     # 基本情報
#     joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
#                         on_delete=CASCADE, related_name="uriage")  # 競馬場マスタ
#     ck_kyounen = IntegerField(verbose_name='年')
#     ck_kyoutuki = IntegerField(verbose_name='月')
#     ck_kyouhi = IntegerField(verbose_name='日')
#     kaisuu = IntegerField(verbose_name='回数')
#     kainichime = IntegerField(verbose_name='開催日目')

#     touuriage = IntegerField(verbose_name='当日売上')

#     class Meta:
#         verbose_name_plural = '【中間DB】売上金'

#     def __str__(self):
#         return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei) + str(self.touuriage)


# ======================================================================================================================


# 【中間DB】場当日情報 （新設）
class Md_Jou_Toujitsu(Model):
    # 基本情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                        on_delete=CASCADE, related_name="uriage")  # 競馬場マスタ
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')

    # 当日情報
    touuriage = IntegerField(verbose_name='当日売上', blank=True, null=True)
    tounyuujinin = IntegerField(verbose_name='当日入場人員', blank=True, null=True)

    tenkou =  CharField(verbose_name='当日の天候（中央競馬で使用している表記）', max_length=30, blank=True, null=True) #１Ｒから曇
    bajousiba =  CharField(verbose_name='当日の馬場状態（芝）中央競馬で使用している表記）', max_length=30, blank=True, null=True) #重後不良
    bajouda =  CharField(verbose_name='当日の馬場状態（ダート）中央競馬で使用している表記）', max_length=30, blank=True, null=True) # １Ｒから不良

    ck_tenkou =  CharField(verbose_name='当日の天候（地方競馬表記）', max_length=30, blank=True, null=True) # １Ｒから晴、７Ｒから曇
    ck_bajousiba =  CharField(verbose_name='当日の馬場状態（芝）地方競馬表記）', max_length=30, blank=True, null=True) #重後不良
    ck_bajouda =  CharField(verbose_name='当日の馬場状態（ダート）地方競馬表記）', max_length=30, blank=True, null=True) # １Ｒから不良

    ck_babamizu =  CharField(verbose_name=' 馬場水分（ばんえい競馬）', max_length=30, blank=True, null=True) #  ２．９－２．３％

    touresuu = IntegerField(verbose_name='当日レース数') # 当日レース数



    class Meta:
        verbose_name_plural = '【中間DB】場当日情報'

    def __str__(self):
        return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei)


# ======================================================================================================================
# 【中間DB】成績・払戻_レース別
class Md_Seiseki_Haraimodoshi(Model):

    # 場当日情報外部キー
    jou_toujitsu = ForeignKey(
        'Md_Jou_Toujitsu', verbose_name='場当日情報', on_delete=CASCADE,  related_name="seiseki")  # 【中間DB】場当日情報


    # 当日情報（レース単位）
    tenkou = ForeignKey('Mst_Weather', verbose_name='天候マスタ',
                        on_delete=CASCADE)  # 天候マスタ
    md_bajyou = ForeignKey('Mst_Track_condition',
                           verbose_name='馬場状態マスタ', on_delete=CASCADE, blank=True, null=True)  # 馬場状態マスタ
    md_sibada = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分',
                           on_delete=CASCADE, related_name="tojitsu")  # 芝・ダート区分マスタ
    ck_babamizu = DecimalField(verbose_name='馬場水分（ばんえい）', max_digits=5,
                               decimal_places=1, blank=True, null=True)

    # レース情報
    rebangou = IntegerField(verbose_name='レース番号')
    rekekka = CharField(verbose_name='レース結果', max_length=20, blank=True, null=True) # レース成立 or レース中止
    shubetsu = ForeignKey('Mst_Breed_age', verbose_name='競争種別',
                          on_delete=CASCADE, related_name="seiseki_shubetu")  # 品種年齢区分マスタ
    tokusouhonsuu = IntegerField(verbose_name='特別競争本題回数')
    tokusoumeihon = CharField(verbose_name='特別競争名本題',
                              max_length=100, blank=True, null=True)
    tokusoumeifuku = CharField(
        verbose_name='特別競争名副題', max_length=100, blank=True, null=True)

    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_fukusyoumei = CharField(
        verbose_name='副賞名', max_length=100, blank=True, null=True)

    guredo = ForeignKey('Mst_Grade', verbose_name='グレード',
                        on_delete=CASCADE, blank=True, null=True)  # グレードマスタ
    md_kyousousyu = ForeignKey(
        'Mst_Race_type', verbose_name='競争種類コード', on_delete=CASCADE)  # 競走種類マスタ
    ck_chuokouryu = ForeignKey(
        'Mst_JRA_exchanges', verbose_name='中央交流区分', on_delete=CASCADE)  # 中央交流区分マスタ
    kyori = IntegerField(verbose_name='競争距離', blank=True, null=True)
    kanhyouki = CharField(verbose_name='完表記', max_length=2, blank=True, null=True) # 当日最終レースを示す(完) ※最終レースのみ編集
    shoribi = IntegerField(verbose_name='処理日', blank=True, null=True) # 当開催・開催日のレースを処理した年月日 ※第１レースのみ編集

    # トラック情報
    ck_shibadat = ForeignKey('Mst_Turf_dirt_class', verbose_name='芝・ダート区分',
                             on_delete=CASCADE, related_name="track")  # 芝・ダート区分マスタ
    ck_naigai = ForeignKey(
        'Mst_Course_class', verbose_name='コース区分', on_delete=CASCADE)  # コース区分マスタ
    ck_mawari = ForeignKey('Mst_Clockwise_class',
                           verbose_name='回り区分', on_delete=CASCADE)  # 回り区分マスタ
    ck_kknaita = ForeignKey(
        'Mst_Night_race_class', verbose_name='ナイター区分マスタ', on_delete=CASCADE)  # ナイター区分マスタ

    ck_shokin1 = IntegerField(verbose_name='1着賞金')
    ck_shokin2 = IntegerField(verbose_name='2着賞金')
    ck_shokin3 = IntegerField(verbose_name='3着賞金')
    ck_shokin4 = IntegerField(verbose_name='4着賞金')
    ck_shokin5 = IntegerField(verbose_name='5着賞金')
    shusuu = IntegerField(verbose_name='出走頭数')
    jyoukenjouhou1 = CharField(
        verbose_name='競争条件１情報', max_length=30, blank=True, null=True)

    # 競争条件情報
    bareijouken = ForeignKey('Mst_Breed_age', verbose_name='競争種別',
                             on_delete=CASCADE, related_name="seiseki_barei")  # 品種年齢区分マスタ

    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_shikaku = CharField(verbose_name='競争資格条件',
                           max_length=30, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_rkaku = CharField(verbose_name='レース格',
                         max_length=20, blank=True, null=True)
    # ★★★　 複数ある場合は、','(カンマ)で区切って格納する。
    ck_rkumi = CharField(verbose_name='レース組',
                         max_length=20, blank=True, null=True)

    jyuuryoushubetsu = ForeignKey(
        'Mst_Handicap', verbose_name='負担重量区分', on_delete=CASCADE)  # 負担重量区分マスタ

    # 成績情報
    # Md_Seiseki_Haraimodoshi_seisekiに外だし

    # 払戻情報
    # 単勝払戻情報
    tanharajyoukyou = CharField(
        verbose_name='単勝払戻状況', max_length=10, blank=True, null=True)

    # 複勝払戻情報
    fukuharajoukyou = CharField(
        verbose_name='複勝払戻状況', max_length=10, blank=True, null=True)

    # 枠連複払戻情報
    wakupukuharajoukyou = CharField(
        verbose_name='枠連複払戻状況', max_length=10, blank=True, null=True)

    # 枠連単払戻情報
    ck_wakutanharajoukyou = CharField(
        verbose_name='枠連単払戻状況', max_length=10, blank=True, null=True)

    # 馬連複払戻情報
    umapukuharajoukyou = CharField(
        verbose_name='馬連複払戻状況', max_length=10, blank=True, null=True)

    # 馬連単払戻情報
    umatanharajoukyou = CharField(
        verbose_name='馬連単払戻状況', max_length=10, blank=True, null=True)

    # 三連複複払戻情報
    sanpukuharajoukyou = CharField(
        verbose_name='三連複払戻状況', max_length=10, blank=True, null=True)

    # 三連単払戻情報
    santanharajoukyou = CharField(
        verbose_name='三連単払戻状況', max_length=10, blank=True, null=True)

    # ワイド払戻情報
    waharajoukyou = CharField(verbose_name='ワイド払戻状況',
                              max_length=10, blank=True, null=True)

    # 処理日
    shoribi = IntegerField(verbose_name='処理日')

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻(レース別)'

    def __str__(self):
        return str(self.jou_toujitsu) + str(self.rebangou)+'R'

# ________________________________________________________________________________________________________________________________________

# 【中間DB】成績・払戻_馬別成績
class Md_Seiseki_Haraimodoshi_seiseki(Model):

    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE, related_name="seiseki")  # 【中間DB】成績・払戻

    # 着順情報
    juni = IntegerField(verbose_name='順位')
    nyuusenjuni = IntegerField(verbose_name='入線順位', blank=True, null=True)
    waku = IntegerField(verbose_name='枠番', blank=True, null=True)
    uma = IntegerField(verbose_name='馬番')
    ck_boiro = CharField(verbose_name='帽色', max_length=10, blank=True, null=True)
    bamei = CharField(verbose_name='馬名', max_length=10)
    ck_umasyozoku = ForeignKey('Mst_Belonging', verbose_name='所属場',on_delete=CASCADE, related_name="seiseki_uma_shozoku", blank=True, null=True)  # 所属場マスタ
    seibetsu = ForeignKey('Mst_Gender', verbose_name='性別',on_delete=CASCADE, blank=True, null=True)  # 性別マスタ
    barei = IntegerField(verbose_name='馬齢', blank=True, null=True)
    fujuu = IntegerField(verbose_name='負担重量', blank=True, null=True)
    ck_sekijuu = IntegerField(verbose_name='積載重量', blank=True, null=True)

    kimei = CharField(verbose_name='騎手名', max_length=30, blank=True, null=True)
    kimei_sei = CharField(verbose_name='騎手名_姓',
                          max_length=20, blank=True, null=True)
    kimei_mei = CharField(verbose_name='騎手名_名',
                          max_length=20, blank=True, null=True)
    ck_kimnbangou = IntegerField(verbose_name='騎手免許番号', blank=True, null=True)
    mikubun = IntegerField(verbose_name='見習区分', blank=True, null=True)
    md_genkigou = CharField(verbose_name='減量記号',
                            max_length=3, blank=True, null=True)

    ck_maekimei = CharField(verbose_name='変更前騎手名', max_length=30, blank=True, null=True)
    ck_maekimei_sei = CharField(verbose_name='変更前騎手名_姓',
                          max_length=20, blank=True, null=True)
    ck_maekimei_mei = CharField(verbose_name='変更前騎手名_名',
                          max_length=20, blank=True, null=True)

    ck_maekimnbangou = IntegerField(verbose_name='変更前騎手免許番号', blank=True, null=True)
    ck_maemikubun = IntegerField(verbose_name='変更前騎手見習区分', blank=True, null=True)
    ck_henriyuu = ForeignKey('Mst_Jockey_changed_reason',
                             verbose_name='騎手変更理由', on_delete=CASCADE, blank=True, null=True)  # 騎手変更理由マスタ

    # タイム
    fun = IntegerField(verbose_name='分', blank=True, null=True)
    byo = IntegerField(verbose_name='秒', blank=True, null=True)
    miri = IntegerField(verbose_name='ミリ', blank=True, null=True)
    reko = CharField(verbose_name='レコード', max_length=5, blank=True, null=True)

    # 着差情報
    # ★★★　 降着時に複数ある場合は、','(カンマ)で区切って格納する。
    # sa = ForeignKey('Mst_Margin', verbose_name='着差',on_delete=CASCADE)  # 着差マスタ
    sa = ManyToManyField('Mst_Margin', verbose_name='着差', blank=True)  # 着差マスタ

    md_doutyaku = IntegerField(verbose_name='同着区分', blank=True, null=True)
    sareigai = ForeignKey('Mst_Accident_type', verbose_name='着差例外',
                          on_delete=CASCADE, related_name="chakusa_reigai", blank=True, null=True)  # 事故種類マスタ
    ck_jikosyu = ForeignKey('Mst_Accident_type', verbose_name='事故種別',
                            on_delete=CASCADE, related_name="jiko_shubetu", blank=True, null=True)  # 事故種類マスタ
    ck_jikoriyuu = ForeignKey(
        'Mst_Accident_reason', verbose_name='事故理由', on_delete=CASCADE, blank=True, null=True)  # 事故理由マスタ
    bajuu = IntegerField(verbose_name='馬体重', blank=True, null=True)
    bajuuzougen = IntegerField(verbose_name='馬体重増減', blank=True, null=True)
    tannin = IntegerField(verbose_name='単勝人気', blank=True, null=True)
    choumei = CharField(verbose_name='調教師名', max_length=30, blank=True, null=True)
    choumei_sei = CharField(verbose_name='調教師名_姓',
                            max_length=20, blank=True, null=True)
    choumei_mei = CharField(verbose_name='調教師名_名',
                            max_length=20, blank=True, null=True)
    ikubunnai = ForeignKey('Mst_Accident_type', verbose_name='異常区分内容',
                           on_delete=CASCADE, related_name="ijou_kubun", blank=True, null=True)  # 事故種類マスタ

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻(馬別)'

    def __str__(self):
        return str(self.seiseki_haraimodoshi)+'/' + str(self.juni) + '着 ' + str(self.bamei)


# ________________________________________________________________________________________________________________________________________

# 【中間DB】成績・払戻_単勝


class Md_Seiseki_Haraimodoshi_tan(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="tanshou")  # 【中間DB】成績・払戻

    tankumijoukyou = CharField(
        verbose_name='単勝組番状況', max_length=10, blank=True, null=True)
    tansaki = IntegerField(verbose_name='単勝先番', blank=True, null=True)
    tanharakin = IntegerField(verbose_name='単勝払戻金', blank=True, null=True)
    tantounin = IntegerField(verbose_name='単勝投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_単勝'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.tansaki) + ' ' + str(self.tanharakin) + '円'


# 【中間DB】成績・払戻_複勝
class Md_Seiseki_Haraimodoshi_fuku(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="fukushou")  # 【中間DB】成績・払戻

    fukukumijoukyou = CharField(
        verbose_name='複勝組番状況', max_length=10, blank=True, null=True)
    fukusaki = IntegerField(verbose_name='複勝先番', blank=True, null=True)
    fukuharakin = IntegerField(verbose_name='複勝払戻金', blank=True, null=True)
    ck_fukutounin = IntegerField(verbose_name='複勝投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_複勝'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.fukusaki) + ' ' + str(self.fukuharakin) + '円'

# 【中間DB】成績・払戻_枠連複


class Md_Seiseki_Haraimodoshi_wakupuku(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="wakupuku")  # 【中間DB】成績・払戻

    wakupukukumijoukyou = CharField(
        verbose_name='枠連複組番状況', max_length=10, blank=True, null=True)
    wakupukusaki = IntegerField(verbose_name='枠連複先番', blank=True, null=True)
    wakupukuato = IntegerField(verbose_name='枠連複後番', blank=True, null=True)
    wakupukuharakin = IntegerField(
        verbose_name='枠連複払戻金', blank=True, null=True)
    wakupukutounin = IntegerField(
        verbose_name='枠連複投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_枠連複'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.wakupukusaki) + '-' + str(self.wakupukuato) + ' ' + str(self.wakupukuharakin) + '円'

# 【中間DB】成績・払戻_枠連単


class Md_Seiseki_Haraimodoshi_wakutan(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="wakutan")  # 【中間DB】成績・払戻

    ck_wakutankumijoukyou = CharField(
        verbose_name='枠連単組番状況', max_length=10, blank=True, null=True)
    ck_wakutansaki = IntegerField(verbose_name='枠連単先番', blank=True, null=True)
    ck_wakutanato = IntegerField(verbose_name='枠連単後番', blank=True, null=True)
    ck_wakutanharakin = IntegerField(
        verbose_name='枠連単払戻金', blank=True, null=True)
    ck_wakutantounin = IntegerField(
        verbose_name='枠連単投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_枠連単'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.ck_wakutansaki) + '-' + str(self.ck_wakutanato) + ' ' + str(self.ck_wakutanharakin) + '円'

# 【中間DB】成績・払戻_馬連複


class Md_Seiseki_Haraimodoshi_umapuku(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="umapuku")  # 【中間DB】成績・払戻

    umapukukumijoukyou = CharField(
        verbose_name='馬連複組番状況', max_length=10, blank=True, null=True)
    umapukusaki = IntegerField(verbose_name='馬連複先番', blank=True, null=True)
    umapukuato = IntegerField(verbose_name='馬連複後番', blank=True, null=True)
    umapukuharakin = IntegerField(verbose_name='馬連複払戻金', blank=True, null=True)
    umapukutounin = IntegerField(verbose_name='馬連複投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_馬連複'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.umapukusaki) + '-' + str(self.umapukuato) + ' ' + str(self.umapukuharakin) + '円'


# 【中間DB】成績・払戻_馬連単
class Md_Seiseki_Haraimodoshi_umatan(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="umatan")  # 【中間DB】成績・払戻

    umatankumijoukyou = CharField(
        verbose_name='馬連単組番状況', max_length=10, blank=True, null=True)
    umatansaki = IntegerField(verbose_name='馬連単先番', blank=True, null=True)
    umatanato = IntegerField(verbose_name='馬連単後番', blank=True, null=True)
    umatanharakin = IntegerField(verbose_name='馬連単払戻金', blank=True, null=True)
    umatantounin = IntegerField(verbose_name='馬連単投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_馬連単'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.umatansaki) + '-' + str(self.umatanato) + ' ' + str(self.umatanharakin) + '円'

# 【中間DB】成績・払戻_三連複
class Md_Seiseki_Haraimodoshi_sanpuku(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="sanpuku")  # 【中間DB】成績・払戻

    sanpukukumijoukyou = CharField(
        verbose_name='三連複組番状況', max_length=10, blank=True, null=True)
    sanpukusaki = IntegerField(verbose_name='三連複先番', blank=True, null=True)
    sanpukunaka = IntegerField(verbose_name='三連複中番', blank=True, null=True)
    sanpukuato = IntegerField(verbose_name='三連複後番', blank=True, null=True)
    sanpukuharakin = IntegerField(verbose_name='三連複払戻金', blank=True, null=True)
    sanpukutounin = IntegerField(verbose_name='三連複投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_三連複'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.sanpukusaki) + '-' + str(self.sanpukunaka) + '-' + str(self.sanpukuato) + ' ' + str(self.sanpukuharakin) + '円'

# 【中間DB】成績・払戻_三連単


class Md_Seiseki_Haraimodoshi_santan(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="santan")  # 【中間DB】成績・払戻

    santankumijoukyou = CharField(
        verbose_name='三連単組番状況', max_length=10, blank=True, null=True)
    santansaki = IntegerField(verbose_name='三連単先番', blank=True, null=True)
    santannaka = IntegerField(verbose_name='三連単中番', blank=True, null=True)
    santanato = IntegerField(verbose_name='三連単後番', blank=True, null=True)
    santanharakin = IntegerField(verbose_name='三連単払戻金', blank=True, null=True)
    santantounin = IntegerField(verbose_name='三連単投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_三連単'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.santansaki) + '-' + str(self.santannaka) + '-' + str(self.santanato) + ' ' + str(self.santanharakin) + '円'


# 【中間DB】成績・払戻_ワイド
class Md_Seiseki_Haraimodoshi_wa(Model):
    # 成績・払戻外部キー
    seiseki_haraimodoshi = ForeignKey(
        'Md_Seiseki_Haraimodoshi', verbose_name='成績・払戻', on_delete=CASCADE,  related_name="wa")  # 【中間DB】成績・払戻

    wakumijoukyou = CharField(verbose_name='ワイド組番状況',
                              max_length=10, blank=True, null=True)
    wasaki = IntegerField(verbose_name='ワイド先番', blank=True, null=True)
    waato = IntegerField(verbose_name='ワイド後番', blank=True, null=True)
    waharakin = IntegerField(verbose_name='ワイド払戻金', blank=True, null=True)
    watounin = IntegerField(verbose_name='ワイド投票人気', blank=True, null=True)

    class Meta:
        verbose_name_plural = '【中間DB】成績・払戻_ワイド'

    def __str__(self):
        return str(self.seiseki_haraimodoshi) + ' ' + str(self.wasaki) + '-' + str(self.waato) + ' ' + str(self.waharakin) + '円'


# ======================================================================================================================


# 【中間DB】コーナー・ラップ
class Md_Corner_Rap(Model):

    # 基本情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                        on_delete=CASCADE, related_name="corner_rap")  # 競馬場マスタ
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')
    rebangou = IntegerField(verbose_name='レース番号')
    # １着馬情報 最大３頭（同着を考慮）
    chaku1uma_1 = IntegerField(verbose_name='１着馬番')
    chaku1uma_2 = IntegerField(verbose_name='１着馬番(同着)')
    chaku1uma_3 = IntegerField(verbose_name='１着馬番(同着)(同着)')

    a4ha = IntegerField(verbose_name='上がり４ハロン')
    a3ha = IntegerField(verbose_name='上がり３ハロン')
    # ハロンラップタイム ハロン数分、繰り返す(,でつなげて格納？)
    ta = IntegerField(verbose_name='タイム')

    # コーナー順位情報　※先頭馬番がグループの場合は、馬番が若い番号を設定。
    kosentouuma = IntegerField(verbose_name='コーナー先頭馬番')
    # コーナー詳細
    koshousai_sa = IntegerField(verbose_name='差')
    # 集団
    shuudan_sa = IntegerField(verbose_name='馬番')

    class Meta:
        verbose_name_plural = '【中間DB】コーナー・ラップ'

    def __str__(self):
        return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei) + str(self.rebangou) + 'R'


# ======================================================================================================================


# 【中間DB】上がり
class Md_Agari(Model):

    # 基本情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                        on_delete=CASCADE, related_name="agari")  # 競馬場マスタ
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')
    rebangou = IntegerField(verbose_name='レース番号')

    # 馬情報
    uma = IntegerField(verbose_name='馬番')
    bamei = CharField(verbose_name='馬名', max_length=10)
    a3hakei = IntegerField(verbose_name='上がり３ハロン計')

    class Meta:
        verbose_name_plural = '【中間DB】上がり'

    def __str__(self):
        return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei) + str(self.rebangou) + 'R'


# ======================================================================================================================


# 【中間DB】通信文
class Md_Tsuushimbun(Model):

    # 基本情報
    joumei = ForeignKey('Mst_Jou', verbose_name='競馬場コード',
                        on_delete=CASCADE, related_name="tsushinbun")  # 競馬場マスタ
    ck_kyounen = IntegerField(verbose_name='年')
    ck_kyoutuki = IntegerField(verbose_name='月')
    ck_kyouhi = IntegerField(verbose_name='日')
    kaisuu = IntegerField(verbose_name='回数')
    kainichime = IntegerField(verbose_name='開催日目')
    rebangou = IntegerField(verbose_name='レース番号')

    # 付加文書内容
    ck_jishou = ForeignKey('Mst_Matter', verbose_name='事象',
                           on_delete=CASCADE)  # 事象マスタ
    ck_taishousya = ForeignKey('Mst_Target_person', verbose_name='対象者',
                               on_delete=CASCADE, blank=True, null=True)  # 対象者マスタ
    uma = IntegerField(verbose_name='馬番')
    ck_jisyoumei = CharField(verbose_name='事象名', max_length=10)
    kijinai = CharField(verbose_name='記事内容', max_length=200)

    class Meta:
        verbose_name_plural = '【中間DB】通信文'

    def __str__(self):
        return str(self.ck_kyounen)+'/' + str(self.ck_kyoutuki) + '/' + str(self.ck_kyouhi) + str(self.joumei) + str(self.rebangou) + 'R ' + str(self.ck_jisyoumei)

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import *
from . import models
import re
from django.db.models import Q


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#                                                               NewsML生成処理　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
#　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　|
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 【共通処理】
# １．半角int（またはdecimal）→ 全角str用の辞書と関数
# （参考） https://qiita.com/YuukiMiyoshi/items/6ce77bf402a29a99f1bf
def intToZen(i):
    HAN2ZEN = str.maketrans({"0": "０", "1": "１", "2": "２", "3": "３", "4": "４",
                             "5": "５", "6": "６", "7": "７", "8": "８", "9": "９", ".": "．", "G": "Ｇ"})
    if i:
        return str(i).translate(HAN2ZEN)
    else:
        return

# ２．,(カンマ)で区切られた文字列をリスト化して返す関数。余分な空白は削除する。
# 文字列がない場合、空白で返す
def makelist(mojiretsu):
    str_list = ""
    if mojiretsu:
        str_list = [x.strip() for x in mojiretsu.split(',')]

    return str_list

# ３．馬名を９文字にする関数。馬名を左詰にして、空いたところには全角スペースを挿入。
def bamei9char(bamei):
    bamei_9char = ""
    if bamei:
     bamei_9char = '{:　<9}'.format(bamei)
    return bamei_9char

# ========================================================================
# 【ヘッダー】(共通)
# 各NewsML共通のヘッダー部分のパラメータ生成処理を実装する



# ========================================================================
# 【成績表A】(InData内部)
def NewsML_seisekiA(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # 年月日と場から場当日情報オブジェクトを取得。無かったら404
    jou_toujitsu = get_object_or_404(Md_Jou_Toujitsu.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi
                                       )

    params = {}

    #１）開催場情報 < joujouhou >・・・</joujouhou > で囲まれて表現される。
    # １）－１ 開催場名（3字、正式名）
    # <joumei hyouki = "3字" > 大井 < /joumei >
    # <joumei hyouki = "正式名" > 大井 < /joumei >
    # 開催競馬場名を3字と正式名を編集。属性値hyoukiの内容で区別する。
    jou_data = Mst_Jou.getJoudata(str(jou_toujitsu.joumei))
    params['joumei_seishiki'] = jou_data[0]
    params['joumei_3'] = jou_data[1]


    # １）－２ 開催回数
    # <kaisuu > １６回 < /kaisuu >
    # 開催回数を編集。『回』付きで編集する。
    params['kaisuu'] = intToZen(jou_toujitsu.kaisuu) + '回'

    # １）－３ 開催日目
    # <kainichime > ２日目 < /kainichime >
    # 開催日目を編集。『日目』付きで編集する。
    params['kainichime'] = intToZen(jou_toujitsu.kainichime) + '日目'

    # １）－４ 競走年月日
    # <ck_kyounichi >
    # <ck_kyounen > ２００４ < /ck_kyounen >
    # <ck_kyoutuki > １０ < /ck_kyoutuki >
    # <ck_kyouhi > １４ < /ck_kyouhi >
    # </ck_kyounichi >
    # 競走年月日を編集する。年・月・日別にそれぞれ編集。
    params['ck_kyounen'] = intToZen(jou_toujitsu.ck_kyounen)
    params['ck_kyoutuki'] = intToZen(jou_toujitsu.ck_kyoutuki)
    params['ck_kyouhi'] = intToZen(jou_toujitsu.ck_kyouhi)

    # １）－５ 当日情報 < toujouhou >・・・</toujouhou > で囲まれて表現される。
    # １）－５－１ 天候
    # <tenkou > 晴後曇 < /tenkou >
    # 当日の天候を編集（中央競馬で使用している表記）
    params['tenkou'] = intToZen(jou_toujitsu.tenkou)

    # １）－５－２ 馬場状態（芝）
    # <bajousiba > 重後不良 < /bajousiba >
    # 当日の馬場状態（芝）を編集（中央競馬で使用している表記）
    params['bajousiba'] = intToZen(jou_toujitsu.bajousiba)

    # １）－５－３ 馬場状態（ダート）
    # <bajouda > 不良 < /bajouda >
    # 当日の馬場状態（ダート）を編集（中央競馬で使用している表記）
    params['bajouda'] = intToZen(jou_toujitsu.bajouda)

    # １）－５－４ 天候
    # <ck_tenkou > １Ｒから晴、７Ｒから曇 < /ck_tenkou >
    # 当日の天候を編集（地方競馬表記）
    params['ck_tenkou'] = intToZen(jou_toujitsu.ck_tenkou)

    # １）－５－５ 馬場状態（芝）
    # <ck_bajousiba > １０Ｒから重 < /ck_bajousiba >
    # 当日の馬場状態（芝）を編集（地方競馬表記）
    params['ck_bajousiba'] = intToZen(jou_toujitsu.ck_bajousiba)

    # １）－５－６ 馬場状態（ダート）
    # <ck_bajouda > １Ｒから不良 < /ck_bajouda >
    # 当日の馬場状態（ダート）を編集（地方競馬表記）
    params['ck_bajouda'] = intToZen(jou_toujitsu.ck_bajousiba)

    # １）－５－７ 馬場水分（ばんえい競馬）
    # <ck_babamizu > ２．９－２．３％< /ck_babamizu >
    # 当日の馬場水分を編集。ばんえい競馬のみ編集。
    params['ck_babamizu'] = intToZen(jou_toujitsu.ck_babamizu)

    # １）－５－８ 当日入場人員
    # <tounyuujinin > ６５９９ < /tounyuujinin >
    # 当日の開催場の入場人員を編集。有料入場人員と無料入場人員の合計。
    params['tounyuujinin'] = intToZen(jou_toujitsu.tounyuujinin)

    # １）－５－９ 当日売上
    # <touuriage > ４６２３４９２００ < /touuriage >
    # 当日の売上を編集
    params['touuriage'] = intToZen(jou_toujitsu.touuriage)

    # ２）レース情報 < rejouhou >・・・</rejouhou > で囲まれて表現される。
    # 1レースごと編集し、開催レース分繰り返される。

    # ○○○○○○○○○レース情報取得○○○○○○○○○
    # 場当日情報オブジェクトからレース別成績オブジェクトのリストを取得。無かったら404
    seiseiki_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi.objects, jou_toujitsu=jou_toujitsu)

    seiseki_params = {}  # レースごとの成績のパラメータ
    seiseki_params_list = []  # ↑のレースごとの成績のパラメータをまとめたリスト

    for seiseki in seiseiki_list:
        # ２）－１ レース番号
        # <rebangou > １ < /rebangou >
        # レース番号を編集する。
        seiseki_params['rebangou'] = intToZen(seiseki.rebangou)

        # ２）－１ レース結果
        # <rekekka > レース成立 < /rekekka >
        # レースが成立した場合「レース成立」と編集する。
        # レースが不成立の場合は「レース中止」と編集し、同レースの着情報および払戻情報は編集しない。
        seiseki_params['rekekka'] = seiseki.rekekka

        # ○○○○○○○○○レース情報取得○○○○○○○○○
        # レース別成績オブジェクトから馬別成績オブジェクトのリストを取得。無かったら404
        seiseiki_umabetsu_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_seiseki.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_umabetsu_params = {}  # 馬ごとの成績のパラメータ
        seiseiki_umabetsu_params_list = []  # ↑の馬ごとの成績のパラメータをまとめたリスト

        # 「juni」が1~3の馬のみ取り出して下記馬別処理を行う（同着も考慮）。できれば順序も担保
        for seiseiki_umabetsu in seiseiki_umabetsu_list:
            if seiseiki_umabetsu.juni <= 3:
                # ３）着情報 < chakujunjouhou >・・・</chakujunjouhou > で囲まれて表現される。
                # レースが成立した場合に編集され、１～３着まで繰り返して表現する。
                # ３）－１ 順位
                # <juni > １ < /juni >
                # 確定順位を編集。
                seiseiki_umabetsu_params['juni'] = intToZen(seiseiki_umabetsu.juni)
                # ３）－２ 入線順位
                # <nyuusenjuni > １ < /nyuusenjuni >
                # ゴールした順位を編集。
                seiseiki_umabetsu_params['nyuusenjuni'] = intToZen(seiseiki_umabetsu.nyuusenjuni)

                # ３）－３ 馬名
                # <bamei hyouki = "9字" > ドンバニヤン < /bamei >
                # <bamei hyouki = "正式名" > ドンバニヤン < /bamei >
                # 馬名の9字と正式名を編集。属性値hyoukiの内容で区別する。
                seiseiki_umabetsu_params['bamei_seishiki'] = seiseiki_umabetsu.bamei
                seiseiki_umabetsu_params['bamei_9char'] = bamei9char(seiseiki_umabetsu.bamei)
                
                # ３）－４ 馬所属
                # <ck_umasyozoku > 川崎 < /ck_umasyozoku >
                # 馬の所属場を編集。
                seiseiki_umabetsu_params['ck_umasyozoku'] = seiseiki_umabetsu.ck_umasyozoku

                # ３）－５ 負担重量
                # <fujuu > ５６ < /fujuu >
                # 負担重量を編集。ばんえい競馬は編集しないため空タグ。
                seiseiki_umabetsu_params['fujuu'] = seiseiki_umabetsu.fujuu

                # ３）－６ 積載重量
                # <ck_sekijuu > ７５０ < /ck_sekijuu >
                # 積載重量を編集。ばんえい競馬のみ編集。
                seiseiki_umabetsu_params['ck_sekijuu'] = seiseiki_umabetsu.ck_sekijuu

                # ３）－７ 騎手名
                # <kimei hyouki = "3字" > 的場文 < /kimei >
                # <kimei hyouki = "姓" > 的場 < /kimei >
                # <kimei hyouki = "名" > 文男 < /kimei >
                # 騎手名の3字、姓、名を編集。属性値hyoukiの内容で区別する。
                # 外国人騎手など姓と名の分割が難しいケースについては、姓に名前を編集し、名については編集しない。
                seiseiki_umabetsu_params['kimei'] = seiseiki_umabetsu.kimei
                seiseiki_umabetsu_params['kimei_sei'] = seiseiki_umabetsu.kimei_sei
                seiseiki_umabetsu_params['kimei_mei'] = seiseiki_umabetsu.kimei_mei

                # ３）－８ 騎手コード
                # <kiko/>
                # 常に空タグを編集する。

                # ３）－９ 騎手免許番号
                # <ck_kimnbangou > ３０１３３ < /ck_kimnbangou >
                # 騎手免許番号を編集する。
                seiseiki_umabetsu_params['ck_kimnbangou'] = intToZen(seiseiki_umabetsu.ck_kimnbangou)

                # ３）－10 見習区分
                # <mikubun > １ < /mikubun >
                # 減量騎手が騎乗した場合の減量重量を編集。
                seiseiki_umabetsu_params['mikubun'] = intToZen(seiseiki_umabetsu.mikubun)

                # ３）－11 変更前騎手（騎手変更があった場合のみ編集）
                # <ck_maekimei hyouki = "3字" > 張田京 < /ck_maekimei >
                # <ck_maekimei hyouki = "姓" > 張田 < /ck_maekimei >
                # <ck_maekimei hyouki = "名" > 京 < /ck_maekimei >
                # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手名の3字、姓、名を編集。属性値hyoukiの内容で区別する。
                seiseiki_umabetsu_params['ck_maekimei'] = seiseiki_umabetsu.ck_maekimei
                seiseiki_umabetsu_params['ck_maekimei_sei'] = seiseiki_umabetsu.ck_maekimei_sei
                seiseiki_umabetsu_params['ck_maekimei_mei'] = seiseiki_umabetsu.ck_maekimei_mei

                # ３）－12 変更前騎手免許番号（騎手変更があった場合のみ編集）
                # <ck_maekimnbangou > ３００５９ < /ck_maekimnbangou >
                # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手の免許番号を編集する。
                seiseiki_umabetsu_params['ck_maekimnbangou'] = intToZen(seiseiki_umabetsu.ck_maekimnbangou)

                # ３）－13 変更前騎手見習区分（騎手変更があった場合のみ編集）
                # <ck_maemikubun > １ < /ck_maemikubun >
                # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手が減量騎手の場合に減量重量を編集。
                seiseiki_umabetsu_params['ck_maemikubun'] = intToZen(seiseiki_umabetsu.ck_maemikubun)

                # ３）－13 騎手変更理由（騎手変更があった場合のみ編集）
                # <ck_henriyuu > 事故 < /ck_henriyuu >
                # 騎手変更があった場合に編集される。騎手変更理由を編集。
                seiseiki_umabetsu_params['ck_henriyuu'] = seiseiki_umabetsu.ck_henriyuu

                # ３）－14 タイム
                # <ta >
                # <fun > １ < /fun >
                # <byo > ４８ < /byo >
                # <miri > ５ < /miri >
                # </ta >
                # 入着タイムを編集。タイムを分、秒、ミリ秒で編集する。
                seiseiki_umabetsu_params['fun'] = intToZen(seiseiki_umabetsu.fun)
                seiseiki_umabetsu_params['byo'] = intToZen(seiseiki_umabetsu.byo)
                seiseiki_umabetsu_params['miri'] = intToZen(seiseiki_umabetsu.miri)

                # ３）－15 レコード
                # <reko > レコード < /reko >
                # レコードが発生した場合に編集。
                seiseiki_umabetsu_params['reko'] = seiseiki_umabetsu.reko

                # ３）－16 着差情報 < sajouhou >・・・</sajouhou > で囲まれる。
                # 着差の対象となる馬が降着した場合は < sajouhou > を繰り返して編集。
                # <sa hyouki = "通常" > １馬身１／４ < /sa >
                # seiseiki_umabetsu_params['salist'] = makelist(seiseiki_umabetsu.sa.all())
                salist = []
                for sa in seiseiki_umabetsu.sa.all():
                    salist.append(sa)
                seiseiki_umabetsu_params['salist'] = salist
                # seiseiki_umabetsu_params['salist'] = seiseiki_umabetsu.sa
                # seiseiki_umabetsu_params['salist'] = ['１馬身１／４']

                # ３）－17 着差例外
                # <sareigai > 同着 < /sareigai >
                # 同着や降着が発生した場合に編集。
                # 例えば３着同着が２頭いる場合は、対象の２頭とも着差例外に「同着」を編集。
                seiseiki_umabetsu_params['sareigai'] = seiseiki_umabetsu.sareigai

                # ３）－18 事故種類
                # <ck_jikosyu > 降着 < /ck_jikosyu >
                # 降着の場合など「降着」と編集。
                seiseiki_umabetsu_params['ck_jikosyu'] = seiseiki_umabetsu.ck_jikosyu

                # ３）－19 事故理由
                # <ck_jikoriyuu > 進路妨害 < /ck_jikoriyuu >
                # 事故種類に対応した事故理由を編集。
                seiseiki_umabetsu_params['ck_jikoriyuu'] = seiseiki_umabetsu.ck_jikoriyuu

                seiseiki_umabetsu_params_list.append(seiseiki_umabetsu_params.copy())

        seiseki_params['seiseiki_umabetsu_params_list'] = seiseiki_umabetsu_params_list

        # ４）払戻情報 <harajouhou>・・・</harajouhou>で囲まれて表現される。
        # 単勝、複勝、枠連複、枠連単、馬連複、馬連単、三連複、三連単、ワイドで式別馬券の発売があるものについて編集する。
        # ４）－１ 単勝払戻情報 < tanharajouhou >・・・</tanharajouhou > で囲まれて編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○単勝払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから単勝払戻オブジェクトのリストを取得。無かったら404
        seiseiki_tan_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_tan.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_tan_params = {}  # 単勝1組分のパラメータ
        seiseiki_tan_params_list = []  # ↑の単勝1組分ごとのパラメータをまとめたリスト

        # ４）－１－１ 単勝払戻状況
        # <tanharajyoukyou > 特払い < /tanharajyoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['tanharajyoukyou'] = seiseki.tanharajyoukyou

        # ４）－１－２ 単勝組番情報 < tankumijouhou >・・・</tankumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_tan in seiseiki_tan_list:
            # ４）－１－２－１ 単勝組番状況
            # <tankumijoukyou > 無投票 < /tankumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_tan_params['tankumijoukyou'] = seiseiki_tan.tankumijoukyou

            # ４）－１－２－２ 単勝組番
            # <tankumi >
            # <tansaki > ４ < /tansaki >
            # </tankumi >
            # 単勝馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_tan_params['tansaki'] = intToZen(seiseiki_tan.tansaki)

            # ４）－１－２－３ 単勝払戻金
            # <tanharakin > １０９０ < /tanharakin >
            # 単勝払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_tan_params['tanharakin'] = intToZen(seiseiki_tan.tanharakin)

            # ４）－１－２－４ 単勝投票人気
            # <tantounin > ９ < /tantounin >
            # 人気を編集する。
            seiseiki_tan_params['tantounin'] = intToZen(seiseiki_tan.tantounin)

            seiseiki_tan_params_list.append(seiseiki_tan_params.copy())

        seiseki_params['seiseiki_tan_params_list'] = seiseiki_tan_params_list
        
        # ４）－２ 複勝払戻情報 < fukuharajouhou >・・・</fukuharajouhou > で囲まれて編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○複勝払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから複勝払戻オブジェクトのリストを取得。無かったら404
        seiseiki_fuku_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_fuku.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_fuku_params = {}  # 複勝1組分のパラメータ
        seiseiki_fuku_params_list = []  # ↑の複勝1組分ごとのパラメータをまとめたリスト

        # ４）－２－１ 複勝払戻状況
        # <fukuharajoukyou > 特払い < /fukuharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['fukuharajoukyou'] = seiseki.fukuharajoukyou

        # ４）－２－２ 複勝組番情報 < fukukumijouhou >・・・</fukukumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_fuku in seiseiki_fuku_list:
            # ４）－２－２－１ 複勝組番状況
            # <fukukumijoukyou > 無投票 < /fukukumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_fuku_params['fukukumijoukyou'] = seiseiki_fuku.fukukumijoukyou

            # ４）－２－２－２ 複勝組番
            # <fukukumi >
            # <fukusaki > ４ < /fukusaki >
            # </fukukumi >
            # 複勝馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_fuku_params['fukusaki'] = intToZen(seiseiki_fuku.fukusaki)

            # ４）－２－２－３ 複勝払戻金
            # <fukuharakin > １０９０ < /fukuharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_fuku_params['fukuharakin'] = intToZen(seiseiki_fuku.fukuharakin)

            # ４）－２－２－４ 複勝投票人気
            # <ck_fukutounin > ９ < /ck_fukutounin >
            # 人気を編集する。
            seiseiki_fuku_params['ck_fukutounin'] = intToZen(seiseiki_fuku.ck_fukutounin)

            seiseiki_fuku_params_list.append(seiseiki_fuku_params.copy())

        seiseki_params['seiseiki_fuku_params_list'] = seiseiki_fuku_params_list


        # ４）－３ 枠連複払戻情報 < wakupukuharajouhou >・・・</wakupukuharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○枠連複払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから枠連複払戻オブジェクトのリストを取得。無かったら404
        seiseiki_wakupuku_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_wakupuku.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_wakupuku_params = {}  # 枠連複1組分のパラメータ
        seiseiki_wakupuku_params_list = []  # ↑の枠連複1組分ごとのパラメータをまとめたリスト

        # ４）－３－１ 枠連複払戻状況
        # <wakupukuharajoukyou > 特払い < /wakupukuharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['wakupukuharajoukyou'] = seiseki.wakupukuharajoukyou

        # ４）－３－２ 枠連複組番情報 < wakupukukumijouhou >・・・</wakupukukumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_wakupuku in seiseiki_wakupuku_list:
            # ４）－３－２－１ 枠連複組番状況
            # <wakupukukumijoukyou > 無投票 < /wakupukukumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_wakupuku_params['wakupukukumijoukyou'] = seiseiki_wakupuku.wakupukukumijoukyou

            # ４）－３－２－２ 枠連複組番
            # <wakupukukumi >
            # <wakupukusaki > ３ < /wakupukusaki >
            # <wakupukuato > ８ < /wakupukuato >
            # </wakupukukumi >
            # 枠番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_wakupuku_params['wakupukusaki'] = intToZen(seiseiki_wakupuku.wakupukusaki)
            seiseiki_wakupuku_params['wakupukuato'] = intToZen(seiseiki_wakupuku.wakupukuato)

            # ４）－３－２－３ 枠連複払戻金
            # <wakupukuharakin > ９８０ < /wakupukuharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_wakupuku_params['wakupukuharakin'] = intToZen(seiseiki_wakupuku.wakupukuharakin)

            # ４）－３－２－４ 枠連複投票人気
            # <wakupukutounin > ４ < /wakupukutounin >
            # 人気を編集する。
            seiseiki_wakupuku_params['wakupukutounin'] = intToZen(seiseiki_wakupuku.wakupukutounin)

            seiseiki_wakupuku_params_list.append(seiseiki_wakupuku_params.copy())

        seiseki_params['seiseiki_wakupuku_params_list'] = seiseiki_wakupuku_params_list


        # ４）－４ 枠連単払戻情報 < ck_wakutanharajouhou >・・・</ck_wakutanharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○枠連単払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから枠連単払戻オブジェクトのリストを取得。無かったら404
        seiseiki_wakutan_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_wakutan.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_wakutan_params = {}  # 枠連単1組分のパラメータ
        seiseiki_wakutan_params_list = []  # ↑の枠連単1組分ごとのパラメータをまとめたリスト

        # ４）－４－１ 枠連単払戻状況
        # <ck_wakutanharajoukyou > 特払い < /ck_wakutanharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['ck_wakutanharajoukyou'] = seiseki.ck_wakutanharajoukyou

        # ４）－４－２ 枠連単組番情報 < ck_wakutankumijouhou >・・・</ck_wakutankumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_wakutan in seiseiki_wakutan_list:
            # ４）－４－２－１ 枠連単組番状況
            # <ck_wakutankumijoukyou > 無投票 < /ck_wakutankumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_wakutan_params['ck_wakutankumijoukyou'] = seiseiki_wakutan.ck_wakutankumijoukyou

            # ４）－４－２－２ 枠連単組番
            # <ck_wakutankumi >
            # <ck_wakutansaki > ３ < /ck_wakutansaki >
            # <ck_wakutanato > ８ < /ck_wakutanato >
            # </ck_wakutankumi >
            # 枠番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_wakutan_params['ck_wakutansaki'] = intToZen(seiseiki_wakutan.ck_wakutansaki)
            seiseiki_wakutan_params['ck_wakutanato'] = intToZen(seiseiki_wakutan.ck_wakutanato)

            # ４）－４－２－３ 枠連単払戻金
            # <ck_wakutanharakin > ９８０ < /ck_wakutanharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_wakutan_params['ck_wakutanharakin'] = intToZen(seiseiki_wakutan.ck_wakutanharakin)

            # ４）－４－２－４ 枠連単投票人気
            # <ck_wakutantounin > ４ < /ck_wakutantounin >
            # 人気を編集する。
            seiseiki_wakutan_params['ck_wakutantounin'] = intToZen(seiseiki_wakutan.ck_wakutantounin)

            seiseiki_wakutan_params_list.append(seiseiki_wakutan_params.copy())

        seiseki_params['seiseiki_wakutan_params_list'] = seiseiki_wakutan_params_list
        

        # ４）－５ 馬連複払戻情報 < umapukuharajouhou >・・・</umapukuharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○馬連複払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから馬連複払戻オブジェクトのリストを取得。無かったら404
        seiseiki_umapuku_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_umapuku.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_umapuku_params = {}  # 馬連複1組分のパラメータ
        seiseiki_umapuku_params_list = []  # ↑の馬連複1組分ごとのパラメータをまとめたリスト

        # ４）－５－１ 馬連複払戻状況
        # <umapukuharajoukyou > 特払い < /umapukuharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['umapukuharajoukyou'] = seiseki.umapukuharajoukyou

        # ４）－５－２ 馬連複組番情報 < umapukukumijouhou >・・・</umapukukumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_umapuku in seiseiki_umapuku_list:
            # ４）－５－２－１ 馬連複組番状況
            # <umapukukumijoukyou > 無投票 < /umapukukumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_umapuku_params['umapukukumijoukyou'] = seiseiki_umapuku.umapukukumijoukyou

            # ４）－５－２－２ 馬連複組番
            # <umapukukumi >
            # <umapukusaki > ４ < /umapukusaki >
            # <umapukuato > １４ < /umapukuato >
            # </umapukukumi >
            # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_umapuku_params['umapukusaki'] = intToZen(seiseiki_umapuku.umapukusaki)
            seiseiki_umapuku_params['umapukuato'] = intToZen(seiseiki_umapuku.umapukuato)

            # ４）－５－２－３ 馬連複払戻金
            # <umapukuharakin > ３０４ < /umapukuharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_umapuku_params['umapukuharakin'] = intToZen(seiseiki_umapuku.umapukuharakin)

            # ４）－５－２－４ 馬連複投票人気
            # <umapukutounin > １０ < /umapukutounin >
            # 人気を編集する。
            seiseiki_umapuku_params['umapukutounin'] = intToZen(seiseiki_umapuku.umapukutounin)

            seiseiki_umapuku_params_list.append(seiseiki_umapuku_params.copy())

        seiseki_params['seiseiki_umapuku_params_list'] = seiseiki_umapuku_params_list

        # ４）－６ 馬連単払戻情報 < umatanharajouhou >・・・</umatanharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○馬連単払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから馬連単払戻オブジェクトのリストを取得。無かったら404
        seiseiki_umatan_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_umatan.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_umatan_params = {}  # 馬連単1組分のパラメータ
        seiseiki_umatan_params_list = []  # ↑の馬連単1組分ごとのパラメータをまとめたリスト

        # ４）－６－１ 馬連単払戻状況
        # <umatanharajoukyou > 特払い < /umatanharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['umatanharajoukyou'] = seiseki.umatanharajoukyou

        # ４）－６－２ 馬連単組番情報 < umatankumijouhou >・・・</umatankumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_umatan in seiseiki_umatan_list:
            # ４）－６－２－１ 馬連単組番状況
            # <umatankumijoukyou > 無投票 < /umatankumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_umatan_params['umatankumijoukyou'] = seiseiki_umatan.umatankumijoukyou

            # ４）－６－２－２ 馬連単組番
            # <umatankumi >
            # <umatansaki > ４ < /umatansaki >
            # <umatanato > １４ < /umatanato >
            # </umatankumi >
            # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_umatan_params['umatansaki'] = intToZen(seiseiki_umatan.umatansaki)
            seiseiki_umatan_params['umatanato'] = intToZen(seiseiki_umatan.umatanato)

            # ４）－６－２－３ 馬連単払戻金
            # <umatanharakin > ３０４ < /umatanharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_umatan_params['umatanharakin'] = intToZen(seiseiki_umatan.umatanharakin)

            # ４）－６－２－４ 馬連単投票人気
            # <umatantounin > １０ < /umatantounin >
            # 人気を編集する。
            seiseiki_umatan_params['umatantounin'] = intToZen(seiseiki_umatan.umatantounin)

            seiseiki_umatan_params_list.append(seiseiki_umatan_params.copy())

        seiseki_params['seiseiki_umatan_params_list'] = seiseiki_umatan_params_list

        # ４）－７ 三連複払戻情報 < sanpukuharajouhou >・・・</sanpukuharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○三連複払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから三連複払戻オブジェクトのリストを取得。無かったら404
        seiseiki_sanpuku_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_sanpuku.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_sanpuku_params = {}  # 三連複1組分のパラメータ
        seiseiki_sanpuku_params_list = []  # ↑の三連複1組分ごとのパラメータをまとめたリスト

        # ４）－７－１ 三連複払戻状況
        # <sanpukuharajoukyou > 特払い < /sanpukuharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['sanpukuharajoukyou'] = seiseki.sanpukuharajoukyou

        # ４）－７－２ 三連複組番情報 < sanpukukumijouhou >・・・</sanpukukumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_sanpuku in seiseiki_sanpuku_list:
            # ４）－７－２－１ 三連複組番状況
            # <sanpukukumijoukyou > 無投票 < /sanpukukumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_sanpuku_params['sanpukukumijoukyou'] = seiseiki_sanpuku.sanpukukumijoukyou

            # ４）－７－２－２ 三連複組番
            # <sanpukukumi >
            # <sanpukusaki > ４ < /sanpukusaki >
            # <sanpukunaka > １３ < /sanpukunaka >
            # <sanpukuato > １４ < /sanpukuato >
            # </sanpukukumi >
            # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_sanpuku_params['sanpukusaki'] = intToZen(seiseiki_sanpuku.sanpukusaki)
            seiseiki_sanpuku_params['sanpukunaka'] = intToZen(seiseiki_sanpuku.sanpukunaka)
            seiseiki_sanpuku_params['sanpukuato'] = intToZen(seiseiki_sanpuku.sanpukuato)

            # ４）－７－２－３ 三連複払戻金
            # <sanpukuharakin > １２３０ < /sanpukuharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_sanpuku_params['sanpukuharakin'] = intToZen(seiseiki_sanpuku.sanpukuharakin)

            # ４）－７－２－４ 三連複投票人気
            # <sanpukutounin > ５ < /sanpukutounin >
            # 人気を編集する。
            seiseiki_sanpuku_params['sanpukutounin'] = intToZen(seiseiki_sanpuku.sanpukutounin)

            seiseiki_sanpuku_params_list.append(seiseiki_sanpuku_params.copy())

        seiseki_params['seiseiki_sanpuku_params_list'] = seiseiki_sanpuku_params_list

        # ４）－８ 三連単払戻情報 < santanharajouhou >・・・</santanharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。

        # ○○○○○○○○○三連単払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトから三連単払戻オブジェクトのリストを取得。無かったら404
        seiseiki_santan_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_santan.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_santan_params = {}  # 三連単1組分のパラメータ
        seiseiki_santan_params_list = []  # ↑の三連単1組分ごとのパラメータをまとめたリスト

        # ４）－８－１ 三連単払戻状況
        # <santanharajoukyou > 特払い < /santanharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['santanharajoukyou'] = seiseki.santanharajoukyou

        # ４）－８－２ 三連単組番情報 < santankumijouhou >・・・</santankumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_santan in seiseiki_santan_list:
            # ４）－８－２－１ 三連単組番状況
            # <santankumijoukyou > 無投票 < /santankumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_santan_params['santankumijoukyou'] = seiseiki_santan.santankumijoukyou

            # ４）－８－２－２ 三連単組番
            # <santankumi >
            # <santansaki > ４ < /santansaki >
            # <santannaka > １４ < /santannaka >
            # <santanato > １３ < /santanato >
            # </santankumi >
            # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_santan_params['santansaki'] = intToZen(seiseiki_santan.santansaki)
            seiseiki_santan_params['santannaka'] = intToZen(seiseiki_santan.santannaka)
            seiseiki_santan_params['santanato'] = intToZen(seiseiki_santan.santanato)

            # ４）－８－２－３ 三連単払戻金
            # <santanharakin > １２３０ < /santanharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_santan_params['santanharakin'] = intToZen(seiseiki_santan.santanharakin)

            # ４）－８－２－４ 三連単投票人気
            # <santantounin > ５ < /santantounin >
            # 人気を編集する。
            seiseiki_santan_params['santantounin'] = intToZen(seiseiki_santan.santantounin)

            seiseiki_santan_params_list.append(seiseiki_santan_params.copy())

        seiseki_params['seiseiki_santan_params_list'] = seiseiki_santan_params_list

        # ４）－９ ワイド払戻情報 < waharajouhou >・・・</waharajouhou > で囲み編集。
        # 式別発売がない場合は編集しない。
        
        # ○○○○○○○○○ワイド払戻情報取得○○○○○○○○○
        # レース別成績オブジェクトからワイド払戻オブジェクトのリストを取得。無かったら404
        seiseiki_wa_list = get_list_or_404(
            Md_Seiseki_Haraimodoshi_wa.objects, seiseki_haraimodoshi=seiseki)
        seiseiki_wa_params = {}  # ワイド1組分のパラメータ
        seiseiki_wa_params_list = []  # ↑のワイド1組分ごとのパラメータをまとめたリスト

        # ４）－９－１ ワイド払戻状況
        # <waharajoukyou > 特払い < /waharajoukyou >
        # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
        seiseki_params['waharajoukyou'] = seiseki.waharajoukyou

        # ４）－９－２ ワイド組番情報 < wakumijouhou >・・・</wakumijouhou > で囲み編集。
        # 払戻が複数ある場合は繰り返して編集。
        for seiseiki_wa in seiseiki_wa_list:
            # ４）－９－２－１ ワイド組番状況
            # <wakumijoukyou > 無投票 < /wakumijoukyou >
            # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
            seiseiki_wa_params['wakumijoukyou'] = seiseiki_wa.wakumijoukyou

            # ４）－９－２－２ ワイド組番
            # <wakumi >
            # <wasaki > ４ < /wasaki >
            # <waato > １４ < /waato >
            # </wakumi >
            # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
            seiseiki_wa_params['wasaki'] = intToZen(seiseiki_wa.wasaki)
            seiseiki_wa_params['waato'] = intToZen(seiseiki_wa.waato)

            # ４）－９－２－３ ワイド払戻金
            # <waharakin > ８６０ < /waharakin >
            # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
            seiseiki_wa_params['waharakin'] = intToZen(seiseiki_wa.waharakin)

            # ４）－９－２－４ ワイド投票人気
            # <watounin > ８ < /watounin >
            # 人気を編集する。
            seiseiki_wa_params['watounin'] = intToZen(seiseiki_wa.watounin)

            seiseiki_wa_params_list.append(seiseiki_wa_params.copy())

        seiseki_params['seiseiki_wa_params_list'] = seiseiki_wa_params_list

        seiseki_params_list.append(seiseki_params.copy())

    params['seiseki_params_list'] = seiseki_params_list



    # xml形式で出力
    res = render(request, 'NewsML_temp/seiseki_A.xml', params)
    res['Content-Type'] = 'application/xml'
    return res

    # return render(request, 'NewsML_temp/NewsML.html', {'title':'【成績表A】NewsMLプレビュー画面作成中(4/30)'})


# ========================================================================















# ========================================================================
# 【通信文A】(InData内部)
def NewsML_tsusinA(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # 年月日と場から通信文オブジェクトのリストを取得。無かったら404
    #  →★通信文が無い場合の処理が必要
    tsuushimbun_list = get_list_or_404(Md_Tsuushimbun.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi
                                       )

    # 場マスタから場のデータを取得
    jou_data = Mst_Jou.getJoudata(joucode)

    # 数値の全角化処理(馬番、レース番号)
    for tb in tsuushimbun_list:
        tb.uma = intToZen(tb.uma)
        tb.rebangou = intToZen(tb.rebangou) + 'Ｒ'
    

    # レース情報を一件目のデータからとる。
    tsuushinbun = tsuushimbun_list[0]

    # パラメータに追加(数値の項目は全角化する)
    params = {
        'joumei_seishiki': jou_data[0],
        'joumei_3': jou_data[1],

        'kaisuu': intToZen(tsuushinbun.kaisuu) + '回',
        'kainichime': intToZen(tsuushinbun.kainichime) + '日目',

        'ck_kyounen': intToZen(tsuushinbun.ck_kyounen),
        'ck_kyoutuki': intToZen(tsuushinbun.ck_kyoutuki),
        'ck_kyouhi': intToZen(tsuushinbun.ck_kyouhi),

        'tsuushimbun_list': tsuushimbun_list
    }

    # xml形式で出力
    res = render(request, 'NewsML_temp/tsuushimbun_A.xml', params)
    res['Content-Type'] = 'application/xml'
    return res

# ========================================================================















# ========================================================================

# 【通信文C】(InData内部)
def NewsML_tsuushimbunC(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # 年月日と場とレース番号から通信文オブジェクトのリストを取得。無かったら404
    tsuushimbun_list = get_list_or_404(Md_Tsuushimbun.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi,
                                       rebangou=rebangou
                                       )

    # 場マスタから場のデータを取得
    jou_data = Mst_Jou.getJoudata(joucode)

    # 数値の全角化処理(馬番)
    for tb in tsuushimbun_list:
        tb.uma = intToZen(tb.uma)

    # レース情報を一件目のデータからとる。
    tsuushinbun = tsuushimbun_list[0]

    # パラメータに追加(数値の項目は全角化する)
    params = {
        'joumei_seishiki': jou_data[0],
        'joumei_3': jou_data[1],

        'kaisuu': intToZen(tsuushinbun.kaisuu),
        'kainichime': intToZen(tsuushinbun.kainichime),

        'ck_kyounen': intToZen(tsuushinbun.ck_kyounen),
        'ck_kyoutuki': intToZen(tsuushinbun.ck_kyoutuki),
        'ck_kyouhi': intToZen(tsuushinbun.ck_kyouhi),
        'rebangou': intToZen(tsuushinbun.rebangou),

        'tsuushimbun_list': tsuushimbun_list
    }

    # xml形式で出力
    res = render(request, 'NewsML_temp/tsuushimbun_C.xml', params)
    res['Content-Type'] = 'application/xml'
    return res
# ========================================================================














# ========================================================================

# 【成績表C】(InData内部)
def NewsML_seisekiC(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # 年月日と場から場当日情報オブジェクトを取得。無かったら404
    jou_toujitsu = get_object_or_404(Md_Jou_Toujitsu.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi
                                       )

    # ○○○○○○○○○レース情報取得○○○○○○○○○
    # 場当日情報オブジェクトとレース番号からレース別成績オブジェクトを取得。無かったら404
    seiseki = get_object_or_404(
        Md_Seiseki_Haraimodoshi.objects, jou_toujitsu=jou_toujitsu, rebangou=rebangou)


    params = {}

    #１）開催関連情報
    # １）－１ 開催場名（3字、正式名）
    # <joumei hyouki = "3字" > 大井 < /joumei >
    # <joumei hyouki = "正式名" > 大井 < /joumei >
    # 開催競馬場名を3字と正式名を編集。属性値hyoukiの内容で区別する。
    jou_data = Mst_Jou.getJoudata(str(jou_toujitsu.joumei))
    params['joumei_seishiki'] = jou_data[0]
    params['joumei_3char'] = jou_data[1]


    # １）－２ 開催回数
    # <kaisuu > １６回 < /kaisuu >
    # 開催回数を編集。『回』付きで編集する。
    params['kaisuu'] = intToZen(jou_toujitsu.kaisuu) + '回'

    # １）－３ 開催日目
    # <kainichime > ２日目 < /kainichime >
    # 開催日目を編集。『日目』付きで編集する。
    params['kainichime'] = intToZen(jou_toujitsu.kainichime) + '日目'

    # １）－４ 完表記
    # <kanhyouki>完</kanhyouki>
    # 当日最終レースを示す。 ※最終レースのみ編集
    params['kanhyouki'] = seiseki.kanhyouki #完

    # １）－５ 競走年月日
    # <ck_kyounichi >
    # <ck_kyounen > ２００４ < /ck_kyounen >
    # <ck_kyoutuki > １０ < /ck_kyoutuki >
    # <ck_kyouhi > １４ < /ck_kyouhi >
    # </ck_kyounichi >
    # 競走年月日を編集する。年・月・日別にそれぞれ編集。
    params['ck_kyounen'] = intToZen(jou_toujitsu.ck_kyounen)
    params['ck_kyoutuki'] = intToZen(jou_toujitsu.ck_kyoutuki)
    params['ck_kyouhi'] = intToZen(jou_toujitsu.ck_kyouhi)


    # ２）場情報 <joujouhou> … </joujouhou>で囲み編集
    # ２）－１ 当日レース数
    # <touresuu>１１</touresuu>
    # 当日開催予定のレース数を編集する。 ※当日第１レースのみに編集する
    params['touresuu'] = intToZen(jou_toujitsu.touresuu)

    # ２）－２ 処理日
    # <shoribi>２００５０３０７</shoribi>
    # 当開催・開催日のレースを処理した年月日を編集する。 ※第１レースのみに編集
    params['shoribi'] = intToZen(seiseki.shoribi)

    # ２）－３ 天候
    # <tenkou>晴</tenkou>
    # レースごとに天候を編集する。
    params['tenkou'] = seiseki.tenkou

    # ２）－４ 馬場状態（芝）
    # <bajousiba>重</bajousiba>
    # 該当レースが芝の場合のみ、馬場状態を編集する。 ※ばんえい競馬は編集しない
    if str(seiseki.md_sibada) == '芝':
        params['bajousiba'] = seiseki.md_bajyou

    # ２）－５ 馬場状態（ダート）
    # <bajouda>不良</bajouda>
    # 該当レースがダートの場合のみ、馬場状態を編集する。 ※ばんえい競馬は編集しない
    if str(seiseki.md_sibada) == 'ダート':
        params['bajouda'] = seiseki.md_bajyou

    # ２）－６ 馬場水分
    # <ck_babamizu>２．９％</ck_babamizu>
    # ばんえい競馬のみの馬場状態で、『％』付きで編集する。
    if seiseki.ck_babamizu:
        params['ck_babamizu'] = intToZen(seiseki.ck_babamizu) + '％'

    # ３）レース情報 <rejouhou> … </rejouhou>で囲み編集

    # ３）－１ レース番号
    # <rebangou > １ < /rebangou >
    # レース番号を『Ｒ』付きで編集する。
    params['rebangou'] = intToZen(seiseki.rebangou) + 'Ｒ'

    # ３）－２ 競走種別
    # <shubetsu>サラ３歳上</shubetsu>
    # 競走種別を編集、馬齢部分は洋数字で編集する。
    params['shubetsu'] = intToZen(seiseki.shubetsu)

    # ３）－３ 特別競走本題回数
    # <tokusouhonsuu >第１５回</tokusouhonsuu >
    # 特別競走本題に回数がある場合は『第』『回』にはさむ形で編集する。
    params['tokusouhonsuu'] = '第' + intToZen(seiseki.tokusouhonsuu) + '回'

    # ３）－４ 特別競走名本題
    # <tokusoumeihon >マーチ賞</tokusoumeihon>
    # レース名称を編集する。
    params['tokusoumeihon'] = seiseki.tokusoumeihon

    # ３）－５ 特別競走名副題
    # <tokusoumeifuku>中央競馬交流</tokusoumeifuku>
    # 付加名称を編集する。
    params['tokusoumeifuku'] = seiseki.tokusoumeifuku

    # ３）－６ 副賞名
    # <ck_fukusyoumei>特別区競馬組合議会議長賞</ck_fukusyoumei>
    # 副賞名を編集する。 ※複数ある場合は繰り返して編集
    ck_fukusyoumei_list = makelist(seiseki.ck_fukusyoumei)
    params['ck_fukusyoumei_list'] = ck_fukusyoumei_list

    # ３）－７ グレード区分
    # <guredo>Ｇ３</guredo>
    # グレード区分を編集する。
    params['guredo'] = intToZen(seiseki.guredo)

    # ３）－８ 中央交流区分
    # <ck_chuokouryu>指定交流</ck_chuokouryu>
    # 中央交流区分を編集する。
    params['ck_chuokouryu'] = seiseki.ck_chuokouryu

    # ３）－９ 競走距離
    # <kyori>１２００</kyori>
    # 競走距離を編集する。
    params['kyori'] = intToZen(seiseki.kyori)

    # ３）－10 トラック
    # <torakku>ダート右・外コース</torakku>
    # 芝・ダート区分、周り、コース区分を『ダート右・外コース』のように編集する。回り
    # やコース区分がない場合などは省略し『ダート左』などになる。
    torakku = str(seiseki.ck_shibadat) + str(seiseki.ck_mawari)
    if seiseki.ck_naigai:
        torakku = torakku + '・' + str(seiseki.ck_naigai)
    params['torakku'] = torakku

    # ３）－11 ナイター区分
    # <ck_naita>ナイター</ck_naita>
    # ナイターの場合のみ編集する。
    params['ck_naita'] = seiseki.ck_kknaita

    # ３）－12 本賞金
    # <ck_shokin ck_chaku=”１着”>３００００００</ck_shokin>
    # ～
    # <ck_shokin ck_chaku=”５着”>２４００００</ck_shokin>
    # レースの着別の本賞金を属性値ck_chaku で区別し、ＭＡＸ５着までの内容を繰り返し
    # て編集する。
    params['ck_shokin1'] = intToZen(seiseki.ck_shokin1)
    params['ck_shokin2'] = intToZen(seiseki.ck_shokin2)
    params['ck_shokin3'] = intToZen(seiseki.ck_shokin3)
    params['ck_shokin4'] = intToZen(seiseki.ck_shokin4)
    params['ck_shokin5'] = intToZen(seiseki.ck_shokin5)

    # ３）－13 出走頭数
    # <shusuu>１４</shusuu>
    # 出走頭数を編集する。
    params['shusuu'] = intToZen(seiseki.shusuu)

    # ３）－14 競走条件
    # <jyoukenjouhou1>オープン</jyoukenjouhou1>
    # オープンや未勝利などを編集する。
    # <jyoukenjouhou>
    # <bareijouken>４歳上</bareijouken>
    # レースの馬齢条件を編集する。
    # <jouken/>
    # 競走条件。常に空タグを設定（中央競馬で必須タグなため）。
    # <ck_shikaku>選定馬</ck_shikaku>
    # 競走資格を編集する。 ※複数ある場合は繰り返して編集
    # <ck_rkaku>Ａ３</ck_rkaku>
    # レース格を編集する。 ※複数ある場合は繰り返して編集
    # <ck_rkumi>ロ</ck_rkumi>
    # レース組を編集する。 ※複数ある場合は繰り返して編集
    # </jyoukenjouhou>
    params['jyoukenjouhou1'] = intToZen(seiseki.jyoukenjouhou1)

    params['bareijouken'] = Mst_Breed_age.getBareiJouken(seiseki.shubetsu)

    params['ck_shikaku_list'] = makelist(seiseki.ck_shikaku)
    params['ck_rkaku_list'] = makelist(seiseki.ck_rkaku)
    params['ck_rkumi_list'] = makelist(seiseki.ck_rkumi)

    # ３）－15 重量種別
    # <juuryoushubetsu>別定</juuryoushubetsu>
    # 重量種別を編集する。
    params['juuryoushubetsu'] = seiseki.jyuuryoushubetsu

    # ３）－16 レース結果
    # <rekekka>レース成立</rekekka>
    # レース結果（レース成立・レース中止）を編集する。
    params['rekekka'] = seiseki.rekekka


    # ４）成績・着情報 <seisekijouhou><chakujunjouhou> … </chakujunjouhou>で囲み編集

    # ○○○○○○○○○馬別成績情報取得○○○○○○○○○
    # レース別成績オブジェクトから馬別成績オブジェクトのリストを取得。無かったら404
    seiseiki_umabetsu_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_seiseki.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_umabetsu_params = {}  # 馬ごとの成績のパラメータ
    seiseiki_umabetsu_params_list = []  # ↑の馬ごとの成績のパラメータをまとめたリスト

    for seiseiki_umabetsu in seiseiki_umabetsu_list:
        # ４）－１ 順位
        # <juni > １ < /juni >
        # 確定順位を編集。
        seiseiki_umabetsu_params['juni'] = intToZen(seiseiki_umabetsu.juni)

        # ４）－２ 入線順位
        # <nyuusenjuni > １ < /nyuusenjuni >
        # ゴールした順位を編集。
        seiseiki_umabetsu_params['nyuusenjuni'] = intToZen(seiseiki_umabetsu.nyuusenjuni)

        # ４）－３ 枠番
        # <waku>３</waku>
        # 枠番を編集する。
        seiseiki_umabetsu_params['waku'] = intToZen(seiseiki_umabetsu.waku)

        # ４）－４ 馬番
        # <uma>３</uma>
        # 馬番を編集する。
        seiseiki_umabetsu_params['uma'] = intToZen(seiseiki_umabetsu.uma)
        
        # ４）－５ 帽子色
        # <ck_boiro>赤</ck_boiro>
        # 帽子の色を編集する。 （白、黒、赤、青、黄、緑、橙、桃、紫など）
        seiseiki_umabetsu_params['ck_boiro'] = seiseiki_umabetsu.ck_boiro

        # ４）－６ 馬名
        # <bamei hyouki = "9字" > ドンバニヤン < /bamei >
        # <bamei hyouki = "正式名" > ドンバニヤン < /bamei >
        # 馬名の9字と正式名を編集。属性値hyoukiの内容で区別する。
        seiseiki_umabetsu_params['bamei_seishiki'] = seiseiki_umabetsu.bamei
        seiseiki_umabetsu_params['bamei_9char'] = bamei9char(seiseiki_umabetsu.bamei)
        
        # ４）－７ 馬の所属
        # <ck_umasyozoku hyouki="１字">大</ck_seisansya>
        # <ck_umasyozoku hyouki="正式名">大井</ck_seisansya>
        # 馬が所属する場を１字略と正式名を属性値hyouki で区別し編集する。
        seiseiki_umabetsu_params['ck_umasyozoku'] = seiseiki_umabetsu.ck_umasyozoku
        seiseiki_umabetsu_params['ck_umasyozoku_1char'] = Mst_Belonging.getBelonging_1char(seiseiki_umabetsu.ck_umasyozoku)

        # ４）－８ 馬の性別
        # <seibetsu>牝</seibetsu>
        # 馬の性別を編集する。
        seiseiki_umabetsu_params['seibetsu'] = seiseiki_umabetsu.seibetsu

        # ４）－９ 馬齢
        # <barei>４</barei>
        # 馬齢を編集する。
        seiseiki_umabetsu_params['barei'] = intToZen(seiseiki_umabetsu.barei)

        # ４）－10 負担重量
        # <fujuu > ５６ < /fujuu >
        # 負担重量を編集。ばんえい競馬は編集しないため空タグ。
        seiseiki_umabetsu_params['fujuu'] = intToZen(seiseiki_umabetsu.fujuu)

        # ４）－11 積載重量（ばんえい競馬のみ）
        # <ck_sekijuu > ７５０ < /ck_sekijuu >
        # 積載重量を編集。ばんえい競馬のみ編集。
        seiseiki_umabetsu_params['ck_sekijuu'] = intToZen(seiseiki_umabetsu.ck_sekijuu)

        # ４）－12 騎手名
        # <kimei hyouki = "3字" > 的場文 < /kimei >
        # <kimei hyouki = "姓" > 的場 < /kimei >
        # <kimei hyouki = "名" > 文男 < /kimei >
        # 騎手名の3字、姓、名を編集。属性値hyoukiの内容で区別する。
        # 外国人騎手など姓と名の分割が難しいケースについては、姓に名前を編集し、名については編集しない。
        seiseiki_umabetsu_params['kimei'] = seiseiki_umabetsu.kimei
        seiseiki_umabetsu_params['kimei_sei'] = seiseiki_umabetsu.kimei_sei
        seiseiki_umabetsu_params['kimei_mei'] = seiseiki_umabetsu.kimei_mei

        # ４）－13 騎手コード
        # <kiko/>
        # 常に空タグを編集する。

        # ４）－14 騎手免許番号
        # <ck_kimnbangou > ３０１３３ < /ck_kimnbangou >
        # 騎手免許番号を編集する。
        seiseiki_umabetsu_params['ck_kimnbangou'] = intToZen(seiseiki_umabetsu.ck_kimnbangou)

        # ４）－15 見習区分
        # <mikubun > １ < /mikubun >
        # 減量騎手が騎乗した場合の減量重量を編集。
        seiseiki_umabetsu_params['mikubun'] = intToZen(seiseiki_umabetsu.mikubun)

        # ４）－16 変更前騎手（騎手変更があった場合のみ編集）
        # <ck_maekimei hyouki = "3字" > 張田京 < /ck_maekimei >
        # <ck_maekimei hyouki = "姓" > 張田 < /ck_maekimei >
        # <ck_maekimei hyouki = "名" > 京 < /ck_maekimei >
        # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手名の3字、姓、名を編集。属性値hyoukiの内容で区別する。
        seiseiki_umabetsu_params['ck_maekimei'] = seiseiki_umabetsu.ck_maekimei
        seiseiki_umabetsu_params['ck_maekimei_sei'] = seiseiki_umabetsu.ck_maekimei_sei
        seiseiki_umabetsu_params['ck_maekimei_mei'] = seiseiki_umabetsu.ck_maekimei_mei

        # ４）－17 変更前騎手免許番号（騎手変更があった場合のみ編集）
        # <ck_maekimnbangou > ３００５９ < /ck_maekimnbangou >
        # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手の免許番号を編集する。
        seiseiki_umabetsu_params['ck_maekimnbangou'] = intToZen(seiseiki_umabetsu.ck_maekimnbangou)

        # ４）―18 変更前騎手見習区分（騎手変更があった場合のみ編集）
        # <ck_maemikubun > １ < /ck_maemikubun >
        # 騎手変更があった場合に編集される。騎手変更前の騎乗予定だった騎手が減量騎手の場合に減量重量を編集。
        seiseiki_umabetsu_params['ck_maemikubun'] = intToZen(seiseiki_umabetsu.ck_maemikubun)

        # ４）－19 騎手変更理由（騎手変更があった場合のみ編集）
        # <ck_henriyuu > 事故 < /ck_henriyuu >
        # 騎手変更があった場合に編集される。騎手変更理由を編集。
        seiseiki_umabetsu_params['ck_henriyuu'] = seiseiki_umabetsu.ck_henriyuu

        # ４）－20 タイム
        # <ta >
        # <fun > １ < /fun >
        # <byo > ４８ < /byo >
        # <miri > ５ < /miri >
        # </ta >
        # 入着タイムを編集。タイムを分、秒、ミリ秒で編集する。
        seiseiki_umabetsu_params['fun'] = intToZen(seiseiki_umabetsu.fun)
        seiseiki_umabetsu_params['byo'] = intToZen(seiseiki_umabetsu.byo)
        seiseiki_umabetsu_params['miri'] = intToZen(seiseiki_umabetsu.miri)

        # ４）－21 レコードタイム
        # <reko > レコード < /reko >
        # レコードが発生した場合に編集。
        seiseiki_umabetsu_params['reko'] = seiseiki_umabetsu.reko

        # ４）－22 着差情報 < sajouhou >・・・</sajouhou > で囲まれる。
        # 着差の対象となる馬が降着した場合は < sajouhou > を繰り返して編集。
        # <sa hyouki = "通常" > １馬身１／４ < /sa >
        salist = []
        for sa in seiseiki_umabetsu.sa.all():
            salist.append(sa)
        seiseiki_umabetsu_params['salist'] = salist

        # 着差例外
        # <sareigai > 降着 < /sareigai >
        # 降着となった当該馬には降着後の着順が編集され、降着となったことを示す着差
        # 例外<sareigai>タグが発生し、内容として“降着”を編集する
        seiseiki_umabetsu_params['sareigai'] = seiseiki_umabetsu.sareigai

        # ４）－23 事故情報
        # 事故種類
        # <ck_jikosyu > 降着 < /ck_jikosyu >
        # 降着の場合など「降着」と編集。
        seiseiki_umabetsu_params['ck_jikosyu'] = seiseiki_umabetsu.ck_jikosyu

        # 事故理由
        # <ck_jikoriyuu > 進路妨害 < /ck_jikoriyuu >
        # 事故種類に対応した事故理由を編集。
        seiseiki_umabetsu_params['ck_jikoriyuu'] = seiseiki_umabetsu.ck_jikoriyuu

        # ４）－24 馬体重
        # <bajuu>４７０</bajuu>
        # 馬体重を編集する。
        seiseiki_umabetsu_params['bajuu'] = intToZen(seiseiki_umabetsu.bajuu)

        # ４）－25 馬体重増減
        # <bajuuzougen>＋４</bajuuzougen>
        # 馬体重が増加の場合は『＋』、減少は『－』付きで編集する。
        seiseiki_umabetsu_params['bajuuzougen'] = intToZen(seiseiki_umabetsu.bajuuzougen) # これintでいいのか？

        # ４）－26 単勝人気
        # <tannin>１</tannin>
        # 単勝の人気を編集する。
        seiseiki_umabetsu_params['tannin'] = intToZen(seiseiki_umabetsu.tannin)

        # ４）－27 調教師名
        # <choumei hyouki="3 字">佐々仁</choumei>
        # <choumei hyouki="姓">佐々木</choumei>
        # <choumei hyouki="名">仁</choumei>
        # 調教師の３字略、姓、名を属性値hyouki で区別し編集する。
        seiseiki_umabetsu_params['choumei'] = seiseiki_umabetsu.choumei
        seiseiki_umabetsu_params['choumei_sei'] = seiseiki_umabetsu.choumei_sei
        seiseiki_umabetsu_params['choumei_mei'] = seiseiki_umabetsu.choumei_mei

        # ４）－28 異常区分内容
        # <ikubunnai>失格</ikubunnai>
        # 異常区分を編集する。
        # ※順位タグは編集しない
        # ※異常区分としては、「出走取消」「出走除外」「競走除外」「競走中止」「失格」
        # 「落馬」など。
        seiseiki_umabetsu_params['ikubunnai'] = seiseiki_umabetsu.ikubunnai

        seiseiki_umabetsu_params_list.append(seiseiki_umabetsu_params.copy())

    params['seiseiki_umabetsu_params_list'] = seiseiki_umabetsu_params_list

    # ５）成績・払戻情報 <harajouhou> … </harajouhou></seisekijouhou>
    # ５）－１ 払戻情報
    # <harajouhou> … </harajouhou>
    # <harajouhou>タグ内に払い戻しの情報「５）－２、５－３）」を編集する。
    # ※レース中止の場合は編集しない

    # ５）－２ 券種
    # <tanharajouhou> … </tanharajouhou>
    # <.fukuharajouhou> … </fukuharajouhou>
    # <wakupukuharajouhou> … </wakupukuharajouho>
    # <ck_wakutanharajouhou> … </ck_wakutanharajouhou>
    # <umapukuharajouhou> … </umapukuharajouhou>
    # <umatanharajouhou> … </umatanharajouhou>
    # <sanpukuharajouhou> … </sanpukuharajouhou>
    # <santanharajouhou> … </santanharajouho>
    # <waharajouhou> … </ waharajouhou >
    # 単勝、複勝、枠複、枠単、馬複、馬単、三連複、三連単、ワイドの順で編集し、ただし
    # 発売のない券種については編集はしない。
    # ※各券種内の構成は同一構成のため、５）－３にて単勝で説明する。

    # ５）－３ 払戻状況
    # <tanharajouhou>
    # <tankumijouhou>
    # <tankumi>
    # <tansaki>３</tansaki>
    # １着馬の馬番号を編集する。
    # </tankumi>
    # <tanharakin>１５０</tanharakin>
    # 払戻金額を編集する。
    # <tantounin>１</tantounin>
    # 投票人気を編集する。
    # </tankumijouhou>
    # </tanharajouhou>

    # ○○○○○○○○○単勝払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから単勝払戻オブジェクトのリストを取得。無かったら404
    seiseiki_tan_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_tan.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_tan_params = {}  # 単勝1組分のパラメータ
    seiseiki_tan_params_list = []  # ↑の単勝1組分ごとのパラメータをまとめたリスト

    # ４）－１－１ 単勝払戻状況
    # <tanharajyoukyou > 特払い < /tanharajyoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['tanharajyoukyou'] = seiseki.tanharajyoukyou

    # ４）－１－２ 単勝組番情報 < tankumijouhou >・・・</tankumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_tan in seiseiki_tan_list:
        # ４）－１－２－１ 単勝組番状況
        # <tankumijoukyou > 無投票 < /tankumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_tan_params['tankumijoukyou'] = seiseiki_tan.tankumijoukyou

        # ４）－１－２－２ 単勝組番
        # <tankumi >
        # <tansaki > ４ < /tansaki >
        # </tankumi >
        # 単勝馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_tan_params['tansaki'] = intToZen(seiseiki_tan.tansaki)

        # ４）－１－２－３ 単勝払戻金
        # <tanharakin > １０９０ < /tanharakin >
        # 単勝払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_tan_params['tanharakin'] = intToZen(seiseiki_tan.tanharakin)

        # ４）－１－２－４ 単勝投票人気
        # <tantounin > ９ < /tantounin >
        # 人気を編集する。
        seiseiki_tan_params['tantounin'] = intToZen(seiseiki_tan.tantounin)

        seiseiki_tan_params_list.append(seiseiki_tan_params.copy())

    params['seiseiki_tan_params_list'] = seiseiki_tan_params_list
    
    # ４）－２ 複勝払戻情報 < fukuharajouhou >・・・</fukuharajouhou > で囲まれて編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○複勝払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから複勝払戻オブジェクトのリストを取得。無かったら404
    seiseiki_fuku_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_fuku.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_fuku_params = {}  # 複勝1組分のパラメータ
    seiseiki_fuku_params_list = []  # ↑の複勝1組分ごとのパラメータをまとめたリスト

    # ４）－２－１ 複勝払戻状況
    # <fukuharajoukyou > 特払い < /fukuharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['fukuharajoukyou'] = seiseki.fukuharajoukyou

    # ４）－２－２ 複勝組番情報 < fukukumijouhou >・・・</fukukumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_fuku in seiseiki_fuku_list:
        # ４）－２－２－１ 複勝組番状況
        # <fukukumijoukyou > 無投票 < /fukukumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_fuku_params['fukukumijoukyou'] = seiseiki_fuku.fukukumijoukyou

        # ４）－２－２－２ 複勝組番
        # <fukukumi >
        # <fukusaki > ４ < /fukusaki >
        # </fukukumi >
        # 複勝馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_fuku_params['fukusaki'] = intToZen(seiseiki_fuku.fukusaki)

        # ４）－２－２－３ 複勝払戻金
        # <fukuharakin > １０９０ < /fukuharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_fuku_params['fukuharakin'] = intToZen(seiseiki_fuku.fukuharakin)

        # ４）－２－２－４ 複勝投票人気
        # <ck_fukutounin > ９ < /ck_fukutounin >
        # 人気を編集する。
        seiseiki_fuku_params['ck_fukutounin'] = intToZen(seiseiki_fuku.ck_fukutounin)

        seiseiki_fuku_params_list.append(seiseiki_fuku_params.copy())

    params['seiseiki_fuku_params_list'] = seiseiki_fuku_params_list


    # ４）－３ 枠連複払戻情報 < wakupukuharajouhou >・・・</wakupukuharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○枠連複払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから枠連複払戻オブジェクトのリストを取得。無かったら404
    seiseiki_wakupuku_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_wakupuku.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_wakupuku_params = {}  # 枠連複1組分のパラメータ
    seiseiki_wakupuku_params_list = []  # ↑の枠連複1組分ごとのパラメータをまとめたリスト

    # ４）－３－１ 枠連複払戻状況
    # <wakupukuharajoukyou > 特払い < /wakupukuharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['wakupukuharajoukyou'] = seiseki.wakupukuharajoukyou

    # ４）－３－２ 枠連複組番情報 < wakupukukumijouhou >・・・</wakupukukumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_wakupuku in seiseiki_wakupuku_list:
        # ４）－３－２－１ 枠連複組番状況
        # <wakupukukumijoukyou > 無投票 < /wakupukukumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_wakupuku_params['wakupukukumijoukyou'] = seiseiki_wakupuku.wakupukukumijoukyou

        # ４）－３－２－２ 枠連複組番
        # <wakupukukumi >
        # <wakupukusaki > ３ < /wakupukusaki >
        # <wakupukuato > ８ < /wakupukuato >
        # </wakupukukumi >
        # 枠番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_wakupuku_params['wakupukusaki'] = intToZen(seiseiki_wakupuku.wakupukusaki)
        seiseiki_wakupuku_params['wakupukuato'] = intToZen(seiseiki_wakupuku.wakupukuato)

        # ４）－３－２－３ 枠連複払戻金
        # <wakupukuharakin > ９８０ < /wakupukuharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_wakupuku_params['wakupukuharakin'] = intToZen(seiseiki_wakupuku.wakupukuharakin)

        # ４）－３－２－４ 枠連複投票人気
        # <wakupukutounin > ４ < /wakupukutounin >
        # 人気を編集する。
        seiseiki_wakupuku_params['wakupukutounin'] = intToZen(seiseiki_wakupuku.wakupukutounin)

        seiseiki_wakupuku_params_list.append(seiseiki_wakupuku_params.copy())

    params['seiseiki_wakupuku_params_list'] = seiseiki_wakupuku_params_list


    # ４）－４ 枠連単払戻情報 < ck_wakutanharajouhou >・・・</ck_wakutanharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○枠連単払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから枠連単払戻オブジェクトのリストを取得。無かったら404
    seiseiki_wakutan_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_wakutan.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_wakutan_params = {}  # 枠連単1組分のパラメータ
    seiseiki_wakutan_params_list = []  # ↑の枠連単1組分ごとのパラメータをまとめたリスト

    # ４）－４－１ 枠連単払戻状況
    # <ck_wakutanharajoukyou > 特払い < /ck_wakutanharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['ck_wakutanharajoukyou'] = seiseki.ck_wakutanharajoukyou

    # ４）－４－２ 枠連単組番情報 < ck_wakutankumijouhou >・・・</ck_wakutankumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_wakutan in seiseiki_wakutan_list:
        # ４）－４－２－１ 枠連単組番状況
        # <ck_wakutankumijoukyou > 無投票 < /ck_wakutankumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_wakutan_params['ck_wakutankumijoukyou'] = seiseiki_wakutan.ck_wakutankumijoukyou

        # ４）－４－２－２ 枠連単組番
        # <ck_wakutankumi >
        # <ck_wakutansaki > ３ < /ck_wakutansaki >
        # <ck_wakutanato > ８ < /ck_wakutanato >
        # </ck_wakutankumi >
        # 枠番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_wakutan_params['ck_wakutansaki'] = intToZen(seiseiki_wakutan.ck_wakutansaki)
        seiseiki_wakutan_params['ck_wakutanato'] = intToZen(seiseiki_wakutan.ck_wakutanato)

        # ４）－４－２－３ 枠連単払戻金
        # <ck_wakutanharakin > ９８０ < /ck_wakutanharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_wakutan_params['ck_wakutanharakin'] = intToZen(seiseiki_wakutan.ck_wakutanharakin)

        # ４）－４－２－４ 枠連単投票人気
        # <ck_wakutantounin > ４ < /ck_wakutantounin >
        # 人気を編集する。
        seiseiki_wakutan_params['ck_wakutantounin'] = intToZen(seiseiki_wakutan.ck_wakutantounin)

        seiseiki_wakutan_params_list.append(seiseiki_wakutan_params.copy())

    params['seiseiki_wakutan_params_list'] = seiseiki_wakutan_params_list
    

    # ４）－５ 馬連複払戻情報 < umapukuharajouhou >・・・</umapukuharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○馬連複払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから馬連複払戻オブジェクトのリストを取得。無かったら404
    seiseiki_umapuku_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_umapuku.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_umapuku_params = {}  # 馬連複1組分のパラメータ
    seiseiki_umapuku_params_list = []  # ↑の馬連複1組分ごとのパラメータをまとめたリスト

    # ４）－５－１ 馬連複払戻状況
    # <umapukuharajoukyou > 特払い < /umapukuharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['umapukuharajoukyou'] = seiseki.umapukuharajoukyou

    # ４）－５－２ 馬連複組番情報 < umapukukumijouhou >・・・</umapukukumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_umapuku in seiseiki_umapuku_list:
        # ４）－５－２－１ 馬連複組番状況
        # <umapukukumijoukyou > 無投票 < /umapukukumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_umapuku_params['umapukukumijoukyou'] = seiseiki_umapuku.umapukukumijoukyou

        # ４）－５－２－２ 馬連複組番
        # <umapukukumi >
        # <umapukusaki > ４ < /umapukusaki >
        # <umapukuato > １４ < /umapukuato >
        # </umapukukumi >
        # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_umapuku_params['umapukusaki'] = intToZen(seiseiki_umapuku.umapukusaki)
        seiseiki_umapuku_params['umapukuato'] = intToZen(seiseiki_umapuku.umapukuato)

        # ４）－５－２－３ 馬連複払戻金
        # <umapukuharakin > ３０４ < /umapukuharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_umapuku_params['umapukuharakin'] = intToZen(seiseiki_umapuku.umapukuharakin)

        # ４）－５－２－４ 馬連複投票人気
        # <umapukutounin > １０ < /umapukutounin >
        # 人気を編集する。
        seiseiki_umapuku_params['umapukutounin'] = intToZen(seiseiki_umapuku.umapukutounin)

        seiseiki_umapuku_params_list.append(seiseiki_umapuku_params.copy())

    params['seiseiki_umapuku_params_list'] = seiseiki_umapuku_params_list

    # ４）－６ 馬連単払戻情報 < umatanharajouhou >・・・</umatanharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○馬連単払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから馬連単払戻オブジェクトのリストを取得。無かったら404
    seiseiki_umatan_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_umatan.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_umatan_params = {}  # 馬連単1組分のパラメータ
    seiseiki_umatan_params_list = []  # ↑の馬連単1組分ごとのパラメータをまとめたリスト

    # ４）－６－１ 馬連単払戻状況
    # <umatanharajoukyou > 特払い < /umatanharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['umatanharajoukyou'] = seiseki.umatanharajoukyou

    # ４）－６－２ 馬連単組番情報 < umatankumijouhou >・・・</umatankumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_umatan in seiseiki_umatan_list:
        # ４）－６－２－１ 馬連単組番状況
        # <umatankumijoukyou > 無投票 < /umatankumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_umatan_params['umatankumijoukyou'] = seiseiki_umatan.umatankumijoukyou

        # ４）－６－２－２ 馬連単組番
        # <umatankumi >
        # <umatansaki > ４ < /umatansaki >
        # <umatanato > １４ < /umatanato >
        # </umatankumi >
        # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_umatan_params['umatansaki'] = intToZen(seiseiki_umatan.umatansaki)
        seiseiki_umatan_params['umatanato'] = intToZen(seiseiki_umatan.umatanato)

        # ４）－６－２－３ 馬連単払戻金
        # <umatanharakin > ３０４ < /umatanharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_umatan_params['umatanharakin'] = intToZen(seiseiki_umatan.umatanharakin)

        # ４）－６－２－４ 馬連単投票人気
        # <umatantounin > １０ < /umatantounin >
        # 人気を編集する。
        seiseiki_umatan_params['umatantounin'] = intToZen(seiseiki_umatan.umatantounin)

        seiseiki_umatan_params_list.append(seiseiki_umatan_params.copy())

    params['seiseiki_umatan_params_list'] = seiseiki_umatan_params_list

    # ４）－７ 三連複払戻情報 < sanpukuharajouhou >・・・</sanpukuharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○三連複払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから三連複払戻オブジェクトのリストを取得。無かったら404
    seiseiki_sanpuku_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_sanpuku.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_sanpuku_params = {}  # 三連複1組分のパラメータ
    seiseiki_sanpuku_params_list = []  # ↑の三連複1組分ごとのパラメータをまとめたリスト

    # ４）－７－１ 三連複払戻状況
    # <sanpukuharajoukyou > 特払い < /sanpukuharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['sanpukuharajoukyou'] = seiseki.sanpukuharajoukyou

    # ４）－７－２ 三連複組番情報 < sanpukukumijouhou >・・・</sanpukukumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_sanpuku in seiseiki_sanpuku_list:
        # ４）－７－２－１ 三連複組番状況
        # <sanpukukumijoukyou > 無投票 < /sanpukukumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_sanpuku_params['sanpukukumijoukyou'] = seiseiki_sanpuku.sanpukukumijoukyou

        # ４）－７－２－２ 三連複組番
        # <sanpukukumi >
        # <sanpukusaki > ４ < /sanpukusaki >
        # <sanpukunaka > １３ < /sanpukunaka >
        # <sanpukuato > １４ < /sanpukuato >
        # </sanpukukumi >
        # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_sanpuku_params['sanpukusaki'] = intToZen(seiseiki_sanpuku.sanpukusaki)
        seiseiki_sanpuku_params['sanpukunaka'] = intToZen(seiseiki_sanpuku.sanpukunaka)
        seiseiki_sanpuku_params['sanpukuato'] = intToZen(seiseiki_sanpuku.sanpukuato)

        # ４）－７－２－３ 三連複払戻金
        # <sanpukuharakin > １２３０ < /sanpukuharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_sanpuku_params['sanpukuharakin'] = intToZen(seiseiki_sanpuku.sanpukuharakin)

        # ４）－７－２－４ 三連複投票人気
        # <sanpukutounin > ５ < /sanpukutounin >
        # 人気を編集する。
        seiseiki_sanpuku_params['sanpukutounin'] = intToZen(seiseiki_sanpuku.sanpukutounin)

        seiseiki_sanpuku_params_list.append(seiseiki_sanpuku_params.copy())

    params['seiseiki_sanpuku_params_list'] = seiseiki_sanpuku_params_list

    # ４）－８ 三連単払戻情報 < santanharajouhou >・・・</santanharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。

    # ○○○○○○○○○三連単払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトから三連単払戻オブジェクトのリストを取得。無かったら404
    seiseiki_santan_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_santan.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_santan_params = {}  # 三連単1組分のパラメータ
    seiseiki_santan_params_list = []  # ↑の三連単1組分ごとのパラメータをまとめたリスト

    # ４）－８－１ 三連単払戻状況
    # <santanharajoukyou > 特払い < /santanharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['santanharajoukyou'] = seiseki.santanharajoukyou

    # ４）－８－２ 三連単組番情報 < santankumijouhou >・・・</santankumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_santan in seiseiki_santan_list:
        # ４）－８－２－１ 三連単組番状況
        # <santankumijoukyou > 無投票 < /santankumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_santan_params['santankumijoukyou'] = seiseiki_santan.santankumijoukyou

        # ４）－８－２－２ 三連単組番
        # <santankumi >
        # <santansaki > ４ < /santansaki >
        # <santannaka > １４ < /santannaka >
        # <santanato > １３ < /santanato >
        # </santankumi >
        # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_santan_params['santansaki'] = intToZen(seiseiki_santan.santansaki)
        seiseiki_santan_params['santannaka'] = intToZen(seiseiki_santan.santannaka)
        seiseiki_santan_params['santanato'] = intToZen(seiseiki_santan.santanato)

        # ４）－８－２－３ 三連単払戻金
        # <santanharakin > １２３０ < /santanharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_santan_params['santanharakin'] = intToZen(seiseiki_santan.santanharakin)

        # ４）－８－２－４ 三連単投票人気
        # <santantounin > ５ < /santantounin >
        # 人気を編集する。
        seiseiki_santan_params['santantounin'] = intToZen(seiseiki_santan.santantounin)

        seiseiki_santan_params_list.append(seiseiki_santan_params.copy())

    params['seiseiki_santan_params_list'] = seiseiki_santan_params_list

    # ４）－９ ワイド払戻情報 < waharajouhou >・・・</waharajouhou > で囲み編集。
    # 式別発売がない場合は編集しない。
    
    # ○○○○○○○○○ワイド払戻情報取得○○○○○○○○○
    # レース別成績オブジェクトからワイド払戻オブジェクトのリストを取得。無かったら404
    seiseiki_wa_list = get_list_or_404(
        Md_Seiseki_Haraimodoshi_wa.objects, seiseki_haraimodoshi=seiseki)
    seiseiki_wa_params = {}  # ワイド1組分のパラメータ
    seiseiki_wa_params_list = []  # ↑のワイド1組分ごとのパラメータをまとめたリスト

    # ４）－９－１ ワイド払戻状況
    # <waharajoukyou > 特払い < /waharajoukyou >
    # 式別発売が不成立もしくは特払いになった場合は、「不成立」「特払い」と編集。
    params['waharajoukyou'] = seiseki.waharajoukyou

    # ４）－９－２ ワイド組番情報 < wakumijouhou >・・・</wakumijouhou > で囲み編集。
    # 払戻が複数ある場合は繰り返して編集。
    for seiseiki_wa in seiseiki_wa_list:
        # ４）－９－２－１ ワイド組番状況
        # <wakumijoukyou > 無投票 < /wakumijoukyou >
        # 式別発売が不成立もしくは特払い以外で該当組番の購入がない場合に編集。
        seiseiki_wa_params['wakumijoukyou'] = seiseiki_wa.wakumijoukyou

        # ４）－９－２－２ ワイド組番
        # <wakumi >
        # <wasaki > ４ < /wasaki >
        # <waato > １４ < /waato >
        # </wakumi >
        # 馬番を編集。式別発売が不成立もしくは特払いの場合は編集しない。
        seiseiki_wa_params['wasaki'] = intToZen(seiseiki_wa.wasaki)
        seiseiki_wa_params['waato'] = intToZen(seiseiki_wa.waato)

        # ４）－９－２－３ ワイド払戻金
        # <waharakin > ８６０ < /waharakin >
        # 払戻金を編集。特払いの場合「７０」、不成立の場合「１００」、無投票の場合は編集しない。
        seiseiki_wa_params['waharakin'] = intToZen(seiseiki_wa.waharakin)

        # ４）－９－２－４ ワイド投票人気
        # <watounin > ８ < /watounin >
        # 人気を編集する。
        seiseiki_wa_params['watounin'] = intToZen(seiseiki_wa.watounin)

        seiseiki_wa_params_list.append(seiseiki_wa_params.copy())

    params['seiseiki_wa_params_list'] = seiseiki_wa_params_list

    # xml形式で出力
    res = render(request, 'NewsML_temp/seiseki_C.xml', params)
    res['Content-Type'] = 'application/xml'
    return res

# ========================================================================















# ========================================================================

# 【ラップ】(InData内部)
def NewsML_rap(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # # 年月日と場とレース番号からコーナー・ラップオブジェクトのリストを取得。無かったら404
    corner_rap_list = get_list_or_404(Md_Corner_Rap.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi,
                                       rebangou=rebangou
                                       )

    # 場マスタから場のデータを取得
    jou_data = Mst_Jou.getJoudata(joucode)

    # レース情報を一件目のデータからとる。
    corner_rap = corner_rap_list[0]

    # コーナ通過順を編集する関数
    def edit_corner_juni(corner_juni):
        if corner_juni:  # (4,5)-2,9,7=(1,8),3=6
            corner_juni = corner_juni.replace("-(", "(-") # 整形する
            corner_juni = corner_juni.replace("=(", "(=") # 整形する (4,5)-2,9,7(=1,8),3=6
            corner_juni = corner_juni.replace(',', '') # 整形する (45)-297(=18)3=6

            shuudan_list = []
            iskakko = False
            before_cj = ""
            for cj in corner_juni: # [['４', '５'], ['-２'], ['９'], ['=１', '８'], ['３'], ['=６']]
                if cj == '(':
                    iskakko = True
                    if shuudan_list:
                        shuudan_list[-1] = []
                    else:
                        shuudan_list.append([])
                elif  cj == ')' and iskakko:
                    iskakko = False
                elif  cj == '-' or cj == '=':
                    before_cj = cj
                else:
                    if iskakko: #括弧()内の時
                        shuudan_list[-1].append(intToZen(before_cj + cj))
                        before_cj = ""
                    else:
                        shuudan_list.append([intToZen(before_cj + cj)])
                        before_cj = ""
            return shuudan_list
        else:
            return

    # コーナー順位情報をリストに格納する
    corner_list = []
    for i in range(8):
        j = i + 1
        corner_mei = 'corner_mei' + str(j)
        corner_juni = 'corner_juni' + str(j)
        
        if getattr(corner_rap, corner_mei):
            corner_list.append([])
            corner_list[i].append(intToZen(getattr(corner_rap, corner_mei)))
            corner_list[i].append(edit_corner_juni(getattr(corner_rap, corner_juni)))
    

    # パラメータに追加(数値の項目は全角化する)
    params = {
        'joumei_seishiki': jou_data[0],
        'joumei_3': jou_data[1],
        'kaisuu': intToZen(corner_rap.kaisuu) + '回',
        'kainichime': intToZen(corner_rap.kainichime) + '日目',
        'ck_kyounen': intToZen(corner_rap.ck_kyounen),
        'ck_kyoutuki': intToZen(corner_rap.ck_kyoutuki),
        'ck_kyouhi': intToZen(corner_rap.ck_kyouhi),
        'rebangou': intToZen(corner_rap.rebangou) + 'Ｒ',
        'chaku1uma_1': intToZen(corner_rap.chaku1uma_1),
        'chaku1uma_2': intToZen(corner_rap.chaku1uma_2),
        'chaku1uma_3': intToZen(corner_rap.chaku1uma_3),
        'a4ha': intToZen(corner_rap.a4ha),
        'a3ha': intToZen(corner_rap.a3ha),
        'ta_list': makelist(corner_rap.ta_list),
        'corner_list': corner_list
    }

    # xml形式で出力
    res = render(request, 'NewsML_temp/corner_rap.xml', params)
    res['Content-Type'] = 'application/xml'
    return res

    # return render(request, 'NewsML_temp/NewsML.html', {'title': '【ラップ】NewsMLプレビュー画面作成中(4/30)'})
# ========================================================================















# ========================================================================
# 【上がり】(InData内部)
def NewsML_agari(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # # 年月日と場とレース番号から通信文オブジェクトのリストを取得。無かったら404
    # tsuushimbun_list = get_list_or_404(Md_Tsuushimbun.objects,
    #                                    joumei=joucode,
    #                                    ck_kyounen=kyounen,
    #                                    ck_kyoutuki=kyoutuki,
    #                                    ck_kyouhi=kyouhi,
    #                                    rebangou=rebangou
    #                                    )

    # # 場マスタから場のデータを取得
    # jou_data = Mst_Jou.getJoudata(joucode)

    # # 数値の全角化処理(馬番)
    # for tb in tsuushimbun_list:
    #     tb.uma = intToZen(tb.uma)

    # # レース情報を一件目のデータからとる。
    # tsuushinbun = tsuushimbun_list[0]

    # # パラメータに追加(数値の項目は全角化する)
    # params = {
    #     'joumei_seishiki': jou_data[0],
    #     'joumei_3': jou_data[1],

    #     'kaisuu': intToZen(tsuushinbun.kaisuu),
    #     'kainichime': intToZen(tsuushinbun.kainichime),

    #     'ck_kyounen': intToZen(tsuushinbun.ck_kyounen),
    #     'ck_kyoutuki': intToZen(tsuushinbun.ck_kyoutuki),
    #     'ck_kyouhi': intToZen(tsuushinbun.ck_kyouhi),
    #     'rebangou': intToZen(tsuushinbun.rebangou),

    #     'tsuushimbun_list': tsuushimbun_list
    # }

    # # xml形式で出力
    # res = render(request, 'NewsML_temp/tsuushimbun_C.xml', params)
    # res['Content-Type'] = 'application/xml'
    # return res

    return render(request, 'NewsML_temp/NewsML.html', {'title': '【上がり】NewsMLプレビュー画面作成中(4/30)'})
# ========================================================================
















# ========================================================================
# 【出走表】(InData内部)
def NewsML_shussouhyou(request, kyounen, kyoutuki, kyouhi, joucode, rebangou):

    # 年月日と場とレース番号から出走表オブジェクトのリストを取得。無かったら404
    shussouhyou_list = get_list_or_404(Md_Shussouhyou.objects,
                                       joumei=joucode,
                                       ck_kyounen=kyounen,
                                       ck_kyoutuki=kyoutuki,
                                       ck_kyouhi=kyouhi,
                                       rebangou=rebangou
                                       )

    # ○○○○○○○○○レース情報取得○○○○○○○○○
    # レース情報を一件目のデータからとる。
    shussouhyou = shussouhyou_list[0]

    params = {}
# 以下、NewsML接続仕様書より

# １）開催関連情報
# １）－１ 開催場名（3 字、正式名）
# <joumei hyouki="3 字">大井 </joumei>
# <joumei hyouki="正式名">大井競馬</joumei>
#  開催競馬場名を 3 字と正式名を編集。属性値 hyouki の内容で区別する。

    # 場マスタから場正式名と場３文字名を取得
    jou_data = Mst_Jou.getJoudata(joucode)
    params['joumei_seishiki'] = jou_data[0]
    params['joumei_3'] = jou_data[1]

# １）－２ 開催回数
# <kaisuu>１５回</kaisuu>
#  開催回数を編集。『回』付きで編集する。
    params['kaisuu'] = intToZen(shussouhyou.kaisuu) + '回'

# １）－３ 開催日目
# <kainichime>１日目</kainichime>
#  開催日目を編集。『日目』付きで編集する。
    params['kainichime'] = intToZen(shussouhyou.kainichime) + '日目'

# １）－４ 競走年月日
# <ck_kyounichi>
#    <ck_kyounen>２００４</ck_kyounen>
#    <ck_kyoutuki>１０</ck_kyoutuki>
#    <ck_kyouhi>１４</ck_kyouhi>
# < /ck_kyounichi>
#  競走年月日を編集する。年・月・日別にそれぞれ編集。
    params['ck_kyounen'] = intToZen(shussouhyou.ck_kyounen)
    params['ck_kyoutuki'] = intToZen(shussouhyou.ck_kyoutuki)
    params['ck_kyouhi'] = intToZen(shussouhyou.ck_kyouhi)

# １）－５ 出馬区分
#  <shutsubakubun>翌日</shutubakubun>
#  通常は前日に出走表を送信するため『翌日』と編集する。
#  もし翌日以降の出走表を編集する場合は、競走がおこなわれる日付を『２００４１０１４』などのように編集。
    # ★→開催日割から値を編集する。とりあえず翌日を設定しておく。
    params['shutsubakubun'] = '翌日'

# ２）レース情報
# ２）－１ レース番号
# <rebangou>４Ｒ</rebangou>
#  レース番号を編集。『Ｒ』付きで編集する。
    params['rebangou'] = intToZen(shussouhyou.rebangou) + 'Ｒ'

# ２）－２ 競走種別
# <shubetsu>サラ３歳上</shubetsu>
#  競走種別を編集。馬齢部分は洋数字で編集。
    shubetsu = shussouhyou.shubetsu  # 後で馬齢条件を算出するのに使うので変数化しておく
    params['shubetsu'] = intToZen(shubetsu)

# ２）－３ 特別競走本題回数
# <tokusouhonsuu >第１５回</tokusouhonsuu >
#  特別競走本題に回数がある場合は回数を編集。『第』『回』ではさむ形で編集。
    if shussouhyou.tokusouhonsuu:
        params['tokusouhonsuu'] = '第' + \
            intToZen(shussouhyou.tokusouhonsuu) + '回'

# ２）－４ 特別競走名本題
# <tokusoumeihon >’０４メトロポリタンオクトーバーカップ</ tokusoumeihon>
#  レース名称を編集。
    params['tokusoumeihon'] = shussouhyou.tokusoumeihon

# ２）－５ 特別競走名副題
# <tokusoumeifuku>中央競馬交流</tokusoumeifuku>
#  付加名称を編集。
    params['tokusoumeifuku'] = shussouhyou.tokusoumeifuku

# ２）－６ 副賞名
# <ck_fukusyoumei>特別区競馬組合議会議長賞</ck_fukusyoumei>
#  副賞名を編集。複数ある場合は繰り返して編集。
    # 副賞名をリスト化して渡す
    ck_fukusyoumei_list = makelist(shussouhyou.ck_fukusyoumei)
    params['ck_fukusyoumei_list'] = ck_fukusyoumei_list

# ２）－７ グレード区分
# <guredo>Ｇ３</guredo>
#  グレード区分を編集
    params['guredo'] = shussouhyou.guredo


# ２）－８ 中央交流区分
# <ck_chuokouryu>指定交流</ck_chuokouryu>
#  中央交流区分を編集。
    params['ck_chuokouryu'] = shussouhyou.ck_chuokouryu

# ２）－９ 競走距離
# <kyori>２０００</kyori>
#  競走距離を編集
    params['kyori'] = intToZen(shussouhyou.kyori)

# ２）－９ トラック
# <torakku>ダート右・外コース</torakku>
#  芝・ダート区分と回りとコース区分を『ダート右・外コース』のように編集する。回り
# やコース区分がない場合は省略する。『ダート左』など。
    torakku = str(shussouhyou.ck_shibadat) + str(shussouhyou.ck_mawari)
    if shussouhyou.ck_naigai:
        torakku = torakku + '・' + str(shussouhyou.ck_naigai)
    params['torakku'] = torakku


# ２）－10 ナイター区分
# <ck_naita>ナイター</ck_naita>
#  ナイターを実施する場合に編集。
    params['ck_naita'] = shussouhyou.ck_naita

# ２）－11 本賞金
# <ck_shokin ck_chaku=”１着”>１０００００００</ck_shokin>
#  レースの着別の本賞金を編集。属性値 ck_chaku の内容で着を区別し、MAX５着までの
# 内容を繰り返して編集する。
    params['ck_shokin1'] = intToZen(shussouhyou.ck_shokin1)
    params['ck_shokin2'] = intToZen(shussouhyou.ck_shokin2)
    params['ck_shokin3'] = intToZen(shussouhyou.ck_shokin3)
    params['ck_shokin4'] = intToZen(shussouhyou.ck_shokin4)
    params['ck_shokin5'] = intToZen(shussouhyou.ck_shokin5)

# ２）－12 レコード区分
# <rekokubun>レコード</rekokubun>
#  レコードタイムを編集する際に付加。
#  ばんえい競馬は編集しない
    params['baneiflag'] = jou_data[2]

# ２）－13 レコード発生年月日
# <ck_rekobi>１９８００９１８</ck_rekobi>
# レコードが発生した年月日を西暦(８桁)で編集。
    params['ck_rekobi'] = intToZen(shussouhyou.ck_rekobi)

# ２）－14 レコードタイム
# <rekota>
#    <refun>１</refun>
#    <rebyo>４９</rebyo>
#    <remiri>９</remiri>
# </rekota>
#  レコードタイムを分、秒、ミリ秒で編集する。
#  ばんえい競馬は編集しない
    params['refun'] = intToZen(shussouhyou.refun)
    params['rebyo'] = intToZen(shussouhyou.rebyo)
    params['remiri'] = intToZen(shussouhyou.remiri)

# ２）－15 レコード馬名
# <rekobamei hyouki="9 字">カツアール </rekobamei>
# <rekobamei hyouki="正式名">カツアール</rekobamei>
#  レコード馬名を 9 字と正式名を編集。属性値 hyouki の内容で区別する。
    params['rekobamei_seishiki'] = shussouhyou.rekobamei
    params['rekobamei_9char'] = bamei9char(shussouhyou.rekobamei)

# ２）－16 レコード騎手名
# <ck_rekokimei>赤嶺本浩</ck_rekokimei>
# レコードタイム馬の騎手名を編集
    params['ck_rekokimei'] = shussouhyou.ck_rekokimei

# ２）－17 レコード負担重量
# <ck_rekofujyuu>５１</ck_rekofujyuu>
# レコードタイム馬の負担重量を編集
    params['ck_rekofujyuu'] = intToZen(shussouhyou.ck_rekofujyuu)

# ２）－18 出走予定頭数
# <shusuu>１５</shusuu>
#  出走予定頭数を編集
    params['shusuu'] = intToZen(shussouhyou.shusuu)

# ２）－19 発送予定時刻
# <hassoujikoku>
# <hji>２０</hji>
# <hfun>２０</hfun>
# </hassoujikoku>
#  発走予定時刻を時、分で編集。
    params['hji'] = intToZen(shussouhyou.hji)
    params['hfun'] = intToZen(shussouhyou.hfun)

# ２）－20 競争条件情報
# <jyoukenjouhou>
#    <bareijouken>３歳</bareijouken>
#    レースの馬齢条件を編集
#    <jouken/>
#    競争条件。常に空タグを設定（中央競馬で必須タグなため）。
#    ※以下、場によって提供される形式が違うため、提供された内容をそのまま編集
#    <ck_shikaku>選定馬</ck_shikaku>
#    競走資格を編集。複数ある場合は繰り返して編集。
#    <ck_rkaku>Ａ３</ck_rkaku>
#    レース格を編集。複数ある場合は繰り返して編集。
#    <ck_rkumi>ロ</ck_rkumi>
#    レース組を編集。複数ある場合は繰り返して編集。
# </jyoukenjouhou>

    # 出走表の競争種別データと品種年齢区分マスタから馬齢条件用名称を取得
    # ★→もし受信時から馬齢条件用名称があるなら、そのまま中間DBに設定して、そこからとった方がいい。
    bareijouken = Mst_Breed_age.getBareiJouken(shubetsu)
    params['bareijouken'] = Mst_Breed_age.getBareiJouken(shubetsu)

    params['ck_shikaku_list'] = makelist(shussouhyou.ck_shikaku)
    params['ck_rkaku_list'] = makelist(shussouhyou.ck_rkaku)
    params['ck_rkumi_list'] = makelist(shussouhyou.ck_rkumi)

# ２）－21 重量種別
# <juuryoushubetsu>別定</juuryoushubetsu>
#  重量種別を編集。
    params['jyuuryoushubetsu'] = shussouhyou.jyuuryoushubetsu


# ３）出走馬情報

    # ○○○○○○○○○出走馬情報取得○○○○○○○○○
    # 出走表に紐付く出走馬情報をとる。
    shussouba_obj_list = get_list_or_404(
        Md_Shussouhyou_shussouba.objects, shussouhyou=shussouhyou)

    shusssouba_params = {}  # 編集した出走馬ごとのパラメータ
    shusssouba_params_list = []  # ↑の編集した出走馬ごとのパラメータをまとめたリスト

    for shussouba in shussouba_obj_list:
        # ３）－１ 枠番
        # <waku>１</waku>
        #  枠番を編集。
        shusssouba_params['waku'] = intToZen(shussouba.waku)
        # ３）－２ 馬番
        # <uma>１</uma>
        #  馬番を編集。
        shusssouba_params['uma'] = intToZen(shussouba.uma)

        # ３）－３ 帽子色
        # <ck_boiro>白</ck_boiro>
        #  帽子の色を編集。
        #  （白、黒、赤、青、黄、緑、橙、桃、紫、茶など）
        shusssouba_params['ck_boiro'] = shussouba.ck_boiro

        # ３）－４－１ 負担重量
        # <fujuu>５０．５</fujuu>
        # 負担重量を編集。騎手変更が発生した場合は騎手変更後の負担重量。
        # ばんえい競馬では積載重量を編集するため負担重量は空タグを編集。
        # 場によって提供される形式が違うため、提供された内容をそのまま編集
        shusssouba_params['fujuu'] = intToZen(shussouba.fujuu)

        # ３）－４－２ 積載重量（ばんえい競馬のみ）
        # <ck_sekijuu>７５０</ck_sekijuu>
        # ばんえい競馬では積載重量を編集。騎手変更が発生した場合は騎手変更後の積載重量。
        shusssouba_params['ck_sekijuu'] = intToZen(shussouba.ck_sekijuu)

        # ３）－５ 馬性別
        # <seibetsu>牡</seibetsu>
        #  馬の性別を編集。
        shusssouba_params['seibetsu'] = shussouba.seibetsu

        # ３）－６ 馬名
        # <bamei hyouki="9 字">マルダイメグ </bamei>
        # <bamei hyouki="正式名">マルダイメグ</bamei>
        #  馬名の 9 字と正式名を編集。属性値 hyouki の内容で区別する。
        shusssouba_params['bamei_seishiki'] = shussouba.bamei
        shusssouba_params['bamei_9char'] = bamei9char(shussouba.bamei)

        # ３）－７ 旧馬名
        # <kyuubamei hyouki="9 字">メグ </bamei>
        # <kyuubamei hyouki="正式名">メグ</bamei>
        #  出走馬に旧馬名がある場合は、9 字と正式名を編集。属性値 hyouki の内容で区別する。
        shusssouba_params['kyuubamei_seishiki'] = shussouba.kyuubamei
        shusssouba_params['kyuubamei_9char'] = bamei9char(
            shussouba.kyuubamei)

        # ３）－８ 馬齢
        # <barei>３</barei>
        #  馬齢を編集。
        shusssouba_params['barei'] = intToZen(shussouba.barei)

        # ３）－９ 毛色
        # <ck_keiro>黒鹿毛</ck_keiro>
        #  毛色を編集
        shusssouba_params['ck_keiro'] = shussouba.ck_keiro

        # ３）－10 父名
        # <ck_chichi>フジキセキ</ck_chichi>
        #  父名を編集
        shusssouba_params['ck_chichi'] = shussouba.ck_chichi

        # ３）－11 母名
        # <ck_haha>マルダイルビー</ck_haha>
        #  母名を編集。
        shusssouba_params['ck_haha'] = shussouba.ck_haha

        # ３）－12 母の父名
        # <ck_hahachichi>ホリスキー</ck_hahachichi>
        #  母の父名を編集。
        shusssouba_params['ck_hahachichi'] = shussouba.ck_hahachichi

        # ３）－13 馬主名
        # <ck_banushi>有 栄光開発</ck_banushi>
        #  馬主名を編集。
        shusssouba_params['ck_banushi'] = shussouba.ck_banushi

        # ３）－14 生産牧場名
        # <ck_seisansya>澤田嘉隆</ck_seisansya>
        #  生産牧場名を編集。
        shusssouba_params['ck_seisansya'] = shussouba.ck_seisansya

        # ３）－15 馬の所属
        # <ck_umasyozoku>川崎</ck_umasyozoku>
        #  馬が所属する場を編集
        shusssouba_params['ck_umasyozoku'] = shussouba.ck_umasyozoku

        # ３）－16 取得賞金
        # <ck_kakutokuskin>２４７３５０００</ck_kakutokuskin>
        #  馬の収得賞金「地方収得賞金」＋「中央収得賞金」＋「中央付加賞金」を編集。
        shusssouba_params['ck_kakutokuskin'] = intToZen(
            shussouba.ck_kakutokuskin)

        # ３）－17 出走取り消し情報
        # <ck_torikeshi>
        # <ck_jikosyu>競走除外</ck_jikosyu>
        # <ck_jikoriyuu>事故</ck_jikoriyuu>
        # </ck_torikeshi>
        # 出走取り消しが発生した場合に事故種別と事故理由を編集。
        shusssouba_params['ck_jikosyu'] = shussouba.ck_jikosyu
        shusssouba_params['ck_jikoriyuu'] = shussouba.ck_jikoriyuu

        # ４）騎手情報
        # ４）－１ 騎手名
        # <kimei hyouki="3 字">北村宏</kimei>
        # <kimei hyouki="姓">北村</kimei>
        # <kimei hyouki="名">宏司</kimei>
        #  騎手名の 3 字、姓、名を編集。属性値 hyouki の内容で区別する。
        #  騎手変更が発生した場合は変更後の騎手名を編集。
        #  外国人騎手など姓と名の分割が難しいケースについては、姓に名前を編集し、名については編集しない。
        shusssouba_params['kimei'] = shussouba.kimei
        shusssouba_params['kimei_sei'] = shussouba.kimei_sei
        shusssouba_params['kimei_mei'] = shussouba.kimei_mei

        # ４）－２ 騎手所属場
        # <ck_kisyozoku>JRA</ck_kisyozoku>
        #  騎手の所属場を編集。騎手変更が発生した場合は変更後の所属場を編集。
        shusssouba_params['ck_kisyozoku'] = shussouba.ck_kisyozoku

        # ４）－３ 騎手コード
        # <kiko/>
        #  常に空タグを設定

        # ４）－４ 騎手免許番号
        # <ck_kimnbangou>３０２０１</ck_kimnbangou>
        #  騎手免許番号を編集。騎手変更が発生した場合は変更後の騎手免許番号を編集。
        shusssouba_params['ck_kimnbangou'] = intToZen(shussouba.ck_kimnbangou)

        # ４）－５ 騎手成績
        # <ck_kiseiseki>
        # <ck_kizen ck_chaku=”1 着”>４</ck_kizen>
        # <ck_kizen ck_chaku=”2 着”>２</ck_kizen>
        # <ck_kizen ck_chaku=”3 着”>４</ck_kizen>
        # <ck_kizen ck_chaku=”着外”>１２</ck_kizen>
        # </ck_kiseiseki>
        #  該当馬と騎手との組み合わせでの地方での成績
        # 騎手変更が発生した場合は騎手成績は編集しない。
        shusssouba_params['ck_kizen_1chaku'] = intToZen(
            shussouba.ck_kizen_1chaku)
        shusssouba_params['ck_kizen_2chaku'] = intToZen(
            shussouba.ck_kizen_2chaku)
        shusssouba_params['ck_kizen_3chaku'] = intToZen(
            shussouba.ck_kizen_3chaku)
        shusssouba_params['ck_kizen_chakugai'] = intToZen(
            shussouba.ck_kizen_chakugai)

        # ４）－６ 見習区分
        # <mikubun>１</mikubun>
        #  減量騎手が騎乗した場合の減量重量を編集。
        # 騎手変更が発生し減量騎手が騎乗した場合は変更後の減量重量を編集。
        shusssouba_params['mikubun'] = intToZen(shussouba.mikubun)

        # ４）－７ 騎手変更情報
        # <ck_kishuhenkou>
        # <ck_henriyuu>疾病</ck_henriyuu>
        # <ck_maekimei hyouki="3 字">石川駿</ck_maekimei>
        # <ck_henmaefujuu>５３</ck_henmaefujuu>
        # </ck_kishuhenkou>
        # 騎手変更が発生した場合に騎手変更理由と変更前騎手名(３字略)と変更前負担重量を編集。
        # ばんえい競馬の場合は負担重量の代わりに積載重量を編集。
        # <ck_henmaesekijuu>５００</ck_henmaesekijuu>
        shusssouba_params['ck_henriyuu'] = shussouba.ck_henriyuu
        shusssouba_params['ck_maekimei'] = shussouba.ck_maekimei
        shusssouba_params['ck_henmaefujuu'] = intToZen(
            shussouba.ck_henmaefujuu)
        shusssouba_params['ck_henmaesekijuu'] = intToZen(
            shussouba.ck_henmaesekijuu)

        # ５）調教師情報
        # ５）－１ 調教師名
        # <choumei hyouki="3 字">佐々仁</choumei>
        # <choumei hyouki="姓">佐々木</choumei>
        # <choumei hyouki="名">仁</choumei>
        #  調教師名の 3 字、姓、名を編集。属性値 hyouki の内容で区別する。
        shusssouba_params['choumei'] = shussouba.choumei
        shusssouba_params['choumei_sei'] = shussouba.choumei_sei
        shusssouba_params['choumei_mei'] = shussouba.choumei_mei

        # ６）過去着成績
        # ６）－１ 距離別成績 <ck_kyoriseiseki>・・・</ck_kyoriseiseki>で囲まれる
        # ６）－１－１ 短距離成績
        # <ck_tan ck_chaku="1 着">４</ck_tan>
        # <ck_tan ck_chaku="2 着">２</ck_tan>
        # <ck_tan ck_chaku="3 着">４</ck_tan>
        # <ck_tan ck_chaku="着外">１２</ck_tan>
        #  該当馬の１４００ｍ以下レースでの着別成績を編集
        shusssouba_params['ck_tan_1chaku'] = intToZen(shussouba.ck_tan_1chaku)
        shusssouba_params['ck_tan_2chaku'] = intToZen(shussouba.ck_tan_2chaku)
        shusssouba_params['ck_tan_3chaku'] = intToZen(shussouba.ck_tan_3chaku)
        shusssouba_params['ck_tan_chakugai'] = intToZen(
            shussouba.ck_tan_chakugai)

        # ６）－１－２ 中距離成績
        # <ck_tyuu ck_chaku="1 着">４</ck_tyuu>
        # <ck_tyuu ck_chaku="2 着">２</ck_tyuu>
        # <ck_tyuu ck_chaku="3 着">４</ck_tyuu>
        # <ck_tyuu ck_chaku="着外">１２</ck_tyuu>
        #  該当馬の１４００ｍ超～２０００ｍレースでの着別成績を編集。
        #  ばんえい競馬では編集しない。
        shusssouba_params['ck_tyuu_1chaku'] = intToZen(
            shussouba.ck_tyuu_1chaku)
        shusssouba_params['ck_tyuu_2chaku'] = intToZen(
            shussouba.ck_tyuu_2chaku)
        shusssouba_params['ck_tyuu_3chaku'] = intToZen(
            shussouba.ck_tyuu_3chaku)
        shusssouba_params['ck_tyuu_chakugai'] = intToZen(
            shussouba.ck_tyuu_chakugai)

        # ６）－１－２ 長距離成績
        # <ck_tyou ck_chaku="1 着">４</ck_tyou>
        # <ck_tyou ck_chaku="2 着">２</ck_tyou>
        # <ck_tyou ck_chaku="3 着">４</ck_tyou>
        # <ck_tyou ck_chaku="着外">１２</ck_tyou>
        #  該当馬の２０００ｍ超レースでの着別成績を編集。
        #  ばんえい競馬では編集しない。
        shusssouba_params['ck_tyou_1chaku'] = intToZen(
            shussouba.ck_tyou_1chaku)
        shusssouba_params['ck_tyou_2chaku'] = intToZen(
            shussouba.ck_tyou_2chaku)
        shusssouba_params['ck_tyou_3chaku'] = intToZen(
            shussouba.ck_tyou_3chaku)
        shusssouba_params['ck_tyou_chakugai'] = intToZen(
            shussouba.ck_tyou_chakugai)

        # ＜＜独自計算その１＞＞
        # ６）－２ 場別距離別累計成績 <ck_kyoriseiseki2 ck_kyori="1400" ck_kousu="ダート">・・・
        # </ck_kyoriseiseki2>などで編集
        # 属性値として ck_kyori で距離、ck_kousu でダート・芝区分を付加。編集する距離は
        # 当該距離（芝 or ダート）＋1000m,1200m,1400m,1600m,1800m,2000m（ダート）の合計７距離を
        # 競争実績があるもののみ編集する。。

        # 当該距離の編集は該当レースがダートの場合はダートを、芝の場合は芝を編集する。ただ
        # し、ダートでの距離実績がない場合は代わりに芝を、芝の距離実績がない場合はダートの
        # 成績を編集する。

        # →この計算をここでやるのか、データとしてもらっているのか、計算しているのか、その場合どんな形でNewsMLに渡しているのかが、
        # 現行の設計書に書いていない。

        # とりあえずSUEのデータから計算する処理を作った。

        # ６）－２－１ 成績
        # <ck_kyoribetsu ck_chaku="1 着">４</ck_kyoribetsu>
        # <ck_kyoribetsu ck_chaku="2 着">３</ck_kyoribetsu>
        # <ck_kyoribetsu ck_chaku="3 着">３</ck_kyoribetsu>
        # <ck_kyoribetsu ck_chaku="着外">４</ck_kyoribetsu>
        # 該当馬の距離別コース別成績を編集。

        # ６）－２－２ 該当馬最高タイム
        # <ck_kyoritime>１分２２秒４</ck_kyoritime>
        # <ck_kyoritimejyou>大井競馬</ck_kyoritimejyou>
        # <ck_kyoritimebaba>良</ck_kyoritimebaba>
        # 該当馬の距離別コース別の最高タイムとそのタイムを出したときの競馬場と馬場状態を
        # 編集する。

        # 当該レースの距離とダート芝区分
        tougaikyori = shussouhyou.kyori
        tougaishibadat = str(shussouhyou.ck_shibadat)  # "ダート" or "芝"

        kyoribetsu_list = {}
        kyoribetsu_data_list = []

        # ○○○○○○○○○出走馬の場別距離別累計成績情報取得○○○○○○○○○
        kyoribetsu_list["1000"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=1000, ck_ruishibadat__Turf_dirt_name='ダート')
        kyoribetsu_list["1200"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=1200, ck_ruishibadat__Turf_dirt_name='ダート')
        kyoribetsu_list["1400"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=1400, ck_ruishibadat__Turf_dirt_name='ダート')
        kyoribetsu_list["1600"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=1600, ck_ruishibadat__Turf_dirt_name='ダート')
        kyoribetsu_list["1800"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=1800, ck_ruishibadat__Turf_dirt_name='ダート')
        kyoribetsu_list["2000"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=2000, ck_ruishibadat__Turf_dirt_name='ダート')
        # ダートの当該距離レコード
        kyoribetsu_list["tougai_dart"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=tougaikyori, ck_ruishibadat__Turf_dirt_name='ダート')
        # 芝の当該距離レコード
        kyoribetsu_list["tougai_shiba"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            shussouba=shussouba, ck_ruikyori=tougaikyori, ck_ruishibadat__Turf_dirt_name='芝')

        # もしダートのレースでダートの当該距離のレコードが存在する場合、芝の当該距離レコード（存在すれば）は不要なので削除する
        if tougaishibadat == "ダート" and kyoribetsu_list["tougai_dart"]:
          del kyoribetsu_list["tougai_shiba"]
          # 且つ、当該距離（ダート）が1000/1200/1400/1600/1800/2000の場合は、レコードがかぶるので当該距離レコードを削除する。
          if tougaikyori == 1000 or tougaikyori == 1200 or tougaikyori == 1400 or tougaikyori == 1600 or tougaikyori == 1800 or tougaikyori == 2000:
              del kyoribetsu_list["tougai_dart"]

        # もし芝のレースで芝の当該距離のレコードが存在する場合、ダートの当該距離レコード（存在すれば）は不要なので削除する
        if tougaishibadat == "芝" and kyoribetsu_list["tougai_shiba"]:
          del kyoribetsu_list["tougai_dart"]

        shusssouba_params['kyoribetsu_list'] = kyoribetsu_list  # テスト用

        for key, value in kyoribetsu_list.items():
            if value:
               ck_kyoribetsu_ck_chaku_1 = 0
               ck_kyoribetsu_ck_chaku_2 = 0
               ck_kyoribetsu_ck_chaku_3 = 0
               ck_kyoribetsu_ck_chakugai = 0
               ck_kyoritime = 0

               # 着別累計回数を計算する
               for ruikei in value:
                    ck_kyoribetsu_ck_chaku_1 = ck_kyoribetsu_ck_chaku_1 + ruikei.ck_ruikai_1chaku
                    ck_kyoribetsu_ck_chaku_2 = ck_kyoribetsu_ck_chaku_2 + ruikei.ck_ruikai_2chaku
                    ck_kyoribetsu_ck_chaku_3 = ck_kyoribetsu_ck_chaku_3 + ruikei.ck_ruikai_3chaku
                    ck_kyoribetsu_ck_chakugai = ck_kyoribetsu_ck_chakugai + ruikei.ck_ruikai_chakugai
                    # 累計最高タイムを選ぶ
                    if ck_kyoritime > ruikei.ck_ruirekuta or ck_kyoritime == 0:
                         ck_kyoritime = ruikei.ck_ruirekuta
                         ck_ruijoumei = ruikei.ck_ruijoumei
                         ck_ruibajru = ruikei.ck_ruibajru

               kyoribetsu_data = {}
               if key == 'tougai_dart':
                   kyoribetsu_data['ck_ruishibadat'] = 'ダート'
                   kyoribetsu_data['ck_ruikyori'] = tougaikyori
               elif key == 'tougai_shiba':
                   kyoribetsu_data['ck_ruishibadat'] = '芝'
                   kyoribetsu_data['ck_ruikyori'] = tougaikyori
               else:
                   kyoribetsu_data['ck_ruishibadat'] = 'ダート'
                   kyoribetsu_data['ck_ruikyori'] = key

               kyoribetsu_data['ck_ruikai_1chaku'] = intToZen(
                   ck_kyoribetsu_ck_chaku_1)
               kyoribetsu_data['ck_ruikai_2chaku'] = intToZen(
                   ck_kyoribetsu_ck_chaku_2)
               kyoribetsu_data['ck_ruikai_3chaku'] = intToZen(
                   ck_kyoribetsu_ck_chaku_3)
               kyoribetsu_data['ck_ruikai_chakugai'] = intToZen(
                   ck_kyoribetsu_ck_chakugai)
               kyoribetsu_data['ck_kyoritime'] = intToZen(ck_kyoritime)
               kyoribetsu_data['ck_kyoritimejyou'] = ck_ruijoumei
               kyoribetsu_data['ck_kyoritimebaba'] = ck_ruibajru

               kyoribetsu_data_list.append(kyoribetsu_data.copy())

        shusssouba_params['kyoribetsu_data_list'] = kyoribetsu_data_list


        # ６）－３ 着別成績 < ck_chakuseiseki>・・・</ ck_chakuseiseki>で囲まれる
        # ６）－３－１ 全成績
        # <ck_zen ck_chaku="1 着">４</ck_zen>
        # <ck_zen ck_chaku="2 着">２</ck_zen>
        # <ck_zen ck_chaku="3 着">４</ck_zen>
        # <ck_zen ck_chaku="着外">１２</ck_zen>
        #  該当馬の全レースでの着別成績を編集。
        shusssouba_params['ck_zen_1chaku'] = intToZen(shussouba.ck_zen_1chaku)
        shusssouba_params['ck_zen_2chaku'] = intToZen(shussouba.ck_zen_2chaku)
        shusssouba_params['ck_zen_3chaku'] = intToZen(shussouba.ck_zen_3chaku)
        shusssouba_params['ck_zen_chakugai'] = intToZen(
            shussouba.ck_zen_chakugai)
        # ６）－３－２ 右回りダート成績
        # <ck_migid ck_chaku="1 着">４</ck_migid>
        # <ck_migid ck_chaku="2 着">２</ck_migid>
        # <ck_migid ck_chaku="3 着">４</ck_migid>
        # <ck_migid ck_chaku="着外">１２</ck_migid>
        #  該当馬の右回りダートレースでの着別成績を編集。
        #  ばんえい競馬では編集しない。
        shusssouba_params['ck_migid_1chaku'] = intToZen(
            shussouba.ck_migid_1chaku)
        shusssouba_params['ck_migid_2chaku'] = intToZen(
            shussouba.ck_migid_2chaku)
        shusssouba_params['ck_migid_3chaku'] = intToZen(
            shussouba.ck_migid_3chaku)
        shusssouba_params['ck_migid_chakugai'] = intToZen(
            shussouba.ck_migid_chakugai)

        # ６）－３－３ 左回りダート成績
        # <ck_hidarid ck_chaku="1 着">４</ck_hidarid>
        # <ck_hidarid ck_chaku="2 着">２</ck_hidarid>
        # <ck_hidarid ck_chaku="3 着">４</ck_hidarid>
        # <ck_hidarid ck_chaku="着外">１２</ck_hidarid>
        #  該当馬の左回りダートレースでの着別成績を編集。
        #  ばんえい競馬では編集しない。
        shusssouba_params['ck_hidarid_1chaku'] = intToZen(
            shussouba.ck_hidarid_1chaku)
        shusssouba_params['ck_hidarid_2chaku'] = intToZen(
            shussouba.ck_hidarid_2chaku)
        shusssouba_params['ck_hidarid_3chaku'] = intToZen(
            shussouba.ck_hidarid_3chaku)
        shusssouba_params['ck_hidarid_chakugai'] = intToZen(
            shussouba.ck_hidarid_chakugai)

        # ６）－３－４ 該当競馬場成績
        # <ck_jyou ck_chaku="1 着">４</ck_jyou>
        # <ck_jyou ck_chaku="2 着">２</ck_jyou>
        # <ck_jyou ck_chaku="3 着">４</ck_jyou>
        # <ck_jyou ck_chaku="着外">１２</ck_jyou>
        #  該当馬の該当競馬場での芝 or ダート（芝もしくはダートかは今回出走するレースのコー
        # スによって違う）での着別成績を編集。
        shusssouba_params['ck_jyou_1chaku'] = intToZen(
            shussouba.ck_jyou_1chaku)
        shusssouba_params['ck_jyou_2chaku'] = intToZen(
            shussouba.ck_jyou_2chaku)
        shusssouba_params['ck_jyou_3chaku'] = intToZen(
            shussouba.ck_jyou_3chaku)
        shusssouba_params['ck_jyou_chakugai'] = intToZen(
            shussouba.ck_jyou_chakugai)

        # ＜＜独自計算その２＞＞
        # ６）－４ 重と不良馬場成績 <ck_babaseiseki ck_kousu="ダート">・・・</ck_babaseiseki>など
        # で編集。属性値として ck_kousu でダート・芝区分を付加。
        #  重馬場と不良馬場の着別成績を競争実績があるもののみ編集する。芝とダート分繰り返し
        # 編集。ばんえいは馬場水分が 2.5%以上の着別成績でダートのみ

        # ６）－４－１ 成績
        # <ck_omo ck_chaku="1 着">１</ck_omo>
        # <ck_omo ck_chaku="2 着">０</ck_omo>
        # <ck_omo ck_chaku="3 着">０</ck_omo>
        # <ck_omo ck_chaku="着外">１</ck_omo>
        # 該当馬の重と不良馬場での成績を編集。

        # →疑問１．ダート開催でも芝のデータが必要なのか不明。とりあえずデータがあれば出すようにする。
        # →疑問２．このデータをもらっているのか、計算しているのか、その場合どんな形でNewsMLに渡しているのか、現行の設計書に書いていない。

        # とりあえずSUEのデータから計算する処理を作った。

        bababetsu_list = {}
        bababetsu_data_list = []
        # ○○○○○○○○○出走馬の重と不良馬場累計成績情報取得○○○○○○○○○
        bababetsu_list["omofuryo_dart"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            Q(shussouba=shussouba), Q(ck_ruishibadat__Turf_dirt_name='ダート'), Q(ck_ruibajru__Track_condition_name='重') | Q(ck_ruibajru__Track_condition_name='不良'))
        bababetsu_list["omofuryo_shiba"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            Q(shussouba=shussouba), Q(ck_ruishibadat__Turf_dirt_name='芝'), Q(ck_ruibajru__Track_condition_name='重') | Q(ck_ruibajru__Track_condition_name='不良'))
        bababetsu_list["omofuryo_banei"] = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            Q(shussouba=shussouba), Q(ck_kkbasui__gte=2.5))

        shusssouba_params['bababetsu_list'] = bababetsu_list  # テスト用

        for key, value in bababetsu_list.items():
            if value:
               ck_bababetsu_ck_chaku_1 = 0
               ck_bababetsu_ck_chaku_2 = 0
               ck_bababetsu_ck_chaku_3 = 0
               ck_bababetsu_ck_chakugai = 0

               # 着別累計回数を計算する
               for ruikei in value:
                   ck_bababetsu_ck_chaku_1 = ck_bababetsu_ck_chaku_1 + ruikei.ck_ruikai_1chaku
                   ck_bababetsu_ck_chaku_2 = ck_bababetsu_ck_chaku_2 + ruikei.ck_ruikai_2chaku
                   ck_bababetsu_ck_chaku_3 = ck_bababetsu_ck_chaku_3 + ruikei.ck_ruikai_3chaku
                   ck_bababetsu_ck_chakugai = ck_bababetsu_ck_chakugai + ruikei.ck_ruikai_chakugai

               bababetsu_data = {}
               if key == 'omofuryo_dart':
                   bababetsu_data['ck_ruishibadat'] = 'ダート'
               elif key == 'omofuryo_shiba':
                   bababetsu_data['ck_ruishibadat'] = '芝'
               elif key == 'omofuryo_banei':
                   bababetsu_data['ck_ruishibadat'] = 'ダート'  # ばんえい馬場水分2.5%以上

               bababetsu_data['ck_omo_1chaku'] = intToZen(
                   ck_bababetsu_ck_chaku_1)
               bababetsu_data['ck_omo_2chaku'] = intToZen(
                   ck_bababetsu_ck_chaku_2)
               bababetsu_data['ck_omo_3chaku'] = intToZen(
                   ck_bababetsu_ck_chaku_3)
               bababetsu_data['ck_omo_chakugai'] = intToZen(
                   ck_bababetsu_ck_chakugai)

               bababetsu_data_list.append(bababetsu_data.copy())

        shusssouba_params['bababetsu_data_list'] = bababetsu_data_list

        # ＜＜独自計算その３＞＞
        # ６）－５ 競馬場別コース別成績 <ck_jyouseiseki ck_jyo="浦和競馬" ck_kousu="ダート" >・・・
        # </ck_jyouseiseki >などで編集
        # 属性値として ck_jyo で競馬場名、ck_kousu でダート・芝区分を付加。
        # 該当競馬場が含まれる下記競馬場グループに属する競馬場をコース別に競争実績があるも
        # ののみ編集する。
        # 競馬場グループ…（帯広ばんえい）、（旭川・門別・札幌）、（盛岡・水沢）、（浦和・船橋・
        # 大井・川崎）、（金沢・笠松・名古屋・中京）、（園田・姫路）、（福山・高
        # 知）、（佐賀・荒尾）

        # ６）－５－１ 成績
        # <ck_jyoubetsu ck_chaku="1 着">０</ck_jyoubetsu>
        # <ck_jyoubetsu ck_chaku="2 着">０</ck_jyoubetsu>
        # <ck_jyoubetsu ck_chaku="3 着">０</ck_jyoubetsu>
        # <ck_jyoubetsu ck_chaku="着外">１</ck_jyoubetsu>
        # 該当馬の場別コース別での成績を編集。

        # とりあえずSUEのデータから計算する処理を作った。

        jou_joubetsu_list = {}
        jou_joubetsu_data_list = []

        # 開催場の所属グループ
        group = Mst_Jou.objects.get(Jou_code=joucode).Group

        # ○○○○○○○○○開催場とその所属グループ場での出走馬累計成績情報取得○○○○○○○○○
        joubetsu_seiseki_dart = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            Q(shussouba=shussouba), Q(ck_ruishibadat__Turf_dirt_name='ダート'), Q(ck_ruijoumei__Group=group))
        joubetsu_seiseki_shiba = Md_Shussouhyou_shussouba_ruikei.objects.filter(
            Q(shussouba=shussouba), Q(ck_ruishibadat__Turf_dirt_name='芝'), Q(ck_ruijoumei__Group=group))

        def get_joubeturuikei(joubetsu_seiseki_data, dartorturf):
          joubetsu_dict = {}
          for joubetsu_seiseki in joubetsu_seiseki_data:
              joumei = str(joubetsu_seiseki.ck_ruijoumei.Jou_name)

              if joumei in joubetsu_dict.keys():
                    joubetsu_dict[joumei]["ck_chaku1"] = joubetsu_dict[joumei]["ck_chaku1"] + \
                       joubetsu_seiseki.ck_ruikai_1chaku
                    joubetsu_dict[joumei]["ck_chaku2"] = joubetsu_dict[joumei]["ck_chaku2"] + \
                        joubetsu_seiseki.ck_ruikai_2chaku
                    joubetsu_dict[joumei]["ck_chaku3"] = joubetsu_dict[joumei]["ck_chaku3"] + \
                        joubetsu_seiseki.ck_ruikai_3chaku
                    joubetsu_dict[joumei]["ck_chakugai"] = joubetsu_dict[joumei]["ck_chakugai"] + \
                        joubetsu_seiseki.ck_ruikai_chakugai
              else:
                    joubetsu_list = {}
                    joubetsu_dict.setdefault(joumei, joubetsu_list)
                    joubetsu_dict[joumei]["joumei"] = joumei
                    joubetsu_dict[joumei]["ck_kousu"] = dartorturf
                    joubetsu_dict[joumei]["ck_chaku1"] = joubetsu_seiseki.ck_ruikai_1chaku
                    joubetsu_dict[joumei]["ck_chaku2"] = joubetsu_seiseki.ck_ruikai_2chaku
                    joubetsu_dict[joumei]["ck_chaku3"] = joubetsu_seiseki.ck_ruikai_3chaku
                    joubetsu_dict[joumei]["ck_chakugai"] = joubetsu_seiseki.ck_ruikai_chakugai

          jou_joubetsu_data = joubetsu_dict.values()
          # 数値の全角化処理
          for jl in jou_joubetsu_data:
               jl["ck_chaku1"] = intToZen(jl["ck_chaku1"])
               jl["ck_chaku2"] = intToZen(jl["ck_chaku2"])
               jl["ck_chaku3"] = intToZen(jl["ck_chaku3"])
               jl["ck_chakugai"] = intToZen(jl["ck_chakugai"])

          return jou_joubetsu_data

        shusssouba_params['joubetsu_dict_dart'] = get_joubeturuikei(
            joubetsu_seiseki_dart, "ダート")
        shusssouba_params['joubetsu_dict_shiba'] = get_joubeturuikei(
            joubetsu_seiseki_shiba, "芝")


        # ７）過去レース成績
        #  該当馬の１レース分の過去成績は<ck_kkseisekijouhou>・・・</ck_kkseisekijouhou>で囲ま
        # れて表現される。

        # ○○○○○○○○○出走馬の過去成績取得○○○○○○○○○
        # 出走馬に紐付く過去成績情報をとる。
        seiseki_obj_list = get_list_or_404(
            Md_Shussouhyou_shussouba_5seiseki.objects, shussouba=shussouba)

        seiseki_params = {}          # 編集した成績ごとのパラメータ
        seiseki_params_list = []          # ↑の編集した編集ごとのパラメータをまとめたリスト

        for seiseki in seiseki_obj_list:
             # ７）－１ 出走日付
             # <ck_kkhiduke>２００４年２月１２日</ck_kkhiduke>
             #  過去成績として編集されるレースの出走日付を編集。

             seiseki_params['ck_kkhiduke'] = seiseki.ck_kkhiduke
             # ７）－２ 開催場情報 <ck_kkkaijouhou>・・・</ck_kkkaijouhou>で囲まれて表現される。
             # ７）－２－１ 競馬場名
             # <ck_kkjoumei>Ｊ阪神</ck_kkjoumei>
             #  出走したレースの開催場名を編集。
             seiseki_params['ck_kkjoumei'] = seiseki.ck_kkjoumei
             # ７）－２－２ 天候
             # <ck_kktenkou>晴</ck_kktenkou>
             #  出走したレースの天候を編集。
             seiseki_params['ck_kktenkou'] = seiseki.ck_kktenkou

             # ７）－２－３ 馬場状態
             # <ck_kkbajou>良</ck_kkbajou>
             #  出走したレースの馬場状態を編集する。
             #  ばんえい競馬では編集しない。
             seiseki_params['ck_kkbajou'] = seiseki.ck_kkbajou

             # ７）－２－４ 馬場水分
             # <ck_kkbasui>３．４％</ck_kkbasui>
             #  出走したレースの馬場水分を編集する。
             #  ばんえい競馬のみ編集する。
             seiseki_params['ck_kkbasui'] = intToZen(seiseki.ck_kkbasui)

             # ７）－３ レース情報 < ck_kkrejouhou>・・・</ ck_kkrejouhou>で囲まれて表現される。
             # ７）－３－１ ナイター区分
             # <ck_kknaita>ナイター</ck_kknaita>
             #  ナイターを実施する場合に編集。
             seiseki_params['ck_kknaita'] = seiseki.ck_kknaita

             # ７）－３－２ 競走種別
             # <ck_kkshubetsu>サラ３歳上</ck_kkshubetsu>
             #  競走種別を編集。
             seiseki_params['ck_kkshubetsu'] = seiseki.ck_kkshubetsu

             # ７）－３－３ レース名称
             # <ck_kkrmei>伊勢菊特別競走</ck_kkrmei>
             #  レース名称を編集。
             seiseki_params['ck_kkrmei'] = seiseki.ck_kkrmei

             # ７）－３－４ 競走資格条件
             # <ck_kkshikaku>オープン</ck_kkshikaku>
             #  競走資格条件を編集。複数ある場合は繰り返して編集。
             seiseki_params['ck_kkshikaku'] = makelist(seiseki.ck_kkshikaku)

             # ７）－３－５ レース格
             # <ck_kkrkaku>３歳上</ck_kkrkaku>
             #  レース格を編集。複数ある場合は繰り返して編集。
             seiseki_params['ck_kkrkaku'] = makelist(seiseki.ck_kkrkaku)

             # ７）－３－５ レース組
             # <ck_kkrkumi>ロ</ck_kkrkumi>
             #  レース組を編集。複数ある場合は繰り返して編集。
             seiseki_params['ck_kkrkumi'] = makelist(seiseki.ck_kkrkumi)

             # ７）－３－６ グレード区分
             # <ck_kkguredo>G３</ck_kkguredo>
             #  グレード区分を編集。
             seiseki_params['ck_kkguredo'] = seiseki.ck_kkguredo

             # ７）－３－７ 競走距離
             # <ck_kkkyori>１４００</ck_kkkyori>
             #  競走距離を編集。
             seiseki_params['ck_kkkyori'] = intToZen(seiseki.ck_kkkyori)

             # ７）－３－８ トラック
             # <ck_kktorakku>ダート右・外コース</ck_kktorakku>
             #  トラック情報を編集。
             torakku = str(seiseki.ck_shibadat) + str(seiseki.ck_mawari)
             if seiseki.ck_naigai:
                 torakku = torakku + '・' + str(seiseki.ck_naigai)
             seiseki_params['ck_kktorakku'] = torakku

             # ７）－３－９ 出走頭数
             # 場によって提供される形式が違うため、提供された内容をそのまま編集
             # <ck_kkshusuu>１６</ck_kkshusuu>
             #  出走頭数を編集。
             seiseki_params['ck_kkshusuu'] = intToZen(seiseki.ck_kkshusuu)

             # ７）－４ 成績情報 < ck_kkumaseiseki>・・・</ck_kkumaseiseki>で囲まれて表現される。
             # ７）－４－１ 順位
             # <ck_kkjuni>３</ck_kkjuni>
             #  順位を編集。
             seiseki_params['ck_kkjuni'] = intToZen(seiseki.ck_kkjuni)

             # ７）－４－２ 入線順位
             # <ck_kknyujuni>３</ck_kknyujuni>
             #  入線順位を編集。
             seiseki_params['ck_kknyujuni'] = intToZen(seiseki.ck_kknyujuni)
             # ７）－４－３ 枠番
             # <ck_kkwaku>４</ck_kkwaku>
             #  枠番を編集。
             seiseki_params['ck_kkwaku'] = intToZen(seiseki.ck_kkwaku)

             # ７）－４－４ 馬番
             # <ck_kkuma>７</ck_kkuma>
             #  馬番を編集。
             seiseki_params['ck_kkuma'] = intToZen(seiseki.ck_kkuma)

             # ７）－４－５ 負担重量
             # <ck_kkfujuu>５５</ck_kkfujuu>
             #  負担重量を編集。
             #  ばんえい競馬は編集しない。
             seiseki_params['ck_kkfujuu'] = intToZen(seiseki.ck_kkfujuu)

             # ７）－４－６ 積載重量
             # <ck_kksekijuu>７５０</ck_kksekijuu>
             #  積載重量を編集。
             #  ばんえい競馬のみ編集。
             seiseki_params['ck_kksekijuu'] = intToZen(seiseki.ck_kksekijuu)

             # ７）－４－７ 減量記号
             # <ck_kkgenkigou>☆</ck_kkgenkigou>
             #  減量騎手が騎乗する場合、減量記号（△、▲、☆、★など）を編集。
             seiseki_params['ck_kkgenkigou'] = seiseki.ck_kkgenkigou

             # ７）－４－８ 騎手名
             # <ck_kkkimei>熊澤重</ck_kkkimei>
             #  騎手名（3 字）を編集。
             seiseki_params['ck_kkkimei'] = seiseki.ck_kkkimei

             # ７）－４－９ タイム
             # <ck_kktime>１分２８秒２</ck_kktime>
             #  タイムを『〇分〇秒〇』『〇秒〇』などの形式で編集。
             seiseki_params['ck_kktime'] = intToZen(
                 seiseki.ck_kktime)  # ★後で編集する

             # ７）－４－10 相手馬
             # <ck_kkaiteuma>ジェットセッター</ck_kkaiteuma>
             #  １着馬名を編集。該当馬が１着の場合は２着馬名を編集。
             seiseki_params['ck_kkaiteuma'] = seiseki.ck_kkaiteuma

             # ７）－４－11 タイム差
             # <ck_kktimesa>０秒３</ck_kktimesa>
             #  １着馬とのタイム差を編集。該当馬が１着の場合は２着馬とのタイム差を編集。
             #  『秒』を付けた形で編集する。
             seiseki_params['ck_kktimesa'] = intToZen(
                 seiseki.ck_kktimesa)  # ★後で編集する

             # ７）－４－12 事故種類
             # <ck_kkjikosyu>競走中止</ck_kkjikosyu>
             #  事故が発生した場合は、事故の種類を編集。
             seiseki_params['ck_kkjikosyu'] = seiseki.ck_kkjikosyu

             # ７）－４－13 事故理由
             # <ck_kkjikoriyuu>落馬</ck_kkjikoriyuu>
             #  事故が発生した場合は、事故の理由を編集。
             seiseki_params['ck_kkjikoriyuu'] = seiseki.ck_kkjikoriyuu

             # ７）－４－14 コーナー通過順位
             # <ck_kkkojuni>３－４－４－５</ck_kkkojuni>
             #  コーナー通過順位を「－」で区切って編集。
             seiseki_params['ck_kkkojuni'] = intToZen(
                 seiseki.ck_kkkojuni)  # ★後で編集する

             # ７）－４－15 上がり３ハロン
             # <ck_kka3ha>３９秒９</ck_kka3ha>
             # ３－15
             #  上がり３ハロンを編集。
             seiseki_params['ck_kka3ha'] = intToZen(
                 seiseki.ck_kka3ha)  # ★後で編集する

             # ７）－４－16 馬体重
             # <ck_kkbajuu>５０４</ck_kkbajuu>
             #  馬体重を編集。
             seiseki_params['ck_kkbajuu'] = intToZen(seiseki.ck_kkbajuu)

             # ７）－４－17 単勝人気
             # <ck_kktannin>５</ck_kktannin>
             #  単勝人気を編集
             seiseki_params['ck_kktannin'] = intToZen(seiseki.ck_kktannin)

             seiseki_params_list.append(seiseki_params.copy())

        shusssouba_params['seiseki_params_list'] = seiseki_params_list

        shusssouba_params_list.append(shusssouba_params.copy())

    params["shusssouba_params_list"] = (shusssouba_params_list)

    # xml形式で出力
    res = render(request, 'NewsML_temp/shussouhyou.xml', params)
    res['Content-Type'] = 'application/xml'
    return res

from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.decorators.http import require_POST

from .models import *
from .forms import *
from .add_views import *

import json
###●●●●●デバッグ用にログ出力を仮設定（正式なログ出力方法の判明後に削除すること）●●●●●
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(module)-18s %(funcName)-10s %(lineno)4s: %(message)s'
)  ###------------------------------


def index(request):
    params = nav_info(request)
    return render(request, 'app_sumo/index.html', params)


# 運用日設定画面
def SUMUDY01(request):
    # # 最初のレコードだけ抽出
    tran_system = Tran_Systemstatus.objects.first()
    ## init は初期値という意味で、更新をかけた後の状態維持に使用 ##
    init = {
        "torikumi_nichime": tran_system.TorikumiDate.Nichime_code,
        "match_nichime": tran_system.MatchDate.Nichime_code,
        "age_calcu_reference_date": tran_system.Age_calcu_reference_date.strftime("%Y-%m-%d"),
        "banzuke_date": tran_system.Banzuke_date.strftime("%Y-%m-%d"),
        "first_date": tran_system.First_date.strftime("%Y-%m-%d")
    }

    nichime = Mst_Nichime.objects.all()

    # formからのデータが送信された場合、request.method内にPOSTが存在する
    if request.method == "POST":
        t_obj = nichime.get(Nichime_code=int(request.POST["torikumi_nichime"]))
        m_obj = nichime.get(Nichime_code=int(request.POST["match_nichime"]))
        tran_system.Age_calcu_reference_date = request.POST["age_calcu_reference_date"]
        tran_system.TorikumiDate = t_obj
        tran_system.MatchDate = m_obj
        tran_system.save()

        # 初期値を再設定
        init["torikumi_nichime"] = tran_system.TorikumiDate.Nichime_code
        init["match_nichime"] = tran_system.MatchDate.Nichime_code
        init["age_calcu_reference_date"] = tran_system.Age_calcu_reference_date

    # ヘッダーの開催場所、取組日目、勝負日目の情報を取得し、mergeする
    nav = nav_info(request)
    d = {
        'init': init,
        'nichime': nichime,
    }
    d.update(nav)

    return render(request, 'app_sumo/SUMUDY01.html', d)


# 予想番付処理画面（階級を選択して次画面へ）
def SUMYOS01(request):
    return render(request, 'app_sumo/SUMYOS01.html')


# 予想番付処理画面
def SUMYOS02(request):
    return render(request, 'app_sumo/SUMYOS02.html')


# 番付処理画面（階級、入力方式、東西を選択）
def SUMBAN01(request):
    return render(request, 'app_sumo/SUMBAN01.html')


# 番付入力画面
def SUMBAN02(request):
    return render(request, 'app_sumo/SUMBAN02.html')


# 番付入力ＯＣＲ画面
def SUMBAN03(request):
    return render(request, 'app_sumo/SUMBAN03.html')


# 番付ＣＯＲ取り込み画面
def SUMBAN04(request):
    return render(request, 'app_sumo/SUMBAN04.html')


# 取組画面（階級、入力方式、東西を選択）
def SUMTOR01(request):
    return render(request, 'app_sumo/SUMTOR01.html')


# 取組入力画面
def SUMTOR02(request):
    return render(request, 'app_sumo/SUMTOR02.html')


# 取組入力ＯＣＲ画面
def SUMTOR03(request):
    return render(request, 'app_sumo/SUMTOR03.html')


# 取組ＣＯＲ取り込み画面
def SUMTOR04(request):
    return render(request, 'app_sumo/SUMTOR04.html')


# 勝負入力処理
def SUMSHO01(request):
    return render(request, 'app_sumo/SUMSHO01.html')


# 勝負入力画面
def SUMSHO02(request):
    return render(request, 'app_sumo/SUMSHO02.html')


# 優勝・三賞入力画面
def SUMYUS01(request):
    nav= nav_info(request)
    match_nichime_id = Tran_Systemstatus.objects.first().MatchDate
    yearmonth = Tran_Systemstatus.objects.first().Event_date
    posts = Tran_YushoSansho.objects.filter(Yearmonth=yearmonth, Nichime_code=match_nichime_id)  # 現在の勝負日目のみを抽出
    return render(request, 'app_sumo/SUMYUS01.html', {'posts': posts, **nav})


# 優勝・三賞入力画面（追加）
def SUMYUS01_create(request):
    nav= nav_info(request)
    initial_dict = {
        'Yearmonth': Tran_Systemstatus.objects.first().Event_date,
        'Nichime_code': Tran_Systemstatus.objects.first().MatchDate, # 取組日目でなく勝負日目でよいか？
    }
    if request.method == 'POST':
        form = Tran_YushoSanshoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('app_sumo:SUMYUS01')
    else:
        #form = Tran_YushoSanshoForm()
        form = Tran_YushoSanshoForm(initial=initial_dict)
    return render(request, 'app_sumo/SUMYUS01_create.html', {'form': form, **nav})


# 優勝・三賞入力画面（参照）
def SUMYUS01_view(request, pk):
    nav= nav_info(request)
    post = Tran_YushoSansho.objects.get(pk=pk)
    return render(request, 'app_sumo/SUMYUS01_view.html', {'post': post, **nav})


# 優勝・三賞入力画面（更新）
def SUMYUS01_update(request, pk):
    nav= nav_info(request)
    post = get_object_or_404(Tran_YushoSansho, pk=pk)
    if request.method == "POST":
        form = Tran_YushoSanshoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('app_sumo:SUMYUS01')
    else:
        form = Tran_YushoSanshoForm(instance=post)
    return render(request, 'app_sumo/SUMYUS01_update.html', {'form': form, 'post': post, **nav})


# 優勝・三賞入力画面（削除）
@require_POST
def SUMYUS01_delete(request, pk):
    post = get_object_or_404(Tran_YushoSansho, pk=pk)
    post.delete()
    return redirect('app_sumo:SUMYUS01')


# コンテンツ出力指示画面
def SUMOUT01(request):
    return render(request, 'app_sumo/SUMOUT01.html')


# 電文／データ出力
def SUMOUT02(request):
    group_name = ["番付", "取組", "勝負", "星取", "成績", "新規"]

    telegram_group = []
    init = {"Group_code": 1, "Input_status": 0, "NewsMLNo": "01"}
    nml = Mst_KindofNewsML.objects.all()

    if request.method == "POST":
        res = Output_NewsML().Create_NewsML(request)
        if "Input_status" in request.POST and request.POST["Input_status"] is "2":
            return res
        for key in init.keys():
            if key is "NewsMLNo":
                init[key] = request.POST[key]
            else:
                init[key] = int(request.POST[key])

    NewsMLNo_by_gcode = [[], [], [], [], [], []]
    code_list = nml.order_by("Group_code").values("Group_code").distinct()
    # NewsMLNo_by_gcode.append([])
    # for code in code_list:
    #     NewsMLNo_by_gcode.append([])

    for n in nml:
        dataset = {"NewsMLNo": n.NewsMLNo, "ContentName": n.ContentName}
        ngcode = int(n.Group_code)
        NewsMLNo_by_gcode[ngcode - 1].append(dataset)

    for code in code_list:
        ngcode = code["Group_code"]
        telegram_group.append({
            "Group_code": ngcode,
            "Group_name": group_name[int(ngcode) - 1],
            "group_data": json.dumps(NewsMLNo_by_gcode[int(ngcode) - 1], ensure_ascii=False)
        })

    telegram = nml.filter(Group_code=int(init["Group_code"]))

    d = {
        'init': init,
        'telegram_group': telegram_group,
        'NewsMLNo': telegram
    }
    d.update(nav_info(request))
    return render(request, 'app_sumo/SUMOUT02.html', d)


# 電文／データ強制出力
def SUMOUT03(request):
    return render(request, 'app_sumo/SUMOUT03.html')


# 状況表示
def SUMJKH01(request):
    return render(request, 'app_sumo/SUMJKH01.html')


# 状況表示画面
def SUMJKH02(request):
    return render(request, 'app_sumo/SUMJKH02.html')


# 付け出し処理
def SUMTKD01(request):
    return render(request, 'app_sumo/SUMTKD01.html')


# 付け出し処理画面
def SUMTKD02(request):
    return render(request, 'app_sumo/SUMTKD02.html')


# 階級上位力士
def SUMJOR01(request):
    nav= nav_info(request)
    match_nichime_id = Tran_Systemstatus.objects.first().MatchDate  # tran_system.MatchDate.Nichime_codeを使用すると１日ずれる！
    yearmonth = Tran_Systemstatus.objects.first().Event_date  # 開催年月YYYYMM
    tbl_top_class_rikishi = Tran_TopClassRikishi.objects.filter(Nichime_code=match_nichime_id)  # 現在の勝負日目のみを抽出
    for i in Mst_Class.objects.all():
        # 階級別にデータの有無をチェック
        rows = tbl_top_class_rikishi.filter(Class_code=i.Class_code)
        if len(rows) == 0:
            # データが未登録の場合に新規作成
            # ●●●●●勝数と敗数をNULLとしたが、前日データがある場合はコピーするという要望があったはず。要検討●●●●●
            tbl_top_class_rikishi.create(Class_code_id=i.Class_code, Nichime_code=match_nichime_id, Yearmonth=yearmonth)
        # デバッグ用。階級と日目の組み合わせで一意となるため、jの値は２以上にならないが、あえてループ処理としている
        # for j in rows:
        #    logging.info('  %s', j.Class_code)
        #    logging.info("  Nichime_code=%s, Nichime_code_id=%s", j.Nichime_code, j.Nichime_code_id)

    # 現在の勝負日目の階級別データを画面表示する
    dict = {
        'tbl_top_class_rikishi': tbl_top_class_rikishi.order_by('Class_code'),  # 階級順に表示させるためソート
        'range_of_wins_or_losses': ['', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # プルダウンメニュー用
    }

    # 画面で選択された値を保存
    if request.method == "POST":
        reqlist_ccid = request.POST.getlist('class_code_id')
        reqlist_wins = request.POST.getlist('win_count')
        reqlist_looses = request.POST.getlist('loss_count')
        # 階級別に勝数と敗数を保存
        for i in range(len(reqlist_ccid)):
            row = tbl_top_class_rikishi.get(Class_code_id=reqlist_ccid[i])
            row.WinCount = reqlist_wins[i] if reqlist_wins[i].isdigit() == True else None
            row.LossCount = reqlist_looses[i] if reqlist_looses[i].isdigit() == True else None
            row.save()

    return render(request, 'app_sumo/SUMJOR01.html', {**dict, **nav})


# 資料出力
def SUMSHI01(request):
    return render(request, 'app_sumo/SUMSHI01.html')


# NewsML修正画面
def SUMNEW01(request):
    return render(request, 'app_sumo/SUMNEW01.html')


# NewsML修正画面内容部
def SUMNEW02(request):
    return render(request, 'app_sumo/SUMNEW02.html')


# 力士マスタ
class Rikishilist(ListView):
    # セッションに検索フォームの値を渡す。
    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.getlist('status_chk'),
        ]
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)

    # セッションから検索フォームの値を取得して、検索フォームの初期値としてセットする。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        status_chk = []
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            # query = form_value[0]
            status_chk = form_value[0]
        default_data = {
            'status_chk': status_chk,  # ステータス
        }
        rikishilist_form = SearchRikishilistForm(initial=default_data)  # 検索フォーム
        context['rikishilist_form'] = rikishilist_form
        return context

    # セッションから取得した検索フォームの値に応じてクエリ発行を行う。
    def get_queryset(self):
        activeDuty = 'activeDuty'
        notActiveDuty = 'notActiveDuty'
        q_word = self.request.POST.get('query')
        checks_value = self.request.POST.getlist('status_chk')
        one = '1'
        two = '2'

        def cheks_filter(rikishilist, checks_value):

            if activeDuty in checks_value and notActiveDuty in checks_value:
                rikishilist = rikishilist.filter(Rikishi_attrib_class__gte=one)
            elif activeDuty in checks_value:
                rikishilist = rikishilist.filter(Rikishi_attrib_class=one)
            elif notActiveDuty in checks_value:
                rikishilist = rikishilist.filter(Rikishi_attrib_class__gte=two)
            return rikishilist

        if q_word:
            rikishilist = Mst_Rikishi.objects.filter(
                Q(Rikishi_name_kanji_official__icontains=q_word) | Q(Rikishi_name_kanji_official__icontains=q_word))
            rikishilist = cheks_filter(rikishilist, checks_value)

        else:
            rikishilist = Mst_Rikishi.objects.all()
            rikishilist = cheks_filter(rikishilist, checks_value)

        return rikishilist


# 力士マスタ作成処理
class RikishiCreateView(CreateView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('app_sumo:rikishi')


# 力士マスタ編集処理
class RikishiUpdateView(UpdateView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('app_sumo:rikishi')


# 力士マスタ削除処理
class RikishiDeleteView(DeleteView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('app_sumo:rikishi')


# def SUMMSM01_heya_form(request):
#    if request.method == "POST":
#        form = Mst_HeyaForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.author = request.user
#            post.pub_date = timezone.now()
#            post.save()
#            return redirect('SUMMSM01_heya_form')
#    else:
#        form = Mst_HeyaForm()
#    return render(request, 'app_sumo/SUMMSM01_heya_form.html', {'form': form})


# マスタテーブル保守画面の部屋マスタ（htmlで表示するパターン）
"""
def SUMMSM01_heya_html(request):
    d = {
        'heyalist': Mst_Heya.objects.all(),
    }

    return render(request, 'app_sumo/SUMMSM01_heya_html.html', d)
"""


# 年度・場所切替画面
# def SUMINT01(request):
#    systemstatus = Tran_Systemstatus.objects.get(id=1)
#    if request.method == "POST":
#        form = Tran_SystemstatusForm(request.POST, instance=systemstatus)
#        if form.is_valid():
#            form.save()
#            return redirect('app_sumo:SUMINT01')
#    else:
#        form = Tran_SystemstatusForm(instance=systemstatus)
#
#    return render(request, 'app_sumo/SUMINT01.html', {'form': form})
def SUMINT01(request):
    systemstatus = Tran_Systemstatus.objects.get(id=1)
    init = {
        'event_date': str(systemstatus.Event_date)[:4],
        'currentbasho': systemstatus.CurrentBasho.Basho_code,
        'first_date': systemstatus.First_date.strftime("%Y-%m-%d"),
        'banzuke_date': systemstatus.Banzuke_date.strftime("%Y-%m-%d"),
    }
    basho = Mst_Basho.objects.all()

    if request.method == "POST":
        year = str(request.POST.get('event_date'))
        basho_record = basho.get(Basho_code=int(request.POST["currentbasho"]))
        basho_month = str(basho_record.Basho_month).zfill(2)

        systemstatus.Event_date = year + basho_month
        systemstatus.CurrentBasho = basho.get(Basho_code=int(request.POST["currentbasho"]))
        systemstatus.First_date = request.POST.get('first_date')
        systemstatus.Banzuke_date = request.POST.get('banzuke_date')
        systemstatus.save()

        init["event_date"] = str(systemstatus.Event_date)[:4]
        init["currentbasho"] = systemstatus.CurrentBasho.Basho_code
        init["first_date"] = systemstatus.First_date
        init["banzuke_date"] = systemstatus.Banzuke_date

    c = {'basho': basho, 'init': init}
    c.update(nav_info(request))
    return render(request, 'app_sumo/SUMINT01.html', c)


# 優勝決定戦階級選択画面
def SUMUKS01(request):
    return render(request, 'app_sumo/SUMUKS01.html')


# 優勝決定戦入力画面
def SUMUKS02(request):
    return render(request, 'app_sumo/SUMUKS02.html')

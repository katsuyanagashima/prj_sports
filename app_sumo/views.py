from datetime import datetime
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import *
from .forms import *
from .add_views import *

import json

def index(request):
    params = nav_info(request)
    return render(request, 'app_sumo/index.html', params)

#運用日設定画面
def SUMUDY01(request):
    params = nav_info(request, 1)
    # nav = params[0]
    tran_system = params[1]

    # # 最初のレコードだけ抽出
    tran_system = Tran_Systemstatus.objects.first()
    # tran_system = Tran_Systemstatus.objects.select_related('TorikumiDate', 'MatchDate').first()
    # tran_system = Tran_Systemstatus.objects.prefetch_related("torikumi", "match")
    ## init は初期値という意味で、更新をかけた後の状態維持に使用 ##
    init = { 
        "torikumi_nichime":tran_system.TorikumiDate.Nichime_code, 
        "match_nichime":tran_system.MatchDate.Nichime_code, 
    }

    nichime = Mst_Nichime.objects.all()

    if request.method == "POST":
        # Foreign key にカラムを指定しない場合は、selectでobjectを登録する必要があるため、
        # models.pyの記述を見直す必要あり
        t_obj = nichime.get(Nichime_code = int(request.POST["torikumi_nichime"]))
        m_obj = nichime.get(Nichime_code = int(request.POST["match_nichime"]))
        tran_system.TorikumiDate = t_obj
        tran_system.MatchDate = m_obj
        # tran_system.TorikumiDate.Nichime_code = int(request.POST["torikumi_nichime"])
        # tran_system.MatchDate.Nichime_code = int(request.POST["match_nichime"])
        tran_system.save()

        init["torikumi_nichime"] = tran_system.TorikumiDate.Nichime_code
        init["match_nichime"] = tran_system.MatchDate.Nichime_code

    # DB登録前に画面が表示されてしまうので、改善しなければならない
    nav = nav_info(request)
    d = {
        'init': init,
        'nichime': nichime,
    }
    d.update(nav)
    
    return render(request, 'app_sumo/SUMUDY01.html', d)

#予想番付処理画面（階級を選択して次画面へ）
def SUMYOS01(request):
    return render(request, 'app_sumo/SUMYOS01.html')

#予想番付処理画面
def SUMYOS02(request):
    return render(request, 'app_sumo/SUMYOS02.html')

#番付処理画面（階級、入力方式、東西を選択）
def SUMBAN01(request):
    return render(request, 'app_sumo/SUMBAN01.html')

#番付入力画面
def SUMBAN02(request):
    return render(request, 'app_sumo/SUMBAN02.html')

#番付入力ＯＣＲ画面
def SUMBAN03(request):
    return render(request, 'app_sumo/SUMBAN03.html')

#番付ＣＯＲ取り込み画面
def SUMBAN04(request):
    return render(request, 'app_sumo/SUMBAN04.html')

#取組画面（階級、入力方式、東西を選択）
def SUMTOR01(request):
    return render(request, 'app_sumo/SUMTOR01.html')

#取組入力画面
def SUMTOR02(request):
    return render(request, 'app_sumo/SUMTOR02.html')

#取組入力ＯＣＲ画面
def SUMTOR03(request):
    return render(request, 'app_sumo/SUMTOR03.html')

#取組ＣＯＲ取り込み画面
def SUMTOR04(request):
    return render(request, 'app_sumo/SUMTOR04.html')

#勝負入力処理
def SUMSHO01(request):
    return render(request, 'app_sumo/SUMSHO01.html')

#勝負入力画面
def SUMSHO02(request):
    return render(request, 'app_sumo/SUMSHO02.html')

#優勝・三賞入力画面
def SUMYUS01(request):
    return render(request, 'app_sumo/SUMYUS01.html')

#コンテンツ出力指示画面
def SUMOUT01(request):
    return render(request, 'app_sumo/SUMOUT01.html')

#電文／データ出力
def SUMOUT02(request):
    group_name = ["番付","取組","勝負","星取","成績","新規"]
    
    telegram_group = []
    init = { "Group_code":1, "Input_status":0, "NewsMLNo":"01" }
    nml = Mst_KindofNewsML.objects.all()

    if request.method == "POST":
        res = output_NewsML(request)
        if "Input_status" in request.POST and request.POST["Input_status"] is "2":
            return res
        for key in init.keys():
            if key is "NewsMLNo":
                init[key] = request.POST[key]
            else:
                init[key] = int(request.POST[key])

    NewsMLNo_by_gcode = [[],[],[],[],[],[]]
    code_list = nml.order_by("Group_code").values("Group_code").distinct()
    # NewsMLNo_by_gcode.append([])
    # for code in code_list:
    #     NewsMLNo_by_gcode.append([])

    for n in nml:
        dataset = {"NewsMLNo":n.NewsMLNo, "ContentName":n.ContentName}
        ngcode = int(n.Group_code)
        NewsMLNo_by_gcode[ngcode-1].append(dataset)

    for code in code_list:
        ngcode = code["Group_code"]
        telegram_group.append({ 
            "Group_code": ngcode, 
            "Group_name": group_name[int(ngcode)-1],
            "group_data": json.dumps(NewsMLNo_by_gcode[int(ngcode)-1], ensure_ascii=False)
        })


    telegram = nml.filter(Group_code=int(init["Group_code"])) 

    d = {
        'init': init,
        'telegram_group': telegram_group,
        'NewsMLNo': telegram
    }
    d.update(nav_info(request))
    return render(request, 'app_sumo/SUMOUT02.html', d)
    
#電文／データ強制出力
def SUMOUT03(request):
    return render(request, 'app_sumo/SUMOUT03.html')

#状況表示
def SUMJKH01(request):
    return render(request, 'app_sumo/SUMJKH01.html')

#状況表示画面
def SUMJKH02(request):
    return render(request, 'app_sumo/SUMJKH02.html')

#付け出し処理
def SUMTKD01(request):
    return render(request, 'app_sumo/SUMTKD01.html')

#付け出し処理画面
def SUMTKD02(request):
    return render(request, 'app_sumo/SUMTKD02.html')

#階級上位力士
def SUMJOR01(request):
    params = nav_info(request)
    return render(request, 'app_sumo/SUMJOR01.html', params)

#資料出力
def SUMSHI01(request):
    return render(request, 'app_sumo/SUMSHI01.html')

#NewsML修正画面
def SUMNEW01(request):
    return render(request, 'app_sumo/SUMNEW01.html')

#NewsML修正画面内容部
def SUMNEW02(request):
    return render(request, 'app_sumo/SUMNEW02.html')

#力士マスタ
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
        rikishilist_form = SearchRikishilistForm(initial=default_data) # 検索フォーム
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
            rikishilist = Mst_Rikishi.objects.filter(Q(Rikishi_name_kanji_official__icontains=q_word) | Q(Rikishi_name_kanji_official__icontains=q_word))                
            rikishilist = cheks_filter(rikishilist, checks_value)

        else:
            rikishilist = Mst_Rikishi.objects.all()
            rikishilist = cheks_filter(rikishilist, checks_value)

        return rikishilist

#力士マスタ作成処理
class RikishiCreateView(CreateView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('rikishi')

#力士マスタ編集処理
class RikishiUpdateView(UpdateView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('rikishi')

#力士マスタ削除処理
class RikishiDeleteView(DeleteView):
    model = Mst_Rikishi
    form_class = Mst_RikishiForm
    success_url = reverse_lazy('rikishi')    

#def SUMMSM01_heya_form(request):
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


#マスタテーブル保守画面の部屋マスタ（htmlで表示するパターン）
def SUMMSM01_heya_html(request):
    d = {
            'heyalist': Mst_Heya.objects.all(),
        }

    return render(request, 'app_sumo/SUMMSM01_heya_html.html', d)  


#年度・場所切替画面
#def SUMINT01(request):
#   return render(request, 'app_sumo/SUMINT01.html')
#年度・場所切替画面
def SUMINT01(request):
    systemstatus = Tran_Systemstatus.objects.all()
    if request.method == "POST":
        systemstatus.delete()
#        initial_dict = {'Torikumi_nichime_code':'0', 'Shoubu_nichime_code':'0', 'Age_calcu_reference_date':'2000-01-01'}
#        form = Mst_Event_Form(request.POST, initial=initial_dict)
        form = Tran_SystemstatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SUMINT01')
    else:
        form = Tran_SystemstatusForm()

    return render(request, 'app_sumo/SUMINT01.html',{'form':form})

#優勝決定戦階級選択画面
def SUMUKS01(request):
    return render(request, 'app_sumo/SUMUKS01.html')
    
#優勝決定戦入力画面
def SUMUKS02(request):
    return render(request, 'app_sumo/SUMUKS02.html')
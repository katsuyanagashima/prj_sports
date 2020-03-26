from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime

from .models import *
from .forms import *
from .add_views import *

def index(request):
    params = nav_info(request)
    return render(request, 'app_sumo/index.html', params)

#運用日設定画面
def SUMUDY01(request):
    return render(request, 'app_sumo/SUMUDY01.html')

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

#取組処理画面（階級、入力方式、東西を選択）
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
    # selectboxの要素変更はjs側で制御します(予定)
    group_name = ["番付","取組","勝負","星取","成績","新規"]
    
    telegram_group = []
    init = { "telegram_kind":1, "Input_status":0, "telegram":1 }
    t = Mst_KindofNewsML.objects.all()

    if request.method == "POST":
        res = output_NewsML(request)
        if "Input_status" in request.POST and request.POST["Input_status"] in ["1","2"]:
            return res
        # for key in init.keys():
        #     init[key] = int(request.POST[key])
        # init = { "telegram_kind":request.POST[""], "Input_status":1, "telegram":1 }

    
    code_list = t.values("Group_code").distinct()
    for code in code_list:
        telegram_group.append({ "Group_code": code["Group_code"], "Group_name": group_name[int(code["Group_code"])-1]})

    telegram = t.filter(Group_code=init["telegram_kind"]) 

    d = {
        'init': init,
        'telegram_group': telegram_group,
        'telegram': telegram
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
    return render(request, 'app_sumo/SUMJOR01.html')

#資料出力
def SUMSHI01(request):
    return render(request, 'app_sumo/SUMSHI01.html')

#NewsML修正画面
def SUMNEW01(request):
    return render(request, 'app_sumo/SUMNEW01.html')

#NewsML修正画面内容部
def SUMNEW02(request):
    return render(request, 'app_sumo/SUMNEW02.html')

#マスタテーブル保守画面の部屋マスタ（Formで表示するパターン）
#def SUMMSM01_heya_form(request):
#    form = Mst_HeyaForm(request.POST)
#    return render(request, 'app_sumo/SUMMSM01_heya_form.html', {'form': form})    


def SUMMSM01_heya_form(request):
    if request.method == "POST":
        form = Mst_HeyaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('SUMMSM01_heya_form')
    else:
        form = Mst_HeyaForm()
    return render(request, 'app_sumo/SUMMSM01_heya_form.html', {'form': form})


#力士マスタメンテナンス画面
def SUMMST01(request):
    d = {
            'rikishilist': Mst_Rikishi.objects.all(),
        }
    return render(request, 'app_sumo/SUMMST01.html', d)

#力士マスタメンテナンス画面（追加）
def SUMMST01_add(request, id):
    return HttpResponse("You're looking at question %s." % id)


#マスタテーブル保守画面の部屋マスタ（htmlで表示するパターン）
def SUMMSM01_heya_html(request):
    d = {
            'heyalist': Mst_Heya.objects.all(),
        }

    return render(request, 'app_sumo/SUMMSM01_heya_html.html', d)  


#年度・場所切替画面
def SUMINT01(request):
    return render(request, 'app_sumo/SUMINT01.html')
    
#優勝決定戦階級選択画面
def SUMUKS01(request):
    return render(request, 'app_sumo/SUMUKS01.html')
    
#優勝決定戦入力画面
def SUMUKS02(request):
    return render(request, 'app_sumo/SUMUKS02.html')
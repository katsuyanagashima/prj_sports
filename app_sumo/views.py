from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime

from .models import *
from .forms import *

def index(request):
    # data = Tran_Systemstatus.objects.all()
    # params = {
    #     'basho':data[0].CurrentBasho,
    #     'systatus':data[0].SystemStatus,
    #     'torikumiday':data[0].TorikumiDate,
    #     'shoubuday':data[0].MatchDate
    # }
    # return render(request, 'app_sumo/index.html', params)
    return render(request, 'app_sumo/index.html')


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

#コンテンツ編集指示
def SUMOUT01(request):
    return render(request, 'app_sumo/SUMOUT01.html')

#電文／データ出力
def SUMOUT02(request):
    d = {
        'list': Mst_KindofNewsML.objects.all(),
        }
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



#マスタテーブル保守画面の部屋マスタ（htmlで表示するパターン）
def SUMMSM01_heya_html(request):
    d = {
            'heyalist': Mst_Heya.objects.all(),
        }

    return render(request, 'app_sumo/SUMMSM01_heya_html.html', d)  
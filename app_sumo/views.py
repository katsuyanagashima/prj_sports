from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime

from .models import Match, Eventinfo
from .forms import MatchForm

from .models import PostCsv

import csv
from io import TextIOWrapper, StringIO

def index(request):
     return render(request, 'app_sumo/index.html')

def sample(request):
    return render(request, 'app_sumo/sample.html')

def xmlout1(request):
    p = {}
    p['status'] = 1
    p['msg'] = 'Success'
    t = loader.get_template('app_sumo/os1.xml')
    context = {'data':p}
    return HttpResponse(t.render(context), content_type='text/xml; charset=utf-8')

def xmlout14(request):
    p = {}
    p['status'] = 1
    p['msg'] = 'Success'
    t = loader.get_template('app_sumo/os14.xml')
    context = {'data':p}
    return HttpResponse(t.render(context), content_type='text/xml; charset=utf-8')

def xmlout_14(request):
    latest_match_list = Match.objects.all().order_by('-pub_date')
    taikai_list = Eventinfo.objects.all()   
    context = {
        'latest_match_list': latest_match_list,
        'taikai_list': taikai_list,
    }
    t = loader.get_template('app_sumo/os14.xml')
    return HttpResponse(t.render(context), content_type='text/xml; charset=utf-8')

def input14(request):
    d = {
        'matchlist': Match.objects.all(),
    }
    return render(request, 'app_sumo/input14.html', d)

def update14(request):
    d = {
        'matchlist': Match.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date'),
    }
    return render(request, 'app_sumo/update14.html', d)

def update14_new(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('update14')
    else:
        form = MatchForm()
    return render(request, 'app_sumo/update14_edit.html', {'form': form})
    
 #   if request.method == 'POST':
 #       if 'button_1' in request.POST:
 #           # ボタン1がクリックされた場合の処理
 #           xmlout_14()
 #       elif 'button_2' in request.POST:
 #           # ボタン2がクリックされた場合の処理
 #           input14(request)

def upload(request):
    if 'csv' in request.FILES:
        form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
        csv_file = csv.reader(form_data)
        for line in csv_file:
            postcsv, created = PostCsv.objects.get_or_create(player_name=line[1])
            postcsv.player_name = line[0]
            postcsv.player_name_formal = line[1]
            postcsv.player_name_formal3 = line[2]
            postcsv.player_name_yomi = line[3]
            postcsv.save()

        return render(request, 'app_sumo/upload.html')

    else:
        return render(request, 'app_sumo/upload.html')

#業務運用メニュー
#def SUMUNY01(request):
#    return render(request, 'app_sumo/SUMUNY01.html')

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
    return render(request, 'app_sumo/SUMOUT02.html')
    
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
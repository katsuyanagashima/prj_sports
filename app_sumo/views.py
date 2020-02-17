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
def SUMUNY01(request):
    return render(request, 'app_sumo/SUMUNY01.html')

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


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from django.views.generic import ListView
from .models import *
from . import forms
from .models import Tran_Systemstatus
import re


# メイン画面
def index(request):
     # json形式のダミーデータを取得
     import os
     import json
     module_dir = os.path.dirname(__file__) # views.pyのあるディレクトリを取得
     json_path = os.path.join(module_dir, 'dammydata.json')
     f = open(json_path, 'r')
     dammydata = json.load(f)

     # システム状態を取得
     tran_system = Tran_Systemstatus.objects.all().first() # ★ システム状態の1件目を見てるだけなので、ここは要検討
     status = str(tran_system.SystemStatus)

     # パラメータに追加
     params = {'status': status, 'data': dammydata, 'unyobi': tran_system.Unyou_date}

     # statusが0（通常業務モード）ではないとき、マスタ編集画面を表示。ステータスと各データと運用日に加えて、マスタのテーブル情報をparamにつめる
     if status != '0':
          joulist = Mst_Jou.objects.all() # マスタ初期画面
          if status == '10': # 通常配信先マスタ編集画面
               joulist = Mst_Haishin.objects.all()
          elif status == '11': # 期間限定配信先マスタ編集画面
               joulist = Mst_Haishin_gentei.objects.all()
          elif status == '12': # 配信社マスタ編集画面
               joulist = Mst_Company.objects.all()
          elif status == '13': # プリンタ出力先マスタ編集画面
               joulist = Mst_Printer.objects.all()
          elif status == '20': # 開催日割編集画面
               joulist = Mst_Kaisai_Hiwari.objects.all()
          elif status == '21': # 本日施行情報編集画面
               joulist = Mst_Honjitu_Shikou.objects.all()
          elif status == '30': # 競馬場マスタ編集画面
               joulist = Mst_Jou.objects.all()
          elif status == '31': # グレードマスタ編集画面
               joulist = Mst_Grade.objects.all()
          elif status == '32': # 品種年齢区分マスタ編集画面
               joulist = Mst_Breed_age.objects.all()
          elif status == '33': # 天候マスタ編集画面
               joulist = Mst_Weather.objects.all()

          # マスタ名を取得
          title = joulist.model._meta.verbose_name_plural.title() # メタ情報から取り出す

          # テーブルのヘッダーを取得
          table_header_meta_data = joulist.model._meta.get_fields()  # メタ情報を取り出す
          table_header_name = []
          for th in table_header_meta_data:
               if str(th).startswith('app_ckeiba'):  # メタ情報から、外部キー情報は取り除く（一度str化して無理やり判別してる）
                    table_header_name.append(th.verbose_name)  # メタ情報からverbose_nameを取り出して配列に格納

          # テーブルの値を取得
          table_value = []
          for obj in joulist.values():
               table_value.append(obj.values())
          
          params = {'status': status,
                    'data': dammydata,
                    'unyobi': tran_system.Unyou_date,
                    'title': title,
                    'table_header_name': table_header_name,
                    'object_list': joulist,
                    'table_value': table_value
                    }
     
     # メイン画面をレンダリング
     return render(request, 'app_ckeiba/index.html', params)

#マスタ編集画面にリダイレクト
def Change_To_Master_Edit_Mode(request):
     tran_system2 = Tran_Systemstatus.objects.all().first() # ★ 
     opemode = Mst_Operationmode.objects.filter(Operationmode_code = '1')[0] #SystemStatus:1 （マスタ編集モード）
     
     # ここでステータスをマスタ編集中に変更
     Tran_Systemstatus.setState(tran_system2, opemode)
     return redirect('../')

# 通常業務にリダイレクト
def Change_To_Nomal_Mode(request):
     tran_system2 = Tran_Systemstatus.objects.all().first() # ★ 
     opemode = Mst_Operationmode.objects.filter(Operationmode_code = '0')[0] #SystemStatus:0 （通常業務モード）
     
     # ここでステータスを通常業務に変更
     Tran_Systemstatus.setState(tran_system2, opemode)
     return redirect('../')

     
# マスタ編集画面にリダイレクト
def Edit_Mst(request, mst_num):
     tran_system2 = Tran_Systemstatus.objects.all().first() # ★ 
     opemode = Mst_Operationmode.objects.filter(Operationmode_code=mst_num)[0]
     
     # ステータスを各マスタの編集中に変更
     Tran_Systemstatus.setState(tran_system2, opemode)
     return redirect('../')

# 更新ボタン押下時
def editbutton(request, values):
     return render(request, '../admin/app_ckeiba/mst_haishin/edit_num/change/')




# オプション送信画面
def option_submit(request):
     # json形式のダミーデータを取得
     import os
     import json
     module_dir = os.path.dirname(__file__) # views.pyのあるディレクトリを取得
     json_path = os.path.join(module_dir, 'dammydata.json')
     f = open(json_path, 'r')
     dammydata = json.load(f)

     # システム状態を取得
     tran_system = Tran_Systemstatus.objects.all().first()
     status = str(tran_system.SystemStatus)


     selected_haishinsha = []
     mst_haishin = []
     joubetsu_filelists = {}
     filelists = []
     submittype = ""

     if request.method == 'POST':
          if 'sentaku' in request.POST:
               # 選択ボタンがクリックされた場合の処理

               # チェック項目を取得
               chklist = []
               chklist = request.POST.getlist('chk', '')

               # チェック項目を整形する
               for filename in chklist:
                    filedetails = {}
                    filenames = filename.split(",")
                    filedetails['jou'] = filenames[0]
                    filedetails['joucode'] = filenames[1]
                    filedetails['race'] = filenames[2]
                    filedetails['fname'] = filenames[3]
                    filedetails['fnamecode'] = filenames[4]
                    filedetails['val'] = filenames[5]

                    filelists.append(filedetails) #いらないかも
                    jouname = filedetails['jou']

                    if joubetsu_filelists.get(jouname):
                         joubetsu_filelists[jouname].append(filedetails)
                    else:
                         joubetsu_filelists[jouname] = []
                         joubetsu_filelists[jouname].append(filedetails)
               
               # 場別選択ファイルリストをセッションに登録
               request.session['filelists'] = filelists

               # 配信社一覧を取得
               mst_haishin = Mst_Company.objects.all()

          elif 'soushin' in request.POST:
               # 送信ボタンがクリックされた場合の処理

               # 選択された送信種別と配信社を取得
               submittype = request.POST.get('submittype', '')
               selected_haishinsha = request.POST.getlist('haishinsha', '')

               # セッションに登録しておいた場別選択ファイルリストを読み込む
               joubetsu_filelists = request.session['filelists'] 
               filelists = request.session['filelists']
               




     # パラメータに追加
     params = {
          'status': status,
          'data': dammydata,
          'unyobi': tran_system.Unyou_date,

          'joubetsu': joubetsu_filelists,
          'filelists' : filelists,
          'mst_haishin': mst_haishin,
          
          'submittype': submittype,
          'selected_haishinsha':selected_haishinsha
     }
     return render(request, 'app_ckeiba/option_submit.html', params)
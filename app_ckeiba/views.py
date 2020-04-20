from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy
from django import forms
from .models import *
from .forms import *
from . import forms
from . import models
from .models import Tran_Systemstatus
import re
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

#CSV取り込み用に追加したviewをインポート
from .views_csv import *


# メイン画面
def index(request):
     # json形式のダミーデータを取得
     import os
     import json
     module_dir = os.path.dirname(__file__) # views.pyのあるディレクトリを取得
     json_path = os.path.join(module_dir, 'dammydata.json')
     f = open(json_path, 'r')
     dammydata = json.load(f)

     # ＜↑のダミーデータをマスタベースの正しい設計にするためにこれからやること＞
     # １．競馬場マスタから競馬場の一覧を取得
     # ２．運用日当日の開催場を、開催日割から取得
     # ３．【受信】受信状況テーブルから、受信状況を取得
     # ４．【編集】中間DB？中間DB管理テーブル？テンプレートの管理テーブル？から、各中間DBへの格納状況を取得
     # ５．【送信】送信管理テーブル？から、新聞配信への送信状況を取得
     # ６．これらの取得済みデータをパラメータ化して渡す。

     # システム状態を取得
     tran_system = Tran_Systemstatus.objects.all().first() # ★ システム状態の1件目のレコードを見てる
     status = str(tran_system.Operationmode)

     # パラメータに追加
     params = {'status': status, 'data': dammydata, 'unyobi': tran_system.Unyou_date}

     # statusがオンラインではないとき、マスタ編集画面を表示。ステータスと各データと運用日に加えて、マスタのテーブル情報をparamにつめる
     if status == 'マスタ編集中':

          joulist = Mst_Jou.objects.all()  # マスタ初期画面（競馬場マスタ）
          mst_num = '30' # マスタ初期画面（競馬場マスタ）

          if 'mst_num' in request.session:

               # セッション情報から編集マスタを選ぶ
               mst_num = str(request.session['mst_num'])

               if mst_num == '10': # 通常配信先マスタ編集画面
                    joulist = Mst_Haishinsaki_Nomal.objects.all()
               elif mst_num == '11': # 期間限定配信先マスタ編集画面
                    joulist = Mst_Haishinsaki_Limited.objects.all()
               elif mst_num == '12': # 配信社マスタ編集画面
                    joulist = Mst_Haishinsha.objects.all()
               elif mst_num == '13': # プリンタ出力先マスタ編集画面
                    joulist = Mst_Printer.objects.all()
               elif mst_num == '20': # 開催日割編集画面
                    joulist = Mst_Kaisai_Hiwari.objects.all()
               elif mst_num == '21': # 本日施行情報編集画面
                    joulist = Mst_Honjitu_Shikou.objects.all()
               elif mst_num == '30': # 競馬場マスタ編集画面
                    joulist = Mst_Jou.objects.all()
               elif mst_num == '31': # グレードマスタ編集画面
                    joulist = Mst_Grade.objects.all()
               elif mst_num == '32': # 品種年齢区分マスタ編集画面
                    joulist = Mst_Breed_age.objects.all()
               elif mst_num == '33': # 天候マスタ編集画面
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

#マスタ編集にリダイレクト　
def Change_To_Master_Edit_Mode(request):
     tran_system2 = Tran_Systemstatus.objects.all().first() # ★ 
     opemode = Mst_Operationmode.objects.filter(Operationmode_code='3')[0]  #SystemStatus:3 （マスタ編集）
     
     # ここでステータスをオフラインに変更
     Tran_Systemstatus.setState(tran_system2, opemode)
     return redirect('../')

# オンラインにリダイレクト
def Change_To_Nomal_Mode(request):
     tran_system2 = Tran_Systemstatus.objects.all().first() # ★ 
     opemode = Mst_Operationmode.objects.filter(Operationmode_code = '0')[0] #SystemStatus:0 （オンライン）
     # セッション情報をクリア
     request.session.clear()

     # ここでステータスを通常業務に変更
     Tran_Systemstatus.setState(tran_system2, opemode)
     return redirect('../')

     
# 編集マスタの番号をセッションに詰めてマスタ編集画面にリダイレクト
def Edit_Mst(request, mst_num):
     # セッション情報をクリア
     request.session.clear()

     # 編集マスタの番号をセッションに登録
     request.session['mst_num'] = mst_num
     
     return redirect('../')



# ★★★マスタ編集フォーム★★★
# 【関数ベース】作成フォーム紐付け機能
def create_forms(request, title):

     # マスタ名(title)から、ModelとModelFormを取得
     Model_and_ModelForm = get_Model_and_ModelForm(title)
     Mst_ModelForm = Model_and_ModelForm[1]

     if request.method == 'POST':
          # 作成ボタン押下時
          form = Mst_ModelForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('app_ckeiba:index')
     else:
          # GETリクエスト（更新画面の初期表示）時はFormを表示
          form = Mst_ModelForm()

     d = {'form': form,'title':title}
     return render(request, 'app_ckeiba/mst_edit_form/mst_create.html', d)

# 【関数ベース】更新フォーム紐付け機能
def update_forms(request, pk, title):

     # マスタ名(title)から、ModelとModelFormを取得
     Model_and_ModelForm = get_Model_and_ModelForm(title)
     Mst_Model = Model_and_ModelForm[0]
     Mst_ModelForm = Model_and_ModelForm[1]


     mst_instance = get_object_or_404(Mst_Model, id=pk)
     if request.method == 'POST':
          # 更新ボタン押下時
          form = Mst_ModelForm(request.POST, instance=mst_instance)
          if form.is_valid():
               form.save()
               return redirect('app_ckeiba:index')
     else:
          # GETリクエスト（更新画面の初期表示）時はDBに保存されているデータをFormに結びつける
          form = Mst_ModelForm(instance=mst_instance)

     d = {'form': form,'title':title}
     return render(request, 'app_ckeiba/mst_edit_form/mst_update.html', d)

# 【関数ベース】削除フォーム紐付け機能
def delete_forms(request, pk, title):

     # マスタ名(title)から、ModelとModelFormを取得
     Model_and_ModelForm = get_Model_and_ModelForm(title)
     Mst_Model = Model_and_ModelForm[0]
     Mst_ModelForm = Model_and_ModelForm[1]


     mst_instance = get_object_or_404(Mst_Model, id=pk)
     if request.method == 'POST':
          # 削除ボタン押下時
          mst_instance.delete()
          return redirect('app_ckeiba:index')
     else:
          # GETリクエスト（更新画面の初期表示）時はDBに保存されているデータをFormに結びつける
          form = Mst_ModelForm(instance=mst_instance)

     d = {'form': form,'title':title}
     return render(request, 'app_ckeiba/mst_edit_form/mst_delete.html', d)


# マスタ名から、ModelとModelFormを返す関数
def get_Model_and_ModelForm(mst_name):
     if mst_name == '競馬場マスタ':
          Mst_Model = Mst_Jou
          Mst_ModelForm = Mst_JouForm
     elif mst_name == '【配信系】配信社マスタ':
          Mst_Model = Mst_Haishinsha
          Mst_ModelForm = Mst_HaishinshaForm
     elif mst_name == '【配信系】通常配信先マスタ':
          Mst_Model = Mst_Haishinsaki_Nomal
          Mst_ModelForm = Mst_Haishinsaki_NomalForm
     elif mst_name == '【配信系】期間限定配信先マスタ':
          Mst_Model = Mst_Haishinsaki_Limited
          Mst_ModelForm = Mst_Haishinsaki_LimitedForm
     elif mst_name == '【配信系】プリンタ出力先マスタ':
          Mst_Model = Mst_Printer
          Mst_ModelForm = Mst_PrinterForm
     elif mst_name == '【スケジュール系】開催日割':
          Mst_Model = Mst_Kaisai_Hiwari
          Mst_ModelForm = Mst_Kaisai_HiwariForm
     elif mst_name == '【スケジュール系】本日施行情報':
          Mst_Model = Mst_Honjitu_Shikou
          Mst_ModelForm = Mst_Honjitu_ShikouForm
     elif mst_name == 'グレードマスタ':
          Mst_Model = Mst_Grade
          Mst_ModelForm = Mst_GradeForm
     elif mst_name == '品種年齢区分マスタ':
          Mst_Model = Mst_Breed_age
          Mst_ModelForm = Mst_Breed_ageForm
     elif mst_name == '天候マスタ':
          Mst_Model = Mst_Weather
          Mst_ModelForm = Mst_WeatherForm

     return Mst_Model, Mst_ModelForm


# 【classベースで実装】競馬場マスタ更新フォーム紐付け　→汎用性がないので通常マスタ更新では使わない
# class JouCreateView(CreateView):
#      template_name = 'app_ckeiba/mst_edit_form/mst_create.html'

#      def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context['title'] = self.kwargs.get('title')
#           return context

#      model = Mst_Jou
#      form_class = Mst_JouForm
#      success_url = reverse_lazy('app_ckeiba:index')
     
# class JouUpdateView(UpdateView):
#      template_name = 'app_ckeiba/mst_edit_form/mst_update.html'

         
#      def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context['title'] = self.kwargs.get('title')
#           return context

#      model = Mst_Jou
#      form_class = Mst_JouForm
#      success_url = reverse_lazy('app_ckeiba:index')

# class JouDeleteView(DeleteView):
#      template_name = 'app_ckeiba/mst_edit_form/mst_delete.html'

         
#      def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context['title'] = self.kwargs.get('title')
#           return context

#      model = Mst_Jou
#      form_class = Mst_JouForm

#      success_url = reverse_lazy('app_ckeiba:index')


# ★★★マスタ編集フォームここまで★★★


# ◎◎◎中間DBフォーム◎◎◎
     
# class Md_ShussouhyouUpdateView(UpdateView):
#      template_name = 'app_ckeiba/mst_edit_form/md_db_update.html'
#      model = Md_Shussouhyou
#      slug_field = 'year', 'month', 'day', 'joucode', 'race'
#      slug_url_kwarg = 'year', 'month', 'day', 'joucode', 'race'
         
#      def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context['title'] = "【中間DB】出走表"
#           return context

#      def get_object(self, queryset=None):
#           return Md_Shussouhyou.objects.filter(ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)[0]

#      # def get_queryset(self):
#      #      return super().get_queryset().select_related('shussouba1')

#      # fields = ('shussouba1',)
#      form_class = Md_ShussouhyouForm
#      success_url = reverse_lazy('app_ckeiba:index')

# 【関数ベース】中間DBフォーム
def md_update_forms(request, year, month, day, joucode, race):

     # URLから、更新対象のレコードを抽出（データがなければ404エラー）
     path = request.path
     if "shussouhyou" in path:
          mst_instance = get_object_or_404(Md_Shussouhyou.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)
          Md_ModelForm = Md_ShussouhyouForm
          title = "【中間DB】出走表"
          
     elif "seiseki" in path:
          mst_instance = get_object_or_404(Md_Seiseki_Haraimodoshi.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)
          Md_ModelForm = Md_Seiseki_HaraimodoshiForm
          title = "【中間DB】成績・払戻"

     elif "corner_rap" in path:
          mst_instance = get_object_or_404(Md_Corner_Rap.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)
          Md_ModelForm = Md_Corner_RapForm
          title = "【中間DB】コーナー・ラップ"
          
     elif "agari" in path:
          mst_instance = get_object_or_404(Md_Agari.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)
          Md_ModelForm = Md_AgariForm
          title = "【中間DB】上がり"
          
     elif "tushinbun" in path:
          mst_instance = get_object_or_404(Md_Tshuushinbun.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode, rebangou=race)
          Md_ModelForm = Md_TshuushinbunForm
          title = "【中間DB】通信文"
          
     elif "nyujo" in path:
          mst_instance = get_object_or_404(Md_Nyujo.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode)
          Md_ModelForm = Md_NyujoForm
          title = "【中間DB】入場人員"
          
     elif "uriage" in path:
          mst_instance = get_object_or_404(Md_Uriagekin.objects, ck_kyounen=year, ck_kyoutuki=month, ck_kyouhi=day, joumei=joucode)
          Md_ModelForm = Md_UriagekinForm
          title = "【中間DB】売上金"

     else:
          pass
          

     if request.method == 'POST':
          # 更新ボタン押下時
          form = Md_ModelForm(request.POST, instance=mst_instance)
          if form.is_valid():
               form.save()
               return redirect('app_ckeiba:index')
     else:
          # GETリクエスト（更新画面の初期表示）時はDBに保存されているデータをFormに結びつける
          form = Md_ModelForm(instance=mst_instance)

     d = {'form': form,'title': title}
     return render(request, 'app_ckeiba/mst_edit_form/md_db_update.html', d)


# ◎◎◎中間DBフォームここまで◎◎◎








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
     status = str(tran_system.Operationmode)


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
               mst_haishin = Mst_Haishinsha.objects.all()

          elif 'soushin' in request.POST:
               # 送信ボタンがクリックされた場合の処理

               # 選択された送信種別と配信社を取得
               submittype = request.POST.get('submittype', '')
               selected_haishinsha = request.POST.getlist('haishinsha', '')

               # セッションに登録しておいた場別選択ファイルリストを読み込む
               joubetsu_filelists = request.session['filelists'] 
               filelists = request.session['filelists']
               
               # 一応ここでセッションの内容をクリアする（ 送信処理をつくったら、送信処理が完了したらクリアにする）
               # 今のままだと送信したあと戻ると落ちる
               request.session.clear()



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
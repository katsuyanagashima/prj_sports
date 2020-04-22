from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from .models import *

from datetime import datetime

temp = [
    'YYYYMMDDOSF01__________01','YYYYMMDDOSF02__________01','YYYYMMDDOSF03__________01','YYYYMMDDOSF04____CC____01','YYYYMMDDOSF05__BB__D___01',
    'YYYYMMDDOSF06AA__CC____01','YYYYMMDDOSF07AA__CC____01','YYYYMMDDOSF08AA________01','YYYYMMDDOSF09AA________01',
    'YYYYMMDDOSF10AABBCC____01','YYYYMMDDOSF11AA__CC____01','YYYYMMDDOSF12AABB______01','YYYYMMDDOSF13AA_____EEE01','YYYYMMDDOSF14AA________01','YYYYMMDDOSF15AA__CC____01',
    'YYYYMMDDOSF16AA________01','YYYYMMDDOSF17AA________01','YYYYMMDDOSF18AABB______01',
    '','YYYYMMDDOSF20AABB__D___01','YYYYMMDDOSF21AA________01','YYYYMMDDOSF22AA________01',
    'YYYYMMDDOSF23AABB______01'
]

def nav_info(request, get_type=0):
    tran_system = Tran_Systemstatus.objects.all().first()

    params = {
            'nav':{
            'basho':tran_system.CurrentBasho,
            'systatus':tran_system.SystemStatus,
            'torikumiday':tran_system.TorikumiDate.Nichime_name,
            'shoubuday':tran_system.MatchDate.Nichime_name
            } 
        }
    if get_type:
        return [params, tran_system]
    else:
        return params

def output_NewsML(request):
    grade = 0 # 階級コード
    now = datetime.now()
    stnow = now.strftime("%Y%m%d")

    if request.method == "POST":
        if "NewsMLNo" not in request.POST:
            return "Input error."
        newsno = request.POST["NewsMLNo"] # NEWSML種別コードを受け取る
        if newsno.startswith("0"):
            newsno.lstrip("0")
        if not newsno.isdigit(): # 全ての文字が数値でない場合、末尾2文字を抽出・削除
            grade = newsno[-2]
            newsno = newsno[:-2]
        temp_product_id = temp[int(newsno)-1] # NEWSML種別コードに対応するtemplateIDを取得
        file_name = '%s.xml' % temp_product_id  # テンプレートのファイル名
        temp_file_name = 'NewsML_temp/%s' % file_name
        t = loader.get_template(temp_file_name) # Djangoのテンプレートとして取得
    # context = {
    #     'latest_match_list': latest_match_list,
    #     'taikai_list': taikai_list,
    # }
    # newsmlmetaから現在の場所と取得して、テンプレートに渡す
    # 力士マスタ、生涯成績マスタから現在の値を取得して、テンプレートに渡す
    # （現状は体重等が力士マスタになっているのでそうなるが、力士マスタは全ての力士を蓄積しているので、番付だけのトランザクションテーブルに移動させて方が良いかも）
    #生涯成績
        if newsno == "01":
            context = {
                'newsmlmeta':Tran_Systemstatus.objects.all(),               #システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="01") ,  #副ヘッダマスタ
                'Banzuke_forecast': Tran_Banzuke_forecast.objects.all(),    #予想番付マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),            #生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),              #生涯受賞マスタ
            }
        elif newsno == "02":
            context = {
                'newsmlmeta':Tran_Systemstatus.objects.all(),       #システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="03") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),              #番付明細マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),    #生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),      #生涯受賞マスタ
            }
        elif newsno == "03":
            context = {
                'newsmlmeta':Tran_Systemstatus.objects.all(),       #システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="03") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),              #番付明細マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),    #生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),      #生涯受賞マスタ
            }
        elif newsno == "06":
            context = {
                'newsmlmeta':Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho':tran_system.CurrentBasho,
                'torikuminichime':tran_system.TorikumiDate.Nichime_4char,
            }                    

        if "Input_status" in request.POST:
            st = request.POST["Input_status"] # パラメータ 0=編集、1=配信、2=プレビュー、3=印刷
            if st in ["0","1"]: # 編集か配信であれば、NewsMLをファイルに出力
                content = loader.render_to_string(temp_file_name, context)
                # file名は運用日付、パラメータに合わせて変更
                newfile_name = file_name.replace("YYYYMMDD", stnow)
                if grade:
                    newfile_name.replace('BB', grade)
                with open('app_sumo/output/hold/%s' % newfile_name,'w') as static_file:
                    static_file.write(content)
        
            elif st == "2": # プレビューであれば、UTF-16に変換し表示
                return HttpResponse(t.render(context), content_type='text/xml; charset=utf-16')


# def xmlout_14(request):
#     latest_match_list = Match.objects.all().order_by('-pub_date')
#     taikai_list = Eventinfo.objects.all()   
#     context = {
#         'latest_match_list': latest_match_list,
#         'taikai_list': taikai_list,
#     }
#     t = loader.get_template('app_sumo/os14.xml')
#     return HttpResponse(t.render(context), content_type='text/xml; charset=utf-8')

# def xmlout_14(request):
#     response = HttpResponse(content_type='text/xml; charset=utf-8')
#     response['Content-Disposition'] =  'attachment; filename=test.xml'

#     latest_match_list = Match.objects.all().order_by('-pub_date')
#     taikai_list = Eventinfo.objects.all()
#     t = loader.get_template('app_sumo/os14.xml')
#     context = {
#         'latest_match_list': latest_match_list,
#         'taikai_list': taikai_list,
#     }

#     response.write(t.render(context))
#     return response

# def input14(request):
#     d = {
#         'matchlist': Match.objects.all(),
#     }
#     return render(request, 'app_sumo/input14.html', d)

# def update14(request):
#     d = {
#         'matchlist': Match.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date'),
#     }
#     return render(request, 'app_sumo/update14.html', d)

# def update14_new(request):
#     if request.method == "POST":
#         form = MatchForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('update14')
#     else:
#         form = MatchForm()
#     return render(request, 'app_sumo/update14_edit.html', {'form': form})
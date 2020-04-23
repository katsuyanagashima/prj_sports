from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from .models import *

from datetime import datetime

temp = [
    'YYYYMMDDOSF01__________01', 'YYYYMMDDOSF02__________01', 'YYYYMMDDOSF03__________01', 'YYYYMMDDOSF04____CC____01', 'YYYYMMDDOSF05__BB__D___01',
    'YYYYMMDDOSF06AA__CC____01', 'YYYYMMDDOSF07AA__CC____01', 'YYYYMMDDOSF08AA________01', 'YYYYMMDDOSF09AA________01',
    'YYYYMMDDOSF10AABBCC____01', 'YYYYMMDDOSF11AA__CC____01', 'YYYYMMDDOSF12AABB______01', 'YYYYMMDDOSF13AA_____EEE01', 'YYYYMMDDOSF14AA________01', 'YYYYMMDDOSF15AA__CC____01',
    'YYYYMMDDOSF16AA________01', 'YYYYMMDDOSF17AA________01', 'YYYYMMDDOSF18AABB______01',
    '', 'YYYYMMDDOSF20AABB__D___01', 'YYYYMMDDOSF21AA________01', 'YYYYMMDDOSF22AA________01',
    'YYYYMMDDOSF23AABB______01'
]


def nav_info(request, get_type=0):
    tran_system = Tran_Systemstatus.objects.all().first()

    params = {
        'nav': {
            'basho': tran_system.CurrentBasho,
            'systatus': tran_system.SystemStatus,
            'torikumiday': tran_system.TorikumiDate.Nichime_name,
            'shoubuday': tran_system.MatchDate.Nichime_name
        }
    }
    if get_type:
        return [params, tran_system]
    else:
        return params


# 編集・配信処理
class Output_NewsML():

    def __init__(self):
        self.grade = 0 # 階級コード
        self.now = datetime.now()
        self.stnow = self.now.strftime("%Y%m%d")
        self.newsno = 0
        self.st = 0

    # NewsML作成関数
    def Create_NewsML(self, request):　

        if request.method == "POST":
            if "NewsMLNo" not in request.POST:
                return "Input error."

            self.newsno = request.POST["NewsMLNo"]  # NEWSML種別コードを受け取る
            if self.newsno.startswith("0"):
                self.newsno.lstrip("0")
            if not self.newsno.isdigit():  # 全ての文字が数値でない場合、末尾2文字を抽出・削除
                self.grade = self.newsno[-2]
                self.newsno = self.newsno[:-2]

            temp_product_id = temp[int(self.newsno)-1]  # NEWSML種別コードに対応するtemplateIDを取得
            file_name = '%s.xml' % temp_product_id  # テンプレートのファイル名
            temp_file_name = 'NewsML_temp/%s' % file_name
            t = loader.get_template(temp_file_name)  # Djangoのテンプレートとして取得

            context = self.Create_context() # 21種のコンテキストを代入する関数

            if "Input_status" in request.POST:
                self.st = request.POST["Input_status"]  # パラメータ 0=編集、1=配信、2=プレビュー、3=印刷
                if self.st in ["0", "1"]:  # 編集か配信であれば、NewsMLをファイルに出力
                    content = loader.render_to_string(temp_file_name, context)
                    # file名は運用日付、パラメータに合わせて変更
                    newfile_name = file_name.replace("YYYYMMDD", self.stnow)
                    if self.grade:
                        newfile_name.replace('BB', self.grade)
                    # 配信済みフォルダに保存する場合のUtf-16保存検証済み
                    # with open('app_sumo/output/deliveried/%s' % newfile_name, 'w', encoding = 'utf-16') as static_file: 
                    with open('app_sumo/output/hold/%s' % newfile_name, 'w') as static_file:
                        static_file.write(content)

                elif self.st == "2":  # プレビューであれば、UTF-16に変換し表示
                    return HttpResponse(t.render(context), content_type='text/xml; charset=utf-16')

    # NewsML内のコンテキスト作成
    def Create_context(self):
        # newsmlmetaから現在の場所と取得して、テンプレートに渡す
        # 力士マスタ、生涯成績マスタから現在の値を取得して、テンプレートに渡す
        # （現状は体重等が力士マスタになっているのでそうなるが、力士マスタは全ての力士を蓄積しているので、番付だけのトランザクションテーブルに移動させて方が良いかも）
        # 生涯成績

        # 'newsmlmeta'が21種類共通であれば、ここに記載して辞書をマージするとよいかもしれません。例として記述させて頂きました。
        # 他の分岐は共通化が難しければ、この関数の行数が100文字以上に増えた場合に、各パターンを関数で分離させる必要があるかもしれません。
        tran_system = Tran_Systemstatus.objects.all()
        context = { 'newsmlmeta':tran_system }
        fix_context = {}
        
        if self.newsno == "01":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader': Mst_SubHeader.objects.all(),  # 副ヘッダマスタ
                'Banzuke_forecast': Tran_Banzuke_forecast.objects.all(),  # 予想番付マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),  # 生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),  # 生涯受賞マスタ
            }
        elif self.newsno == "02":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader': Mst_SubHeader.objects.all(),  # 副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),  # 生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),  # 生涯受賞マスタ
            }
        elif self.newsno == "03":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader': Mst_SubHeader.objects.all(),  # 副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),  # 生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),  # 生涯受賞マスタ
            }
        elif self.newsno == "06":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }        

        return context.update(fix_context)

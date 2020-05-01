from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from datetime import datetime
from .models import *
from .consts import *

from datetime import datetime
from logging import getLogger

logger = getLogger('app_sumo')

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
        self.file_name = "" # NewsML_templateのファイル名
        self.temp_file_name = "" # NewsML_templateの置き場所
        self.newfile_name = "" # 補完されたファイル名 = Content_id
    
    # 初期動作 編集、チェック、配信とループを管理
    def Start_NewsML(self, request):
        if "NewsMLNo" not in request.POST:
            return "Input error."

        if "Input_status" in request.POST:
            self.st = int(request.POST["Input_status"])  # パラメータ 0=編集、1=配信、2=プレビュー、3=印刷
            logger.info("%s処理 開始" % NewsML_status[self.st]) 

        self.newsno = request.POST["NewsMLNo"]  # NEWSML種別コードを受け取る
        if self.newsno.startswith("0"):
            self.newsno.lstrip("0")
        if not self.newsno.isdigit():  # 全ての文字が数値でない場合、末尾2文字を抽出・削除
            self.grade = self.newsno[-2]
            self.newsno = self.newsno[:-2]            

        temp_product_id = NewsML_template[int(self.newsno)-1]  # NEWSML種別コードに対応するtemplateIDを取得
        self.file_name = '%s.xml' % temp_product_id  # テンプレートのファイル名
        self.temp_file_name = 'NewsML_temp/%s' % self.file_name
        
        if self.st == 2: # プレビューであれば、UTF-16に変換し表示
            t = loader.get_template(self.temp_file_name)  # Djangoのテンプレートとして取得
            logger.info("%s処理 終了" % NewsML_status[self.st])
            return HttpResponse(t.render(self.Create_context()), content_type='text/xml; charset=utf-16')
        else: # それ以外は、NewsMLをファイルに出力
            ## nesnoによる判定により、都道府県、東西、取組順にてループ予定
            self.Create_NewsML(request)
            if self.st == 3:
                self.PrintOut_NewsML(request) # 印刷を行う関数(仮)
                logger.info("%s処理 終了" % NewsML_status[self.st])
            
            ## nesnoによる判定により、都道府県、東西、取組順にてループ予定
            self.Check_NewsML(request)
            if self.st == 0:
                ## 編集の場合、Tran_NewsMLStatus を status = 0に更新。処理終了 (この関数を呼ぶ前に分解)
                logger.info("%s処理 終了" % NewsML_status[self.st])
            else:
                ## 配信の場合、次へ
                ## nesnoによる判定により、都道府県、東西、取組順にてループ予定
                self.Delivery_NewsML(request)
                logger.info("%s処理 終了" % NewsML_status[self.st])

            



    # NewsML作成関数
    def Create_NewsML(self, request):
        ## file名を運用日付、部署コード、都道府県コード、東西コード、取組順に合わせて変更 = コンテンツIDの作成
        self.newfile_name = self.file_name.replace("YYYYMMDD", self.stnow)
        if self.grade:
            self.newfile_name.replace('BB', self.grade)
        ## Tran_NewsMLStatusのContent_id＝コンテンツID、status=3であれば処理終了。
        
        context = self.Create_context(1,1,1,0) # 21種のコンテキストを代入する関数
        content = loader.render_to_string(self.temp_file_name, context)
        with open('app_sumo/output/hold/%s' % self.newfile_name, 'w') as static_file:
            static_file.write(content)

    def PrintOut_NewsML(self, request):
        ## 印刷はどのようなロジックを組むか 要確認
        return {}

    def Check_NewsML(self, request):
        ## DTDチェック
        ## ファイルサイズチェック
        ## Tran_NewsMLStatus と Content_id＝コンテンツIDのレコードのdelivery_flag=TRUEを取得
        ## 分岐1：レコードが存在すれば、配信済みフォルダコンテンツ内容のチェック
        ## 分岐1：同一コンテンツチェックで内容の違う場合、修正区分を編集。
        ## 分岐1：編注に「修正 == XX」を編集。次へ
        ## 分岐1：修正があったNewsMLだけDelivery_NewsMLで処理
        ## 分岐2：レコードが存在しなければ、次へ
        return {}


    def Delivery_NewsML(self, request):
        ## 配信参照区分が0(電文／データ出力画面)である場合、MQ配信先としてTran_SystemstatusのMQSend_addressを参照。
        ## 配信参照区分が1(コンテンツ出力画面)である場合、MQ配信先としてパラメータ("MQSend_address")を参照。
        ## IBMMQへ配信　関数を呼んだ方がよさそう
        ## 当日配信済みフォルダ、配信済みフォルダへそれぞれ保存
        content = loader.render_to_string(self.temp_file_name, self.Create_context()) # (仮)
        ## 配信済みフォルダに保存する場合のUtf-16保存検証済み
        with open('app_sumo/output/today\'s_delivered/%s' % self.newfile_name, 'w', encoding = 'utf-16') as static_file: 
            static_file.write(content)
        ## NewsMLStatusのContent_id＝コンテンツID、status=1で更新。
        ## 出力状況テーブル(出力回数、出力時間)を更新、MQ_sequenceのsequenceを+1で更新。
        ## 次へ


    def Create_context(self, prefecture_code=1, class_code=1, eastwest_code=1, display_order=0):
        """NewsML内のコンテキスト作成
        
        Parameters
        ----------
        prefecture_code : int
            対象の都道府県コード。
        class_code : int
            対象の部署コード。
        eastwest_code : int
            対象の東西コード。
        display_order : int
            対象の取組順。

        Returns
        -------
        context : dict
            NewsMl_template内に渡す変数。
        """
        # newsmlmetaから現在の場所と取得して、テンプレートに渡す
        # 力士マスタ、生涯成績マスタから現在の値を取得して、テンプレートに渡す
        # （現状は体重等が力士マスタになっているのでそうなるが、力士マスタは全ての力士を蓄積しているので、番付だけのトランザクションテーブルに移動させて方が良いかも）
        # 生涯成績

        # 例として記述させて頂きました。
        # 'newsmlmeta'が21種類共通であれば、または他のテーブルを共通記述出来れば、ここに記載して辞書をマージするとよいかもしれません。
        # 他の分岐は共通化が難しければ、この関数の行数が100文字以上に増えた場合に、各パターンを関数で分離させる必要があるかもしれません。
        tran_system = Tran_Systemstatus.objects.all()
        context = { 'newsmlmeta':tran_system,'test':'abcdefg' }
        fix_context = {}

        #01新番付資料
        if self.newsno == "01":
            fix_context = {
                'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="01") ,  #副ヘッダマスタ
                'Banzuke_forecast': Tran_Banzuke_forecast.objects.all(),  # 予想番付マスタ
                'Liferesult': Mst_Lifetime_result.objects.all(),  # 生涯成績マスタ
                'Lifeaward': Mst_Lifetime_award.objects.all(),  # 生涯受賞マスタ
                'Lifechii': Mst_Lifetime_statusinfo.objects.all(),  # 生涯地位マスタ
            }
        #02新番付資料・補正
        elif self.newsno == "02":
            fix_context = {
                'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="02") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
            }
        #03新番付
        elif self.newsno == "03":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="03") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
            }
        #04郷土力士新番付
        elif self.newsno == "04":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="04") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
            }
        #05幕下以下新番付
        elif self.newsno == "05":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),  # システム状態マスタ
                'subheader':Mst_SubHeader.objects.filter(Content_code__NewsMLNo="05") ,  #副ヘッダマスタ
                'Banzuke': Tran_Banzuke.objects.all(),  # 番付明細マスタ
            }
        #06郷土力士取組
        elif self.newsno == "06":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }  
        #06郷土力士取組
        elif self.newsno == "06":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }
        #07幕下以下取組
        elif self.newsno == "07":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }
        #08十両取組
        elif self.newsno == "08":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }
        #09中入り取組
        elif self.newsno == "09":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
                'Banzuke': Tran_Banzuke.objects.all(),
                'Liferesult': Mst_Lifetime_result.objects.all(),
                'Lifeaward': Mst_Lifetime_award.objects.all(),
                'basho': tran_system.first().CurrentBasho,
                'torikuminichime': tran_system.first().TorikumiDate.Nichime_4char,
            }
        #10郷土力士勝負・階級別
        elif self.newsno == "10":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #11郷土力士勝負・まとめ
        elif self.newsno == "11":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #12幕下以下勝負
        elif self.newsno == "12":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #13勝負
        elif self.newsno == "13":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #14まとめ勝負
        elif self.newsno == "14":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #15郷土力士星取表
        elif self.newsno == "15":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #16外国力士成績
        elif self.newsno == "16":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #17優勝三賞受賞力士
        elif self.newsno == "17":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #18階級別成績上位力士
        elif self.newsno == "18":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #20幕下以下全成績
        elif self.newsno == "20":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }
        #21十両星取表
        elif self.newsno == "21":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }  
        #2222幕内星取表
        elif self.newsno == "22":
            fix_context = {
                # 'newsmlmeta': Tran_Systemstatus.objects.all(),
            }

        return dict(context, **fix_context)


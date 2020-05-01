from django.contrib import admin
from .models import *

#出走表Ａ
class Trn_Running_list_A_SUAAdmin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('開催曜日', {'fields':['Held_day'] }),
	    ('競馬場名称', {'fields':['Track_name'] }),
        ('レース番号', {'fields':['Race_No'] }),
        ('発走時刻', {'fields':['Start_time'] }),
	    ('距離', {'fields':['Race_Distance'] }),
        ('芝ダート区分名称', {'fields':['Turf_Dart_name'] }),
    ]
    list_display = ('Race_date', 'Held_day', 'Track_name', 'Race_No', 'Start_time', 'Race_Distance', 'Turf_Dart_name')


admin.site.register(Tran_Systemstatus)
admin.site.register(Mst_Operationmode)
admin.site.register(Mst_Environment)
admin.site.register(Mst_Grade)
admin.site.register(Mst_Breed_age)
admin.site.register(Mst_Jou)
admin.site.register(Mst_Weather)
admin.site.register(Mst_Margin)
admin.site.register(Mst_Difference)
admin.site.register(Mst_Accident_type)
admin.site.register(Mst_Accident_reason)
admin.site.register(Mst_Gender)
admin.site.register(Mst_Belonging)
admin.site.register(Mst_JRA_exchanges)
admin.site.register(Mst_Turf_dirt_class)
admin.site.register(Mst_Course_class)
admin.site.register(Mst_Clockwise_class)
admin.site.register(Mst_Night_race_class)
admin.site.register(Mst_Handicap)
admin.site.register(Mst_Track_condition)
admin.site.register(Mst_Jockey_changed_reason)
admin.site.register(Mst_Matter)
admin.site.register(Mst_Target_person)
admin.site.register(Mst_Race_type)

admin.site.register(Mst_Haishinsha)
admin.site.register(Mst_Haishinsaki_Nomal)
admin.site.register(Mst_Haishinsaki_Limited)
admin.site.register(Mst_Printer)


admin.site.register(Mst_Kaisai_Hiwari)
admin.site.register(Mst_Honjitu_Shikou)

admin.site.register(Mst_Fix_annotation)


# 中間DB
admin.site.register(Md_Shussouhyou)
admin.site.register(Md_Shussouhyou_shussouba)
admin.site.register(Md_Shussouhyou_shussouba_ruikei)
admin.site.register(Md_Shussouhyou_shussouba_5seiseki)
admin.site.register(Md_Nyujo)
admin.site.register(Md_Uriagekin)

admin.site.register(Md_Seiseki_Haraimodoshi)
admin.site.register(Md_Seiseki_Haraimodoshi_tan)
admin.site.register(Md_Seiseki_Haraimodoshi_fuku)
admin.site.register(Md_Seiseki_Haraimodoshi_wakupuku)
admin.site.register(Md_Seiseki_Haraimodoshi_wakutan)
admin.site.register(Md_Seiseki_Haraimodoshi_umapuku)
admin.site.register(Md_Seiseki_Haraimodoshi_umatan)
admin.site.register(Md_Seiseki_Haraimodoshi_sanpuku)
admin.site.register(Md_Seiseki_Haraimodoshi_santan)
admin.site.register(Md_Seiseki_Haraimodoshi_wa)
admin.site.register(Md_Seiseki_Haraimodoshi_seiseki)

admin.site.register(Md_Corner_Rap)
admin.site.register(Md_Agari)
admin.site.register(Md_Tsuushimbun)

# CSV取り込み
admin.site.register(Schedule_BA7)
admin.site.register(Trn_Enforcement_information_today_INI)
admin.site.register(Trn_Running_list_A_SUA, Trn_Running_list_A_SUAAdmin)
admin.site.register(Trn_Running_list_B_SUB)
admin.site.register(Trn_Running_list_C_SUC)
admin.site.register(Trn_Running_list_D_SUD)
admin.site.register(Trn_Running_list_E_SUE)
admin.site.register(Trn_Cancellation_exclusion_SU1)
admin.site.register(Trn_Change_riding_SU3)
admin.site.register(Trn_Corner_passing_order_BA2)
admin.site.register(Trn_Fallon_time_BA3)
admin.site.register(Last_3_Fallon_BA4)
admin.site.register(Trn_Visitors_BA5)
admin.site.register(Trn_Attached_document_BU1)
admin.site.register(Trn_Result_SU6)
admin.site.register(Trn_Win_place_dividend_WI2)
admin.site.register(Trn_Bracket_quinella_exacta_dividend_BL2)
admin.site.register(Trn_Quinella_exacta_wide_dividend_QU2)
admin.site.register(Trn_Trio_dividend_TB3)
admin.site.register(Trn_Trifecta_dividend_TB4)

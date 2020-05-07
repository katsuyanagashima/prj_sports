from django.contrib import admin
from .models import *

#出走表_SUA
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

#着タイムデータ_SU6
class Trn_Result_SU6Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('馬名', {'fields':['Horse_name'] }),
        ('年齢', {'fields':['Horse_age'] }),
	    ('枠番', {'fields':['Bracket_No'] }),
        ('馬番', {'fields':['Horse_No'] }),
        ('騎手略名', {'fields':['Jockey_shortened'] }),
        ('着', {'fields':['Result'] }),
        ('タイム', {'fields':['Finish_time'] }), 
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Horse_name', 'Horse_age', 'Bracket_No', 'Horse_No', 'Jockey_shortened', 'Result', 'Finish_time')

#単勝複勝払戻データ_WI2
class Trn_Win_place_dividend_WI2Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('単勝払戻馬番１', {'fields':['Win_No_1'] }),
        ('単勝払戻金額１', {'fields':['Win_1'] }),
	    ('単勝払戻人気順１', {'fields':['Win_pick_1'] }),
        ('複勝着順１', {'fields':['Place_Resutl_1'] }),
        ('複勝払戻馬番１', {'fields':['Place_No_1'] }),
        ('複勝払戻金額１', {'fields':['Place_1'] }),
        ('複勝着順２', {'fields':['Place_Resutl_2'] }),
        ('複勝払戻馬番２', {'fields':['Place_No_2'] }),
        ('複勝払戻金額２', {'fields':['Place_2'] }),
        ('複勝着順３', {'fields':['Place_Resutl_3'] }),
        ('複勝払戻馬番３', {'fields':['Place_No_3'] }),
        ('複勝払戻金額３', {'fields':['Place_3'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Win_No_1', 'Win_1', 'Win_pick_1', 'Place_Resutl_1', 'Place_No_1', 'Place_1', 'Place_Resutl_2', 'Place_No_2', 'Place_2', 'Place_Resutl_3', 'Place_No_3', 'Place_3')

#枠複枠単払戻データ_BL2
class Trn_Bracket_quinella_exacta_dividend_BL2Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('レコード区分', {'fields':['Data_Classification'] }),
        ('枠連枠番１１', {'fields':['Bracket_No_1_1'] }),
        ('枠連枠番１２', {'fields':['Bracket_No_1_2'] }),
	    ('枠連払戻金額１', {'fields':['Bracket_quinella_exacta_1'] }),
        ('枠連払戻人気順１', {'fields':['Bracket_quinella_exacta_pic_1'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Data_Classification', 'Bracket_No_1_1', 'Bracket_No_1_2', 'Bracket_quinella_exacta_1', 'Bracket_quinella_exacta_pic_1')

#馬連馬単ワイド払戻データ_QU2
class Trn_Quinella_exacta_wide_dividend_QU2Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('レコード区分', {'fields':['Data_Classification'] }),
        ('馬連馬番１１', {'fields':['Horce_No_1_1'] }),
        ('馬連馬番１２', {'fields':['Horce_No_1_2'] }),
	    ('馬連払戻金額１', {'fields':['Quinella_exacta_wide_1'] }),
        ('馬連払戻人気順１', {'fields':['Quinella_exacta_wide_pic_1'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Data_Classification', 'Horce_No_1_1', 'Horce_No_1_2', 'Quinella_exacta_wide_1', 'Quinella_exacta_wide_pic_1')

#三連複払戻データ_TB3
class Trn_Trio_dividend_TB3Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('三連複馬番１１', {'fields':['Horce_No_1_1'] }),
        ('三連複馬番１２', {'fields':['Horce_No_1_2'] }),
        ('三連複馬番１３', {'fields':['Horce_No_1_3'] }),
	    ('三連複払戻金額１', {'fields':['Trio_1'] }),
        ('三連複払戻人気順１', {'fields':['Trio_pic_1'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Horce_No_1_1', 'Horce_No_1_2', 'Horce_No_1_3', 'Trio_1', 'Trio_pic_1')

#三連単払戻データ_TB4
class Trn_Trifecta_dividend_TB4Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('三連単馬番１１', {'fields':['Horce_No_1_1'] }),
        ('三連単馬番１２', {'fields':['Horce_No_1_2'] }),
        ('三連単馬番１３', {'fields':['Horce_No_1_3'] }),
	    ('三連単払戻金額１', {'fields':['Trifecta_1'] }),
        ('三連単払戻人気順１', {'fields':['Trifecta_pic_1'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Horce_No_1_1', 'Horce_No_1_2', 'Horce_No_1_3', 'Trifecta_1', 'Trifecta_pic_1')

#付加文書_BU1
class Trn_Attached_document_BU1Admin(admin.ModelAdmin):
    fieldssets = [
        ('競走年月日', {'fields':['Race_date'] }),
        ('競馬場', {'fields':['Track_code'] }),
	    ('レース番号', {'fields':['Race_No'] }),
        ('事象名', {'fields':['Event_name'] }),
        ('レース付加文書１', {'fields':['Attached_document_1'] }),
    ]
    list_display = ('Race_date', 'Track_code', 'Race_No', 'Event_name', 'Attached_document_1')

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

admin.site.register(Md_Jou_Toujitsu)

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
admin.site.register(Trn_Attached_document_BU1, Trn_Attached_document_BU1Admin)
admin.site.register(Trn_Result_SU6, Trn_Result_SU6Admin)
admin.site.register(Trn_Win_place_dividend_WI2, Trn_Win_place_dividend_WI2Admin)
admin.site.register(Trn_Bracket_quinella_exacta_dividend_BL2, Trn_Bracket_quinella_exacta_dividend_BL2Admin)
admin.site.register(Trn_Quinella_exacta_wide_dividend_QU2, Trn_Quinella_exacta_wide_dividend_QU2Admin)
admin.site.register(Trn_Trio_dividend_TB3, Trn_Trio_dividend_TB3Admin)
admin.site.register(Trn_Trifecta_dividend_TB4, Trn_Trifecta_dividend_TB4Admin)

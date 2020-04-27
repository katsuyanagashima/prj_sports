from django.contrib import admin

from .models import *
"""
from .models import Mst_Race_track, Mst_Commemorative_Race, Mst_Special_Commemorative_Race, Mst_Handicap_Open, Mst_Player_class, Mst_Auto_class, Mst_Accident_type, Mst_Race_status, Mst_Illegal_start, Mst_Disturbed, Mst_Release_status, Mst_Putout_Reason, Mst_Outside_track
from .models import Trn_Schedule, Trn_Program, Trn_Running_list, Trn_Result, Trn_Rider_results, Trn_Top_30_Prize, Trn_Outside_track
"""

#番組編成データレコード
class Trn_ProgramAdmin(admin.ModelAdmin):
    fieldssets = [
        ('場コード', {'fields':['Track_code'] }),
        ('場名', {'fields':['Track_name'] }),
	    ('開催日', {'fields':['Date_AD'] }),
        ('開催回日目', {'fields':['Held_day'] }),
	    ('節日数', {'fields':['Period_days'] }),
        ('レースNO', {'fields':['Race_No'] }),
    ]
    list_display = ('Track_code', 'Track_name', 'Date_AD', 'Held_day', 'Period_days', 'Race_No')

#出走選手テーブル
class Trn_Running_listAdmin(admin.ModelAdmin):
    fieldssets = [
        ('場コード', {'fields':['Track_code'] }),
        ('開催日', {'fields':['Date_AD'] }),
	    ('レースNO', {'fields':['Race_No'] }),
        ('連勝番号', {'fields':['Bracket_No'] }),
	    ('車番', {'fields':['Rider_No'] }),
        ('選手コード', {'fields':['Rider_code'] }),
        ('選手名', {'fields':['Rider_full_name'] }),
    ]
    list_display = ('Track_code', 'Date_AD', 'Race_No', 'Bracket_No', 'Rider_No', 'Rider_code', 'Rider_full_name')

#レース結果データレコード
class Trn_ResultAdmin(admin.ModelAdmin):
    fieldssets = [
        ('場コード', {'fields':['Track_code'] }),
        ('場名', {'fields':['Track_name'] }),
	    ('開催日', {'fields':['Date_AD'] }),
        ('レースNO', {'fields':['Race_No'] }),
    ]
    list_display = ('Track_code', 'Track_name', 'Date_AD', 'Race_No')

#選手成績テーブル
class Trn_Rider_resultsAdmin(admin.ModelAdmin):
    fieldssets = [
        ('場コード', {'fields':['Track_code'] }),
        ('開催日', {'fields':['Date_AD'] }),
	    ('レースNO', {'fields':['Race_No'] }),
        ('連勝番号', {'fields':['Bracket_No'] }),
	    ('車番', {'fields':['Rider_No'] }),
        ('選手コード', {'fields':['Rider_code'] }),
        ('選手名', {'fields':['Rider_full_name'] }),
        ('着', {'fields':['Result'] }),
    ]
    list_display = ('Track_code', 'Date_AD', 'Race_No', 'Bracket_No', 'Rider_No', 'Rider_code', 'Rider_full_name', 'Result')

#選手取得賞金上位３０位レコード
class Trn_Top_30_PrizeAdmin(admin.ModelAdmin):
    fieldssets = [
        ('送信日', {'fields':['Send_date'] }),
        ('集計日', {'fields':['Totaling_date'] }),
	    ('順位', {'fields':['Ranking'] }),
        ('選手コード', {'fields':['Rider_code'] }),
	    ('選手名', {'fields':['Rider_full_name'] }),
        ('取得賞金', {'fields':['Prize'] }),
    ]
    list_display = ('Send_date', 'Totaling_date', 'Ranking', 'Rider_code', 'Rider_full_name', 'Prize')

#場外売場情報
class Trn_Outside_trackAdmin(admin.ModelAdmin):
    fieldssets = [
        ('場コード', {'fields':['Track_code'] }),
        ('場名', {'fields':['Track_name'] }),
	    ('開催日', {'fields':['Date_AD'] }),
        ('開催回日目', {'fields':['Held_day'] }),
	    ('節日数', {'fields':['Period_days'] }),
        ('開催初日', {'fields':['First_day_of_the_event'] }),
    ]
    list_display = ('Track_code', 'Track_name', 'Date_AD', 'Held_day', 'Period_days', 'First_day_of_the_event')

#DBマスターテーブル
admin.site.register(Mst_Operationmode)
admin.site.register(Mst_Environment)
admin.site.register(Mst_Race_track)
admin.site.register(Mst_Commemorative_Race)
admin.site.register(Mst_Special_Commemorative_Race)
admin.site.register(Mst_Handicap_Open)
admin.site.register(Mst_Player_class)
admin.site.register(Mst_Auto_class)
admin.site.register(Mst_Accident_type)
admin.site.register(Mst_Race_status)
admin.site.register(Mst_Illegal_start)
admin.site.register(Mst_Disturbed)
admin.site.register(Mst_Release_status)
admin.site.register(Mst_Putout_Reason)
admin.site.register(Mst_Outside_track)

#DBトランザクションテーブル
admin.site.register(Tran_Systemstatus)
admin.site.register(Trn_Schedule)
admin.site.register(Trn_Program, Trn_ProgramAdmin)
admin.site.register(Trn_Running_list, Trn_Running_listAdmin)
admin.site.register(Trn_Result, Trn_ResultAdmin)
admin.site.register(Trn_Rider_results, Trn_Rider_resultsAdmin)
admin.site.register(Trn_Top_30_Prize, Trn_Top_30_PrizeAdmin)
admin.site.register(Trn_Outside_track, Trn_Outside_trackAdmin)

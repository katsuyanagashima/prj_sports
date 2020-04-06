from django.contrib import admin

#from .models import Mst_Rikishi, Mst_Rikishistatus, Mst_Heya, Mst_Basho, Mst_Kimarite, Mst_Award_category, Mst_Hometown, Mst_Class, Mst_Chii, Mst_Event, Mst_Nichime, Mst_Eastwest, Mst_Lifetime_result, Mst_Lifetime_award, Mst_Lifetime_statusinfo, Mst_Gameinfo
from .models import *

class Mst_HeyaAdmin(admin.ModelAdmin):
    fieldssets = [
        ('部屋コード', {'fields':['Heya_code'] }),
        ('正式名称漢字', {'fields':['Heya_official_kanji'] }),
	    ('正式名称かな', {'fields':['Heya_official_kana'] }),
        ('２文字部屋名漢字', {'fields':['Heya_kanji_2char'] }),
	    ('３文字部屋名漢字', {'fields':['Heya_kanji_3char'] }),
    ]
    list_display = ('Heya_code', 'Heya_official_kanji', 'Heya_official_kana', 'Heya_kanji_2char', 'Heya_kanji_3char')

class Mst_ChiiAdmin(admin.ModelAdmin):
    fieldssets = [
        ('地位コード', {'fields':['Chii_code'] }),
        ('地位名漢字', {'fields':['Chii_kanji'] }),
	    ('地位名かな', {'fields':['Chii_kana'] }),
        ('２文字略称', {'fields':['Chii_2char'] }),
	    ('３文字名称', {'fields':['Chii_3char'] }),
    ]
    list_display = ('Chii_code', 'Chii_kanji', 'Chii_kana', 'Chii_2char', 'Chii_3char')

class Mst_KindofNewsMLAdmin(admin.ModelAdmin):
    fieldssets = [
        ('グループID', {'fields':['Group_code'] }),
        ('電文種別名称', {'fields':['ContentName'] }),
	    ('NewsML種別コード', {'fields':['NewsMLNo'] }),
    ]
    list_display = ('Group_code', 'ContentName', 'NewsMLNo')

admin.site.register(Mst_Rikishi)
admin.site.register(Mst_Rikishistatus)
admin.site.register(Mst_Heya, Mst_HeyaAdmin)
admin.site.register(Mst_Basho)
admin.site.register(Mst_Kimarite)
admin.site.register(Mst_Award_category)
admin.site.register(Mst_Hometown)
admin.site.register(Mst_Class)
admin.site.register(Mst_Chii, Mst_ChiiAdmin)
admin.site.register(Mst_Event)
admin.site.register(Mst_Nichime)
admin.site.register(Mst_Eastwest)
admin.site.register(Mst_Lifetime_statusinfo)
admin.site.register(Mst_Lifetime_result)
admin.site.register(Mst_Lifetime_award)
admin.site.register(Mst_Gameinfo)
admin.site.register(Mst_KindofNewsML, Mst_KindofNewsMLAdmin)
admin.site.register(Mst_Operationmode)
# --------------------
admin.site.register(Tran_Systemstatus)
# --------------------
admin.site.register(Tran_Banzuke)
# --------------------
class Tran_TopClassRikishiAdmin(admin.ModelAdmin):
    fieldssets =[
        ('階級', {'fields':['Class_code']}),
        ('開催年月西暦', {'fields':['Yearmonth']}),
        ('日目', {'fields':['Nichime_code']}),
        ('負け数', {'fields':['LossCount']}),
        ('勝ち数', {'fields':['WinCount']}),
    ]
    list_display = ('Class_code', 'Yearmonth', 'Nichime_code', 'LossCount', 'WinCount')

admin.site.register(Tran_TopClassRikishi, Tran_TopClassRikishiAdmin)
# --------------------




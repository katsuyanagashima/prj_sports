from django.contrib import admin

from .models import Eventinfo, Player, Waza, Outcome, Match, PostCsv, Mst_Rikishi, Mst_Rikishistatus, Mst_Heya, Mst_Basho, Mst_Kimarite, Mst_Award_category, Mst_Hometown, Mst_Class, Mst_Chii, Mst_Event, Mst_Nichime, Mst_Eastwest


class Mst_ChiiAdmin(admin.ModelAdmin):
    fieldssets = [
        ('地位コード', {'fields':['Chii_code'] }),
        ('地位名漢字', {'fields':['Chii_kanji'] }),
	    ('地位名かな', {'fields':['Chii_kana'] }),
        ('２文字略称', {'fields':['Chii_2char'] }),
	    ('３文字名称', {'fields':['Chii_3char'] }),
    ]
    list_display = ('Chii_code', 'Chii_kanji', 'Chii_kana', 'Chii_2char', 'Chii_3char')


admin.site.register(Eventinfo)
admin.site.register(Player)
admin.site.register(Waza)
admin.site.register(Outcome)
admin.site.register(Match)
admin.site.register(PostCsv)

# ----------------------------------------------------------------------
admin.site.register(Mst_Rikishi)
admin.site.register(Mst_Rikishistatus)
admin.site.register(Mst_Heya)
admin.site.register(Mst_Basho)
admin.site.register(Mst_Kimarite)
admin.site.register(Mst_Award_category)
admin.site.register(Mst_Hometown)
admin.site.register(Mst_Class)
admin.site.register(Mst_Chii, Mst_ChiiAdmin)
admin.site.register(Mst_Event)
admin.site.register(Mst_Nichime)
admin.site.register(Mst_Eastwest)



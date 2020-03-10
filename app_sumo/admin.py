from django.contrib import admin

from .models import Eventinfo, Player, Waza, Outcome, Match, PostCsv, Mst_Rikishi, Mst_Rikishistatus, Mst_Heya, Mst_Basho, Mst_Kimarite, Mst_Award_category, Mst_Hometown, Mst_Class, Mst_Chii, Mst_Event, Mst_Nichime, Mst_Eastwest, Mst_Lifetime_result, Mst_Lifetime_award
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
admin.site.register(Mst_Chii)
admin.site.register(Mst_Event)
admin.site.register(Mst_Nichime)
admin.site.register(Mst_Eastwest)
admin.site.register(Mst_Lifetime_result)
admin.site.register(Mst_Lifetime_award)

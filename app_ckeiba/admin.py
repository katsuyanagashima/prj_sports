from django.contrib import admin
from .models import *

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
admin.site.register(Md_Shussouba)
admin.site.register(Md_Shussouba_kako)
admin.site.register(Md_Nyujo)
admin.site.register(Md_Uriagekin)
admin.site.register(Md_Seiseki_Haraimodoshi)
admin.site.register(Md_Seiseki_Haraimodoshi_seiseki)
admin.site.register(Md_Corner_Rap)
admin.site.register(Md_Agari)
admin.site.register(Md_Tshuushinbun)
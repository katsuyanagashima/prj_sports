from django.contrib import admin

from .models import *

from .models import Mst_Race_track, Mst_Commemorative_Race, Mst_Special_Commemorative_Race, Mst_Handicap_Open, Mst_Player_class, Mst_Auto_class, Mst_Accident_type, Mst_Race_status, Mst_Illegal_start, Mst_Disturbed, Mst_Release_status, Mst_Putout_Reason, Mst_Outside_track
#from .models import Trn_Schedule, Trn_Program, Trn_Running_list, Trn_Result, Trn_Rider_results, Trn_Top_30_Prize, Trn_Outside_track
#from .models import systemstatus, csvtest1, auto_schedule, Trn_Schedule, Trn_Program, Trn_Running_list, Trn_Result

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
#-----------------------------------
admin.site.register(Trn_Schedule)
admin.site.register(Trn_Program)
admin.site.register(Trn_Running_list)
admin.site.register(Trn_Result)
admin.site.register(Trn_Rider_results)
admin.site.register(Trn_Top_30_Prize)
admin.site.register(Trn_Outside_track)

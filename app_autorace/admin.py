from django.contrib import admin

from .models import systemstatus, csvtest1, auto_schedule, Trn_Schedule, Trn_Program, Trn_Running_list, Trn_Result

admin.site.register(systemstatus)
admin.site.register(csvtest1)
admin.site.register(auto_schedule)

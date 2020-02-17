from django.contrib import admin

from .models import systemstatus, csvtest1, auto_schedule

admin.site.register(systemstatus)
admin.site.register(csvtest1)
admin.site.register(auto_schedule)

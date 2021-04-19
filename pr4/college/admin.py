from django.contrib import admin
from college.models import Notice
from django.contrib.admin.options import ModelAdmin

class NoticeAdmin(ModelAdmin):
    list_display = ["subject","cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]


# Register your models here.
admin.site.register(Notice, NoticeAdmin)
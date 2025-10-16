from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Asset, ProblemType, Report

@admin.register(Asset)
class AssetAdmin(DjangoMpttAdmin):
    mptt_level_indent = 25  
    list_display = ('name',)
    
admin.site.register(ProblemType)
admin.site.register(Report)

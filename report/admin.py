from django.contrib import admin
from .models import Report, Asset, ProblemType

# Register your models here.
admin.site.register(Asset)
admin.site.register(ProblemType)
admin.site.register(Report)

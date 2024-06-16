from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Internship_Data)
admin.site.register(Internship_Lesson)
admin.site.register(Internship_Topic)

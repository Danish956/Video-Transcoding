from django.contrib import admin
from .models.customuser import*
from import_export.admin import ImportExportModelAdmin

class AdminCustomuser(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['user_type','username','decrypt_password','first_name', 'last_name','email','mobile_number','gender','status']
admin.site.register(CustomeUser, AdminCustomuser)
from django.contrib import admin
from .Client import *
from import_export.admin import ImportExportModelAdmin

class ClientAdmin(ImportExportModelAdmin):
    pass

admin.site.register(ClientTable,ClientAdmin)
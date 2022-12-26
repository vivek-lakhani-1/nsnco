from django.contrib import admin
from .Artist_Feedback import *
from .Artist_Project_Demo import *
from .Artist_Request import *
from .Artist import *
from import_export.admin import ImportExportModelAdmin

class ArtistAdmin(ImportExportModelAdmin):
    pass
# Register your models here.

admin.site.register(ArtistFeedback,ArtistAdmin)
admin.site.register(ProjectDemos,ArtistAdmin)
admin.site.register(ArtistRequest,ArtistAdmin)
admin.site.register(ArtistTable,ArtistAdmin)
admin.site.register(worklink,ArtistAdmin)
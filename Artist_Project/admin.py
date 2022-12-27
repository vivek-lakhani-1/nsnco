from django.contrib import admin
from .Other_Table import *
from .project import *
from .Project_Fees import *
from import_export.admin import ImportExportModelAdmin

class ProjectAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Skill,ProjectAdmin)
admin.site.register(Location,ProjectAdmin)
admin.site.register(Genre,ProjectAdmin)
admin.site.register(Language,ProjectAdmin)
admin.site.register(Project_Fee,ProjectAdmin)
admin.site.register(Project_Table,ProjectAdmin)

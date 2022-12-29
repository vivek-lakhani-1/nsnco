from django.contrib import admin
from .Artist_Feedback import *
from .Artist_Project_Demo import *
from .Artist_Request import *
from .Artist import *
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import resources,fields
from Artist_Project import Other_Table


class ArtistAdmin(resources.ModelResource):
    location=fields.Field(attribute='location', widget=ManyToManyWidget(Other_Table.Location,field='name'))
    genre=fields.Field(attribute='genre', widget=ManyToManyWidget(Other_Table.Genre,field='name'))
    language=fields.Field(attribute='language', widget=ManyToManyWidget(Other_Table.Language,field='name'))
    skill=fields.Field(attribute='skill', widget=ManyToManyWidget(Other_Table.Skill,field='name'))
    # worklink=fields.Field(attribute='worklink', widget=ManyToManyWidget(Other_Table.Skill,field='name'))
    class Meta:
        model = ArtistTable
        fields = ('id','skill','name','profile_image','age','city','genre','location','language','worklink','otherperformart','social_link_f','social_link_l','social_link_p','number','manger','budget_range','budget_idea','am_note','pm_note','rating')
        
        
class data(ImportExportModelAdmin):
    resource_class = ArtistAdmin
    
admin.site.register(ArtistFeedback)
admin.site.register(ProjectDemos)
admin.site.register(ArtistRequest)
admin.site.register(ArtistTable,data)
admin.site.register(worklink)
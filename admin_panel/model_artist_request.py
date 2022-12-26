from django.db import models
from .other_tables import skill
from .other_tables import genre_table
from .other_tables import location
from .other_tables import language
from .model_project import project_table
from .model_artist_panel import artist_table


hiring_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
class artist_request(models.Model):
    skill = models.ForeignKey(skill,on_delete=models.DO_NOTHING,default="NONE")
    location = models.ForeignKey(location,on_delete=models.DO_NOTHING,default="NONE")
    genre = models.ManyToManyField(genre_table)
    language = models.ManyToManyField(language)
    Other_Performing_Art_Details = models.TextField()
    min_budget = models.IntegerField()
    max_budget = models.IntegerField()
    budget = models.TextField()
    project = models.ForeignKey(project_table,on_delete=models.DO_NOTHING,default="NONE")
    production_hiring = models.IntegerField()
    servicing_hiring = models.IntegerField()
    # shorlisted_artist = models.ForeignKey.one_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING,default="NONE")
    # selected_artist = models.ForeignKey.many_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING,default="NONE")
    # rejected_artist = models.ForeignKey.many_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING,default="NONE")
    target = models.IntegerField()
    comments = models.TextField()
    hiring_process = models.CharField(
        max_length=100,
        choices=hiring_status,
        default=1
    )


    
    
    
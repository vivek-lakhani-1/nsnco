from django.db import models
from Artist_Project.project import *
# from .Artist import *


hiring_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
class ArtistRequest(models.Model):
    skill = models.ForeignKey(Skill,on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING)
    genre = models.ManyToManyField(Genre)
    language = models.ManyToManyField(Language)
    other_Performing_Art_Details = models.TextField()
    min_budget = models.SmallIntegerField()
    max_budget = models.SmallIntegerField()
    budget = models.TextField()
    project = models.ForeignKey(Project_Table,on_delete=models.DO_NOTHING)
    production_hiring = models.SmallIntegerField()
    servicing_hiring = models.SmallIntegerField()
    # shorlisted_artist = models.ForeignKey.one_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING)
    # selected_artist = models.ForeignKey.many_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING)
    # rejected_artist = models.ForeignKey.many_to_many(artist_table.artist_id,on_delete=models.DO_NOTHING)
    target = models.SmallIntegerField()
    comments = models.TextField()
    hiring_process = models.CharField(
        max_length=100,
        choices=hiring_status,
        default=1
    )


    
    
    
from django.db import models



hiring_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
class ArtistRequest(models.Model):
    skill = models.ForeignKey('Artist_Project.Skill',on_delete=models.DO_NOTHING,related_name='Skill')
    location = models.ForeignKey('Artist_Project.Location',on_delete=models.DO_NOTHING,related_name='Location')
    genre = models.ManyToManyField('Artist_Project.Genre',related_name='Genre')
    language = models.ManyToManyField('Artist_Project.Language',related_name='Language')
    other_Performing_Art_Details = models.TextField()
    min_budget = models.SmallIntegerField()
    max_budget = models.SmallIntegerField()
    budget = models.TextField()
    project = models.ForeignKey('Artist_Project.Project_Table',on_delete=models.DO_NOTHING,related_name='Project_Table')
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


    
    
    
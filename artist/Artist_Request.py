from django.db import models



hiring_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
class ArtistRequest(models.Model):
    skill = models.ManyToManyField('Artist_Project.Skill',related_name='Skill')
    location = models.ManyToManyField('Artist_Project.Location',related_name='Location')
    genre = models.ManyToManyField('Artist_Project.Genre',related_name='Genre')
    language = models.ManyToManyField('Artist_Project.Language',related_name='Language')
    other_Performing_Art_Details = models.TextField()
    min_budget = models.SmallIntegerField()
    max_budget = models.SmallIntegerField()
    budget = models.TextField()
    project = models.OneToOneField('Artist_Project.Project_Table',on_delete=models.DO_NOTHING,related_name='Project_Table1',null=True)
    production_hiring = models.SmallIntegerField()
    servicing_hiring = models.SmallIntegerField()
    target = models.SmallIntegerField()
    comments = models.TextField()
    hiring_process = models.CharField(
        max_length=100,
        choices=hiring_status,
        default=1
    )


    
    
    
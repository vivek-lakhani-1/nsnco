from django.db import models


rating = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10")
   
)

class worklink(models.Model):
    worklink = models.CharField(max_length=200)

class ArtistTable(models.Model):
    id = models.IntegerField(primary_key=True)
    skill = models.ManyToManyField('Artist_Project.Skill',related_name='Skill1')
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images')
    age = models.SmallIntegerField()
    city = models.CharField(max_length=255)
    genre = models.ManyToManyField('Artist_Project.Genre',related_name='Genre1')
    location = models.ManyToManyField('Artist_Project.Location',related_name='Location1')
    language = models.ManyToManyField('Artist_Project.Language',related_name='Language1')
    worklink = models.ManyToManyField(worklink)
    otherperformart = models.TextField()
    social_link_f = models.CharField(max_length=100) 
    social_link_l = models.CharField(max_length=100) 
    social_link_p = models.CharField(max_length=100) 
    number = models.SmallIntegerField()
    manger = models.BooleanField()
    budget_range = models.TextField()
    budget_idea = models.TextField()
    am_note = models.TextField()
    pm_note = models.TextField()
    rating = models.CharField(
        max_length=2,
        choices=rating,
        default=1
    )
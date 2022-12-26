from django.db import models
from .other_tables import skill
from .other_tables import language
from .other_tables import location

class worklink(models.Model):
    worklink = models.CharField(max_length=200)

class artist_table(models.Model):
    artist_id = models.CharField(primary_key=True,max_length=100)
    skill = models.ManyToManyField(skill)
    Name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images')
    age = models.IntegerField()
    city = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    location = models.ManyToManyField(location)
    language = models.ManyToManyField(language)
    # worklink = models.ManyToManyField()
    otherperformart = models.TextField()
    social_link_f = models.CharField(max_length=100) 
    social_link_l = models.CharField(max_length=100) 
    social_link_p = models.CharField(max_length=100) 
    number = models.IntegerField()
    manger = models.BooleanField()
    budget_range = models.TextField()
    budget_idea = models.TextField()
    am_note = models.TextField()
    pm_note = models.TextField()
    rating = models.IntegerField()
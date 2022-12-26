from django.db import models

class skill(models.Model):
    skill = models.CharField(max_length=100)
class genre_table(models.Model):
    genre = models.CharField(max_length=100)
class location(models.Model):
    location = models.CharField(max_length=100)
class language(models.Model):
    lanuage = models.CharField(max_length=100)
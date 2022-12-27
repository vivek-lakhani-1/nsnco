from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)
class Language(models.Model):
    name = models.CharField(max_length=100)
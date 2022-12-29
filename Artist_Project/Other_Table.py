from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
        
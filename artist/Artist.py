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
    def __str__(self):
        return self.worklink

class ArtistTable(models.Model):
    id = models.AutoField(primary_key=True)
    skill = models.ManyToManyField('Artist_Project.Skill',related_name='Skill1')
    name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='images')
    age = models.SmallIntegerField(null=True,blank=True)
    city = models.CharField(max_length=255)
    genre = models.ManyToManyField('Artist_Project.Genre',related_name='Genre1')
    location = models.ManyToManyField('Artist_Project.Location',related_name='Location1')
    language = models.ManyToManyField('Artist_Project.Language',related_name='Language1')
    worklink = models.ManyToManyField(worklink)
    number = models.SmallIntegerField()
    manger = models.BooleanField(blank=True)
    manager_name = models.CharField(max_length=100,blank=True)
    manager_contact_no = models.CharField(max_length=100,blank=True)
    manager_contact_email = models.CharField(max_length=100,blank=True)
    min_budget = models.SmallIntegerField(null=True)
    max_budget = models.SmallIntegerField(null=True)
    budget_idea = models.TextField()
    am_note = models.TextField()
    pm_note = models.TextField()
    professional_rating = models.CharField(
        max_length=2,
        choices=rating,
        default=1
    )
    attitude_rating = models.CharField(
        max_length=2,
        choices=rating,
        default=1
    )
  
    def __str__(self):
        return str(self.id) + "__" + self.name
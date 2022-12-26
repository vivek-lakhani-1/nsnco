from django.db import models
from .Artist import *

class ArtistFeedback(models.Model):
    artist = models.ForeignKey(ArtistTable,on_delete=models.DO_NOTHING)
    Pre_Project_Production_Feedbacks = models.TextField()
    On_Project_Production_Feedbacks = models.TextField()
    Post_Production_Client_Feedbacks = models.TextField()
        
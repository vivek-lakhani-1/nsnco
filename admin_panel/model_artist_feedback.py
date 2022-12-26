from django.db import models
from .model_artist_panel import artist_table

class artist_feedback(models.Model):
    artist = models.ForeignKey(artist_table,on_delete=models.DO_NOTHING,default="NONE")
    Pre_Project_Production_Feedbacks = models.TextField()
    On_Project_Production_Feedbacks = models.TextField()
    Post_Production_Client_Feedbacks = models.TextField()
        
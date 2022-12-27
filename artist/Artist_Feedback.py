from django.db import models


class ArtistFeedback(models.Model):
    artist = models.ForeignKey('Artist.ArtistTable',on_delete=models.DO_NOTHING,related_name='ArtistTable')
    Pre_Project_Production_Feedbacks = models.TextField()
    On_Project_Production_Feedbacks = models.TextField()
    Post_Production_Client_Feedbacks = models.TextField()
        
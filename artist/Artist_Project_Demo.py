from django.db import models



status = (
    ("Shorlisted","Shorlisted"),
    ("Selected","Selected"),
    ("Rejected","Rejected")
)

class ProjectDemos(models.Model):
    artist = models.ForeignKey('Artist.ArtistTable',on_delete=models.DO_NOTHING,related_name='ArtistTable1')
    demo_work = models.ForeignKey('Artist.worklink',on_delete=models.DO_NOTHING,related_name='worklink0')
    project = models.ForeignKey('Artist_Project.Project_Table',on_delete=models.DO_NOTHING,related_name='Project_Table3')
    Artist_Status = models.CharField(
        max_length=100,
        choices=status,
        default=1
    )
    
    comment = models.TextField()
    

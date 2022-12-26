from django.db import models
from .Artist import *
from .Artist import worklink
from Project_Data.project import *


status = (
    ("Shorlisted","Shorlisted"),
    ("Selected","Selected"),
    ("Rejected","Rejected")
)

class ProjectDemos(models.Model):
    artist = models.ForeignKey(ArtistTable,on_delete=models.DO_NOTHING)
    demo_work = models.ForeignKey(worklink,on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project_Table,on_delete=models.DO_NOTHING)
    Artist_Status = models.CharField(
        max_length=100,
        choices=status,
        default=1
    )
    
    comment = models.TextField()
    
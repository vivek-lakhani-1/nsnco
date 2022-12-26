from django.db import models
from .model_artist_panel import artist_table
from .model_artist_panel import worklink
from .model_project import project_table


status = (
    ("Shorlisted","Shorlisted"),
    ("Selected","Selected"),
    ("Rejected","Rejected")
)

class project_demos(models.Model):
    artist = models.ForeignKey(artist_table,on_delete=models.DO_NOTHING,default="NONE")
    demo_work = models.ForeignKey(worklink,on_delete=models.DO_NOTHING,default="NONE")
    project = models.ForeignKey(project_table,on_delete=models.DO_NOTHING,default="NONE")
    Artist_Status = models.CharField(
        max_length=100,
        choices=status,
        default=1
    )
    comment = models.TextField()
    
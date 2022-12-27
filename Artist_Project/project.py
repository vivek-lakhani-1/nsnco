from django.db import models
# from Client_Data.Client import ClientTable
from Artist.Artist import *
from Artist.Artist_Project_Demo import ProjectDemos

status = (
    ("Unpaid","Unpaid"),
    ("Partially","Partially"),
    ("Paid","Paid")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)



class Project_Table(models.Model):
    project = models.IntegerField(primary_key=True)
    # client = models.ForeignKey(ClientTable,on_delete=models.DO_NOTHING)
    comment = models.TextField()
    # shorlisted_artist = models.ManyToManyField(ArtistTable)
    assigned_artist = models.ManyToManyField(ArtistTable)
    showcase_demo = models.ManyToManyField(worklink)
    project_demo = models.ManyToManyField(ProjectDemos)
    post_project_client_feedbacks = models.TextField()
    project_fees_status = models.CharField(
        max_length=10,
        choices=status,
        default=1
    )
    Contract_Document_Signing_Status = models.CharField(
        max_length=10,
        choices=contract_doc_status,
        default=1
    )

    
    
    

    
  
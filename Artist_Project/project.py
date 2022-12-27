from django.db import models


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
    client = models.ForeignKey('Client_Data.ClientTable',on_delete=models.DO_NOTHING,related_name='ClientTable5')
    comment = models.TextField()
    shorlisted_artist = models.ManyToManyField('Artist.ArtistTable',related_name='ArtistTable5')
    assigned_artist = models.ManyToManyField('Artist.ArtistTable',related_name='ArtistTable4')
    showcase_demo = models.ManyToManyField('Artist.worklink',related_name='worklink1')
    project_demo = models.ManyToManyField('Artist.ProjectDemos',related_name='ProjectDemos2')
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

    
    
    

    
  
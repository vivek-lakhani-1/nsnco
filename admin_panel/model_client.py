from django.db import models
from .model_project import project_table
client_payout = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)



class client_table(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.TextField()
    details = models.TextField()
    project = models.ForeignKey(project_table,on_delete=models.DO_NOTHING,default="NONE")
    Client_Previous_Payout = models.IntegerField()
    Production_Suggested_Project_Advance  = models.IntegerField()
    Latest_Project_Advance = models.IntegerField()
    Latest_Client_Payout_Status = models.CharField(
        max_length=100,
        choices=client_payout,
        default=1
    )
    Total_Client_Payout = models.IntegerField()
    Contract_Document_Signing_Status = models.CharField(
        max_length=100,
        choices=contract_doc_status,
        default=1
    )

    

    
    
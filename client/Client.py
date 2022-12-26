from django.db import models
from Project_Data.Other_table import *
from Project_Data.project import *
client_payout = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)



class ClientTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    details = models.TextField()
    # project = models.ForeignKey(Project_Table,on_delete=models.DO_NOTHING,default="NONE")
    Client_Previous_Payout = models.SmallIntegerField()
    Production_Suggested_Project_Advance  = models.SmallIntegerField()
    Latest_Project_Advance = models.SmallIntegerField()
    Latest_Client_Payout_Status = models.CharField(
        max_length=100,
        choices=client_payout,
        default=1
    )
    Total_Client_Payout = models.SmallIntegerField()
    Contract_Document_Signing_Status = models.CharField(
        max_length=100,
        choices=contract_doc_status,
        default=1
    )

    

    
    
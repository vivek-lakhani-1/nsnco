from django.db import models
from .model_project import project_table
from .model_client import client_table
advance_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)

class project_fee(models.Model):
    project_id = models.ForeignKey(project_table,on_delete=models.DO_NOTHING,default="NONE")
    client_id = models.ForeignKey(client_table,on_delete=models.DO_NOTHING,default="NONE")
    solution_fee = models.IntegerField()
    Production_Advance = models.IntegerField()
    Negotiated_Advance = models.IntegerField()
    Final_Advance = models.IntegerField()
    Advance_Status = models.CharField(
        max_length=100,
        choices=advance_status,
        default=1
    )
    Assigned_Artists_Payouts = models.CharField(max_length=100)
    Assigned_Artists_Advance_Payout_Status = models.CharField(
        max_length=100,
        choices=advance_status,
        default=1
    )
    Final_Fee_Settlement_Status = models.BooleanField()
    Post_Project_Client_Total_Payout = models.IntegerField()
    project_fee_status = models.CharField(
        max_length=100,
        choices=contract_doc_status,
        default=1
    )
    
    
    




    
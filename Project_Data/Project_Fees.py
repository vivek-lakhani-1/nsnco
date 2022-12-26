from django.db import models
from .project import *
# from client.Client import *
advance_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)

class Project_Fee(models.Model):
    project_id = models.ForeignKey(Project_Table,on_delete=models.DO_NOTHING)
    # client_id = models.ForeignKey(ClientTable,on_delete=models.DO_NOTHING)
    solution_fee = models.SmallIntegerField()
    Production_Advance = models.SmallIntegerField()
    Negotiated_Advance = models.SmallIntegerField()
    Final_Advance = models.SmallIntegerField()
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
    Post_Project_Client_Total_Payout = models.SmallIntegerField()
    project_fee_status = models.CharField(
        max_length=100,
        choices=contract_doc_status,
        default=1
    )
    
    
    




    
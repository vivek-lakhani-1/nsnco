from django.db import models

advance_status = (
   ("In-Progress","In-Progress"),
   ("Done","Done")
)
contract_doc_status = (
    ("SM","SM"),
    ("FM","FM")
)

class Project_Fee(models.Model):
    project_id = models.ForeignKey('Artist_Project.Project_Table',on_delete=models.DO_NOTHING,related_name='Project_Table0')
    client_id = models.ForeignKey('Client_Data.ClientTable',on_delete=models.DO_NOTHING,related_name='ClientTable3')
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
    
    
    




    
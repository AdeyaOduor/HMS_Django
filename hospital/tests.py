from django.test import TestCase
from hospital.models import models.Model


class PatientDischargeDetails(models.Model):
    def patientDetails(self):
        patientId=models.PositiveIntegerField(null=True)
        patientName=models.CharField(max_length=40)
        assignedDoctorName=models.CharField(max_length=40)
        
    def address(self):
        address = models.CharField(max_length=40)
        mobile = models.CharField(max_length=20,null=True)
        symptoms = models.CharField(max_length=100,null=True)
   
    def patientChargeSheet(self):
        admitDate=models.DateField(null=False)
        releaseDate=models.DateField(null=False)
        daySpent=models.PositiveIntegerField(null=False)
        roomCharge=models.PositiveIntegerField(null=False)
        medicineCost=models.PositiveIntegerField(null=False)
        doctorFee=models.PositiveIntegerField(null=False)
        OtherCharge=models.PositiveIntegerField(null=False)
        total=models.PositiveIntegerField(null=False)

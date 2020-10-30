from django.db import models


class Swap(models.Model):
    id = models.AutoField(primary_key=True)
    txHash = models.CharField(max_length=255)
    atoloAddress = models.CharField(max_length=256, default='')
    hdacAddress = models.CharField(max_length=1024, default='')
    code = models.CharField(max_length=18)
    msg = models.CharField(max_length=60)
    success = models.CharField(max_length=18)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.txHash

class KYC_Complete(models.Model):
    id = models.AutoField(primary_key=True)
    kycID = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.CharField(max_length=127)
    txHash = models.CharField(max_length=127, default='')
    kycLevel = models.CharField(max_length=11)
    status = models.CharField(max_length=127)
    comment = models.CharField(max_length=256)
    date_of_birth = models.CharField(max_length=256)
    gender = models.CharField(max_length=127)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.txHash

class KYC_Submit(models.Model):
    id = models.AutoField(primary_key=True)
    wallet_address = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255,unique=True)
    kyc_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    kycLevel = models.CharField(max_length=11)
    nationality = models.CharField(max_length=256)
    date_of_birth = models.CharField(max_length=256)
    id_type = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    photoid_res = models.CharField(max_length=1024)
    selfie_res = models.CharField(max_length=1024)
    contribution_type =  models.CharField(max_length=256)
    estimated_amount = models.CharField(max_length=256)
    created_at = models.CharField(max_length=256)
    
    def __str__(self):
        return self.email

class KYC_Reject(models.Model):
    id = models.AutoField(primary_key=True)
    kycID = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    status = models.CharField(max_length=256)
    kycLevel = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    updatedAt = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    date_of_birth = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    
    def __str__(self):
        return self.email
    
class AML(models.Model):
    amlID = models.CharField(max_length=255,primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    date_of_birth = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    gender = models.CharField(max_length=256)
    webhook_trigger = models.CharField(max_length=256)
    currentStatus = models.CharField(max_length=256)
    riskLevelSummary = models.CharField(max_length=256)
    riskLevel = models.CharField(max_length=256)
    riskIcon = models.CharField(max_length=256)

    def __str__(self):
        return self.email
   

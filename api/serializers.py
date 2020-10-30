
from rest_framework import serializers

from .models import Swap, KYC_Complete, KYC_Reject, KYC_Submit, AML

class SwapSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Swap
        fields = ('code', 'msg', 'success', 'txHash', 'createdAt', 'updatedAt')

class KYCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KYC_Complete
        fields = ('address', 'email', 'txHash', 'kycLevel', 'status','createdAt', 'updatedAt')


class KYC_SubmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KYC_Submit
        fields = ('first_name','last_name','kyc_level','email','nationality','date_of_birth','id_type','gender','photoid_res','selfie_res','userid','contribution_type','wallet_address','estimated_amount','projectId','created_at')

class KYC_RejectKYCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = KYC_Reject
        fields = ('status','comment','updated_at','first_name','last_name','nationality','date_of_birth','gender','email')

class AMLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AML
        fields = ('first_name','last_name','date_of_birth','email','amlID','nationality','gender','webhook_trigger','currentStatus','riskLevelSummary','riskLevel','riskIcon')
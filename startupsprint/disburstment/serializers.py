from rest_framework import serializers
from .models import Disbursement

class DisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disbursement
        fields = [
            'id', 
            'Loan', 
            'insurance_doc', 
            'payment_mode', 
            'net_disbursed_amount', 
            'disbursed_to_account_no', 
            'receipt_doc', 
            'status', 
            'response_timestamp'
        ]

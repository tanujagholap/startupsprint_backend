from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    useremail = serializers.EmailField(source='user.email', read_only=True)
    class Meta:
        model = Application
        fields = [
            'id', 'useremail', 'aadhaar_no', 'pan_no', 'type_of_employment',
            'business_title', 'business_type', 'business_address', 'gst_registration_no',
            'business_license_no', 'expected_average_annual_turnover', 'years_in_current_business',
            'collateral', 'status', 'application_timestamp', 'remark', 'credit_score'
        ]
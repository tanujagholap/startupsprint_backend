from rest_framework import serializers
from .models import Enquiry
import re
from datetime import date

class EnquirySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Enquiry
        fields = ['first_name','last_name','email','mobile','message','enquiry_date']

    def create(self, validated_data):
        if 'otp_entered' in validated_data:
            validated_data.pop('otp_entered')
        return super().create(validated_data)


    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name must contain only letters.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only letters.")
        return value

    def validate_mobile_number(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError("Mobile number must be 10 digits long.")
        return value

    def validate_message(self, value):
        if not value:
            raise serializers.ValidationError("Message cannot be empty.")
        return value

    def validate_inquiry_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Inquiry date cannot be in the future.")
        return value








    
from rest_framework import serializers
from .models import Application

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def validate_aadhaar_no(self, value):
        """
        Validate Aadhaar number.
        """
        if not value.isdigit() or len(value) != 12:
            raise serializers.ValidationError("Aadhaar number must be a 12-digit number.")
        return value

    def validate_pan_no(self, value):
        """
        Validate PAN number.
        """
        if len(value) != 10:
            raise serializers.ValidationError("PAN number must be a 10-character string.")
        return value

    def validate_years_in_current_business(self, value):
        """
        Validate years in current business.
        """
        if value < 0:
            raise serializers.ValidationError("Years in current business must be a positive integer.")
        return value

    def validate_credit_score(self, value):
        """
        Validate credit score.
        """
        if value is not None and (value < 300 or value > 900):
            raise serializers.ValidationError("Credit score must be between 300 and 900.")
        return value

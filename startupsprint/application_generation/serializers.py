from rest_framework import serializers
from .models import Document, Guarantor
from datetime import date  # Import the date class
import re  # Import the re module for email validation



class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'application', 'aadhaar_card', 'pan_card', 'business_address_proof_or_copy_of_rent_agreement', 
            'electricity_bill', 'msme_certificate', 'gst_certificate', 'udyog_aadhaar_registration', 
            'business_license', 'business_plan_or_proposal', 'three_year_itr_with_balance_sheet', 
            'collateral_document', 'stamp_duty', 'status', 'response_timestamp', 'remark'
        )

    def validate(self, data):
        max_upload_size = 2 * 1024 * 1024  # 2MB in bytes
        for field in self.fields:
            file = data.get(field)
            if file and hasattr(file, 'size'):
                if file.size > max_upload_size:
                    raise serializers.ValidationError(f"{field} size should not exceed 2MB.")
        return data




class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = (
            'application', 'relation_with_customer', 'name', 'dob', 'gender', 'email', 
            'address', 'city', 'state', 'country', 'pin_code', 'mobile', 'photo', 
            'profession', 'income_certificate', 'bank_name', 'current_account_no', 
            'passbook_copy', 'ifsc_code'
        )

    def validate_relation_with_customer(self, value):
        if not value:
            raise serializers.ValidationError("Relation with customer is required.")
        return value

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name is required.")
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters long.")
        return value

    def validate_dob(self, value):
        if value >= date.today():
            raise serializers.ValidationError("Date of birth must be in the past.")
        return value

    def validate_gender(self, value):
        if value not in ['male', 'female', 'transgender']:
            raise serializers.ValidationError("Gender must be one of 'male', 'female', or 'transgender'.")
        return value

    def validate_email(self, value):
        if value and not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def validate_address(self, value):
        if not value:
            raise serializers.ValidationError("Address is required.")
        return value

    def validate_city(self, value):
        if not value:
            raise serializers.ValidationError("City is required.")
        return value

    def validate_state(self, value):
        if not value:
            raise serializers.ValidationError("State is required.")
        return value

    def validate_country(self, value):
        if not value:
            raise serializers.ValidationError("Country is required.")
        return value

    def validate_pin_code(self, value):
        if value and (len(str(value)) != 6 or not str(value).isdigit()):
            raise serializers.ValidationError("Pin code must be exactly 6 digits.")
        return value

    def validate_mobile(self, value):
        if value and (len(value) != 10 or not value.isdigit()):
            raise serializers.ValidationError("Mobile number must be exactly 10 digits.")
        return value

    def validate_profession(self, value):
        if not value:
            raise serializers.ValidationError("Profession is required.")
        return value

    def validate_current_account_no(self, value):
        if not value:
            raise serializers.ValidationError("Current account number is required.")
        if len(value) > 20:
            raise serializers.ValidationError("Current account number cannot exceed 20 characters.")
        return value

    def validate_ifsc_code(self, value):
        if value and len(value) != 11:
            raise serializers.ValidationError("IFSC code must be exactly 11 characters.")
        return value

    def validate_file(self, file, field_name):
        max_upload_size = 2 * 1024 * 1024  # 2MB in bytes
        valid_mime_types = ['image/jpeg', 'image/png', 'application/pdf']
        
        if file.size > max_upload_size:
            raise serializers.ValidationError(f"{field_name} size should not exceed 2MB.")
        
        if file.content_type not in valid_mime_types:
            raise serializers.ValidationError(f"{field_name} should be a valid file type (jpg, png, pdf).")
        
        return file

    def validate_photo(self, value):
        return self.validate_file(value, "Photo")

    def validate_income_certificate(self, value):
        return self.validate_file(value, "Income Certificate")

    def validate_passbook_copy(self, value):
        return self.validate_file(value, "Passbook Copy")

    def validate(self, data):
        if not data.get('email') and not data.get('mobile'):
            raise serializers.ValidationError("Either email or mobile must be provided.")
        return data


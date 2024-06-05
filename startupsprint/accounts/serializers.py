from rest_framework import serializers
from .models import User
from datetime import date
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'mobile', 'dob', 'gender', 'permanent_address', 'current_address', 'photo', 'signature', 'role', 'password']

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name should only contain alphabetic characters.")
        if len(value) < 2:
            raise serializers.ValidationError("First name must be at least 2 characters long.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name should only contain alphabetic characters.")
        if len(value) < 2:
            raise serializers.ValidationError("Last name must be at least 2 characters long.")
        return value

    dob = serializers.DateField()

    def validate_dob(self, value):
        if value >= date.today():
            raise serializers.ValidationError("Date of birth cannot be in the future.")
        
        today = date.today()
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

        if age < 18:
            raise serializers.ValidationError("Age must be at least 18 years old.")
        if age > 60:
            raise serializers.ValidationError("Age must be at most 60 years old.")
        
        return value
    
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format.")
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            mobile=validated_data['mobile'],
            dob=validated_data['dob'],
            gender=validated_data['gender'],
            permanent_address=validated_data['permanent_address'],
            current_address=validated_data['current_address'],
            photo=validated_data.get('photo'),
            signature=validated_data.get('signature'),
            role=validated_data['role']
        )
        user.is_staff = True
        user.save()
        return user

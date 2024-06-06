from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'dob', 'gender', 'email', 
            'permanent_address', 'current_address', 'mobile', 'photo', 
            'signature', 'role', 'is_active'
        ]

from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name','username', 'dob', 'gender', 'email', 'permanent_address', 'current_address', 'mobile', 'photo', 'signature', 'role', 'is_active']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user

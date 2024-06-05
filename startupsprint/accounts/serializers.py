from rest_framework import serializers
from .models import User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'mobile', 'password', 'dob', 'gender', 'permanent_address', 'current_address', 'photo', 'signature', 'role')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        customer = User.objects.create_user(**validated_data)
        customer.is_active = False
        customer.save()
        return customer

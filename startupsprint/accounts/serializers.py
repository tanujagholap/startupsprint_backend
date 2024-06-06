from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'gender', 'dob', 'email', 'mobile', 'photo',
                  'permanent_address', 'current_address', 'signature', 'role', 'is_active')
        

    def create(self, validated_data):
        obj = User.objects.create_user(**validated_data)
        obj.is_active = True
        obj.save()
        return obj
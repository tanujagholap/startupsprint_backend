from rest_framework import serializers
from .models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['first_name', 'last_name', 'email', 'ratings', 'feedback_text']

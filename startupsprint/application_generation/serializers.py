from rest_framework import serializers
from .models import Application, Guarantor, Document

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class ApplicationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class GuarantorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guarantor
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'




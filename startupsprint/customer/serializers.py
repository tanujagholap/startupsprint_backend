from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = "__all__"

    def validate(self, data):

        if data.get('father_name') and len(data['father_name'].strip()) < 3:
            raise serializers.ValidationError({'father_name': 'Father name must be at least 3 characters long.'})

    
        if data.get('father_profession') and len(data['father_profession'].strip()) < 3:
            raise serializers.ValidationError({'father_profession': 'Father profession must be at least 3 characters long.'})

        
        if data.get('father_income', 0.0) < 0:
            raise serializers.ValidationError({'father_income': 'Father income cannot be negative.'})

        
        if data.get('mother_name') and len(data['mother_name'].strip()) < 3:
            raise serializers.ValidationError({'mother_name': 'Mother name must be at least 3 characters long.'})

        
        if data.get('mother_profession') and len(data['mother_profession'].strip()) < 3:
            raise serializers.ValidationError({'mother_profession': 'Mother profession must be at least 3 characters long.'})

        
        if data.get('mother_income', 0.0) < 0:
            raise serializers.ValidationError({'mother_income': 'Mother income cannot be negative.'})

        
        if data.get('marital_status') == 'married' and not data.get('spouse_name'):
            raise serializers.ValidationError({'spouse_name': 'Spouse name is required if marital status is married.'})
        if data.get('marital_status') != 'married' and data.get('spouse_name'):
            raise serializers.ValidationError({'spouse_name': 'Spouse name should be empty if marital status is not married.'})

    
        if data.get('marital_status') == 'married':
            if not data.get('spouse_profession'):
                raise serializers.ValidationError({'spouse_profession': 'Spouse profession is required if marital status is married.'})
            if data.get('spouse_income', 0.0) <= 0:
                raise serializers.ValidationError({'spouse_income': 'Spouse income must be greater than 0 if marital status is married.'})
            

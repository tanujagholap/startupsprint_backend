
from rest_framework import serializers

class EMICalculatorSerializer(serializers.Serializer):
    principal = serializers.DecimalField(max_digits=15, decimal_places=2)
    rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    tenure = serializers.IntegerField()

    def validate_principal(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan amount must be a positive number.")
        return value

    def validate_rate(self, value):
        if value <= 0 or value > 100:
            raise serializers.ValidationError("Interest rate must be between 0 and 100 percent.")
        return value

    def validate_tenure(self, value):
        if value <= 0:
            raise serializers.ValidationError("Loan term must be a positive number of years.")
        return value

    
    

# from rest_framework import serializers
# from customer.models import Bank
# from accounts.models import User
# from disburstment.models import Installment, Disbursement

# class BankSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bank
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

# class DisbursementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Disbursement
#         fields = '__all__'

# class InstallmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Installment
#         fields = '__all__'

# class CustomerSerializer(serializers.ModelSerializer):
#     bank = BankSerializer()
#     disbursements = DisbursementSerializer(many=True)
#     installments = InstallmentSerializer(many=True)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'bank', 'disbursements', 'installments']

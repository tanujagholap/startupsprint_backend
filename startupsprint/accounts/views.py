# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from customer.models import Bank
# from .serializers import BankSerializer, CustomerSerializer, InstallmentSerializer, DisbursementSerializer
# from accounts.models import User
# from disburstment.models import Installment, Disbursement

# class BankCompleteDetailApi(APIView):
#     def get(self, request, pk):
#         try:
#             obj = Bank.objects.get(user=pk)
#             serializer = BankSerializer(instance=obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Bank.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
    

# class DisbursementDetailApi(APIView):
#     def get(self, request, pk):
#         try:
#             obj = Disbursement.objects.get(user=pk)
#             serializer = DisbursementSerializer(instance=obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Disbursement.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        

# class InstallmentDetailApi(APIView):
#     def get(self, request, pk):
#         try:
#             obj = Installment.objects.get(user=pk)
#             serializer = InstallmentSerializer(instance=obj)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Installment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)



# class OnlyCustomerCompletaDetailApi(APIView):
#     def get(self, request):
#         customers = User.objects.filter(role="customer")
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


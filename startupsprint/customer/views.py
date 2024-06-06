from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bank
from .serializers import BankSerializer
from .models import Family
from .serializers import FamilySerializer

class BankView(APIView):
    def get(self, request, user_id):
        try:
            banks = Bank.objects.filter(user_id=user_id)
            serializer = BankSerializer(banks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Bank.DoesNotExist:
            return Response({'error': 'Bank data not found'}, status=status.HTTP_404_NOT_FOUND)


class FamilyView(APIView):
    def get(self, request, user_id):
        try:
            family = Family.objects.get(user_id=user_id)
            serializer = FamilySerializer(family)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Family.DoesNotExist:
            return Response({'error': 'Family data not found'}, status=status.HTTP_404_NOT_FOUND)

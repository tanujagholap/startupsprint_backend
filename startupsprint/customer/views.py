from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from .models import Family, Bank
from application_generation.models import Application
from .serializers import FamilySerializer, BankSerializer, ApplicationSerializer

class ApplicationAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                application = Application.objects.get(pk=pk)
                serializer = ApplicationSerializer(application)
            except Application.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            applications = Application.objects.filter(status='document_verified')
            serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data)

    def delete(self, request, pk=None):
        try:
            application = Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def more_details(request, pk=None):
    try:
        application = Application.objects.get(pk=pk)
    except Application.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if application.status == 'document_verified':
        family = Family.objects.filter(application=application)
        bank = Bank.objects.filter(application=application).first()
        family_data = FamilySerializer(family, many=True).data
        bank_data = BankSerializer(bank).data if bank else {}
        return Response({
            'application': ApplicationSerializer(application).data,
            'family': family_data,
            'bank': bank_data,
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'detail': 'Application is not document verified'
        }, status=status.HTTP_400_BAD_REQUEST)

class FamilyListCreateAPIView(APIView):
    def get(self, request):
        families = Family.objects.all()
        serializer = FamilySerializer(families, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get('document_verified', False):
                raise ValidationError('Document must be verified to add family details.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BankListCreateAPIView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            if not serializer.validated_data.get('document_verified', False):
                raise ValidationError('Document must be verified to add bank details.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

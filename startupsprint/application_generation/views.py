from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Application, Guarantor, Document
from .serializers import ApplicationSerializer, ApplicationCreateUpdateSerializer, GuarantorSerializer, DocumentSerializer
from customer.serializers import FamilySerializer, BankSerializer
from customer.models import Family, Bank

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

    def post(self, request):
        serializer = ApplicationCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            application = Application.objects.get(pk=pk)
        except Application.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ApplicationCreateUpdateSerializer(application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        guarantors = Guarantor.objects.filter(application=application)
        document = Document.objects.filter(application=application).first()
        guarantors_data = GuarantorSerializer(guarantors, many=True).data
        document_data = DocumentSerializer(document).data if document else {}
        # fetching family details
        family_obj = Family.objects.get(user_id=application.user_id)
        family_data = FamilySerializer(family_obj).data if family_obj else {}

        # fetching bank details
        bank_obj = Bank.objects.get(user_id=application.user_id)
        bank_data = BankSerializer(bank_obj).data if bank_obj else {}

        return Response({
            'application': ApplicationSerializer(application).data,
            'guarantors': guarantors_data,
            'document': document_data,
            'family': family_data,
            'bank': bank_data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'detail': 'Application is not document verified'
        }, status=status.HTTP_400_BAD_REQUEST)

class GuarantorAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                application = Application.objects.get(pk=pk)
                if application.status == 'document_verified':
                    guarantor = Guarantor.objects.filter(application=application)
                    serializer = GuarantorSerializer(guarantor, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'detail': 'Application is not document verified'}, status=status.HTTP_400_BAD_REQUEST)
            except Application.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # The post, put, and delete methods remain the same as before

class DocumentAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                application = Application.objects.get(pk=pk)
                if application.status == 'document_verified':
                    document = Document.objects.filter(application=application)
                    serializer = DocumentSerializer(document, many=True)
                    return Response(serializer.data)
                else:
                    return Response({'detail': 'Application is not document verified'}, status=status.HTTP_400_BAD_REQUEST)
            except Application.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




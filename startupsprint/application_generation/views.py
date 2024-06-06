from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document, Guarantor
from .serializers import DocumentSerializer, GuarantorSerializer
from django.http import Http404
from django.core.exceptions import ValidationError
from .models import Guarantor, Application


class DocumentListCreateAPIView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = self.get_object(pk)
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#for the Guarantor Model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Guarantor
from .serializers import GuarantorSerializer

   
 
class AddGuarantorToApplication(APIView):
    def get(self, request):
        guarantors = Guarantor.objects.all()
        serializer = GuarantorSerializer(guarantors, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        formData = request.data

        # Check if the input data is a dictionary
        if not isinstance(formData, dict):
            return Response({"error": "Please provide data for one guarantor."}, status=status.HTTP_400_BAD_REQUEST)

        application_id = formData.get('application')

        if not application_id:
            return Response({"error": "Application ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the application already has two guarantors
        existing_guarantors_count = Guarantor.objects.filter(application_id=application_id).count()

        if existing_guarantors_count >= 2:
            return Response({"error": "This application already has two guarantors."}, status=status.HTTP_400_BAD_REQUEST)

        # Create and validate the serializer
        serializer = GuarantorSerializer(data=formData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GuarantorRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Guarantor.objects.get(pk=pk)
        except Guarantor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        guarantor = self.get_object(pk)
        serializer = GuarantorSerializer(guarantor)
        return Response(serializer.data)

    def put(self, request, pk):
        guarantor = self.get_object(pk)
        serializer = GuarantorSerializer(guarantor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guarantor = self.get_object(pk)
        guarantor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

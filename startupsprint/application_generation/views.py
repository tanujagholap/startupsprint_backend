from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application, Document
from .serializers import ApplicationSerializer, DocumentSerializer
from django.http import FileResponse, Http404
import os


class AllApplicationsView(APIView):

    def get(self, request, format=None):
        applications = Application.objects.all()
        serializer = ApplicationSerializer(applications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ApplicationByUserView(APIView):

    def get(self, request, user_id, format=None):
        try:
            application = Application.objects.filter(user_id=user_id).order_by('-application_timestamp').first()
            if application:
                serializer = ApplicationSerializer(application)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Application not found for this user."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, user_id, format=None):
        request.data['user'] = user_id  # Add user_id to the request data
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApplicationByIdView(APIView):

    def get(self, request, application_id, format=None):
        try:
            application = Application.objects.get(id=application_id)
            serializer = ApplicationSerializer(application)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Application.DoesNotExist:
            return Response({"detail": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, application_id, format=None):
        try:
            application = Application.objects.get(id=application_id)
            serializer = ApplicationSerializer(application, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Application.DoesNotExist:
            return Response({"detail": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

class DocumentByApplicationView(APIView):

    def get(self, request, application_id, format=None):
        try:
            document = Document.objects.get(application_id=application_id)
            serializer = DocumentSerializer(document)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Document.DoesNotExist:
            return Response({"detail": "Document not found for this application."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, application_id, format=None):
        request.data['application'] = application_id  # Add application_id to the request data
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, application_id, format=None):
        try:
            document = Document.objects.get(application_id=application_id)
            serializer = DocumentSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Document.DoesNotExist:
            return Response({"detail": "Document not found for this application."}, status=status.HTTP_404_NOT_FOUND)


class DocumentByUserView(APIView):
    def get(self, request, user_id, format=None):
        try:
            application = Application.objects.filter(user_id=user_id).order_by('-application_timestamp').first()
            if application:
                documents = Document.objects.filter(application_id=application.id)
                document_list = []
                for doc in documents:
                    doc_data = DocumentSerializer(doc).data
                    doc_data['aadhaar_card_url'] = request.build_absolute_uri(settings.MEDIA_URL + doc.aadhaar_card.name)
                    doc_data['pan_card_url'] = request.build_absolute_uri(settings.MEDIA_URL + doc.pan_card.name)
                    # Add URLs for other documents similarly
                    document_list.append(doc_data)
                return Response(document_list, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Application not found for this user."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        

class ServeDocumentView(APIView):
    def get(self, request, file_path, format=None):
        try:
            document_path = os.path.join(settings.MEDIA_ROOT, file_path)
            if os.path.exists(document_path):
                return FileResponse(open(document_path, 'rb'))
            else:
                raise Http404("Document not found.")
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


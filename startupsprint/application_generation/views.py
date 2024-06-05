from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationAPI(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        obj = Application.objects.all()
        serializer = ApplicationSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        obj = Application.objects.get(pk=pk)
        serializer = ApplicationSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


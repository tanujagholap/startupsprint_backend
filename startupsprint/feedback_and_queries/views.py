from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeedBack
from .serializers import FeedBackSerializer

class FeedBackAPIView(APIView):
    def get(self, request):
        feedbacks = FeedBack.objects.all()
        serializer = FeedBackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

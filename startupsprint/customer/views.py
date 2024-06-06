from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FamilySerializer, Family
from django.shortcuts import get_object_or_404


class FamilyInfo(APIView):
    def get(self, request):
        families = Family.objects.all()
        serializer = FamilySerializer(families, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FamilyDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Family, pk=pk)

    def get(self, request, pk):
        family = self.get_object(pk)
        serializer = FamilySerializer(family)
        return Response(serializer.data)

    def put(self, request, pk):
        family = self.get_object(pk)
        serializer = FamilySerializer(family, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        family = self.get_object(pk)
        family.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

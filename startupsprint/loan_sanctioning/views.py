from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoanSerializer,Loan
from django.shortcuts import get_object_or_404

class LoanListCreateView(APIView):
    def get(self, request):
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Loan, pk=pk)

    def get(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    def put(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        loan = self.get_object(pk)
        serializer = LoanSerializer(loan, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        loan = self.get_object(pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

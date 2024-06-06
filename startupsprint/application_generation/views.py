from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Application
from .serializers import LoanApplicationSerializer
from django.core.mail import send_mail
from django.conf import settings


class LoanApplicationView(APIView):

    def get(self,request):
        obj = Application.objects.all()
        serializer = LoanApplicationSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = LoanApplicationSerializer(data=request.data)
        if serializer.is_valid():
            application = serializer.save()
            application_id = application.id  
            
            self.send_application_email(application_id, request.data.get('email'))
            
            return Response({"message": f"Loan application submitted successfully - Application ID: {application_id}"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def send_application_email(self, application_id, email):
        subject = f"Loan Application Submitted - Application ID: {application_id}"
        message = f"Welcome! Loan application submitted successfully. Please contact our support team for further assistance - Application ID: {application_id}"
        
        send_mail(
            subject=subject,
            message=message,
            from_email= settings.DEFAULT_FROM_EMAIL,
            recipient_list=['kabhipatil26@gmail.com'],
            fail_silently=False,
        )




# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Application
# from .serializers import LoanApplicationSerializer

# class LoanApplicationListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Application.objects.all()
#     serializer_class = LoanApplicationSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": f"Loan application created successfully. Application ID: {serializer.data.get('id')} "}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

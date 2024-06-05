from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StaffSerializer, User
from django.core.mail import send_mail



class RegisterStaffView(APIView):
    def post(self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                # Send email to the new staff member
                subject = 'Welcome to the Team'
                message = f'Hi {user.first_name},\n\nYou have been added as a staff member  your username is {user.email} and password is {user.password}.'
                recipient_list = [user.email]
                send_mail(subject, message, 'your_email@example.com', recipient_list)
                return Response({'message': 'Staff member created and email sent.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'User creation failed.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def get(self, request):
        objs = User.objects.all()
        serializer = StaffSerializer(objs, many=True)
        return Response(data=serializer.data, status=200)
    

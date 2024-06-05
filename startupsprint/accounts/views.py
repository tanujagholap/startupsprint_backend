from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import CustomerSerializer
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class CustomerRegistration(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            self.send_activation_email(request, customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def send_activation_email(self, request, customer):
        current_site = get_current_site(request)
        domain = current_site.domain
        uid = urlsafe_base64_encode(force_bytes(customer.pk))
        token = default_token_generator.make_token(customer)
        activation_link = reverse('customer-activation', kwargs={'uidb64': uid, 'token': token})
        activation_url = f"http://{domain}{activation_link}"
        
        subject = 'Activate Your Account'
        message = f"Hello {customer.email},\n\nPlease click on the link below to activate your account:\n\n{activation_url}"
        
        send_mail(subject, message, settings.EMAIL_HOST_USER, [customer.email])

class CustomerActivation(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            customer = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            customer = None

        if customer and default_token_generator.check_token(customer, token):
            customer.is_active = True
            customer.save()
            return Response({'message': 'Your account has been activated.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)



class CustomerDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        customer = request.user
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request):
        customer = request.user
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



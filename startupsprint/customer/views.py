from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client
from .serializers import EnquirySerializer
from django.conf import settings

account_sid = getattr(settings, 'TWILIO_ACCOUNT_SID')
auth_token = getattr(settings, 'TWILIO_AUTH_TOKEN')
verify_sid = getattr(settings, 'TWILIO_VERIFY_SID')
verified_number = "+918010144359"

client = Client(account_sid, auth_token)


class GenerateOTP(APIView):
    def post(self, request):
        mobile_number = request.data.get('mobile_number')
        try:
                client = Client(account_sid, auth_token)
                verification = client.verify.v2.services(verify_sid) \
                                    .verifications \
                                    .create(to=verified_number , channel='sms')
                print(verification.status)
                return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyAndSaveEnquiry(APIView):
    verify_sid = getattr(settings, 'TWILIO_VERIFY_SID')
    def post(self, request):
        try:
            otp_entered = request.data.get('otp')

            if not otp_entered:
                return Response({'error': ' OTP are required'}, status=status.HTTP_400_BAD_REQUEST)
            
            client = Client(account_sid, auth_token)
            verification = client.verify.v2.services(verify_sid) \
                                           .verification_checks \
                                           .create(to=verified_number, code=otp_entered)
            print(verification.status)

            if verification.status == 'approved':
                
                serializer = EnquirySerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






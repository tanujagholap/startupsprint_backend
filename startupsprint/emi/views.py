from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EMICalculatorSerializer


class EMICalculatorView(APIView):
    def post(self, request):
        serializer = EMICalculatorSerializer(data=request.data)
        if serializer.is_valid():
            principal = serializer.validated_data['principal']
            rate = serializer.validated_data['rate']
            tenure = serializer.validated_data['tenure']

            monthly_interest_rate = rate / 100 / 12
            number_of_payments = tenure * 12
            monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -number_of_payments))
    
            return Response({
                'monthly_interest_rate': round(rate),
                'number_of_payments': round(number_of_payments),
                'monthly_payment': round(monthly_payment, 2),
            
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
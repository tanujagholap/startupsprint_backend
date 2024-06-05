from django.urls import path
from .views import GenerateOTP,VerifyAndSaveEnquiry

urlpatterns = [
    path('otp/', GenerateOTP.as_view()),
    path('verify/', VerifyAndSaveEnquiry.as_view()),
    
]
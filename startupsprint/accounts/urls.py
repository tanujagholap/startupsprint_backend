# urls.py
from django.urls import path
from .views import CustomerRegistration, CustomerActivation, CustomerDetailView
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

urlpatterns = [
    path('api/register/', CustomerRegistration.as_view(), name='customer-registration'),
    path('api/activate/<str:uidb64>/<str:token>/', CustomerActivation.as_view(), name='customer-activation'),
    path('api/customer/', CustomerDetailView.as_view(), name='customer-detail'),
    path('access/', token_obtain_pair),
    path('refresh/', token_refresh)
]




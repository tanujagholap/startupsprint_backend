from django.urls import path
from .views import EMICalculatorView


urlpatterns = [
    path('calculate-emi/', EMICalculatorView.as_view(), name='calculate-emi'),
]

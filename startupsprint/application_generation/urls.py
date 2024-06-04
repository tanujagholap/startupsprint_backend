from django.urls import path
from .views import (ApplicationAPIView, more_details, GuarantorAPIView, DocumentAPIView)

urlpatterns = [
    path('application/', ApplicationAPIView.as_view(), name='application-list'),
    path('application/<int:pk>/', ApplicationAPIView.as_view(), name='application-detail'),
    path('application/<int:pk>/more_details/', more_details, name='more-details'),
    path('guarantor/', GuarantorAPIView.as_view(), name='guarantor-list'),
    path('guarantor/<int:pk>/', GuarantorAPIView.as_view(), name='guarantor-detail'),
    path('document/', DocumentAPIView.as_view(), name='document-list'),
    path('document/<int:pk>/', DocumentAPIView.as_view(), name='document-detail'),
]



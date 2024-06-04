from django.urls import path
from .views import FamilyListCreateAPIView, BankListCreateAPIView

urlpatterns = [
    path('family/', FamilyListCreateAPIView.as_view(), name='family-list-create'),
    path('bank/', BankListCreateAPIView.as_view(), name='bank-list-create'),
]

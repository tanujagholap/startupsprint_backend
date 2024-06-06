from django.urls import path
from .views import FamilyView
from .views import BankView

urlpatterns = [
    path('familys/user/<int:user_id>/', FamilyView.as_view(), name='user-family'),
    path('banks/user/<int:user_id>/', BankView.as_view(), name='user-banks'),
]

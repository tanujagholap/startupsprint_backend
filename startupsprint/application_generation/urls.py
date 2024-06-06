from django.urls import path
from .views import LoanApplicationView

urlpatterns = [
    path("loanapplicationform/", LoanApplicationView.as_view()),
    
]
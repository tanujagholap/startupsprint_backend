from django.urls import path
from .views import LoanListCreateView, LoanDetailView

urlpatterns = [
    path('loan/', LoanListCreateView.as_view(), name='loan-list-create'),
    path('loan/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
]

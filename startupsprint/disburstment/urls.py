
from django.urls import path
from .views import DisbursementView

urlpatterns = [
    path('disbursement/', DisbursementView.as_view(), name='disbursement_list'),
]
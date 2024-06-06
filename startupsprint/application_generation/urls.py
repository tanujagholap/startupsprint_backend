from django.urls import path
from .views import (DocumentListCreateAPIView, DocumentRetrieveUpdateDestroyAPIView,  GuarantorRetrieveUpdateDestroyAPIView,
                
            
                AddGuarantorToApplication
)

urlpatterns = [
    path('documents/', DocumentListCreateAPIView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyAPIView.as_view(), name='document-detail'),
    
    path('guarantors/<int:pk>/', GuarantorRetrieveUpdateDestroyAPIView.as_view(), name='guarantor-detail'),
    path('applications/add-guarantor/', AddGuarantorToApplication.as_view(), name='add-guarantor'),
]










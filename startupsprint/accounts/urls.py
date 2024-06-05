

from django.urls import path
from .views import RegisterStaffView



urlpatterns = [
    path('staff/', RegisterStaffView.as_view(), name='register-staff'),
]

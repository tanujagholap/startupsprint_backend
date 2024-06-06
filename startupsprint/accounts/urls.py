from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserInfo.as_view(), name='application-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='application-detail'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserInfo.as_view(), name='family-list'),
    path('user/<int:pk>/', UserDetail.as_view(), name='family-detail'),
]
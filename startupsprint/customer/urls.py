from django.urls import path
from .views import *


urlpatterns = [
    path('family/', FamilyInfo.as_view(), name='family-list'),
    path('family/<int:pk>/', FamilyDetail.as_view(), name='family-detail'),
]
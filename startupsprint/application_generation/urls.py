from django.urls import path
from .views import ApplicationAPI

urlpatterns = [
    path('application/', ApplicationAPI.as_view()),
    path('application/<pk>/', ApplicationAPI.as_view()),
]
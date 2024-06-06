from django.urls import path
from .views import FeedBackAPIView

urlpatterns = [
    path('feedback/', FeedBackAPIView.as_view(), name='feedback-list-create'),
]

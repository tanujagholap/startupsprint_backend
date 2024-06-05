

from django.urls import path
from .views import EMIReminder


urlpatterns = [
    path('emi-reminder/', EMIReminder.as_view() ),
]

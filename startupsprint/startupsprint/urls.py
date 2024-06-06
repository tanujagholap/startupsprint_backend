from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include('customer.urls')),
    path('a1/',include('feedback_and_queries.urls')),
    path('a1/',include('disburstment.urls')),
    path('a1/',include('loan_sanctioning.urls'))
]

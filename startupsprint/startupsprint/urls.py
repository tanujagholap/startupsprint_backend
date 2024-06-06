
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include('accounts.urls')),
    path('a1/',include('application_generation.urls')),
    path('a1/',include('customer.urls')),
]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/', include('emi.urls')),
    path('a1/', include('customer.urls')),
    path('a1/', include('application_generation.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




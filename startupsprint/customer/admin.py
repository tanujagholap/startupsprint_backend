from django.contrib import admin
from .models import Enquiry
from .models import Family,Bank
# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Family)
admin.site.register(Bank)

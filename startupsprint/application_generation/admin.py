from django.contrib import admin
from .models import Document,Application,Guarantor

# Register your models here.
admin.site.register(Document)
admin.site.register(Application)
admin.site.register(Guarantor)


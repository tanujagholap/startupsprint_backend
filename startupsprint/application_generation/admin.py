from django.contrib import admin
from .models import Application, Guarantor, Document

admin.site.register(Application)
admin.site.register(Guarantor)
admin.site.register(Document)
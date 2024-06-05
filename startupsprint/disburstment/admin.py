from django.contrib import admin
from .models import Disbursement, Installment, Defaulter




admin.site.register(Defaulter)
admin.site.register(Installment)
admin.site.register(Disbursement)

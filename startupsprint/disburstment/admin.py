from django.contrib import admin
from .models import Disbursement
from .models import Installment


class ModelDisburstment(admin.ModelAdmin):
    fieldset = 'all'

admin.site.register(Disbursement, ModelDisburstment)

class ModelInstallment(admin.ModelAdmin):
    fieldset = 'all'
admin.site.register(Installment, ModelInstallment)


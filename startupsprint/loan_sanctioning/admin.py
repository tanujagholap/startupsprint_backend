from django.contrib import admin
from .models import Loan

# Register your models here.
class ModelLoan(admin.ModelAdmin):
    fieldset = 'all'
admin.site.register(Loan, ModelLoan)

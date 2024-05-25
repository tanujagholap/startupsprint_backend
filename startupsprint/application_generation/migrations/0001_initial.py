# Generated by Django 5.0.6 on 2024-05-25 08:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_no', models.CharField(blank=True, default=0, max_length=12)),
                ('pan_no', models.CharField(blank=True, default=0, max_length=10)),
                ('type_of_employment', models.CharField(blank=True, choices=[('', ''), ('self_employed', 'self_employed'), ('salaried', 'salaried')], default=0, max_length=250)),
                ('business_title', models.CharField(blank=True, default=0, max_length=250)),
                ('business_type', models.CharField(blank=True, choices=[('', ''), ('manufacturing', 'manufacturing'), ('trading', 'trading'), ('service', 'service')], default=0, max_length=250)),
                ('business_address', models.TextField(blank=True, default=0)),
                ('gst_registration_no', models.CharField(blank=True, default=0, max_length=50)),
                ('business_license_no', models.CharField(blank=True, default=0, max_length=50)),
                ('expected_average_annual_turnover', models.CharField(blank=True, default=0, max_length=250)),
                ('years_in_current_business', models.IntegerField(blank=True, default=0)),
                ('collateral', models.CharField(blank=True, default=0, max_length=250)),
                ('status', models.CharField(choices=[('', ''), ('generated', 'generated'), ('document_verified', 'document_verified'), ('sanctioned', 'sanctioned'), ('disbursed', 'disbursed'), ('rejected', 'rejected')], default=0, max_length=250)),
                ('application_timestamp', models.DateTimeField(auto_now_add=True)),
                ('remark', models.CharField(blank=True, default=0, max_length=250)),
                ('credit_score', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar_card', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('pan_card', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('business_address_proof_or_copy_of_rent_agreement', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('electricity_bill', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('msme_certificate', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('gst_certificate', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('udyog_aadhaar_registration', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('business_license', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('business_plan_or_proposal', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('three_year_itr_with_balance_sheet', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('collateral_document', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('stamp_duty', models.FileField(blank=True, default=0, upload_to='customer/document/')),
                ('status', models.CharField(blank=True, choices=[('', ''), ('pending', 'pending'), ('done', 'done'), ('rejected', 'rejected')], default=0, max_length=250)),
                ('response_timestamp', models.DateTimeField(auto_now=True)),
                ('remark', models.CharField(blank=True, default=0, max_length=250)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='application_generation.application')),
            ],
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_with_customer', models.CharField(blank=True, default=0, max_length=250)),
                ('name', models.CharField(blank=True, default=0, max_length=150)),
                ('dob', models.DateField(blank=True, default='2000-12-12')),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female'), ('transgender', 'transgender')], default=0, max_length=50)),
                ('email', models.EmailField(blank=True, default=0, max_length=254)),
                ('address', models.TextField(blank=True, default=0, max_length=250)),
                ('city', models.CharField(blank=True, default=0, max_length=50)),
                ('state', models.CharField(blank=True, default=0, max_length=50)),
                ('country', models.CharField(blank=True, default=0, max_length=250)),
                ('pin_code', models.IntegerField(blank=True, default=0)),
                ('mobile', models.CharField(blank=True, default=0, max_length=10)),
                ('photo', models.ImageField(blank=True, default=0, upload_to='customer/guarantor/')),
                ('profession', models.CharField(blank=True, default=0, max_length=250)),
                ('income_certificate', models.FileField(blank=True, default=0, upload_to='customer/guarantor/')),
                ('bank_name', models.CharField(blank=True, default=0, max_length=250)),
                ('current_account_no', models.CharField(blank=True, default=0, max_length=20)),
                ('passbook_copy', models.FileField(blank=True, default=0, upload_to='customer/guarantor/')),
                ('ifsc_code', models.CharField(blank=True, default=0, max_length=20)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guarantors', to='application_generation.application')),
            ],
        ),
    ]
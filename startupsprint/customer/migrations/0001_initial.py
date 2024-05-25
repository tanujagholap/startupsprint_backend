# Generated by Django 5.0.6 on 2024-05-25 08:59

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('message', models.TextField()),
                ('enquiry_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('rejected', 'rejected')], max_length=10)),
                ('response_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('account_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ifsc_code', models.CharField(blank=True, default='', max_length=20)),
                ('passbook_copy', models.ImageField(blank=True, null=True, upload_to='customer/bank/')),
                ('bank_address', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(blank=True, default='', max_length=30)),
                ('father_profession', models.CharField(blank=True, default='', max_length=30)),
                ('father_income', models.FloatField(blank=True, default=0.0)),
                ('father_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN')),
                ('mother_name', models.CharField(blank=True, default='', max_length=30)),
                ('mother_profession', models.CharField(blank=True, default='', max_length=30)),
                ('mother_income', models.FloatField(blank=True, default=0.0)),
                ('mother_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN')),
                ('marital_status', models.CharField(choices=[('married', 'married'), ('unmarried', 'unmarried'), ('divorced', 'divorced')], default='unmarried', max_length=20)),
                ('spouse_name', models.CharField(blank=True, default='', max_length=30)),
                ('spouse_income', models.FloatField(blank=True, default=0.0)),
                ('spouse_profession', models.CharField(blank=True, default='', max_length=30)),
                ('spouse_contact', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='IN')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='family', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

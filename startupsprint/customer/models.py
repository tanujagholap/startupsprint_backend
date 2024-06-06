from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Enquiry (models.Model):
    ENQUIRY_STATUS = [
        ('pending', 'pending'),
        ('done', 'done'),
        ('rejected', 'rejected')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20) 
    email = models.EmailField()
    mobile = PhoneNumberField(region='IN')
    message = models.TextField()
    enquiry_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False) 
    status = models.CharField(max_length=10, choices=ENQUIRY_STATUS) 
    response_timestamp = models.DateTimeField(blank=True, null=True)


class Family(models.Model):
    MARITAL_STATUS_CHOICES = [
         ('married', 'married'), 
         ('unmarried', 'unmarried'), 
         ('divorced', 'divorced')
    ]
    user = models.OneToOneField('accounts.User', on_delete=models. CASCADE, related_name='family') 
    father_name = models.CharField(max_length=30, blank=True, default='')
    father_profession = models.CharField(max_length=30, blank=True, default='')
    father_income = models.FloatField(blank=True, default=0.0)
    father_contact = PhoneNumberField(region='IN', blank=True, null=True)
    mother_name = models.CharField(max_length=30, blank=True, default='') 
    mother_profession=models.CharField(max_length=30, blank=True, default='')
    mother_income = models.FloatField(blank=True, default=0.0)
    mother_contact = PhoneNumberField(region='IN', blank=True, null=True)
    marital_status = models.CharField(max_length=20, default='unmarried', choices=MARITAL_STATUS_CHOICES) 
    spouse_name = models.CharField(max_length=30, default='', blank=True)
    spouse_income = models.FloatField(default=0.0, blank=True)
    spouse_profession= models.CharField(max_length=30, blank=True, default='')
    spouse_contact = PhoneNumberField(region='IN', blank=True, null=True)
    
    def clean(self):
        # Validation for father_name
        if self.father_name and len(self.father_name.strip()) < 3:
            raise ValidationError({'father_name': 'Father name must be at least 3 characters long.'})

        
        if self.father_profession and len(self.father_profession.strip()) < 3:
            raise ValidationError({'father_profession': 'Father profession must be at least 3 characters long.'})

    
        if self.father_income < 0:
            raise ValidationError({'father_income': 'Father income cannot be negative.'})

        

        if self.mother_name and len(self.mother_name.strip()) < 3:
            raise ValidationError({'mother_name': 'Mother name must be at least 3 characters long.'})

        
        if self.mother_profession and len(self.mother_profession.strip()) < 3:
            raise ValidationError({'mother_profession': 'Mother profession must be at least 3 characters long.'})

    
        if self.mother_income < 0:
            raise ValidationError({'mother_income': 'Mother income cannot be negative.'})


        
        if self.marital_status == 'married' and not self.spouse_name:
            raise ValidationError({'spouse_name': 'Spouse name is required if marital status is married.'})
        if self.marital_status != 'married' and self.spouse_name:
            raise ValidationError({'spouse_name': 'Spouse name should be empty if marital status is not married.'})

        
        if self.marital_status == 'married':
            if not self.spouse_profession:
                raise ValidationError({'spouse_profession': 'Spouse profession is required if marital status is married.'})
            if self.spouse_income <= 0:
                raise ValidationError({'spouse_income': 'Spouse income must be greater than 0 if marital status is married.'})


    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)


class Bank(models.Model):

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='banks') 
    bank_name = models.CharField(max_length=30, default='', blank=True, null=True) 
    account_number = models.CharField(max_length=20, default='', blank=True, null=True) 
    ifsc_code = models.CharField(max_length=20, blank=True, default='')
    passbook_copy = models.ImageField(upload_to='customer/bank/', blank=True, null=True) 
    bank_address = models.TextField(blank=True, null=True)

from celery import shared_task
from .models import Installment
from datetime import date, timedelta
from django.core.mail import send_mail



@shared_task
def check_for_upcoming_installments():
    today = date.today()
    upcoming_date = today + timedelta(days=5)
    
    # Check for installments due in the next 5 days
    upcoming_installments = Installment.objects.filter(
        status='pending', 
        installment_expected_date__gte=today, 
        installment_expected_date__lte=upcoming_date
    )
    
    for installment in upcoming_installments:
        # Assuming there is a related user and email field
        user_email = installment.Loan.application.user.email
        send_upcoming_notification_email(user_email, installment)
    
    return f"Checked {upcoming_installments.count()} upcoming installments."

def send_upcoming_notification_email(to_email, installment):
    subject = "Upcoming Installment Reminder"
    message = f"Dear {installment.Loan.application.user.email},\n\n" \
              f"Your installment number {installment.installment_no} for loan {installment.Loan.id} is due on {installment.installment_expected_date}.\n" \
              f"Please ensure the payment before {installment.installment_paid_date}. \n" \
              f"Your Installemnt amount is {installment.monthly_installment_amount}Rs. \n" \
              f"to avoid penalties which is {installment.penalty_amount}Rs.\n\n" \
              f"Thank you."
    from_email = "no-reply@example.com"
    recipient_list = [to_email]

    try:
        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
        )
        print(f"Upcoming reminder sent to {to_email}")
    except Exception as e:
        print(f"Error sending upcoming email to {to_email}: {e}")

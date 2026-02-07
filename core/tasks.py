from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage

@shared_task
def send_email(full_password_reset_url, email):

    email_body = f'Reset your password using the link below:\n\n\n{full_password_reset_url}'

    email_message = EmailMessage(
        'Reset your password', # email subject
        email_body,
        settings.EMAIL_HOST_USER, # email sender
        [email] # email  receiver 
    )

    email_message.fail_silently = True
    email_message.send()

@shared_task
def greet():
    print("Hello, this is a test task from Celery Beat!")
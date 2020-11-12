from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, emails, from_email=None, html_message=None):
    return send_mail(subject, message, from_email, emails, html_message=html_message, fail_silently=False)

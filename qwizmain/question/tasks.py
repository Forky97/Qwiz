from .models import Question
from django.contrib.auth.models import User
from celery import shared_task
from django.core.mail import send_mail




@shared_task
def file_write():
    with open('test.txt','w') as f:
        f.write(f'task complete\n')

@shared_task
def send_mail_task(subject, message, email_from, recipient_list):
    send_mail(subject,message,email_from,recipient_list)


@shared_task
def top_users():
    top_users = User.objects.order_by('-raiting')[:10]



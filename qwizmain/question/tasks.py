from .models import Question
from .models import CustomUser
from celery import shared_task
from django.core.mail import send_mail
from django.db.models import F
from .serializers import CumstomUserSerializer





@shared_task
def file_write():
    with open('test.txt','w') as f:
        f.write(f'task complete\n')

@shared_task
def send_mail_task(subject, message, email_from, recipient_list):
    send_mail(subject,message,email_from,recipient_list)


@shared_task
def top_users():
    top_users = CustomUser.objects.order_by(F('raiting').desc(nulls_last=True)).values('custom_user__username', 'raiting')[:10]
    print(top_users)



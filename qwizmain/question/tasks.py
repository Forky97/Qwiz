from .models import Question
from .models import CustomUser
from celery import shared_task
from django.core.mail import send_mail
from django.db.models import F
from .serializers import CumstomUserSerializer
import  redis
from django.core.serializers import serialize,deserialize






@shared_task
def file_write():
    with open('test.txt','w') as f:
        f.write(f'task complete\n')

@shared_task
def send_mail_task(subject, message, email_from, recipient_list):
    send_mail(subject,message,email_from,recipient_list)


@shared_task
def show_top10():
    '''получение топ 10 юзеров'''
    top_users = CustomUser.objects.order_by('-raiting')[:10]

    serialized_obj = serialize('json',top_users)

    with redis.Redis(host='localhost',port=6379,db=0) as red:
        red.set('top10',serialized_obj)
        red.expire('mykey', 40)

    return






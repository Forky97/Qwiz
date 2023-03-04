from .models import Question
from django.contrib.auth.models import User
from celery import shared_task




@shared_task
def file_write():
    with open('test.txt','w') as f:
        f.write(f'task complete\n')

@shared_task
def count_widgets():
    return Question.objects.count()


@shared_task
def top_users():
    top_users = User.objects.order_by('-raiting')[:10]



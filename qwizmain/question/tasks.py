from .models import Question

from celery import shared_task




@shared_task
def file_write():
    with open('test.txt','w') as f:
        f.write(f'task complete\n')

@shared_task
def count_widgets():
    return Question.objects.count()


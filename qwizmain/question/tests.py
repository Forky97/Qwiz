from django.test import TestCase
from .models import Question,CustomUser
from django.contrib.auth.models import User
from django.db import models
from django.core.serializers import serialize,deserialize
import redis
from .tasks import *



class QuestionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создание тестовых данных
        Question.objects.create(
            question='Какой год был основан город Москва?',
            a1='1147',
            a2='1200',
            a3='1300',
            a4='1400',
            correct='1'
        )

        user = User.objects.create_user(
            username='dima',
            email='dima@mail.ru',
            password='demo'

        )


        CustomUser.objects.create(
            custom_user = user,
        )

    def test_question_content(self):
        question = Question.objects.get(id=1)
        expected_question = f'Вопрос {question.id} про {question.question}'
        print(question,expected_question)
        self.assertEqual(expected_question, str(question))

    def test_question_choices(self):
        question = Question.objects.get(id=1)
        choices = dict(question.choices_var)
        expected_choices = {
            '1': '1',
            '2': '2',
            '3': '3',
            '4': '4'
        }
        self.assertEqual(choices, expected_choices)

    def test_question_correct_answer(self):
        question = Question.objects.get(id=1)
        self.assertEqual(question.correct, '1')


    def test_question_str(self):
        question = Question.objects.get(id=1)
        self.assertEqual(str(question), f'Вопрос {question.id} про {question.question}')

    def test_custom_user_correct(self):
        all_id = CustomUser.objects.get(id=1)
        self.assertEqual(str(all_id),f'dima : 0')


    def test_user_corect(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username,'dima')

    def test_custom_user_corect_raiting(self):
        custom_user = CustomUser.objects.get(id=1)
        self.assertEqual(custom_user.raiting,0)


    def test_redis_connect(self):
        with redis.Redis(host='localhost',port=6379,db=0) as red:
            red.set('key',20)
            new_value = red.incr('key')
        self.assertEqual(new_value,21)
from django.test import TestCase
from .models import Question,CustomUser



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
        self.assertEqual(str(all_id),f'admin : 15')

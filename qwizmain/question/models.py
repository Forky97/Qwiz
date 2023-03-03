from django.db import models





class Question (models.Model):
    choices_var = [('1', '1',),
                   ('2', '2'),
                   ('3', '3'),
                   ('4', '4')

                   ]

    question = models.CharField(max_length=500)
    a1=models.CharField(max_length=300,verbose_name='ответ_1')
    a2 = models.CharField(max_length=300,verbose_name='ответ_2')
    a3 = models.CharField(max_length=300,verbose_name='ответ_3')
    a4 = models.CharField(max_length=300,verbose_name='ответ_4')
    correct = models.CharField(choices=choices_var,max_length=10)





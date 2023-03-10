# Generated by Django 4.1.7 on 2023-03-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('a1', models.CharField(max_length=300, verbose_name='ответ_1')),
                ('a2', models.CharField(max_length=300, verbose_name='ответ_2')),
                ('a3', models.CharField(max_length=300, verbose_name='ответ_3')),
                ('a4', models.CharField(max_length=300, verbose_name='ответ_4')),
                ('correct', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=10)),
            ],
        ),
    ]

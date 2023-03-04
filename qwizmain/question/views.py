from django.shortcuts import render
from django.views import View
from .forms import SignInForm,SignUpForm,ContactForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Question,CustomUser
from random import randint as ri
from django.core.mail import send_mail
from django.contrib.auth.models import User









class BaseHelloView(View):


    def get(self,request):

        return render(request,'home.html')


class SignInView(View):

    def get(self,request):
        form = SignInForm()

        return render(request,'signin.html',context={'form': form})



    def post(self,request):
        recieve_post_form  = SignInForm(request.POST)
        if recieve_post_form.is_valid():
            username = recieve_post_form.cleaned_data['username']
            password = recieve_post_form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:

                messages.error(request, 'Неправильный логин или пароль')

        form  = SignInForm()
        return render(request,'signin.html',context={'form': form})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)


                CustomUser.objects.create(custom_user=user)

                return HttpResponseRedirect('/')

        return render(request, 'signup.html', context={
            'form': form,
        })



class QuestionDetailView(View):

    def get(self,request):
        message = 'Выберите пожалуйства правильный ответ '

        count = Question.objects.count()
        question  = Question.objects.get(id=ri(1,count))


        return render(request,'question_detail.html',context={'question':question,
                                                              'message':message,})



    def post(self,request):

        answer = request.POST.get('answer')
        print(answer)
        count = Question.objects.count()
        question = Question.objects.get(id=ri(1, count))


        if answer[0]==answer[1]:
            message = 'Вы ответили правильно'


            return render(request, 'question_detail.html',context={'question':question,
                                                                   'message':message})

        else:
            message = None
            return render(request, 'question_detail.html', context={'question': question,
                                                                    'message':message,})






class ContactView(View):

    def get(self,request):
        form = ContactForm()



        return render(request,'contact.html',context={'form':form,
                                                      })




    def post(self,request):
        ...

    # from django.core.mail import send_mail
    #
    # # Определение параметров отправки электронной почты
    # subject = 'Тема письма'
    # message = 'Текст письма.'
    # email_from = 'от кого'
    # recipient_list = ['адрес1@mail.ru', 'адрес2@mail.ru']
    #
    # # Отправка электронной почты
    # send_mail(subject, message, email_from, recipient_list)

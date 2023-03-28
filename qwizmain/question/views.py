from django.shortcuts import render
from django.views import View
from .forms import SignInForm,SignUpForm,ContactForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Question,CustomUser
from random import randint as ri
from django.core.mail import send_mail
from django.views.generic.base import RedirectView
from django.urls import reverse
from .tasks import send_mail_task,show_top10
from django.http import HttpResponse
import redis
from django.core.serializers import deserialize





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

        question  = Question.objects.order_by('?').first()


        CustomUserRaiting = CustomUser.objects.get(custom_user=request.user)



        return render(request,'question_detail.html',context={'question':question,
                                                              'message':message,
                                                              'custom_user':CustomUserRaiting})



    def post(self,request):

        answer = request.POST.get('answer')
        question = Question.objects.order_by('?').first()
        CustomUserRaiting = CustomUser.objects.get(custom_user=request.user)


        if answer[0]==answer[1]:
            message = 'Вы ответили правильно'
            CustomUserRaiting.raiting +=1
            CustomUserRaiting.save()


            return render(request, 'question_detail.html',context={'question':question,
                                                                   'message':message,
                                                                   'custom_user':CustomUserRaiting,})

        else:
            message = None
            return render(request, 'question_detail.html', context={'question': question,
                                                                    'message':message,
                                                                    'custom_user':CustomUserRaiting,})





class ContactView(View):

    def get(self,request):
        form = ContactForm()



        return render(request,'contact.html',context={'form':form,
                                                      })




    def post(self,request):
        recieve_form = ContactForm(request.POST)
        if recieve_form.is_valid():
            subject = recieve_form.data.get('topic')
            message = recieve_form.data.get('text')
            email_from = recieve_form.data.get('your_email')
            recipient_list =['inginerii.biomedicale@gmail.com']

            send_mail_task.delay(subject, message, email_from, recipient_list)

            return HttpResponseRedirect(reverse('success'))


        return render(request, 'contact.html', context={'form': recieve_form,
                                                            })


class Top10(View):
    def get(self,request):
    # try:
        with redis.Redis(host='localhost', port=6379, db=0) as red:
            top_users = red.get('top10')

            deserialized_obj = [d.object for d in deserialize('json', top_users)]

            return render(request,'rating.html',context={'top_users': deserialized_obj})
        # except:
        #     return render(request,'home.html')


def Success(request):

    return render(request,'success.html')







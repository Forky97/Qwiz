from django.shortcuts import render
from django.views import View
from .forms import SignInForm,SignUpForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Question
from random import randint as ri






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
                return HttpResponseRedirect('/')
        return render(request, 'signup.html', context={
            'form': form,
        })



class QuestionDetailView(View):

    def get(self,request):
        count = Question.objects.count()
        question  = Question.objects.get(id=ri(1,count))


        return render(request,'question_detail.html',context={'question':question})



    def post(self,request):
        ...





class ContactView(View):

    def get(self,request):
        ...




    def post(self,request):
        ...

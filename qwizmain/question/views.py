from django.shortcuts import render
from django.views import View
from .forms import SignInForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect





class BaseHelloView(View):


    def get(self,request):

        return render(request,'home.html')


class SignInView(View):

    def get(self,request):
        recieve_form = SignInForm()

        return render(request,'signin.html',context={'form:':recieve_form})


    def post(self,request):
        recieve_post_form  = SignInForm(request.POST)
        if recieve_post_form.is_valid():
            username = recieve_post_form.cleaned_data['username']
            password = recieve_post_form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')

        return render(request,'signin.html')








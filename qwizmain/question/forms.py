from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate




class SignInForm(forms.Form):

    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder':'введите логин'
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'placeholder':'введите пароль'
        }),
    )


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder':'введите логин'
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'placeholder':'введите пароль'
        }),
    )

    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'placeholder': 'введите пароль'
        }),
    )


    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )



    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()

        auth = authenticate(**self.cleaned_data)
        return auth


class ContactForm(forms.Form):
    topic = forms.CharField(max_length=100,required=True,widget=forms.TextInput(attrs={"id":"theme",
                                                                                       "placeholder":"Тема",
                                                                                       "class":"form-control"}))
    text = forms.CharField(max_length=100, required=True, widget=forms.Textarea(attrs={"id": "theme",
                                                                                         "placeholder": "таше сообщение",
                                                                                         "class": "form-control"}))
    your_email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={"id": "theme",
                                                                                         "placeholder": "ваша почта",
                                                                                         "class": "form-control"}))
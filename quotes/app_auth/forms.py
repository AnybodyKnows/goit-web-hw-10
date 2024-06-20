from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, CharField,  TextInput,  EmailInput, PasswordInput


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = CharField(max_length=25, min_length=4, required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    pwd1 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))
    pwd2 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'pwd1', 'pwd2')


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    pwd = CharField(required=True, widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'pwd')

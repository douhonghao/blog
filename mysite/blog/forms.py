from django import forms


#from .models import Treasure


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=64)
    password = forms.CharField(label='密 码',

                               widget=forms.PasswordInput())

from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from .models import TaskUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {'email': 'Email ID'}
        USERNAME_FIELD = 'email'

   


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_('password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-pasword','class':'form-control'}))

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskUser
        fields = ['taskdetails', 'assignee', ]


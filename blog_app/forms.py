from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm 
from .models import post, comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class postform(ModelForm):
    class Meta:
        model = post
        fields = ['Topic', 'post', 'image']

class commentform(ModelForm):
    class Meta:
        model = comment
        fields = ['comment']

class UserCreateForm(UserCreationForm):
    email = models.EmailField(unique=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    class Meta:
        model = User
        fields =  ['username', 'email' , 'first_name', 'last_name', 'password1', 'password2']
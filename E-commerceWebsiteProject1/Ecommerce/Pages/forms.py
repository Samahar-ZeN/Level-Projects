from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Pages.models import *




#.............ContactusPage-Form................#
class contactusform(ModelForm):
    class Meta:
        model = ContactusPage
        fields = ['name', 'email', 'message']






#..............SignupPage-Form.................#
class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
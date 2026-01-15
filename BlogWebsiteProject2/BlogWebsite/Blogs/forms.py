from django.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Blogs.models import *






#.............ContactusPage-Form................#
class contactusform(ModelForm):
    class Meta:
        model = contactuspage
        fields = ['name', 'email', 'message']









#..............SignupPage-Form................#
class signuppageform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']







#..............UpdateProfilePage-Form................#
class updateprofilepageformone(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']



class updateprofilepageformtwo(ModelForm):
    class Meta:
        model = profile
        fields = ['image']

















        
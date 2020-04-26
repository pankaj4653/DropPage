from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from . models import Profile
from django import forms

class Profile_Form(ModelForm):
	bio=forms.CharField(max_length=1000,required=False,help_text="Add Some Line About Youself")
	comp = forms.CharField(max_length=100,required=False,help_text="Add Your Organization Name")
	class Meta:
		model = Profile
		exclude=['user']


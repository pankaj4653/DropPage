from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from . models import Profile
from django import forms

class Profile_Form(ModelForm):
	bio=forms.CharField(max_length=1000,required=False,help_text="Add Some Line About Youself")
	comp = forms.CharField(max_length=100,required=False,help_text="Add Your Organization Name")
	first_name=forms.CharField(max_length=100)
	last_name=forms.CharField(max_length=100)
	class Meta:
		model = Profile
		fields=['first_name','last_name','image','country','dob','gender','prof','comp','bio']


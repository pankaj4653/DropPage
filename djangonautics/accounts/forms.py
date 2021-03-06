from django.forms import ModelForm
#from . models import Moreinfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class user_info_form(UserCreationForm):
	first_name = forms.CharField(max_length =30,required=False,help_text='Optional.')
	last_name = forms.CharField(max_length=30,required=False,help_text='Optional.')
	email = forms.EmailField(max_length=254,help_text='Required . Inform a valid email Address')
	

	class Meta:
		model = User
		fields = ('username','first_name','last_name','email','password1','password2')


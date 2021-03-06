# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login,logout

from . forms import user_info_form

# Create your views here.

def sign_up(request):
	if(request.method == "POST"):
		form = user_info_form(request.POST)
		if (form.is_valid()):
			user = form.save()
			login(request,user)

			return redirect("articles:list")
	else:
	 form = user_info_form()
	
	return render(request,"accounts/sign_up.html",{'form':form})



def log_in(request):
	if(request.method == "POST"):
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			return redirect('articles:list')
	else:
		form = AuthenticationForm()
	return render(request,"accounts/log_in.html",{'form':form})


def log_out(request):
	logout(request)
	return render(request,'accounts/log_out.html')




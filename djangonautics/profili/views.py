# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from . forms import Profile_Form

from django.contrib.auth.models import User


def profile_detail(request):
	return render(request,'profili/profile_detail.html',{'user':request.user})




def profile_edit(request):
	user=request.user
	if request.method == "POST":
		form = Profile_Form(request.POST or None,instance=user.profile)
		if form.is_valid():
			user.first_name=form.cleaned_data.get('first_name') # user.refresh_from_db()
			user.last_name=form.cleaned_data.get('last_name')
			form.save()
			user.save()
			return redirect("http://127.0.0.1:8000/")
	else:
		form = Profile_Form(instance=user.profile)
		form['first_name'].initial = user.first_name
		form['last_name'].initial=user.last_name
	return render(request,'profili/profile.html',{'form':form})








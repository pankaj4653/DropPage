# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse

from . forms import Profile_Form

from django.contrib.auth.models import User


def profile_detail(request):
	return render(request,'profili/profile_detail.html',{'user':request.user})




def profile_edit(request):
	if request.method == "POST":
		form = Profile_Form(request.POST or None,instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect("http://127.0.0.1:8000/")
	else:
		form = Profile_Form(instance=request.user.profile)
	return render(request,'profili/profile.html',{'form':form})






# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Article

from django.http import HttpResponse

from . forms import ArticleForm

# Create your views here.


def article_list(request):
	u = request.user
	article = Article.objects.filter(author=u).order_by("date")
	return render(request,'articles/articlelist.html',{'article':article,'current_user':u})


def article_detail(request,slug):
	u = request.user
	#return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request,'articles/article_detail.html',{'article':article,'current_user':u})


def articleformfill(request):
	u=request.user
	if request.method == "POST":
		form = ArticleForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect("http://127.0.0.1:8000/")
	else:
		form=ArticleForm()

	return render(request,'articles/artform.html',{'form':form,'current_user':u})



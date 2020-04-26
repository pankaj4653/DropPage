from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm

def about(request):
	#return HttpResponse("About")
	return render(request,'about.html')

def homepage(request):
	#return HttpResponse("Homepage")
	form = AuthenticationForm()
	context = {'form':form}
	return render(request,'homepage.html',context)
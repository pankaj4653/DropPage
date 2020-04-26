# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver


# Create your models here.


Gender=[('M',"Male"),
		('F',"Female"),
		('O',"Others")]

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete= models.CASCADE)
	image = models.ImageField(blank=True,verbose_name = "Profile Pic")
	country = models.CharField(max_length=100, default="INDIA")
	dob = models.DateField(default="1980-01-01")
	gender=models.CharField(max_length=2,choices=Gender,default="M")
	prof = models.CharField(max_length=100,blank=True)
	comp = models.CharField(max_length=100,blank=True)
	bio = models.TextField(max_length=1000,blank=True)

	def __str__(self):
		return self.user.username


def create_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

post_save.connect(create_profile,sender=User)



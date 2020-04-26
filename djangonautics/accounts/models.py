# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Moreinfo(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length = 100)
	phone_no = models.CharField(max_length=13)
	country = models.CharField(max_length =100, blank = "True")
	dob = models.DateField(default = "1980-01-01")


	def __str__(self):
		return self.fname + self.lname



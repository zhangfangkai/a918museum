# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    CREDIT_LEVEL = (
        ('1',"admin"),
        ('2',"member"),
    )
    userName = models.CharField(max_length=30)
    realName = models.CharField(max_length=30)
    password = models.CharField(max_length=20, blank =True)
    userrole = models.CharField(choices = CREDIT_LEVEL,default=2)
    address = models.CharField(max_length=80)


class Museum(models.Model):
    theme = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    square = models.CharField(max_length=20)


class Wenwu(models.Model):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)


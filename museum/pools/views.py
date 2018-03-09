# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,render_to_response
from django.template.context import RequestContext
from models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from django.utils import timezone
from django.shortcuts import render

# Create your views here.
@csrf_exempt
def login(req):
    if req.method == 'GET':
        return render(req, 'login.html', {})
        # return HttpResponse('Hello World')
    else:
        username = req.POST.get("username")
        password = req.POST.get("password")
        data = {}
        data['password'] = password
        return render(req, 'index.html', data)
        # return HttpResponse('Hello World')

@csrf_exempt
def index(req):
    if req.method == 'GET':
        return render(req, 'index.html', {})
        # return HttpResponse('Hello World')

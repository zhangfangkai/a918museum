# -*- coding: utf-8 -*-
from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', login),
    url(r'^login', login),
    url(r'^index', index),
]
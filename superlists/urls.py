from django.conf.urls import url
from django.contrib import admin
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home')
]


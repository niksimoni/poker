from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from users import views


urlpatterns = [
    url(r'^createuser$', views.CreateUser.as_view(), name="createuser"),
    url(r'^login$', views.Login.as_view(), name='login'),
]
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'ner'

urlpatterns = [
    url(r'^index$|^home$|^$', views.index, name='index'),
    # url(r'^login', views.LoginView.as_view(), name='employee_login')
]
from django.urls import path
from django.http import HttpResponse
from .views import *

from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('<str:short_code>/', redirect_to_url, name='redirect_to_url'),
]

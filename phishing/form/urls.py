from django.urls import path
from . import views

app_name = 'form'
urlpatterns = [
    path('login', views.create, name = 'login.html')
]

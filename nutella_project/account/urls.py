from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('myAccount/', views.myAccount, name='myAccount'),
]
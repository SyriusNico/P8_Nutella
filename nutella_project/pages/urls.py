from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('legal/', views.LegalView.as_view(), name='legal')
]
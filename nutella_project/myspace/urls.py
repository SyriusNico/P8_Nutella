from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('register/', TemplateView.as_view(template_name="myspace/register.html"), name="register"),
]
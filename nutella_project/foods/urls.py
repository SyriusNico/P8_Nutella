from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.result, name='result'),
    path('result/<int:product_id>/', views.detail, name='detail')
]



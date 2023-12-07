from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('infomy/', views.it_s_me),
    path('infomy/<pk>/', views.hobbies),
]

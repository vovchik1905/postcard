from django.urls import path
from . import views


app_name='pcard'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('send/', views.send, name='send'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_to_ascii, name='text_to_ascii'),
]
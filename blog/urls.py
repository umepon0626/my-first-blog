from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('contact', views.contact, name='contact'),
    path('skill', views.skill, name='skill')
]

from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('One_on_One/', views.One_on_One, name = 'One_on_One'),
    path('pomodoro/', views.Pomodoro, name = 'pomodoro'),
]

urlpatterns += staticfiles_urlpatterns()
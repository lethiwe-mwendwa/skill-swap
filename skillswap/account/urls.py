from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login/', views.mobile_login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('manage/', views.manage, name = 'manage'),
    path('', views.account),
]

urlpatterns += staticfiles_urlpatterns()
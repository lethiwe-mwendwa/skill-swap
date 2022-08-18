from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('account.urls'), name = 'account'),
    path('learningSpace/',include('learningSpace.urls'), name = 'learningSpace'),
    path('about/', views.about, name = 'about'),
    path('ussd/', views.offline_learning, name = 'projects'),
    path('', views.homepage, name = 'homepage'),
]

urlpatterns += staticfiles_urlpatterns()
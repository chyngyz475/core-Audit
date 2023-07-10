from django.urls import path
from . import views
from .views import restart_view

urlpatterns = [
     path('', views.index, name ='core'),
     path('home/', views.HomeView.as_view(), name ='home'),
     path('logout/', views.LogoutView.as_view(), name ='logout'),
     path('restart.html', views.restart_view, name='restart'),
     path('restart1.html', views.restart1_view, name='restart1'),
]
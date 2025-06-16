from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for routing pages

urlpatterns = [
    path('', views.home, name='home'),              
    path('login/', auth_views.LoginView.as_view(template_name='citizen/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('user/', views.user, name='user'),        
    path('staff/', views.staff_home, name='staff'),
    path('myadmin/', views.admin_home, name='myadmin'),
]
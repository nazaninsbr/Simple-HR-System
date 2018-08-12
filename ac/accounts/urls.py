from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/<slug:slug>/', views.home, name='home'),
]
from django.urls import path
from . import views 

urlpatterns = [
    path('create/', views.create, name='create_announcement'),
    path('', views.view, name='view_announcement'),
]
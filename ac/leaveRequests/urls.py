from django.urls import path
from . import views 

urlpatterns = [
    path('', views.view_leave_requests, name='leave_requests'),
    path('create/', views.create, name='create_leave_request'),
    path('view/<slug:slug>', views.view_single_request, name='view_single_request')
]
from django.urls import path
from . import views 

urlpatterns = [
    path('upload/', views.upload, name='upload_share'),
    path('', views.all, name='view_shares'),
    path('download/<slug:slug>', views.download, name='download_file'), 
]
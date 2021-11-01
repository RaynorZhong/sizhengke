from django.urls import path

from . import views

urlpatterns = [
    path('', views.file_list, name='index'),
    path('file_list.json', views.file_list_json, name='file_list_json'),
    path('<int:file_upload_id>/', views.file_detail, name='file_detail'),
    path('<int:file_upload_id>/downloads.json', views.add_file_downloads, name='file_downloads'),
    path('random', views.file_random, name='file_random'),
]
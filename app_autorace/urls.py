from django.urls import path
from . import views
from django.conf.urls import url, static

app_name = 'app_autorace'
urlpatterns = [
    path('', views.index, name='index'),
    path('unyou', views.unyou, name='unyou'),
    path('master', views.master, name='master'),
    path('upload1/', views.upload1, name='upload1'),
    path('upload_schedule/', views.upload_schedule, name='upload2'),
]


from django.urls import path
from . import views
from django.conf.urls import url, static

app_name = 'app_ckeiba'
urlpatterns = [
    path('', views.index, name='index'),
]

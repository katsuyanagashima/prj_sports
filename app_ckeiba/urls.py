from django.urls import path
from . import views
from django.conf.urls import url, static

app_name = 'app_ckeiba'
urlpatterns = [
    path('', views.index, name='index'),
    path('option_submit', views.option_submit, name='option_submit'),
    path('Change_To_Master_Edit_Mode/', views.Change_To_Master_Edit_Mode, name='Change_To_Master_Edit_Mode'),
    path('Change_To_Nomal_Mode/', views.Change_To_Nomal_Mode, name='Change_To_Nomal_Mode'),
    path('<int:mst_num>/', views.Edit_Mst, name='Edit_Mst'),
    path('editbutton/<int:values>', views.editbutton, name='editbutton'),
    #CSV検証用
    path('upload/', views.upload, name='upload'),
    path('upload2/', views.upload2, name='upload2'),
]

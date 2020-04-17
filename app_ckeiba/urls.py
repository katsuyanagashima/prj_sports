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


    # path('create_30/<str:title>/', views.create_forms, name='master_create_30'),  #競馬場マスタメンテ作成画面
    # path('update_30/<str:title>/<int:pk>/', views.update_forms, name='master_update_30'),  #競馬場マスタメンテ更新画面
    # path('delete_30/<str:title>/<int:pk>/', views.delete_forms, name='master_delete_30'),  #競馬場マスタメンテ削除画面

    
    path('create/<str:title>/', views.create_forms, name='master_create'),  #マスタメンテ作成画面
    path('update/<str:title>/<int:pk>/', views.update_forms, name='master_update'),  #マスタメンテ更新画面
    path('delete/<str:title>/<int:pk>/', views.delete_forms, name='master_delete'),  #マスタメンテ削除画面
    
]

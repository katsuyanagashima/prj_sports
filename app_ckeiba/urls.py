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


    path('create/<str:title>/', views.create_forms, name='master_create'),  #マスタメンテ作成画面
    path('update/<str:title>/<int:pk>/', views.update_forms, name='master_update'),  #マスタメンテ更新画面
    path('delete/<str:title>/<int:pk>/', views.delete_forms, name='master_delete'),  #マスタメンテ削除画面
    
    
    path('shussouhyou/<int:year>/<int:month>/<int:day>/<int:joucode>/<int:race>/', views.md_update_forms, name='shussouhyou'),  #中間DB_出走表編集画面
    path('seiseki/<int:year>/<int:month>/<int:day>/<int:joucode>/<int:race>/', views.md_update_forms, name='seiseki'),  #中間DB_成績・払戻編集画面
    path('corner_rap/<int:year>/<int:month>/<int:day>/<int:joucode>/<int:race>/', views.md_update_forms, name='corner_rap'),  #中間DB_コーナー・ラップ編集画面
    path('agari/<int:year>/<int:month>/<int:day>/<int:joucode>/<int:race>/', views.md_update_forms, name='agari'),  #中間DB_上がり編集画面
    path('tushinbun/<int:year>/<int:month>/<int:day>/<int:joucode>/<int:race>/', views.md_update_forms, name='tushinbun'),  #中間DB_通信文編集画面
    
    path('nyujo/<int:year>/<int:month>/<int:day>/<int:joucode>/', views.md_update_forms, name='nyujo'),  #中間DB_入場人員編集画面
    path('uriage/<int:year>/<int:month>/<int:day>/<int:joucode>/', views.md_update_forms, name='uriage'),  #中間DB_売上金編集画面

    #CSV検証用
    path('upload/', views.upload, name='upload'),
    path('upload2/', views.upload2, name='upload2'),
]

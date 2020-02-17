from django.urls import path
from . import views
from django.conf.urls import url, static

urlpatterns = [
    path('', views.index, name='index'),
    path('sample', views.sample, name='sample'),
    path('xmlout1', views.xmlout1, name='xmlout1'),
    path('xmlout14', views.xmlout14, name='xmlout14'),
    path('xmlout_14', views.xmlout_14, name='xmlout_14'),
    path('input14', views.input14, name='input14'),
    path('update14', views.update14, name='update14'),
    path('update14_new', views.update14_new, name='update14_new'),
    path('upload/', views.upload, name='upload'),
    path('SUMUNY01/', views.SUMUNY01, name='SUMUNY01'), #業務運用メニュー
    path('SUMUNY01/SUMUDY01/', views.SUMUDY01, name='SUMUDY01'), #運用日設定画
    path('SUMUNY01/SUMYOS01/', views.SUMYOS01, name='SUMYOS01'), #予想番付処理①
    path('SUMUNY01/SUMYOS01/SUMYOS02/', views.SUMYOS02, name='SUMYOS02'), #予想番付処理②
    path('SUMUNY01/SUMBAN01/', views.SUMBAN01, name='SUMBAN01'), #番付処理
    
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

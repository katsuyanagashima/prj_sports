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
 #   path('SUMUNY01/', views.SUMUNY01, name='SUMUNY01'), #業務運用メニュー
    path('SUMUDY01/', views.SUMUDY01, name='SUMUDY01'), #運用日設定画
    path('SUMYOS01/', views.SUMYOS01, name='SUMYOS01'), #予想番付処理
    path('SUMYOS01/SUMYOS02/', views.SUMYOS02, name='SUMYOS02'), #予想番付処理画面
    path('SUMBAN01/', views.SUMBAN01, name='SUMBAN01'), #番付処理
    path('SUMBAN01/SUMBAN02', views.SUMBAN02, name='SUMBAN02'), #番付入力画面
    path('SUMBAN01/SUMBAN03', views.SUMBAN03, name='SUMBAN03'), #番付入力ＯＣＲ画面
    path('SUMBAN01/SUMBAN04', views.SUMBAN04, name='SUMBAN04'), #【新】番付ＯＣＲ取り込み画面
    path('SUMTOR01/', views.SUMTOR01, name='SUMTOR01'), #取組処理
    path('SUMTOR01/SUMTOR02', views.SUMTOR02, name='SUMTOR02'), #取組入力画面
    path('SUMTOR01/SUMTOR03', views.SUMTOR03, name='SUMTOR03'), #取組入力ＯＣＲ画面
    path('SUMTOR01/SUMTOR04', views.SUMTOR04, name='SUMTOR04'), #【新】取組ＯＣＲ取り込み画面
    path('SUMSHO01/', views.SUMSHO01, name='SUMSHO01'), #勝負入力処理
    path('SUMSHO01/SUMSHO02/', views.SUMSHO02, name='SUMSHO02'), #勝負入力処理
    path('SUMYUS01/', views.SUMYUS01, name='SUMYUS01'), #勝負入力処理
    path('SUMOUT01/', views.SUMOUT01, name='SUMOUT01'), #コンテンツ編集指示
    path('SUMOUT02/', views.SUMOUT02, name='SUMOUT02'), #電文／データ出力
    path('SUMOUT03/', views.SUMOUT03, name='SUMOUT03'), #電文／データ強制出力
    path('SUMJKH01/', views.SUMJKH01, name='SUMJKH01'), #状況表示
    path('SUMJKH01/SUMJKH02/', views.SUMJKH02, name='SUMJKH02'), #状況表示画面
    path('SUMTKD01/', views.SUMTKD01, name='SUMTKD01'), #付け出し処理
    path('SUMTKD01/SUMTKD02/', views.SUMTKD02, name='SUMTKD02'), #付け出し処理画面
    path('SUMJOR01/', views.SUMJOR01, name='SUMJOR01'), #階級上位力士
    path('SUMSHI01/', views.SUMSHI01, name='SUMSHI01'), #資料出力
    path('SUMNEW01/', views.SUMNEW01, name='SUMNEW01'), #NewsML修正画面
]

#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

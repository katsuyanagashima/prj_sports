from django.urls import path
from . import views
from . import add_views
from django.conf.urls import url, static

app_name = 'app_sumo'
urlpatterns = [
    path('', views.index, name='index'),
    path('SUMUDY01/', views.SUMUDY01, name='SUMUDY01'),  # 運用日設定画
    path('SUMYOS01/', views.SUMYOS01, name='SUMYOS01'),  # 予想番付処理
    path('SUMYOS01/SUMYOS02/', views.SUMYOS02, name='SUMYOS02'),  # 予想番付処理画面
    path('SUMBAN01/', views.SUMBAN01, name='SUMBAN01'),  # 番付処理
    path('SUMBAN01/SUMBAN02', views.SUMBAN02, name='SUMBAN02'),  # 番付入力画面
    path('SUMBAN01/SUMBAN03', views.SUMBAN03, name='SUMBAN03'),  # 番付入力ＯＣＲ画面
    path('SUMBAN01/SUMBAN04', views.SUMBAN04, name='SUMBAN04'),  # 【新】番付ＯＣＲ取り込み画面
    path('SUMTOR01/', views.SUMTOR01, name='SUMTOR01'),  # 取組処理
    path('SUMTOR01/SUMTOR02', views.SUMTOR02, name='SUMTOR02'),  # 取組入力画面
    path('SUMTOR01/SUMTOR03', views.SUMTOR03, name='SUMTOR03'),  # 取組入力ＯＣＲ画面
    path('SUMTOR01/SUMTOR04', views.SUMTOR04, name='SUMTOR04'),  # 【新】取組ＯＣＲ取り込み画面
    path('SUMSHO01/', views.SUMSHO01, name='SUMSHO01'),  # 勝負入力処理
    path('SUMSHO01/SUMSHO02/', views.SUMSHO02, name='SUMSHO02'),  # 勝負入力処理
    ###path('SUMYUS01/', views.SUMYUS01, name='SUMYUS01'), #勝負入力処理
    path('SUMYUS01/', views.SUMYUS01, name='SUMYUS01'),  # 優勝・三賞入力画面
    path('SUMYUS01/create/', views.SUMYUS01_create, name='SUMYUS01_create'),  # 優勝・三賞入力画面（追加）
    path('SUMYUS01/view/<int:pk>', views.SUMYUS01_view, name='SUMYUS01_view'),  # 優勝・三賞入力画面（参照）
    path('SUMYUS01/update/<int:pk>', views.SUMYUS01_update, name='SUMYUS01_update'),  # 優勝・三賞入力画面（更新）
    path('SUMYUS01/delete/<int:pk>', views.SUMYUS01_delete, name='SUMYUS01_delete'),  # 優勝・三賞入力画面（削除）

    # path('<int:memo_id>', views.detail, name='detail'),
    # path('new_memo', views.new_memo, name='new_memo'),
    # path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
    # path('edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),
    ###
    path('SUMOUT01/', views.SUMOUT01, name='SUMOUT01'),  # コンテンツ出力指示画面
    path('SUMOUT02/', views.SUMOUT02, name='SUMOUT02'),  # 配信・作成・プレビュー・印刷
    path('SUMOUT03/', views.SUMOUT03, name='SUMOUT03'),  # 電文／データ強制出力
    path('SUMJKH01/', views.SUMJKH01, name='SUMJKH01'),  # 状況表示
    path('SUMJKH01/SUMJKH02/', views.SUMJKH02, name='SUMJKH02'),  # 状況表示画面
    path('SUMTKD01/', views.SUMTKD01, name='SUMTKD01'),  # 付け出し処理
    path('SUMTKD01/SUMTKD02/', views.SUMTKD02, name='SUMTKD02'),  # 付け出し処理画面
    path('SUMJOR01/', views.SUMJOR01, name='SUMJOR01'),  # 階級上位力士
    ###path('SUMJOR01/', views.SUMJOR01.as_view(), name='SUMJOR01'), #階級上位力士
    path('SUMSHI01/', views.SUMSHI01, name='SUMSHI01'),  # 資料出力
    path('SUMNEW01/', views.SUMNEW01, name='SUMNEW01'),  # NewsML修正画面
    path('SUMNEW02/', views.SUMNEW02, name='SUMNEW02'),  # NewsML修正画面内容部
    path('SUMINT01/', views.SUMINT01, name='SUMINT01'),  # 画面・年度切替画面
    path('SUMUKS01/', views.SUMUKS01, name='SUMUKS01'),  # 優勝決定戦階級選択画面
    path('SUMUKS02/', views.SUMUKS02, name='SUMUKS02'),  # 優勝決定戦入力画面
    path('SUMMST01/', views.Rikishilist.as_view(), name='rikishi'),  # 力士マスタメンテ画面
    path('SUMMST01/create/', views.RikishiCreateView.as_view(), name='rikishiCreate'),  # 力士マスタメンテ作成画面
    path('SUMMST01/update/<int:pk>/', views.RikishiUpdateView.as_view(), name='rikishiUpdate'),  # 力士マスタメンテ更新画面
    path('SUMMST01/delete/<int:pk>/', views.RikishiDeleteView.as_view(), name='rikishiDelete'),  # 力士マスタメンテ削除画面
    # path('output/', add_views.xmlout_14, name=''), #NewsML修正画面

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

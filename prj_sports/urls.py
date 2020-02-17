from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('app_sumo/', include('app_sumo.urls')),
    path('app_ckeiba/', include('app_ckeiba.urls')),
    path('app_autorace/', include('app_autorace.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


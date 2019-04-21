from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import path, include
from cleverbots import settings

urlpatterns = [
    path('service/admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('service/admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

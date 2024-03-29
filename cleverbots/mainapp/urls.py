from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cleverbots import settings
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'photos', views.SnippetViewSet, 'photos')
router.register(r'photo', views.UploadPhotoView, 'photo')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('service/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
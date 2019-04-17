from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cleverbots import settings
from mainapp import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
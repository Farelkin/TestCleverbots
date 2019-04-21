from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cleverbots import settings
from mainapp import views
from django.http import HttpResponseRedirect

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'photos', views.SnippetViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('service/', include(router.urls)),
    path('', views.test_redirect, name='test_redirect'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
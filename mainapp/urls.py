# from mainapp import views
# from django.urls import path
#
#
# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mainapp import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

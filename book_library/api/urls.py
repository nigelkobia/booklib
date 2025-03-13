from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

#Here, we create a router, register our BookViewSet with the URL prefix books, and include the router's URLs in our Django urlpatterns.
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'categoria', CategoriaViewSet)
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
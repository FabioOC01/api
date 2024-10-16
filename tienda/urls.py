from django.urls import path
from .views import CategoriaView, CategoriaDetailView, ProductoView, ProductoDetailView

urlpatterns = [
    # Rutas para Categoria
    path('categoria/', CategoriaView.as_view(), name='categoria-list'),
    path('categoria/<int:pk>/', CategoriaDetailView.as_view(), name='categoria-detail'),
    
    # Rutas para Producto
    path('producto/', ProductoView.as_view(), name='producto-list'),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
]

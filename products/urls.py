from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreateView, ProductListCreateView, ProductDetailView, ReviewListCreateView, ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
urlpatterns = router.urls


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_id>/reviews/', ReviewListCreateView.as_view(), name='product-reviews'),
]
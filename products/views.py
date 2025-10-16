from rest_framework import generics, permissions, filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly
# Category List and Create 
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# Product List and Create
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['price', 'created_date']
    search_fields = ['name','description', 'category__name']
    filterset_fields = {
        'category__name': ['exact'],
        'price': ['gte', 'lte'],
        'stock_quantity': ['gte', 'lte'],
    }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    

# Product Retrieve, Udate, Delete
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Review.objects.filter(product_id=product_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product_id=self.kwargs['product_id'])

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # ✅ Enable filtering, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # ✅ Fields that can be filtered
    filterset_fields = ['category', 'user']

    # ✅ Fields that can be searched
    search_fields = ['name', 'description']

    # ✅ Default ordering
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']
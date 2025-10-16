from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    
    @property
    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(sum([r.rating for r in reviews]) / reviews.count(), 1)
        return 0

    

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('product', 'user')  

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"

    @property
    def short_comment(self):
        return self.comment[:30]
    
from django.db import models
import uuid
# Create your models here.

class Product(models.Model):
    vendor_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default = True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name
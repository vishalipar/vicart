from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','vendor_id','product_name','price')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
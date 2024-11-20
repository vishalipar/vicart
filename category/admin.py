from django.contrib import admin
from .models import Category
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}



admin.site.register(Category, categoryAdmin)
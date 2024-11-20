from django.urls import path 
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/', views.prod_detail, name='prod_detail'),
]

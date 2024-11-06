from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('business_login/', views.business_login, name='business_login'),
    path('login/business_login/', views.business_login, name='business_login'),
    
    # activateion
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
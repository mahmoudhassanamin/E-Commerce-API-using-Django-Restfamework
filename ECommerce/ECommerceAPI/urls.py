from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [

    path('api-auth/', AuthView.as_view()),
    path('product/',ProductList.as_view()),
    path('CategoryList/',CategoryList.as_view()),
    path('CategoryDetail/<str:pk>',CategoryDetail.as_view()),
  
    path('ProductList/', ProductList.as_view(), name='product-list'),
    path('ProductDetail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    
    path('users/create/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>/orders/', OrderHistory.as_view(), name='order-history'),
    
    path('checkout/user-information/', UserInformationView.as_view()),
    path('checkout/shipping-details/', ShippingDetailsView.as_view()),
    path('checkout/payment-information/', PaymentInformationView.as_view()),

]
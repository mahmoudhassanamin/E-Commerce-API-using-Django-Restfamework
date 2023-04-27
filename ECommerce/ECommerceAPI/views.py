import datetime
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins, generics
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer


class AuthView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


   
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class OrderHistory(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class UserInformationView(generics.CreateAPIView):
    serializer_class = UserInformationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_info = UserInformation.objects.create(
            user=request.user,
            name=serializer.validated_data['name'],
            email=serializer.validated_data['email'],
            phone_number=serializer.validated_data['phone_number']
        )
        return Response(serializer.data)

class ShippingDetailsView(generics.CreateAPIView):
    serializer_class = ShippingDetailsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        shipping_details = ShippingDetails.objects.create(
            user=request.user,
            address=serializer.validated_data['address'],
            city=serializer.validated_data['city'],
            state=serializer.validated_data['state'],
            country=serializer.validated_data['country'],
            zip_code=serializer.validated_data['zip_code']
        )
        return Response(serializer.data)

class PaymentInformationView(generics.CreateAPIView):
    serializer_class = PaymentInformationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment_info = PaymentInformation.objects.create(
            user=request.user,
            card_number=serializer.validated_data['card_number'],
            expiration_month=serializer.validated_data['expiration_month'],
            expiration_year=serializer.validated_data['expiration_year'],
            cvv=serializer.validated_data['cvv']
        )
        return Response(serializer.data)
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    def returnUser():
        queryset=User.objects.all()
        return queryset
        
class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = '__all__'
    def returnProduct():
        queryset=Product.objects.all()
        return queryset

class OrderSerializer(serializers.Serializer):
    product = ProductSerializer.returnProduct()
    user = UserSerializer.returnUser()
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = Order
        fields = '__all__'


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ['name', 'email', 'phone_number']

class ShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetails
        fields = ['address', 'city', 'state', 'country', 'zip_code']

class PaymentInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInformation
        fields = ['card_number', 'expiration_month', 'expiration_year', 'cvv']






from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ecommerce.models import Category, Product, Customer, Coupon, Order, ProductOrder


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_active', 'is_staff', 'is_superuser', 'date_joined']


class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    class Meta:
        model = Customer
        fields = ['email', 'password', 'first_name', 'last_name', 'username']


class ProductAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['product', 'quantity']


class CreateOrderSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    address = serializers.CharField(required=False)
    products = ProductAmountSerializer(many=True, allow_empty=True)
    coupons = serializers.ListSerializer(child=serializers.CharField(), required=False)

    # def validate_email(self, value):
    #     if self.context.get('request').user is None and value is None:
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     else:
    #         return super().validate_email(value)
    #     return self.context.get('request').user.email

    def is_valid(self, raise_exception=True):
        super().is_valid(raise_exception=raise_exception)
        validated_data = self._validated_data
        request = self.context.get('request')
        user = request.user

        if validated_data.get('address') is None and user.is_anonymous:
            self._errors['address'] = [self.error_messages['required']]

        if validated_data.get('email') is None and user.is_anonymous:
            self._errors['email'] = [self.error_messages['required']]

        super().is_valid(raise_exception=raise_exception)

        if not user.is_anonymous:
            if user.customer is None:
                raise BadRequest("Solo clientes")

            self._validated_data.setdefault('email', user.email)
            self._validated_data.setdefault('address', user.address)

        return super().is_valid(raise_exception=raise_exception)

    class Meta:
        model = Order
        exclude = ['created_at', 'updated_at', 'customer', 'total']

from django.shortcuts import render
from faker.providers import address
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, \
    DjangoObjectPermissions, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView

from ecommerce.models import Category, Product, Customer, Coupon, Order
from ecommerce.serializers import CategorySerializer, ProductSerializer, CustomerSerializer, CouponSerializer, \
    UserSerializer, RegisterUserSerializer, CreateOrderSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [DjangoObjectPermissions]


class CouponViewSet(viewsets.ModelViewSet):
    serializer_class = CouponSerializer
    queryset = Coupon.objects.all()


# Autenticacion
class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data.get('user')
            Token.objects.filter(user=user).delete()
            token, created = Token.objects.get_or_create(user=user)
            user = UserSerializer(user).data
            return Response({'token': token.key, 'user': user})
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({'detail': 'Sesion Cerrada Correctamente'}, HTTP_200_OK)


class RegisterCustomer(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        # customer = Customer.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=user)
        user = UserSerializer(user).data
        return Response({'token': token.key, 'user': user}, status=HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class CreateOrder(CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data


        order = Order.objects.create(
            customer=request.user.id,
            email=validated_data['email'],
            address=validated_data['address'],
            destination_address=validated_data['destination_address']
        )


        return Response({'order': validated_data})

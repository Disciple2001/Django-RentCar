from django.urls import path,include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'coupons', views.CouponViewSet)
router.register(r'customers', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.CustomObtainAuthToken.as_view(), name="login"),
    path('register', views.RegisterCustomer.as_view(), name="register"),
    path('order', views.CreateOrder.as_view(), name="order"),
]

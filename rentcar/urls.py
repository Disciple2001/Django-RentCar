from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("cars", views.CarView.as_view(), name="cars"),
    path("cars/create", views.CarCreateView.as_view(), name="car_create"),
    path("cars/<int:pk>/details", views.CarDetailView.as_view(), name="car_detail"),

    path("models", views.ModelView.as_view(), name="models"),
    path("models/create", views.ModelCreateView.as_view(), name="model_create"),
    path("models/<int:pk>/delete", views.ModelDeleteView.as_view(), name="model_delete"),
    path("models/<int:pk>/details", views.ModelDetailView.as_view(), name="model_detail"),
    path("models/<int:pk>/update", views.ModelUpdateView.as_view(), name="model_update"),

    # path("brands", views.BrandView.as_view(), name="brands"),
    # path("brands/<int:pk>/details", views.BrandDetailView.as_view(), name="brand_detail"),
    # path("brands/create", views.BrandCreateView.as_view(), name="brand_create"),
    # path("brands/<int:pk>/delete", views.BrandDeleteView.as_view(), name="brand_delete"),
    # path("brands/<int:pk>/edit", views.BrandUpdateView.as_view(), name="brand_update"),

    path("tourist", views.TouristView.as_view(), name="tourist"),
    path("tourist/list", views.TouristListView.as_view(), name="tourist_list"),
    path("tourist/<int:pk>/delete", views.TouristDeleteView.as_view(), name="tourist_delete"),
    path("tourist/<int:pk>/detail", views.TouristDetailView.as_view(), name="tourist_detail"),
    path("tourist/<int:pk>/update", views.TouristUpdateView.as_view(), name="tourist_update"),
    path("tourist/create", views.TouristCreateView.as_view(), name="tourist_create"),

    path("brandv2", views.BrandIndexView.as_view(), name='brandv2'),
    path("brandv2/list", views.BrandListView.as_view(), name="brand_list"),
    path("brandv2/<int:pk>/delete", views.BrandDeleteView.as_view(), name="brand_delete"),
    path("brandv2/<int:pk>/detail", views.BrandDetailView.as_view(), name="brand_detail"),
    path("brandv2/<int:pk>/update", views.BrandUpdateView.as_view(), name="brand_update"),
    path("brandv2/create", views.BrandCreateView.as_view(), name="brand_create"),



]

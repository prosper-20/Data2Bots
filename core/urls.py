from django.urls import path
from .views import HomeView, ItemDetailView, checkout, add_to_cart, remove_from_cart


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", checkout, name="checkout"),
    path("product/<slug:slug>/", ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<slug:slug>/", add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<slug:slug>/", remove_from_cart, name="remove-from-cart")
] 
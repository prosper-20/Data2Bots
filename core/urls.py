from django.urls import path
from .views import HomeView, ItemDetailView, checkout


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("checkout/", checkout, name="checkout"),
    path("product/<slug:slug>/", ItemDetailView.as_view(), name="products")
]
from django.urls import path
from . import views

urlpatterns = [
    path("api/menu", views.MenuView.as_view(), name="menu"),
    path("api/toppings", views.ToppingView.as_view(), name="topping")
]

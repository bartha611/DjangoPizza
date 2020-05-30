from django.db import models
from Menu.models import MenuItem
from Profile.models import Profile
from django_extensions.db.models import TimeStampedModel

# Create your models here.


class Invoice(TimeStampedModel):
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)


class CartItem(TimeStampedModel):
    menu_item = models.ForeignKey(
        to=MenuItem, on_delete=models.CASCADE, related_name="cart_items")
    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE)


class OrderItem(TimeStampedModel):
    menu_item = models.ForeignKey(
        to=MenuItem, on_delete=models.CASCADE, related_name="order_items")
    invoice = models.ForeignKey(to=Invoice, on_delete=models.CASCADE)

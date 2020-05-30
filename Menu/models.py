from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class MenuItem(models.Model):
    SIZE_CHOICES = [('small', 'small'), ('large', 'large')]
    CATEGORY_CHOICES = [('Regular Pizza', 'Regular Pizza'), ('Sicilian Pizza', 'Sicilian Pizza'), (
        'Subs', 'Subs'), ('Pasta', 'Pasta'), ('Salads', 'Salads'), ('Dinner Platters', 'Dinner Platters')]

    name = models.CharField(_("name"), max_length=30)
    category = models.CharField(
        _("category"), max_length=30, choices=CATEGORY_CHOICES)
    size = models.CharField(_("size"), max_length=5, choices=SIZE_CHOICES)
    price = models.DecimalField(_("price"), max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name


class Topping(models.Model):
    CATEGORY_CHOICES = [('meat', 'meat'), ('veggies', 'veggies')]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

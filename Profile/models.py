from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from localflavor.us.models import USStateField
# Create your models here.


class Profile(AbstractUser):
    address = models.CharField(_("address"), max_length=100)
    city = models.CharField(_("city"), max_length=64)
    state = USStateField(_("state"), default="IL")
    zip_code = models.CharField(_("Zip Code"), max_length=5, default="60526")

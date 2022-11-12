from django.forms import SlugField
from django.db import models
import uuid, os
from django.utils.translation import gettext as _


class CategoryType(models.IntegerChoices):
    Main = 0 ,
    Sub = 1 ,

class MainCategories(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    categoryengname = models.CharField(_("English Name Of Categroy"), max_length=500)
    categorypersianname = models.CharField(_("Persian Name Of Categroy"), max_length=500)
    typeofcategory = models.IntegerField(_("Type Of Category "), default=CategoryType.Main, choices=CategoryType.choices)
    active = models.BooleanField(_("Active ?"), default=True)

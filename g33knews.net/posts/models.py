from django.forms import SlugField
from django.db import models
from ckeditor.fields import RichTextField 
import uuid, os
from django.utils.translation import gettext as _
from category.models import MainCategories

def PostPosterPath(instance, filename):
    name = instance.categoryengname.replace(' ','-')
    filename = filename.replace(' ','-')
    return 'Categories/Images/{0}/{1}'.format(name,filename)

class Post(models.Model):
    slug = models.SlugField(default=uuid.uuid4)
    # enName = models.CharField(_("English Name Of Categroy"), max_length=500)
    # faName = models.CharField(_("Persian Name Of Categroy"), max_length=500)
    Category = models.ForeignKey(MainCategories , on_delete= models.CASCADE)
    poster = models.ImageField(_('Post Poster'), upload_to=PostPosterPath , null=True , blank=True)
    title = models.CharField(_('Title of Post'), max_length=50)
    desceibtion = models.CharField(_('Title of Post'), max_length=100)
    author = models.CharField(_('Author of Post'), max_length=50)
    tags = models.CharField(_('Title of Post'), max_length=500) #its need new app for tags
    articleText = RichTextField( )
    active = models.BooleanField(_("Active ?"), default=True)

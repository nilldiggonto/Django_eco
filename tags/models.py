from django.db import models
from django.db.models.signals import pre_save
from ecommerce_v2.utils import unique_slug_generator
from products.models import Product

# Create your models here.
class Tag(models.Model):
    product       = models.ManyToManyField(Product,blank=True)
    title         = models.CharField(max_length=120)
    slug          = models.SlugField(blank=True)
    timestamp     = models.DateTimeField(auto_now_add=True)
    active        = models.BooleanField(default=True)

    def __str__(self):
        return self.title


def tag_pre_save(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(tag_pre_save,sender=Tag)
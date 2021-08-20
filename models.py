from django.db import models

from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from ecommerce.utils import unique_slug_generator
# creating relationship between Product and Tag models
from products.models import Product
# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # Relationship between Product and Tag
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance)  # genrate the  slug unique name


 # How to save the unique-slug_generator, we use pre_save to before saving it to daabase.
pre_save.connect(tag_pre_save_receiver, sender=Tag)

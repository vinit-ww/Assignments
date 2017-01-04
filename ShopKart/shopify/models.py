# Create your models here.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.conf import settings



def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    return "%s/%s" % (instance.image_name, filename)


# # Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    created_date = models.DateTimeField(default=timezone.now)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shopify:restricted", kwargs={"id": self.id})


# Create your categories here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey('self', blank=True, null=True)
    created_by = models.ForeignKey(User)
    created_date = models.DateField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    # def __str__(self):
    #     return self.user.id

    @staticmethod
    def get_absolute_url():
        return reverse("shopify:index")

class Brand(models.Model):
    brand = models.CharField(max_length=100)


    def __unicode__(self):
        return self.brand


class Product(models.Model):
    name = models.CharField(max_length=100)
    brands = models.ForeignKey(Brand)
    price=models.IntegerField()
    quantity=models.IntegerField()
    short_description = models.CharField(max_length=100)
    long_description = models.TextField()
    # special_price_from=models.DateField("Date")
    # special_price_to=models.DateField("Date")
    status = models.BooleanField(default=False)
    # quantity=models.IntegerField(max_length=10)
    meta_title = models.CharField(max_length=45)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    created_by = models.ForeignKey(User)
    created_date = models.DateField()
    modified_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-created_date"]



class ProductCategories(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_id.name

    def __unicode__(self):
        return self.category_id.name


class ProductImage(models.Model):
    image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_by = models.ForeignKey(User)
    created_date = models.DateField()
    modified_by = models.IntegerField(null=True, blank=True, unique=True)
    modified_date = models.DateField(null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_date"]

    def get_absolute_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image.url)


    def __unicode__(self):
        return self.image_name




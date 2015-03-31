from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(default='', unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class CustomerProfile(models.Model):
    user = models.OneToOneField(User)
    representative = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username


class Offer(models.Model):
    category = models.ForeignKey(Category)
    representative = models.ForeignKey(CustomerProfile)
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    amount = models.IntegerField(default=0)
    top = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    description = models.TextField(max_length=300, default="")
    picture = models.ImageField(upload_to='offer_images', default='offer_images/default_offer_img.jpg')

    def save(self, *args, **kwargs):
        if self.price < 0:
            self.price = 0.0
        if self.amount < 0:
            self.amount = 0
        if self.views < 0:
            self.views = 0
        if self.likes < 0:
            self.likes = 0

    def __unicode__(self):
        return self.name


class Basket(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    item = models.ManyToManyField(Offer)
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __unicode__(self):
        return self.customer.user.username


class Transaction(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    item = models.ForeignKey(Offer)
    date = models.DateField(auto_now_add=True)
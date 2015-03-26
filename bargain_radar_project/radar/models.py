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
    representative = models.BooleanField(default='False')
    def __unicode__(self):
        return self.user.username


class Offer(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    top = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    description = models.TextField(max_length=300, default="")
    picture = models.ImageField(upload_to='offer_images', default='default_offer_img.jpg')

    def __unicode__(self):
        return self.name

class Basket(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    #this may not working. there is a warning in the django documentation
    item = models.ManyToManyField(Offer)
    total = models.IntegerField(default=0)

    def __unicode__(self):
        #if not working = self.customer.user.username
        return self.customer.name


class Transaction(models.Model):
    customer = models.ForeignKey(CustomerProfile)
    item = models.ForeignKey(Offer)
    date = models.DateField(auto_now_add=True)
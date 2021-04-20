from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy
from django.utils.translation import activate, get_language
from django.contrib.auth.models import User


# Create your models here.

class Order (models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    delivery_date = models.DateField(blank=True, default=timezone.now())
    product_id = models.TextField(max_length=300, default='EGGS')
    payment_option = models.CharField(max_length=50)
    px_per_tray = models.IntegerField(default=9000)
    px_per_egg = models.IntegerField(default=300)
    total = models.IntegerField(default=0)
    no_of_trays = models.IntegerField(null=False, default=0)
    order_status = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.total = self.px_per_tray * self.no_of_trays
        super(Order, self).save(*args, **kwargs)



class Collected(models.Model):
    eggs = models.IntegerField()
    trays = models.CharField(max_length=50)
    damaged = models.IntegerField()
    Date = models.DateTimeField(default=timezone.now)

class Employee(models.Model) :
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    tel = models.CharField(max_length=10)
    address = models.TextField()
    email = models.CharField(max_length=30)
    role = models.CharField(max_length=50)

class Customer(models.Model) :
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=10)
    address = models.TextField()
    email = models.CharField(max_length=30)

class Supplier(models.Model) :
    supplier_name = models.CharField(max_length=100)
    supplier_description = models.CharField(max_length=40)
    tel = models.CharField(max_length=10)
    address = models.TextField()
    email = models.CharField(max_length=100)

class Expense(models.Model) :
    classification = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    amount = models.CharField(max_length=20)
    date = models.DateTimeField(default=timezone.now())

class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    unit_price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    supplier = models.CharField(max_length=100)
    Date = models.DateTimeField(default=timezone.now)
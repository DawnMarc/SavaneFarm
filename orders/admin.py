from django.contrib import admin
from django.utils.translation import ugettext
from django.utils.translation import activate, get_language

# Register your models here.

from orders.models import Order, Collected, Employee, Customer, Supplier, Expense, Inventory

admin.site.register(Order)
admin.site.register(Collected)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Expense)
admin.site.register(Inventory)

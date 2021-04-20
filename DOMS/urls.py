"""DOMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from orders.models import Collected, Employee, Customer, Supplier, Expense, Inventory
from orders import views as my_order
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from orders.views import set_language
admin.autodiscover()

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.savane, name='index-food-shop'),
    url(r'^contact$',my_order.contact_us, name='contact'),
    url(r'^about$',my_order.about_us, name='about'),
    url(r'^index/', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='deleteorder'),
    url(r'^collect_now$', my_order.eggcollections, name='collect_now'),

    url(r'^new_staff$', my_order.newemployee, name='new_staff'),
    url(r'^all_staff$', my_order.all_staff, name='all_staff'),
    url(r'^staff/editstaff/(?P<employee_id>\d+)/$', my_order.editstaff, name='editemployee'),
    url(r'^staff/deletestaff/(?P<employee_id>\d+)/$', my_order.destroystaff, name='deletestaff'),

    url(r'^customer$', my_order.newscustomer, name='new_client'),
    url(r'^all_customer$', my_order.all_customer, name='all_customer'),
    url(r'^customer/editcustomer/(?P<customer_id>\d+)/$', my_order.editcustomer, name='editcustomer'),
    url(r'^deletecustomer/(?P<customer_id>\d+)/$', my_order.destroycustomer, name='deletecustomer'),

    url(r'^supplier$', my_order.newsupplier, name='new_supplier'),
    url(r'^all_supplier$', my_order.all_supplier, name='all_supplier'),
    url(r'^supplier/editsupplier/(?P<supplier_id>\d+)/$', my_order.editsupplier, name='editsupplier'),
    url(r'^deletesupplier/(?P<supplier_id>\d+)/$', my_order.destroysupplier, name='deletesupplier'),

    url(r'^expense$', my_order.newexpense, name='newexpense'),
    url(r'^all_expense$', my_order.all_expense, name='all_expense'),
    url(r'^expense/editexpense/(?P<expense_id>\d+)/$', my_order.editexpense, name='editexpense'),
    url(r'^deleteexpense/(?P<expense_id>\d+)/$', my_order.destroyexpense, name='deleteexpense'),

    url(r'^inventory$', my_order.newinventory, name='new_inventory'),
    url(r'^all_inventory$', my_order.all_inventory, name='all_inventory'),
    url(r'^inventory/editinventory/(?P<inventory_id>\d+)/$', my_order.editinventory, name='editinventory'),
    url(r'^deleteinventory/(?P<inventory_id>\d+)/$', my_order.destroyinventory, name='deleteinventory'),

    url(r'^collect$', my_order.collections, name='collections'),
    url(r'^collected$', my_order.collections, name='collections'),
    url(r'^collected/delete/(?P<collected_id>\d+)/$', my_order.collectiondestroy, name='delete'),

    url(r'^users/login/$', LoginView.as_view(), name='login'),
    url(r'^users/logout/$',LogoutView.as_view(), name='logout'),
    url(r'^users/change_password/$', login_required(), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),

    path('i18n/set_language', include('django.conf.urls.i18n')),

)
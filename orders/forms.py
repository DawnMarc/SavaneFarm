from django.utils.translation import ugettext
from django.utils.translation import activate, get_language
from django.forms import ModelForm
from django import forms
from .models import Order, Collected, Employee, Customer, Supplier, Expense, Inventory


class OrderForm(ModelForm):
    OPTIONS = (
        ('Cash','Cash'),
        ('Cheque','Cheque'),
        ('Mobile Money', 'Mobile Money')
    )
    OPTIONS2 = (
        ('Confirmed', 'Confirmed'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect)
    payment_option = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address',
                  'delivery_date', 'product_id', 'payment_option',
                  'px_per_tray', 'px_per_egg', 'no_of_trays',
                  'order_status']
        widgets = {
            'px_per_tray': forms.NumberInput(attrs={'id':'px_per_tray'}),
            'px_per_egg': forms.NumberInput(attrs={'id':'px_per_egg','readonly': 'readonly'}),
            'product_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'delivery_date': forms.DateInput(),
        }


class CollectionForm(ModelForm):
    class Meta:
        model = Collected
        fields = ['eggs', 'trays', 'damaged', 'Date']
        widgets = {
            'eggs': forms.NumberInput(),
            'trays': forms.NumberInput(),
            'damaged':  forms.NumberInput(),
            'Date': forms.DateTimeInput()
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['fname', 'lname', 'tel', 'address', 'email', 'role']
        widgets = {
            'fname': forms.TextInput(),
            'lname': forms.TextInput(),
            'tel':  forms.TextInput(),
            'address': forms.TextInput(),
            'email': forms.TextInput(),
            'role': forms.TextInput()
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'tel', 'address', 'email']
        widgets = {
            'name': forms.TextInput(),
            'tel': forms.TextInput(),
            'address': forms.TextInput(),
            'email': forms.TextInput()
        }

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'supplier_description', 'tel', 'address', 'email']
        widgets = {
            'supplier_name': forms.TextInput(),
            'supplier_description': forms.TextInput(),
            'tel': forms.TextInput(),
            'address': forms.TextInput(),
            'email': forms.TextInput()
        }

class ExpenseForm(ModelForm):

    OPTIONS3 = (
        ('Utilities Expense', 'Utilities Expense'),
        ('Advertising Expense', 'Advertising Expense'),
        ('Repairs Expense', 'Repairs Expense'),
        ('Rent Expense','Rent Expense'),
        ('Salaries Expense','Salaries Expense'),
        ('Feeds Expense','Feeds Expense')
    )
    classification = forms.ChoiceField(choices=OPTIONS3)
    class Meta:
        model = Expense
        fields = ['description', 'amount', 'classification','date']
        widgets = {
            'description': forms.TextInput(),
            'amount': forms.NumberInput(),
            'date': forms.DateInput()
        }

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['product_name', 'product_category', 'unit_price', 'quantity', 'supplier', 'Date']
        widgets = {
            'product_name': forms.TextInput(),
            'product_category': forms.TextInput(),
            'unit_price': forms.NumberInput(),
            'quantity': forms.NumberInput(),
            'supplier': forms.TextInput(),
            'Date': forms.DateTimeInput()
        }








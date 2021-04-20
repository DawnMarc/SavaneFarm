from django.shortcuts import render, redirect
from .models import Order, Collected, Employee, Supplier, Customer, Expense, Inventory
from .forms import OrderForm, CollectionForm, EmployeeForm, SupplierForm, CustomerForm, ExpenseForm, InventoryForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView)
from django.utils.translation import ugettext
from django.utils.translation import activate, get_language
from django.http import HttpResponseRedirect


class login_view(LoginView):
    # The line below overrides the default template path of <appname>/<modelname>_login.html
    template_name = 'templates/login.html'


@login_required
def collections(request):
    collecteds = Collected.objects.all()
    return render(request, 'collections.html', {'collecteds': collecteds})


@login_required
def eggcollections(request):
    if request.POST:
        form = CollectionForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/collect', messages.success(request, 'Collection data was successfully registered.', 'alert-success'))
            else:
                return redirect('/collect', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/collect', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = CollectionForm()
    return render(request, 'collect_now.html', {'form': form})


@login_required
def collectiondestroy(request, collected_id):
    collecteds = Collected.objects.get(id=collected_id)
    collecteds.delete()
    return redirect('/collect', messages.success(request, 'Collection Data was successfully deleted.', 'alert-success'))



@login_required
def newemployee(request):
    if request.POST:
        form2 = EmployeeForm(request.POST or None)
        if form2.is_valid():
            if form2.save():
                return redirect('/all_staff', messages.success(request,'Employee was added successfully', 'alert-success'))
            else:
                return redirect('/all_staff', messages.error(request, 'Staff details not saved', 'alert-danger'))
        else:
            return redirect('/all_staff', messages.error(request,'Form is not valid', 'alert-danger'))
    else:
        form2 = EmployeeForm()
    return render(request, 'new_staff.html', {'form': form2})


@login_required
def all_staff(request):
    employees = Employee.objects.all()
    return render(request, 'all_staff.html', {'Employee': employees})


@login_required
def editstaff(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.POST:
        form8 = EmployeeForm(request.POST, instance=employee)
        if form8.is_valid():
            if form8.save():
                return redirect('/all_staff', messages.success(request, 'Staff data was successfully updated.', 'alert-success'))
            else:
                return redirect('/all_staff', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/all_staff', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form8 = EmployeeForm(instance=employee)
        return render(request, 'editemployee.html', {'form': form8})


@login_required
def destroystaff(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect('/all_staff', messages.success(request, 'Staff was successfully deleted.', 'alert-success'))



@login_required
def newscustomer(request):
    if request.POST:
        form3 = CustomerForm(request.POST or None)
        if form3.is_valid():
            if form3.save():
                return redirect('/all_customer', messages.success(request, 'Customer was registered successfully', 'alert-success'))
            else:
                return redirect('/customer', messages.error(request, 'Customer details no saved', 'alert-danger'))
        else:
            return redirect('/customer', messages.error(request, 'Form is not valid', 'alert-danger)'))
    else:
        form3 = CustomerForm()
    return render(request, 'new_client.html', {'form':form3})


@login_required
def all_customer(request):
    customer = Customer.objects.all()
    return render(request, 'all_customer.html', {'Customer': customer})


@login_required
def editcustomer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    if request.POST:
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            if form.save():
                return redirect('/all_customer', messages.success(request, 'Customer was successfully updated.', 'alert-success'))
            else:
                return redirect('/all_customer', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/all_customer', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = CustomerForm(instance=customer)
        return render(request, 'editcustomer.html', {'form': form})


@login_required
def destroycustomer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect('/all_customer', messages.success(request, 'Customer was successfully deleted.', 'alert-success'))



@login_required
def newsupplier(request):
    if request.POST:
        form4 = SupplierForm(request.POST or None)
        if form4.is_valid():
            if form4.save():
                return redirect('/all_supplier', messages.success(request,'Supplier was registered successfully', 'alert-success'))
            else:
                return redirect('/all_supplier', messages.error(request, 'Supplier details no saved', 'alert-danger'))
        else:
            return redirect('/all_supplier', messages.error(request,'Form is not valid', 'alert-danger)'))
    else:
        form4 = SupplierForm()
    return render(request, 'new_supplier.html', {'form':form4}
)


@login_required
def all_supplier(request):
    supplier = Supplier.objects.all()
    return render(request, 'all_supplier.html', {'Supplier': supplier})


@login_required
def editsupplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if request.POST:
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            if form.save():
                return redirect('/all_supplier', messages.success(request, 'Supplier was successfully updated.', 'alert-success'))
            else:
                return redirect('/all_supplier', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/all_supplier', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = SupplierForm(instance=supplier)
        return render(request, 'editsupplier.html', {'form': form})

@login_required
def destroysupplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    supplier.delete()
    return redirect('/all_supplier', messages.success(request, 'Supplier was successfully deleted.', 'alert-success'))



@login_required
def newexpense(request):
    if request.POST:
        form5 = ExpenseForm(request.POST or None)
        if form5.is_valid():
            if form5.save():
                return redirect('/all_expense', messages.success(request,'Expense was registered successfully', 'alert-success'))
            else:
                return redirect('/expense', messages.error(request, 'Expense details no saved', 'alert-danger'))
        else:
            return redirect('/expense', messages.error(request,'Form is not valid', 'alert-danger)'))
    else:
        form5 = ExpenseForm()
    return render(request, 'newexpense.html', {'form': form5}
)


@login_required
def all_expense(request):
    expenses = Expense.objects.all()
    return render(request, 'all_expense.html', {'Expense': expenses})


@login_required
def editexpense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    if request.POST:
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            if form.save():
                return redirect('/all_expense', messages.success(request, 'Expense  was successfully updated.', 'alert-success'))
            else:
                return redirect('/all_expense', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/all_expense', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = ExpenseForm(instance=expense)
        return render(request, 'editexpense.html', {'form': form})

@login_required
def destroyexpense(request, expense_id):
    expense = Expense.objects.get(id=expense_id)
    expense.delete()
    return redirect('/all_expense', messages.success(request, 'Expense was successfully deleted.', 'alert-success'))



@login_required
def newinventory(request):
    if request.POST:
        form6 = InventoryForm(request.POST or None)
        if form6.is_valid():
            if form6.save():
                return redirect('/all_inventory', messages.success(request,'Item was registered successfully', 'alert-success'))
            else:
                return redirect('/inventory.html', messages.error(request, 'Item details no saved', 'alert-danger'))
        else:
            return redirect('/inventory.html', messages.error(request,'Form is not valid', 'alert-danger)'))
    else:
        form6 = InventoryForm()
    return render(request, 'new_inventory.html', {'form': form6}
)

@login_required
def all_inventory(request):
    inventory = Inventory.objects.all()
    return render(request, 'all_inventory.html', {'Inventory': inventory})

@login_required
def editinventory(request, inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    if request.POST:
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            if form.save():
                return redirect('/all_inventory', messages.success(request, 'Item was successfully updated.', 'alert-success'))
            else:
                return redirect('/all_inventory', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/all_inventory', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = InventoryForm(instance=inventory)
        return render(request, 'editinventory.html', {'form': form})

@login_required
def destroyinventory(request, inventory_id):
    inventory = Inventory.objects.get(id=inventory_id)
    inventory.delete()
    return redirect('/all_inventory', messages.success(request, 'Item was successfully deleted.', 'alert-success'))



@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})


@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})


@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/orders', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/orders', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/orders', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form': form})


@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/orders', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/orders', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/orders', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form': form})


@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/orders', messages.success(request, 'Order was successfully deleted.', 'alert-success'))


def savane(request):
    from django.utils import translation
    #user_language = 'fr'
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return render(request, 'index-food-shop.html')


def set_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language !=settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = '/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path ='/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        return response


def about_us(request):
    return render(request, 'about.html')


def contact_us(request):
    return render(request, 'contact.html')
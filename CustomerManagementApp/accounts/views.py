from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm, CustomUserCreationForm, CustomerForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .filters import OrderFilter
from .decorators import *


@unauthenticated_user
def register_page(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully!!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Username OR Password is incorrect!!')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all().order_by('-date_created')
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders[:5], 'customers': customers, 'total_orders': total_orders, 'delivered': delivered,
               'pending': pending, 'total_customers': total_customers}
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user_page(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'total_orders': total_orders, 'delivered': delivered, 'pending': pending}
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def account_settings(request):
    user = request.user.customer
    form = CustomerForm(instance=user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all().order_by('-date_created')
    total_orders = orders.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders, 'my_filter': my_filter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_order(request, pk):
    order_form_set = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)

    # form = OrderForm(initial={'customer': customer})
    # form = OrderForm()

    form_set = order_form_set(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        form_set = order_form_set(request.POST, instance=customer)
        if form_set.is_valid():
            form_set.save()
            return redirect('home')

    context = {'form_set': form_set}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form_set = OrderForm(instance=order)
    if request.method == 'POST':
        form_set = OrderForm(request.POST, instance=order)
        if form_set.is_valid():
            form_set.save()
            return redirect('home')
    context = {'form_set': form_set}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
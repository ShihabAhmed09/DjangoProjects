from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # sending multiple category products
    # params = {'no_of_slides': no_of_slides, 'range': range(1, no_of_slides), 'product': products}
    # all_products = [[products, range(1, no_of_slides), no_of_slides],[products, range(1, no_of_slides), no_of_slides]]
    all_products = []
    category_products = Product.objects.values('category', 'id')  # getting category and id
    categories = {item['category'] for item in category_products}  # set comprehension
    # print(categories)
    for category in categories:
        products = Product.objects.filter(category=category)
        # print(products)
        n = len(products)
        no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
        all_products.append([products, range(1, no_of_slides), no_of_slides])
    params = {'all_products': all_products}
    return render(request, 'shop/index.html', params)


def about_us(request):
    return render(request, 'shop/about_us.html')


def contact_us(request):
    form_submit = False
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        description = request.POST.get('description', "")
        contact = Contact(name=name, email=email, phone=phone, description=description)
        contact.save()
        form_submit = True
    return render(request, 'shop/contact_us.html', {'form_submit': form_submit})


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id', "")
        email = request.POST.get('email', "")
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            # print(order, order[0].items_json, len(order))
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates = []
                response = ""
                for item in update:
                    updates.append({'text': item.update_description, 'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "items_json": order[0].items_json},
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "no item"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')
    return render(request, 'shop/tracker.html')


def search_match(query, item):
    """Return true only if query matches the item"""
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search').lower()
    all_products = []
    category_products = Product.objects.values('category', 'id')  # getting category and id
    categories = {item['category'] for item in category_products}  # set comprehension
    for category in categories:
        products_temp = Product.objects.filter(category=category)
        products = [item for item in products_temp if search_match(query, item)]
        # print(products)
        n = len(products)
        no_of_slides = n // 4 + ceil((n / 4) - (n // 4))
        if len(products) != 0:
            all_products.append([products, range(1, no_of_slides), no_of_slides])
    params = {'all_products': all_products, 'message': ""}
    if len(all_products) == 0 or len(query) < 4:
        params = {'message': "Please make sure to enter relevant search query."}
    return render(request, 'shop/search.html', params)


def product_view(request, my_id):
    # Fetching product using id
    product = Product.objects.filter(id=my_id)  # product is a list
    # print(product[0])
    param = {'product': product[0]}
    return render(request, 'shop/product_view.html', param)


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', "")
        amount = request.POST.get('amount', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        address = request.POST.get('address1', "") + ", " + request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip_code = request.POST.get('zip_code', "")
        order = Order(items_json=items_json, amount=amount, name=name, email=email, phone=phone, address=address, city=city,
                      state=state, zip_code=zip_code)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_description="The order has been placed")
        update.save()
        confirm_order = True
        order_id = order.order_id
        return render(request, 'shop/checkout.html', {'confirm_order': confirm_order, 'order_id': order_id})
    return render(request, 'shop/checkout.html')

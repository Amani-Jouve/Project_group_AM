from django.shortcuts import render

# Pages / vues principales 

def home(request):
    return render(request,'Main/home.html')

def customers(request):
    return render(request,'Main/customers.html')

def products(request):
    return render(request,'Main/products.html')

def orders(request):
    return render(request,'Main/orders.html')

# Pages / vues - Création

def create_customers(request):
    return render(request,'Main/customers_form.html')

def create_products(request):
    return render(request,'Main/products_form.html')

def create_orders(request):
    return render(request,'Main/orders_form.html')

# Pages / vues - Update

def update_customers(request):
    return render(request,'Main/customers_form.html')

def update_products(request):
    return render(request,'Main/products_form.html')

def update_orders(request):
    return render(request,'Main/orders_form.html')
from django.shortcuts import render
from .models import Customer,Product

# Pages / vues principales 

def home(request):
    return render(request,'Main/home.html')

def customers(request):
    if request.method=="POST":
        customer=Customer()
        customer.name=request.POST['customer_name']
        customer.customer_type=request.POST['customer_type']
        customer.DoB=request.POST['customer_DoB']
        customer.gender=request.POST['customer_gender']
        customer.email=request.POST['customer_email']
        customer.phone=request.POST['customer_phone']
        customer.address=request.POST['customer_address']
        customer.town=request.POST['customer_town']
        customer.region=request.POST['customer_region']
        customer.save()
        return redirect('/')
    else:
        my_customer=Customer.objects.all()
        context={"my_customer": my_customer}
        return render(request,'Main/customers.html',context)

def products(request):
    if request.method=="POST":
        product=Product()
        product.name=request.POST['product_name']
        product.description=request.POST['product_description']
        product.category=request.POST['product_category']
        product.n_lot=request.POST['product_n_lot']
        product.price_pdt_HT=request.POST['product_price_pdt_HT']
        product.price_pdt_TTC=request.POST['product_price_pdt_TTC']
        product.commercial_margin=request.POST['product_commercial_margin']
        product.stock_q=request.POST['product_stock_q']
        product.stock_security=request.POST['product_stock_security']
        product.stock_status=request.POST['product_stock_status']
        product.save()
        return redirect('/')
    else:
        my_product=Product.objects.all()
        context={"my_product": my_product}
        return render(request,'Main/products.html',context)
    
    
    
    
    
    
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
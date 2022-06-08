from django.db import models
from django.utils import timezone



class Customer(models.Model):
    """docstring fos Customer"""
    
    GENDER_CHOICES=(('Masculin','Masculin'),('Féminin','Féminin'),('Autre','Autre')
    )
    
    name=models.CharField(max_length=255, null=True)
    customer_type=models.CharField(max_length=255, null=True)
    DoB=models.DateTimeField(null=True)
    gender=models.CharField(max_length=255, null=True,choices=GENDER_CHOICES)
    email=models.CharField(max_length=255, null=True) 
    phone=models.CharField(max_length=12, null=True)
    address=models.CharField(max_length=255, null=True)
    town=models.CharField(max_length=255, null=True)
    region=models.CharField(max_length=255, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    
######Trouver la solution pour renvoyer ces calculs######

#     nb_orders=models.IntegerField(null=True)
#     total_orders=models.FloatField(null=True)
#     segment=models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name



class Product(models.Model):
    """docstring fos Product"""
    
    CATEGORY_CHOICES=(('PC','PC'),('Autre','Autre'))
    
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    category=models.CharField(max_length=200, null=True,choices=CATEGORY_CHOICES)
    n_lot=models.CharField(max_length=200, null=True)
    price_pdt_HT=models.FloatField(null=True)
    price_pdt_TTC=models.FloatField(null=True)
    commercial_margin=models.FloatField(null=True)
    stock_q=models.IntegerField(null=True)
    stock_security=models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.name    
    
    @property
    def stock_status(self):#for particular product order total
        if self.stock_q < self.stock_security:
            stock_res="A réapprovisionner"
        else:
            stock_res="Okay"
        return stock_res
    
    
    
class Order(models.Model):  
    """docstring fos Order"""
    
    STATUS_CHOICES=(('en préparation','en préparation'),('expédié','expédié'),('livré','livré'),('retour client','retour client'))
    
    customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    
    quantity=models.FloatField(null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    
    status=models.CharField(max_length=255, null=True,choices=STATUS_CHOICES)
    Delivery_date_expected=models.DateTimeField(null=True)
    Delivery_date_final=models.DateTimeField(blank=True, null=True)                   # Ce champ ne doit pas être obligatoire 
       
    #discount=models.FloatField(null=True)
    #price_after_discount==models.FloatField(null=True)

    @property
    def get_total_item_price_HT(self):#for particular product order total
        return self.quantity * self.product.price_pdt_HT
    
    @property
    def get_total_item_price_TTC(self):#for particular product order total
        return self.quantity * self.product.price_pdt_TTC
    
    @property
    def late_delivery(self):
        today=timezone.now()
        if self.Delivery_date_expected < today:
            delivery_res="En retard"
        else:
            delivery_res="Dans les temps"
        return delivery_res
    
    @property
    def delivery_fees(self):
        if self.get_total_item_price_HT<2000:
            fees_res=10
        else:
            fees_res=0
        return fees_res
    
    @property
    def get_total_order_price_TTC(self):#for particular product order total
        return self.get_total_item_price_TTC+self.delivery_fees
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
from django.db import models

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
    
#     Trouver la solution pour renvoyer ces calculs
#     nb_orders=models.IntegerField(null=True)
#     total_orders=models.FloatField(null=True)
#     segment=models.CharField(max_length=255, null=True)


    def __str__(self):
        return self.name



class Product(models.Model):
    """docstring fos Product"""
    
    CATEGORY_CHOICES=(('PC','PC'),('Autre','Autre'))
    STOCK_CHOICES=(('Okay','Okay'),('A réapprovisionner','A réapprovisionner'))
    
    name=models.CharField(max_length=200, null=True)
    description=models.CharField(max_length=200, null=True)
    category=models.CharField(max_length=200, null=True,choices=CATEGORY_CHOICES)
    n_lot=models.CharField(max_length=200, null=True)
    price_pdt_HT=models.FloatField(null=True)
    price_pdt_TTC=models.FloatField(null=True)
    commercial_margin=models.FloatField(null=True)
    stock_q=models.IntegerField(null=True)
    stock_security=models.IntegerField(null=True)
    stock_status=models.CharField(max_length=255, null=True,choices=STOCK_CHOICES)
    
    def __str__(self):
        return self.name    
    
class Order(models.Model):  
    """docstring fos Order"""
    customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    STATUS_CHOICES=(('en préparation','en préparation'),('expédié','expédié'),('livré','livré'),('retour client','retour client'))
    products=models.ManyToManyField(Product,related_name='re_name',db_column='name')
#     p_ordered_HT=models.ManyToManyField(Product,related_name='re_price_pdt_HT',db_column='price_pdt_HT')
#     p_ordered_TTC=models.ManyToManyField(Product,related_name='re_price_pdt_TTC',db_column='price_pdt_TTC')
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    #transport_fees=models.FloatField(null=True)
    total_price_HT=models.FloatField(null=True)
    total_price_TTC=models.FloatField(null=True)
    #discount=models.FloatField(null=True)
    #price_after_discount==models.FloatField(null=True)
    status=models.CharField(max_length=255, null=True,choices=STATUS_CHOICES)
    Delivery_date_expected=models.DateTimeField(null=True)
    Delivery_date_final=models.DateTimeField()                   # Ce champ ne doit pas être nul : à vérifier
    #late_delivery=models.CharField(max_length=255, null=True)   # formule à trouver
    
    def __str__(self):
        return self.name
    
# class Ordered_Product(models.Model):
#     product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
#     price_pdt_HT_O=models.ForeignKey(Product,null=True, through="price_pdt_HT", on_delete=models.SET_NULL)
#     price_pdt_TTC_O=models.ForeignKey(Product,through="price_pdt_TTC",null=True, on_delete=models.SET_NULL)
#     ordered_quantity=models.FloatField(null=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
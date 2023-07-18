from django.db import models
from datetime import datetime

class Product(models.Model):
    #Attributs 
    name=models.CharField(max_length=50,verbose_name='Title')
    content=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,default=500.00)
    image=models.ImageField(upload_to='photos/%y/%m/%d')
    active=models.BooleanField(default=True)
    category=models.CharField(max_length=50,blank=True,null=True,choices=[('pc','PC'),('phone','Phone')])
    
    
    def __str__(self) -> str:
        return self.name
    
    
#Classe pour les dates 
class Test(models.Model):
    date=models.DateField()
    time=models.TimeField(null=True)
    datetime=models.DateTimeField(null=True,default=datetime.now)
    
    
    def __str__(self) -> str:
        return str(self.date.day)
    
    
    
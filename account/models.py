from django.db import models

# Create your models here.

class Customer(models.Model):    
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=250)
    mobileno=models.CharField(max_length=15)
    dateofbirth=models.DateField(blank=True)
    emailid=models.EmailField(max_length=50,null=True)
    def __str__(self):
        return self.name
    
    



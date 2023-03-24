from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    employe_id = models.BigIntegerField()
    date = models.DateField(auto_now=True)
    phone = models.BigIntegerField(null=True)
    
    def __str__(self):
        return self.name
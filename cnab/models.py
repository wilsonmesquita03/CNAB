from django.db import models

class Cnab(models.Model):
    type = models.CharField(max_length=22)
    date = models.DateField()
    hour = models.TimeField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    nature = models.CharField(max_length=10)
    
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name="operations")




# Create your models here.

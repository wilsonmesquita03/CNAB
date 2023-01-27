from django.db import models

class Cnab(models.Model):
    type = models.CharField(max_length=12)
    data = models.DateTimeField()
    value = models.IntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, related_name="operations")




# Create your models here.

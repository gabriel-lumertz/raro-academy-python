from django.db import models

# Create your models here.

class Caixinha(models.Model):
    name = models.CharField(max_length=200)
    objective = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
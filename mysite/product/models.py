from django.db import models


class Product(models.Model):
    type_of_product = models.CharField(max_length=100)
    cost = models.IntegerField()

    def __str__(self):
        return self.type_of_product
# Create your models here.

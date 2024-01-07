from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ["type_of_product", "cost"]

admin.site.register(Product, ProductAdmin)
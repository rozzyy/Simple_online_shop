from django.contrib import admin
from .models import Product, Cart, Order, Contact
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'stock', 'price', 'category']
    list_filter = ['category', 'brand', 'created_date']

admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Contact)

#title and header
admin.site.site_header = "Simple Online Shop"
admin.site.site_title = "Simple Online Shop"

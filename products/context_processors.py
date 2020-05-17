def brand(request):
    from products.models import Product
    brand = Product.objects.all().values('brand').order_by('-brand')
    return {'brand': brand}
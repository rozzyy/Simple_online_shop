def brand(request):
    from products.models import Product
    from django.core.paginator import Paginator

    brand = Product.objects.all().values('brand').order_by('-brand')
    paginator = Paginator(brand, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return {'brand': page_obj}
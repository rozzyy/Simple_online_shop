def brand(request):
    from products.models import Product, Contact
    from django.core.paginator import Paginator

    brand = Product.objects.all().values('brand').order_by('-brand')
    paginator = Paginator(brand, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    pesan = Contact.objects.order_by('-created_date')
    view_count = 0
    for view_boolean in pesan.values('view'):
        if view_boolean['view'] == True:
            view_count += 1

    return {'brand': page_obj, 'pesan': pesan, 'view_count': view_count }
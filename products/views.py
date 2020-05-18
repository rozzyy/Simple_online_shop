from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView, 
    DetailView,
)
from django.views.generic.base import View
from django.urls import reverse_lazy
from .models import Contact, Product, Cart, Order
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist


# User Profile View
class ProfilePageView(TemplateView):
    template_name = 'account/profile.html'

class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        latest = Product.objects.order_by('-created_date')
        category = Product.objects.all().values('category').order_by('category')
        popular = Product.objects.order_by('-reviews')

        return render(request, self.template_name, {'latest': latest, 'category': category, 'popular': popular})

class ProductPageView(View):
    template_name = 'product.html'

    def get(self, request):
        product = Product.objects.all()
        categories = Product.objects.all().values('category').order_by('category')
        brands = Product.objects.all().values('brand').order_by('brand')
        title = Product.objects.all().values('title').order_by('title')[:10]

        return render(request, self.template_name, {'product': product, 'categories': categories, 'brands': brands, 'title': title})

class DetailPageView(DetailView):
    model = Product 
    template_name = 'detail.html'

class CartView(View):
    template_name = 'cart.html'

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            total = 0
            for item in order.item.all():
                total += item.total_price
            
            discount = 10/100 * float(total)

            total_all = float(total) - discount + 14

            context = {
                'object': order,
                'total': total,
                'discount': discount,
                'total_all': total_all
            }
            return render(self.request, self.template_name, context)
        except ObjectDoesNotExist:
            return redirect('/')

def add_to_cart(request, id):
    item = get_object_or_404(Product, pk=id)
    order_item, created = Cart.objects.get_or_create(
        product=item, user=request.user, ordered=False
    )

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(product__id=item.pk).exists():
            rating = request.POST.get('rating')
            cart = Cart.objects.filter(product=item.pk)
            if rating == None:
                rating = 0
                order_item.rating += rating
            else: 
                order_item.rating = int(rating)

            order_item.quantity += 1
            total = order_item.quantity * item.price
            order_item.total_price = total
            order_item.save()
            total_rating = 0
            users = cart.values('user').count()
            for crating in cart:
                total_rating += crating.rating 

            total = total_rating / users
            item.rating = total
            item.reviews = users
            item.save()
            return redirect("cart")
        else:
            total = order_item.quantity * item.price
            order_item.total_price = total
            rating = request.POST.get('rating')
            cart = Cart.objects.filter(product=item.pk)
            if rating == None:
                rating = 0
                order_item.rating += rating
                users = cart.values('user').count() - 1
            else: 
                order_item.rating = int(rating)
                users = cart.values('user').count()

            order_item.rating = int(rating)
            order_item.save()
            order.item.add(order_item)
            total_rating = 0
            for crating in cart:
                total_rating += crating.rating 

            total = total_rating / users
            item.rating = total
            item.reviews = users
            item.save()
            return redirect('cart')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, date_ordered=ordered_date
        )
        order.item.add(order_item)
        total = order_item.quantity * item.price
        order_item.total_price = total
        rating = request.POST.get('rating')
        cart = Cart.objects.filter(product=item.pk)
        if rating == None:
            rating = 0
            order_item.rating += rating
        else: 
            order_item.rating = int(rating)

        order_item.rating = int(rating)
        order_item.save()
        total_rating = 0
        users = cart.values('user').count()
        for crating in cart:
            total_rating += crating.rating 
        if total_rating == 0:
            total = 0
        else:
            total = total_rating / users
        item.rating = total
        item.reviews = users
        item.save()
        return redirect("cart")


def remove_from_cart(request, id):
    item = get_object_or_404(Product, pk=id)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(product__id=item.pk).exists():
            order_item = Cart.objects.filter(
                product=item,
                user=request.user,
                ordered=False
            )[0]
            order.item.remove(order_item)
            order_item.delete()
            total_rating = 0
            cart = Cart.objects.filter(product=item.pk)
            for crating in cart:
                total_rating += crating.rating 

            users = cart.values('user').count()
            total = total_rating / users
            item.rating = total
            item.reviews = users
            item.save()
            return redirect('cart')
        else:
            return redirect('cart')
    else:
        return redirect('cart')

def single_remove_item(request, id):
    item = get_object_or_404(Product, pk=id)
    order_qs = Order.objects.filter(
        user=request.user, 
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.item.filter(product__id=item.pk).exists():
            order_item = Cart.objects.filter(
                product=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                total = order_item.quantity * item.price
                order_item.total_price = total
                order_item.save()
            else:
                order.item.remove(order_item)
            return redirect('cart')
        else:
            return redirect('product', pk=id)
    else:
        return redirect('product', pk=id)



class OrderView(TemplateView):
    template_name = 'order.html'

class PaymentView(TemplateView):
    template_name = 'payment.html'

class SignUpDoneView(TemplateView):
    template_name = 'signup_done.html'

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

class SearchView(View):
   template_name = 'search.html'

   def get(self, request):
       query = self.request.GET.get('q')
       search = Product.objects.filter(Q(title__icontains=query) | Q(category__icontains=query) | Q(brand__icontains=query))

       return render(request, self.template_name, {'query': query, 'search': search})
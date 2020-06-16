from django.contrib.auth.views import LoginView
from django.views.generic import View, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import admin_required
from django.shortcuts import redirect, render
from products.models import Product, Contact
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy


class LoginPage(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True

@login_required
def login_success(request):
    if request.user.is_superuser:
        return redirect('dashboard')
    else:
        return redirect('home')

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class DashboardPage(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, *args, **kwargs):
        try:
            product = Product.objects.order_by('-created_date')
            User = get_user_model()
            member = User.objects.order_by('date_joined')

            return render(self.request, self.template_name, {'product': product, 'member': member})
        except ObjectDoesNotExist:
            return redirect('home')

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class ProductPage(View):
    template_name = 'dashboard/product.html'

    def get(self, *args, **kwargs):
        try:
            product = Product.objects.order_by('-created_date')
        
            return render(self.request, self.template_name, {'product': product})
        except ObjectDoesNotExist:
            return redirect('home')

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class InboxPage(View):
    template_name = 'dashboard/contact.html'

    def get(self, *args, **kwargs):
        contact = Contact.objects.order_by('created_date')

        return render(self.request, self.template_name, {'contact': contact})

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class InboxDetailPage(View):
    template_name = 'dashboard/detail_contact.html'

    def get(self, request, id):
        contact = Contact.objects.get(id=id)
        contact.view = True
        contact.save()
        
        return render(request, self.template_name, {'inbox': contact})

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class MemberPage(View):
    template_name = 'dashboard/user_page.html'

    def get(self, *args, **kwargs):
        User = get_user_model()
        member = User.objects.order_by('-date_joined')

        return render(self.request, self.template_name, {'member': member})

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class EditProductPage(UpdateView):
    model = Product
    fields = ['title', 'brand', 'category', 'price', 'description', 'stock', 'image']
    template_name = 'dashboard/edit_product.html'
    success_url = reverse_lazy('dashboard_products')

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class DeleteProductPage(DeleteView):
    model = Product
    template_name = 'dashboard/delete_product.html'
    success_url = reverse_lazy('dashboard_product')

@method_decorator([login_required(login_url='dashboard_login'), admin_required], name='dispatch')
class AddProductPage(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'dashboard/add_product.html'
    success_url = reverse_lazy('dashboard_product')



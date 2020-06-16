from django.urls import path
from .views import (
    LoginPage, 
    DashboardPage, 
    login_success,
    ProductPage,
    InboxPage,
    InboxDetailPage,
    MemberPage,
    EditProductPage,
    DeleteProductPage,
    AddProductPage,
)

urlpatterns = [
    path('', LoginPage.as_view(), name='dashboard_login'),
    path('home/', DashboardPage.as_view(), name='dashboard'),
    path('login_success/', login_success, name='login_success'),
    path('products/', ProductPage.as_view(), name='dashboard_products'),
    path('inbox/', InboxPage.as_view(), name='inbox'),
    path('member/', MemberPage.as_view(), name='member'),
    path('inbox/<int:id>/', InboxDetailPage.as_view(), name='detail_inbox'),
    path('product/<int:pk>/', EditProductPage.as_view(), name='edit_dashboard_product'),
    path('product/delete/<int:pk>/', DeleteProductPage.as_view(), name='delete_dashboard_product'),
    path('product/add/', AddProductPage.as_view(), name='add_dashboard_product'),
]

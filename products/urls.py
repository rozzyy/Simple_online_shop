from django.urls import path
from .views import ( 
    ProfilePageView, 
    HomePageView, 
    ProductPageView, 
    DetailPageView, 
    CartView,
    OrderView,
    PaymentView,
    SignUpDoneView,
    ContactView,
    SearchView,
    add_to_cart,
    remove_from_cart,
    single_remove_item,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('product/', ProductPageView.as_view(), name='product'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('single_remove_item/<int:id>/', single_remove_item, name='single_remove_item'),
    path('order/', OrderView.as_view(), name='order'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('signup_done/', SignUpDoneView.as_view(), name='signup_done'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
]

from itertools import product
from django.urls import path
from. import views
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/', views.shop, name='shop'),
    path('product_details/', views.product_details, name='product_details'),
    path('blog/', views.blog, name='blog'),
    path('blog_single/', views.blog_single, name='blog_single'),
    path('contact_us/', views.contact_us, name='contact_us'),
] 
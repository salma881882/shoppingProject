from .import views
from django.urls import path
app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('detail/', views.cart_detail, name='cart_detail'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('delete_cart/<int:product_id>/', views.delete_cart, name='delete_cart'),

    ]
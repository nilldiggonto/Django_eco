from django.urls import path
from .views import cart_home,cart_update,checkout_home,checkout_done_view,cart_detail_api_view
app_name = 'carts'
urlpatterns = [
    path('',cart_home,name='cart'),
    path('checkout/',checkout_home,name='checkout'),
    path('api/cart/',cart_detail_api_view,name='api-cart'),

    path('cart_update/',cart_update,name='cart-update'),
    path('cart_done/',checkout_done_view,name='checkout-done')
    

]

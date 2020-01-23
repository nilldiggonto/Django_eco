from django.shortcuts import render,redirect
from products.models import Product
from orders.models import Order
from .models import Cart
from accounts.models import GuestEmail
from accounts.forms import LoginForm,GuestForm
from billing.models import BillingProfile
from addresses.forms import AddressForm
from addresses.models import Address
from django.http import JsonResponse


def cart_detail_api_view(request):
       cart_obj,new_obj = Cart.objects.new_or_get(request)
       products = [{
          'id':x.id,
          'url':x.get_absolute_url(),
          'title':x.title,
          'price':x.price

            } for x in cart_obj.products.all()]

       cart_data = {'products': products, 'subtotal':cart_obj.subtotal, 'total':cart_obj.total}
       return JsonResponse(cart_data)

def cart_home(request):
    template= 'carts/cart.html'                # del request.session['cart_id']
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    context = {
       'cart':cart_obj,
    }
    return render(request,template,context) 


def cart_update(request):
       print(request.POST)
       product_id = request.POST.get('product_id')
       
       if product_id is not None:
         try:
            product_obj = Product.objects.get(id=product_id)
         except Product.DoesNotExist:
            return redirect('carts:cart')
         cart_obj,new_obj = Cart.objects.new_or_get(request)
         if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
         else:
            cart_obj.products.add(product_obj)
            added = True
         request.session['cart_item'] = cart_obj.products.count()
      #  return redirect(product_obj.get_absolute_url())
         if request.is_ajax():
              print('Ajax request')
              json_data = {
                 'added': added,
                 'removed': not added,
                 'cart_item_count':cart_obj.products.count(),
              }
              return JsonResponse(json_data)
       return redirect('carts:cart')

def checkout_home(request):
       cart_obj,cart_created = Cart.objects.new_or_get(request)
       order_obj = None
       if cart_created or cart_obj.products.count() == 0:
              return redirect('carts:cart')
     
      
      
       login_form = LoginForm()
       guest_form = GuestForm()
       address_form = AddressForm()
      #  billing_address_form = AddressForm()
       billing_address_id = request.session.get('billing_address_id', None)
       shipping_address_id = request.session.get('shipping_address_id', None)


       billing_profile,billing_profile_created = BillingProfile.objects.new_or_get(request)
       address_qs = None
       if billing_profile is not None:
             if request.user.is_authenticated:
                  address_qs = Address.objects.filter(billing_profile=billing_profile)
            #  shipping_address_qs = address_qs.filter(address_type = 'shipping')
            #  billing_address_qs = address_qs.filter(address_type = 'billing')
             order_obj,order_obj_created = Order.objects.new_or_get(billing_profile,cart_obj)
             if shipping_address_id:
                    order_obj.shipping_address  =Address.objects.get(id=shipping_address_id)
                    del request.session['shipping_address_id']
             if billing_address_id:
                    order_obj.billing_address  = Address.objects.get(id = billing_address_id)
                    del request.session['billing_address_id']
             if billing_address_id or shipping_address_id:
                    order_obj.save()
       if request.method == 'POST':
              is_done = order_obj.check_done()
              if is_done:
                     order_obj.mark_paid()
                     request.session['cart_item'] = 0
                     del request.session['cart_id']
                     return redirect('carts:checkout-done')
       context = {
          'object': order_obj,
          'billing_profile': billing_profile,
          'login_form': login_form,
          'guest_form':guest_form,
          'address_form':address_form,
          'address_qs' :address_qs
         #  'billing_address_form': billing_address_form,
       }
       return render(request,'carts/checkout.html',context)


         # order_qs = Order.objects.filter(cart=cart_obj,active=True)
         # if order_qs.exists():
         #       order_qs.update(active=False)
         # else:
         #       order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)









def checkout_done_view(request):
    return render(request,'carts/checkout-done.html')




# Create your views here.
# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print('nEw cart Created')
#     return cart_obj

 # if cart_id is None: 
        
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    #     print('create new cart')
    # else:
 # print('cart exist')
    # print(cart_id)

 # print(request.session)
    # print(dir(request.session))
    # key = request.session.session_key
    # print(key)
    # request.session['cart_id'] = 12
    # request.session['user'] = request.user.username
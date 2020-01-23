from django.shortcuts import render,Http404,get_object_or_404
from django.views.generic import ListView,DetailView
from carts.models import Cart

from analytics.mixins import ObjectViewdMixin

from .models import Product
# Create your views here.
class ProductListView(ListView):
    # queryset = Product.objects.all()
    model = Product
    template_name ='products/product_list.html'

class ProductFeaturedListView(ListView):
    model = Product

    template_name= 'products/product_list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()



class ProductDetailView(ObjectViewdMixin,DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        request = self.request
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context
    

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug , active=True)
        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404('Not Found')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404('ok what do yo want??')
        # object_viewd_signal.send(instance.__class__, instance=instance, request=request)

        return instance


class ProductFeaturedDetailView(ObjectViewdMixin,DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()


    # def get_object(self,*args,**kwargs):
    #     request= self.request
    #     pk =self.kwargs.get('pk')

    #     instance = Product.objects.get_by_id(pk)
    #     if instance is None:
    #         raise Http404('Product doesnt Exist')
    #     return instance
    
    
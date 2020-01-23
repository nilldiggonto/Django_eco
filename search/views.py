from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q
# Create your views here.

class ProductSearchView(ListView):
    model = Product
    template_name = 'search/search.html'

     
    def get_context_data(self, **kwargs):
        context = super(ProductSearchView, self).get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
    

    def get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q',None)
        if query is not None:
            
            return Product.objects.search(query)
        return Product.objects.none()

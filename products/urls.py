from django.urls import path
from .views import ProductListView,ProductDetailView,ProductFeaturedListView,ProductFeaturedDetailView

urlpatterns = [
    path('',ProductListView.as_view(),name='product_list'),
    path('featured/',ProductFeaturedListView.as_view(),name='featured'),
    path('<str:slug>/',ProductDetailView.as_view(),name='product_detail'),
    
    path('featured/<str:slug>/',ProductFeaturedDetailView.as_view(),name='featured_detail'),

    # path('<str:slug>/',ProductDetailView.as_view(),name='detail')
]

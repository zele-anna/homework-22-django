from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.HomeTemplateView.as_view(), name='home'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]

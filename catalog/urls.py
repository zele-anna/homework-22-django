from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', views.HomeTemplateView.as_view(), name='home'),
    path('contacts/', views.ContactsTemplateView.as_view(), name='contacts'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('product_list/', views.ProductListView.as_view(), name='product_list'),
    path('products/new/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/unpublish/', views.ProductUnpublishView.as_view(), name='product_unpublish'),
    path('product_list/category/<int:category_id>/', views.ProductByCategoryListView.as_view(), name='product_by_cat_list'),
]

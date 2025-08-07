from unicodedata import category

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, TemplateView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class CategoryListView(ListView):
    model = Category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        key = 'products_queryset'
        queryset = cache.get(key)
        if not queryset:
            queryset = super().get_queryset()
            cache.set(key, queryset, 60 * 15)
        return queryset


class ProductByCategoryListView(ListView):
    model = Product
    template_name = 'catalog/product_by_cat_list.html'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return get_products_by_category(category_id)


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        else:
            raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

    def has_permission(self):
        user = self.request.user
        product = self.get_object()
        return user == product.owner or user.has_perm('catalog.can_delete_product')


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    @staticmethod
    def post(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            return HttpResponse(f'{name}, Ваше сообщение отправлено!')
        return render(request, 'catalog/contacts.html')

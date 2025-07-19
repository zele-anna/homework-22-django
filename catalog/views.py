from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

class ProductListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    @staticmethod
    def post(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            return HttpResponse(f'{name}, Ваше сообщение отправлено!')
        return render(request, 'catalog/contacts.html')

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         return HttpResponse(f'{name}, Ваше сообщение отправлено!')
#     return render(request, 'contacts.html')

# def product_details(request, pk):
#     product = Product.objects.get(id=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context)

class ProductDetailView(DetailView):
    model = Product

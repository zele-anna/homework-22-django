from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'{name}, Ваше сообщение отправлено!')
    return render(request, 'contacts.html')

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'product_details.html', context)

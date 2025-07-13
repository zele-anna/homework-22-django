from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'{name}, Ваше сообщение отправлено!')
    return render(request, 'catalog/contacts.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def index(request):
    # value = -10
    # n1 = News('Новость1', 'text1', '07.11.23')
    # n2 = News('Новость2', 'text2', '08.11.23')
    # n3 = News('Новость3', 'text3', '09.11.23')
    # l = [n1, n2, n3]
    # context = {'title': 'Страница главная',
    #            'Header1': 'Заголовок страницы',
    #            'value': value,
    #            'numbers': l
    #            }
    if request.method == 'POST':
        print('Получили post-запрос')
        print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if title != None:
            new_product = Product(title, float(price), int(quantity))
            print('создан товар:', new_product.title, 'Общая сумма:', new_product.amount())

    else:
        print('Получили get-запрос')
    water = Product('Минералка', 43, 2)
    chocolate = Product('Шоколадка', 80, 1)

    colors = ['red', 'blue', 'golden', 'black']
    context = {
        'colors': colors,
        'water': water,
        'chocolate': chocolate
    }
    return render(request, 'main/index.html', context)

def get_demo(request, a):
    return HttpResponse(f'Вы ввели: {a}')

def about(request):
    return HttpResponse('<h1> About </h1>')


def contacts(request):
    return HttpResponse('<h1> Contacts </h1>')


def sidebar(request):
    return render(request, 'main/sidebar.html')

def custom_404(request, exception):
    return HttpResponse(f'Sorry, page not found... {exception}')

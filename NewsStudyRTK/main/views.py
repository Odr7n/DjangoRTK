from django.shortcuts import render
from django.http import HttpResponse
from .models import News


# Create your views here.

def index(request):
    value = -10
    n1 = News('Новость1', 'text1', '07.11.23')
    n2 = News('Новость2', 'text2', '08.11.23')
    n3 = News('Новость3', 'text3', '09.11.23')
    l = [n1, n2, n3]
    context = {'title': 'Страница главная',
               'Header1': 'Заголовок страницы',
               # 'value': value,
               'numbers': l
               }
    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('<h1> About </h1>')


def contacts(request):
    return HttpResponse('<h1> Contacts </h1>')


def sidebar(request):
    return render(request, 'main/sidebar.html')

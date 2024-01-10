import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as mpl
from .models import *


# Create your views here.

# Главная страница
def index(request):
    # dashboard = Dashboard.objects.all().first()
    # print('Автор новости', dashboard.title, ':', dashboard.author.account.gender)
    # context = {'dashboard': dashboard}

    # dashboards = Dashboard.objects.filter(author=request.user.id)
    # print(dashboards)

    dashboards = Dashboard.objects.get(author=2)
    # print(dashboards.tags.all())

    tag = Tag.objects.filter(title='Math').first()
    tagged_dashboards = Dashboard.objects.filter(tags=tag)
    print(tagged_dashboards)

    # Список всех дашбордов в разрезе пользователей
    user_list = User.objects.all()
    for u in user_list:
        print(Dashboard.objects.filter(author=u))
    print(user_list)

    context = {'dashboard': dashboards}

    return render(request, "pmdash/index_page.html", context)


# Страница отдельного дашборда
def mainBoard(request):
    mpl.use('agg')
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Главный дашборд')
    fig = plt.gcf()
    fig.savefig('pmdash/static/pmdash/dashboards/test.png')

    context = {'dashboard': 'pmdash/static/pmdash/dashboards/test.png', }
    return render(request, "pmdash/mainBoard_page.html", context)


# Страница со списком дашбордов
def allBoards(request):
    return render(request, "pmdash/allBoards_page.html")


# Страница аккаунта пользователя
def account(request):
    return render(request, "pmdash/account_page.html")


# Страница контактов
def contacts(request):
    return render(request, "pmdash/contacts_page.html")


# Детализация последней записи из БД
def detail(request, id):
    dashboard = Dashboard.objects.filter(id=id).first()

    # Пример создания дашборда
    # author=User.objects.get(id=request.user.id)
    # dashboard=Dashboard(author=author, title='Заголовок1', anouncement='Анонс', text='Текст')
    # dashboard.save()

    # Пример итерирования по объектам QuerySet
    dahsboards = Dashboard.objects.all()
    s = ''
    for d in dahsboards:
        s += f'<h1>{dashboard.title}</h1><br>'

    return HttpResponse(s)


# Страница 404
def page404(request):
    return HttpResponse("404 page")

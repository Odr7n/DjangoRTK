import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib as mpl


# Create your views here.

# Главная страница
def index(request):
    return render(request, "pmdash/index_page.html")


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

    context = {'dashboard': 'pmdash/static/pmdash/dashboards/test.png',}
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


# Страница 404
def page404(request):
    return HttpResponse("404 page")

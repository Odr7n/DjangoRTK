from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Главная страница
def index(request):
    return render(request, "pmdash/index.html")

# Страница отдельного дашборда
def mainBoard(request):
    return render(request, "pmdash/mainBoard.html")

# Страница со списком дашбордов
def allBoards(request):
    return render(request, "pmdash/allBoards.html")

# Страница аккаунта пользователя
def account(request):
    return render(request, "pmdash/account.html")

# Страница контактов
def contacts(request):
    return render(request, "pmdash/contacts.html")

# Страница 404
def page404(request):
    return HttpResponse("404 page")


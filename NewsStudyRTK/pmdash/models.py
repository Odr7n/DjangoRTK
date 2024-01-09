from django.db import models
from django.contrib.auth.models import User
import matplotlib as mpl


# Create your models here.

def sinGen():
    x = [1, 2, 3, 4, 5]
    return x


class Dashboard(models.Model):
    #Переменные
    categories = (('Tr', 'Trigonometric'),
                  ('Ln', 'Linear'),
                  ('Log', 'Logarithmic'))

    # Поля
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('Название', max_length=50, default='')
    anouncement = models.TextField('Аннотация', max_length=250)
    text = models.TextField('Текст новости')
    date = models.DateTimeField('Дата загрузки данных', auto_now=True)
    category = models.CharField(choices=categories, max_length=20, verbose_name='Категории')


    # Методы
    def __str__(self):
        return f'{self.title} от: {str(self.date)[:10]}'

    def get_absolute_url(self):
        return f'/pmdash/dashboards/{self.id}'


    # Метаданные модели - используются в панели администратора
    class Meta:
        ordering = ['title', 'date']
        verbose_name = 'Дашборд'
        verbose_name_plural = 'Дашборды'

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

menu = ['Про сайт', 'Добавитии статтю', 'звоторній звязок', 'Ввійти']

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def index(request):
    data = {
        'title': 'Головна сторінка',
        'menu': menu,
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 22)
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'Про сайт'})

def categories(request, cat_id):

    return HttpResponse(f'<h1> Статті по  категоріям </h1><p>id: {cat_id} </p>')

def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1> Статті по  категоріям </h1><p>slug: {cat_slug} </p>')

def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)
    return HttpResponse(f'<h1> Архів по рокам  </h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Сторінка не знайдена</h1>')


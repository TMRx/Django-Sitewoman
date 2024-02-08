from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse('Сторінка додатку Women')

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


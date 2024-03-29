from . import views
from django.urls import path, register_converter
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cats_it'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]
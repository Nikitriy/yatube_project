from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Тронный зал')


def group_posts(request, any_slug):
    return HttpResponse(f'Каракули отсортировано по {any_slug}')

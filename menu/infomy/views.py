from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'infomy/index.html'
    return render(request, template)


def it_s_me(request):
    return HttpResponse('Кто я')


def hobbies(request, pk):
    return HttpResponse(f'Мои увлечения {pk}')

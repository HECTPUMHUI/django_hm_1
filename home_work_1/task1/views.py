from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse('Домашня сторінка')


def progression(request, start, count, step):
    res = start - step
    list1 = []
    while count != 0:
        res += step
        count -= 1
        list1.append(res)
        list1.append(' ')
    return HttpResponse(list1)


def fib(request, n):
    f1 = 1
    f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    return HttpResponse(f2)


def greeting(request, name):
    return HttpResponse(f'Greeting, {name}')

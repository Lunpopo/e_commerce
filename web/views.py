# encoding: utf-8
"""
this is main function
"""

from django.shortcuts import render
from django.shortcuts import HttpResponse


def route(request):
    return render(request, 'index.html')


def industry_solution(request):
    return render(request, 'industry_solutions.html')


def test_page(request):
    return render(request, 'test_ui.html')


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')

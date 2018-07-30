# encoding: utf-8
"""
this is main function
"""

from django.shortcuts import render
from django.shortcuts import HttpResponse


def route(request):
    # return HttpResponse('你大爷')
    return render(request, 'index.html')

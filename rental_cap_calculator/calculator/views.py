from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import ImmobilienScout


class IndexView(generic.ListView):
    template_name = 'calculator/index.html'
    context_object_name = 'urls'

    def get_queryset(self):
        return ImmobilienScout.


def index(request):
    return HttpResponse("Hello, world. You entered the calculator!")


def calculate(request, url):
    context = {'url': url}
    return render(request, 'calculate/index.html', context)


def result(request, url):
    context = None
    return render(request, 'calculator/result.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.

def index(request):
    type = Type.objects.all()

    context = {
        'eno':type
    }

    return render(request, 'index.html', context)
    # return HttpResponse('This foodmart will serve king and queens worldwide in Jesus mighty name Amen')

def food(request, id):
    prep = Preparation.objects.filter(type_id=id)

    context = {
        'harry':prep
    }

    return render(request, 'food.html', context)


def details(request):
    detail = Preparation.objects.get(pk=id)

    context = {
        'detail':detail
    }

    return render(request, 'detail.html', context)

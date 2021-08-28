from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
from myapp.models import Women


def index(request):
    w = Women.objects.all()
    title = 'Home page'
    list = ['About','contacts','projects']
    context = {'women':w,'title':title,'list':list}
    return render(request, 'myapp/index.html',context)


def categories(request, s):
    return HttpResponse(f"<h1 style = 'font-size:50;'>categoriya</h1>  {s}")


def archive(request, year):
    if int(year)> 2021:
        # raise Http404()
        return redirect('search')
    else:
        return HttpResponse(f'<h1>{year}</h1>')


def search(request):
    return HttpResponse(f'search')


def pageNotFound(request,exception):
    return render(request, 'myapp/index.html')


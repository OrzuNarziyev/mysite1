from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.


def index(request,id):
    print('------------', id, '---------------')
    a = 'salom'
    return HttpResponse(f'hello world {a} {id}')


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
    return render(request,'index.html')


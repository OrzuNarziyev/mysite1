from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
from myapp.models import Women


def index(request):
    w  = Women.objects.order_by('-time_update')[:3]
    # w = Women.objects.get(id=1)
    # w.title = 'Rayxon Ganiyeva'
    # w.save()
    # w1 = Women()
    # w1.title = 'Selena Gomez'
    # w1.content ="lorem ipsum dolor sit"
    # w1.photo = "photos/2021/08/28/tigr_3d_art_3d.jpg"
    # w1.save()
    title = 'Home page'
    list = ['home','about', 'contacts', 'projects']
    context = {'women': w, 'title': title, 'list': list}
    return render(request, 'myapp/index.html', context)


def categories(request):
    return render(request,'myapp/categories.html')


def archive(request, year):
    if int(year) > 2021:
        raise Http404()
    else:
        return HttpResponse(f'<h1>{year}</h1>')

def about(request):
    return render(request,'myapp/about.html')

def post_detail(request):
    return render(request,'myapp/post_detail.html')


def pageNotFound(request, exception):
    return render(request, 'myapp/index.html')

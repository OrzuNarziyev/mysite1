from django.urls import path,re_path
from . import views

urlpatterns = [
    path('home/<int:id>',views.index ,name = 'home'), #http://127.0.0.1:8000/myapp/home/
    path('categories/<slug:s>',views.categories), #http://127.0.0.1:8000/myapp/categories/
    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),
    path('search/',views.search, name = 'search' )
]

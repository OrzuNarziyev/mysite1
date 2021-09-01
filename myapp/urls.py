from django.urls import path,re_path
from . import views


urlpatterns = [
    path('',views.index , name = 'home'), #http://127.0.0.1:8000/myapp/home/
    path('categories/',views.categories , name= 'categories'),
    path('about/', views.about, name='about'),
    path('post_detail/', views.post_detail, name='post_detail'),#http://127.0.0.1:8000/myapp/categories/
    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),


]


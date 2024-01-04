from django.urls import path
from . import views

urlpatterns = [
    path("",views.myfunctioncall, name="index"),
    path("about",views.myfunctionabout, name="index"),
    path("add/<int:a>/<int:b>", views.add, name="add"),
    path("intro/<str:name>/<str:age>",views.intro,name="intro"),
    path('myfirstpage',views.myfirstpage, name='myfirstpage'),
    path("mysecondpage",views.mysecondpage,name="mysecondpage"),
]
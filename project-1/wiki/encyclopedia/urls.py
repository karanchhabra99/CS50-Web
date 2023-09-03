from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    ,path(f"wiki/<str:wikiname>", views.wikiname, name="wikiname")
]

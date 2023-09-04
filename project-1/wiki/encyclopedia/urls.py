from django.urls import path

from . import views

app_name ="encyclopedia"
urlpatterns = [
    path("", views.index, name="index")
    ,path(f"wiki/<str:wikiname>", views.wikiname, name="wikiname")
    ,path("create", views.create_wiki, name="create_wiki")
    ,path(f"edit/<str:wikiname>", views.edit_wiki, name="edit_wiki")
]

from django.shortcuts import render
from django.http import Http404,HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikiname(request, wikiname):
    data =util.get_entry(wikiname)
    if data != None:
        return render(request, "encyclopedia/wikiname.html", {
        "wikiname": wikiname.capitalize(), "data": data
        })
    
    return HttpResponse('Page Not Found')
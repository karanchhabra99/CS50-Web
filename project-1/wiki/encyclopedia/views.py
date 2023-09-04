from django.shortcuts import render
from django.http import Http404,HttpResponse

from . import util



def wikipage(request, wikiname):
    '''
    This helps in rendering wikipages when clicked on hyperlink, searched
    '''
    data =util.get_entry(wikiname)
    if data != None:
        return render(request, "encyclopedia/wikiname.html", {
        "wikiname": wikiname.capitalize(), "data": data
            })
    elif util.get_related_entry(wikiname):
        return render(request, "encyclopedia/search_results.html", {
        "entries": util.get_related_entry(wikiname)
        })
    else:
        return render(request, "encyclopedia/PageNotFound.html", {
        "wikiname": wikiname
            })

def index(request):
    if request.method == "POST":
        wikiname= request.POST["q"]
        return wikipage(request, wikiname)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikiname(request, wikiname):
    return wikipage(request, wikiname)
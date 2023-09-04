from django.shortcuts import render
from django.http import Http404,HttpResponse
from django import forms
import random
import markdown2

  

from . import util

class Wiki_Form(forms.Form):
    title = forms.CharField(label="Title")
    body = forms.CharField(label="Body", widget=forms.Textarea(attrs={'style': 'height: 40em;'}))



def wikipage(request, wikiname):
    '''
    This helps in rendering wikipages when clicked on hyperlink, searched
    '''
    data =util.get_entry(wikiname)
    if data != None:
        return render(request, "encyclopedia/wikiname.html", {
        "wikiname": wikiname.capitalize(), "data": markdown2.markdown(data)
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
    if wikiname == 'Select a Random entry':
        wikiname = random.choice(util.list_entries())
    return wikipage(request, wikiname)


def create_wiki(request):
    if request.method == "POST":
        form = Wiki_Form(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            if title in util.list_entries():
                return render(request, "encyclopedia/Create_Error.html", {
                "entries": util.list_entries()
            })
            util.save_entry(title, body)
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })

    return render(request, "encyclopedia/create_wiki.html", {
        "form": Wiki_Form()
    })


def edit_wiki(request, wikiname="POST"):
    if request.method == "POST":
        form = Wiki_Form(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            util.save_entry(title, body)
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
        
    return render(request, "encyclopedia/edit_wiki.html", {
        "form": Wiki_Form({"title": wikiname, "body":util.get_entry(wikiname)})
    })
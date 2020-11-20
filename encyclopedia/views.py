from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
import markdown2
from .forms import searchForm
import random

from . import util

allentries = util.list_entries()


def index(request):
    allentries = util.list_entries()
    
    return render(request, "encyclopedia/index.html", {
        "entries": allentries,
        "searchForm": searchForm()
    })

def entry(request, entry):
    try:
        data = util.get_entry(entry)
        entryinfo =  markdown2.markdown(data)
        return render(request, 'encyclopedia/entry.html',{
            'entry':entry,
            'entryinfo':entryinfo,
            "searchForm": searchForm(),
            'entryFound': True
        })
    except:
        return render(request, 'encyclopedia/entry.html',{
            'message':'Entry not found',
            'entryFound':False,
            "searchForm": searchForm()
        })



def search(request):

    # If the form has been submitted...
    # A form bound to the POST data
    data = request.POST.copy()
    query = data.get('q')
    print('hello')
    print(allentries)
    print(query)

    if query in allentries:
        return redirect('entry page', entry= query)

    else:
    
        matches = [ x for x in allentries if re.search(query,x,re.IGNORECASE)]

        print(matches)
        return render(request, 'encyclopedia/search.html',{
            'matches': matches,
            "searchForm": searchForm()
        })

def newPage(request):
    allentries = util.list_entries()

    if request.method == 'POST':
        data = request.POST.copy()
        
        pageInfo = data.get('info')
        pageName = data.get('name')
        
        if pageName in allentries:
            return render(request, 'encyclopedia/new page.html',{
                'exists': True
                })
        else:
            util.save_entry(pageName, pageInfo)
            allentries = util.list_entries()

            return redirect('entry page', entry= pageName)

    else:
        return render(request, 'encyclopedia/new page.html',{
            'exists': False
        })

def edit(request, entry):
    if request.method == 'POST':
        data = request.POST.copy()
        print(data)
        pageInfo = data.get('info')
        pageName = data.get('name')
        util.save_entry(pageName, pageInfo)
        allentries = util.list_entries()
        return redirect('entry page', entry= pageName)

    else:
        data = util.get_entry(entry)
        print(data)
        return render(request, 'encyclopedia/edit.html', {
            'entry_info': data,
            'entry_name': entry
        })

def save(request, entry):
    if request.method == 'POST':
        data = request.POST.copy()
        pageInfo = data.get('info')
        pageName = data.get('name')
        util.save_entry(pageName, pageInfo)
        allentries = util.list_entries()
        return redirect('entry page', entry= pageName), allentries

    else:
        data = util.get_entry(entry)
        entryInfo =  markdown2.markdown(data)
        return render(request, 'encyclopedia/edit.html', {
            'entryInfo': entryInfo
        }) 

def randompg(request):
    entry = random.choice(allentries)

    return redirect('entry page', entry= entry)


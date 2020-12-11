from django.shortcuts import render

from . import util

import markdown

from django.contrib import messages


def index(request):
    entries = util.list_entries()
    query = request.GET.get('q','')
    results = []
    
    if query:
        for entry in entries:
            if query.lower() == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": entry,
                    "info": markdown.markdown(util.get_entry(entry))
                })
            else:
                if query.lower() in entry.lower():
                    results.append(entry) 

        return render(request, "encyclopedia/results.html", {
            "entries": results
        })

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def entry(request, title):
    entries = util.list_entries()
    query = request.GET.get('q','')
    results = []
    
    if query:
        for entry in entries:
            if query.lower() == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": entry,
                    "info": markdown.markdown(util.get_entry(entry))
                })
            else:
                if query.lower() in entry.lower():
                    results.append(entry) 

        return render(request, "encyclopedia/results.html", {
            "entries": results
        })

    else:
        info = util.get_entry(title)

        if info == None: 
            info = "File Not Found"
        else:
            info = markdown.markdown(info)
        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "info": info
        })


def new(request):
    
    entries = util.list_entries()
    print(entries)

    title = request.POST.get('title')
    content = request.POST.get('content')

    if title:
        for entry in entries:
            if title.lower() == entry.lower():
                messages.error(request, 'Entry exists!')
        
        util.save_entry(title, content)


    return render(request, "encyclopedia/new.html")
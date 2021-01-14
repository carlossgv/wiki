from django.shortcuts import render, redirect

from . import util

import markdown, random

from django.contrib import messages


def index(request):
    entries = util.list_entries()
    query = request.GET.get('q','')
    results = []
    randomEntry = random.choice(entries)
    
    if query:
        for entry in entries:
            if query.lower() == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": entry,
                    "content": markdown.markdown(util.get_entry(entry)),
                    "prueba": 'Cambio de prueba'
                })
            else:
                if query.lower() in entry.lower():
                    results.append(entry) 

        return render(request, "encyclopedia/results.html", {
            "entries": results
        })

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "randomEntry": randomEntry
        })


def entry(request, title):
    entries = util.list_entries()
    query = request.GET.get('q','')
    results = []
    randomEntry = random.choice(entries)
    
    if query:
        for entry in entries:
            if query.lower() == entry.lower():
                return render(request, "encyclopedia/entry.html", {
                    "title": entry,
                    "content": markdown.markdown(util.get_entry(entry))
                })
            else:
                if query.lower() in entry.lower():
                    results.append(entry) 

        return render(request, "encyclopedia/results.html", {
            "entries": results
        })

    else:
        content = util.get_entry(title)

        if content == None: 
            content = "File Not Found"
        else:
            content = markdown.markdown(content)
        
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content,
            "randomEntry": randomEntry
        })


def new(request):
    entries = util.list_entries()
    randomEntry = random.choice(entries)

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        for entry in entries:
            if title.lower() == entry.lower():
                messages.error(request, 'Entry exists!')
        
        util.save_entry(title, content)

        return redirect(f"/wiki/{title}", {
            "title": title,
            "content": content
        })

    elif request.method == 'GET':
        return render(request, "encyclopedia/new.html", {
            "randomEntry": randomEntry
        })

def edit(request, title):
    if request.method == "GET":    
        content = util.get_entry(title)
            
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

    elif request.method == "POST":
        content = request.POST.get('content')
        util.save_entry(title, content)

        return redirect(f"/wiki/{title}", {
            "title": title,
            "content": content
        })

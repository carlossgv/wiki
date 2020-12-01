from django.shortcuts import render

from . import util

import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):

    info = util.get_entry(title)

    if info == None: 
        info = "File Not Found"

    else:
        info = markdown.markdown(info)
        print(info)
    
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "info": info
    })

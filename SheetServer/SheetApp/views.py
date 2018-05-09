from django.shortcuts import render

from django.http import HttpResponse

from SheetApp import SheetConvert as SC



def index(request):
    SC.retrieveAndOutput()

    context = {
        'table':SC.retrieveAndOutput().iterrows()
    }
    return render(request, 'index.html', context )

def search(request):
    SC.retrieveAndOutput()
    difContext = {
    'table':SC.retrieveAndOutput().iterrows(),
    'term':request.POST.get('term',False)

    }

    return render(request, 'search.html',difContext )

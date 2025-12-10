from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render



def base_index(request):
    ctx = {"counts" : range(5)}
    # return HttpResponse('This is Base Page')
    return render(request, 'base.html', context=ctx)

def error_404_view(request, exception):
    ''' views에 404 코드를 통해 page를 나타냄 '''
    # return HttpResponseNotFound("The page is not Found ~!")
    return render (request, '404.html')
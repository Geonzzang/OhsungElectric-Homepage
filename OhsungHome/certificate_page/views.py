from django.shortcuts import render



# Create your views here.


def certi_render(request):
    return render(request,'certificate_page/certi.html')



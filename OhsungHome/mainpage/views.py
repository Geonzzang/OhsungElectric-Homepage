from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request) : 
    # return HttpResponse('Hello World')
    ''' 첫번째 기본 render를 통한 Html Templates 보내기'''
    return render(request, 'mainpage/main.html')

    # ''' context example '''
    # ctx = {
    #     "greetings" : "Hello there!", 
    #     "location" : {
    #         "city":"Seoul",
    #         "country": "South Korea"
    #     },
    #     "languages":["Korean","English"]
    # }

    # return render(request, "base.html", context=ctx)

def detail(request, question_id ):
    return HttpResponse(f'Hello world {question_id}')






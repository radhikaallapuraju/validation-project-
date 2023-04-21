from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
from app.models import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic submited successfully.....')
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WPFO=WebpageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('webpage inserted successufull.....')

    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    AFO=Access_RecordsForm()
    d={'AFO':AFO}
    if request.method=='POST':
        APFO=Access_RecordsForm(request.POST)
        APFO.save()
        return HttpResponse('access_recors inserted succussefully.....')
    return render(request,'insert_accessrecords.html',d)

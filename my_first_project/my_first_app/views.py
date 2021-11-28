from django.shortcuts import render
from my_first_app.models import Topic,WebPage,AccessRecord

# from django.http import HttpResponse
# Create your views here.

def index(request) :
    webpages_list = AccessRecord.objects.order_by('date')
    my_dict = {'access_records' : webpages_list}
    return render(request,'index.html',context = my_dict)

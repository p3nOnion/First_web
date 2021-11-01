from django.http import HttpResponse
from django.shortcuts import render
from Blog.models import *


# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by( 'date' )
    date_dicts = {'access_record': webpages_list}

    return render( request,'Blog/index.html',context=date_dicts )

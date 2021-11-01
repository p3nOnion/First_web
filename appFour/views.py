from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='appFour/index.html',)

def base(request):
    return render( request,template_name='appFour/base.html',)

def other(request):
    return render( request,template_name='appFour/other.html',)

def relative(request):
    return render( request,template_name='appFour/relative_url_template.html',)

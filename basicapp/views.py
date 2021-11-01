from django.shortcuts import render
from django.template import RequestContext
from . import form as forms


# Create your views here.
def index(request):
    return render( request,'basicapp/index.html',)


def form_page(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName( request.POST )

        if form.is_valid():
            print( "VALIDATION SUCCESS!" )
            print( "Name: ",form.cleaned_data['name'] )
            print( "Email: ",form.cleaned_data['email'] )
            print( "Text: ",form.cleaned_data['text'] )

    return render( request,'basicapp/form.html',{'form': form} )

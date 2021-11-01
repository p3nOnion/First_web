from django.shortcuts import render
from django.urls import reverse

from Home.forms import *

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse

from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def special(request):
    return HttpResponse( "You are logged in, Nice!" )


@login_required
def user_logout(request):
    logout( request )
    return HttpResponseRedirect( reverse( 'home:index' ) )


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserFrom( data=request.POST )
        profile_form = UserProfileInfoForm( data=request.POST )

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password( user.password )
            user.save()

            profile = profile_form.save( commit=False )
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print( user_form.errors,profile_form.errors )
    else:
        user_form = UserFrom()
        profile_form = UserProfileInfoForm()

    return render( request,'Home/registration.html',
                   {'user_form': user_form,'profile_form': profile_form,'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get( 'username' )
        password = request.POST.get( 'password' )
        print( "Username: {} and Password: {}".format( username,password ) )
        user = authenticate( username=username,password=password )
        if user:
            if user.is_active:
                login( request,user )
                return HttpResponseRedirect( reverse( 'home:index' ) )
            else:
                return HttpResponseRedirect( "Account not active!" )
        else:
            print( "Someone tried to login and failed" )
            print( "Username: {} and Password: {}".format( username,password ) )
            return HttpResponse( "Invalid login details supplied!" )
    else:
        print( "none" )
        return render( request,'Home/login.html' )


def index(request):
    return render( request,'Home/index.html')

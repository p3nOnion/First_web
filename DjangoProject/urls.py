from django.urls import include,path
from django.conf.urls import url
from django.contrib import admin
from Home import views

urlpatterns = [
    url( r'^admin/',admin.site.urls ),
    url( r'^logout/$',views.logout,name='logout' ),
    url( r'^special/$',views.special,name='special' ),

    url( r'^',include( 'Home.urls' ),name='home' ),

    # path( r'index/',include( 'Blog.urls' ),name='blog' ),

    url( r'^blog/',include( 'Blog.urls' ),name='blog' ),
    url( r'^apptwo/',include( 'appTwo.urls' ),name='apptwo' ),
    url( r'^basicapp/',include( 'basicapp.urls' ),name='basicapp' ),
    url( r'^appfour/',include( 'appFour.urls' ),name='appfour' ),

]

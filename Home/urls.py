from django.urls import include,path
from django.conf.urls import include,url

from Home import views

app_name = 'home'
urlpatterns = [
    url( r"^$",views.index,name='index' ),
    url( r'^index/',views.index ),
    url( r"^login",views.user_login,name='login' ),
    url( r"^logout",views.user_logout,name='logout' ),
    url( r"^register",views.register,name='register' ),
]

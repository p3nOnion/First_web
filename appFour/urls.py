from django.urls import include,path
from appFour import views

app_name = 'appfour'
urlpatterns = [
    path( r'',views.index,name='index' ),
    path( r'index/',views.index ),
    path( r'other/',views.other,name='other' ),
    path( r'relative/',views.relative,name='relative' ),

]

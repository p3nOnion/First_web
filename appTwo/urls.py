from django.urls import include,path
from appTwo import views
app_name='apptwo'
urlpatterns = [
    path( r"",views.index,name='index' ),
    path( r"users/",views.users,name='users' ),
]

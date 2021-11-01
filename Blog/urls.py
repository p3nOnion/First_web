from django.urls import include, path
from Blog import views
app_name='blog'
urlpatterns = [
    path( r"",views.index,name='index' ),
    path(r'index/', views.index, name='index'),
]
from django.urls import path,include
from basicapp import views
app_name ='basicapp'
urlpatterns = [
    path( r'',views.index,name='index' ),
    path( r'form/',views.form_page,name='form' ),
]

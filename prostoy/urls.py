from django.template.defaulttags import url
from django.urls import path
from prostoy import views
from prostoy.views import logIn,logOut

urlpatterns = [
    path('', views.index, name='home'),
    path(r'update', views.update, name='update'),
    path('getData', views.getData, name='getData'),
    path('otchet',views.otchet,name='otchet'),
    path('update_items/',views.update_items,name='update_items'),
    path('logIn', logIn, name='logIn'),
    path('logOut', logOut, name='logOut'),


]

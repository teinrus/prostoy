from django.template.defaulttags import url
from django.urls import path
from prostoy import views
from prostoy.views import profile_view, profileOut_view

urlpatterns = [
    path('', views.index, name='home'),

    path(r'update', views.update, name='update'),
    path(r'update2', views.update2, name='update2'),

    path('getData', views.getData, name='getData'),
    path('getData2', views.getData2, name='getData2'),

    path('update_items5/', views.update_items5, name='update_items5'),
    path('update_items2/', views.update_items2, name='update_items2'),

    path('otchet', views.otchet, name='otchet'),


    path('profile', profile_view, name='profile'),
    path('profileOut', profileOut_view, name='profileOut'),

]

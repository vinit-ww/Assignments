from django.conf.urls import url
from django.contrib import admin

from . import views
app_name='posts'
urlpatterns = [
   # ex: /posts/
    url(r'^$', views.posts_create, name='create'),
     # ex: /posts/1/
    url(r'^(?P<id>\d+)/$', views.posts_detail, name='detail'),
     # ex: /posts/list/      
    url(r'^list$', views.posts_list, name='list'),
     # ex: /posts/update/
    url(r'^update$', views.posts_update, name='update'),
     # ex: /posts/delete/
    url(r'^delete$', views.posts_delete, name='delete'),
 ]

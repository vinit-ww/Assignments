from django.conf.urls import url
from . import views

app_name = 'myapp'
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^myapp/$', views.new , name='detail'),
  url(r'^postman/$', views.some_post , name='postman'),
  url(r'^(?P<some_key>[a-zA-Z]+)/$', views.some_try , name='try'),

]
from django.conf.urls import url
from . import views

app_name = 'myapp'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
  url(r'^add/$', views.PostCreate.as_view(), name='add'),
  url(r'^(?P<pk>[0-9]+)/edit/$', views.PostEdit.as_view(), name='edit'),
  url(r'^(?P<pk>[0-9]+)/delete/$', views.PostDelete.as_view(), name='delete'),
  #url(r'^data/$', views.Home , name='data'),



]
# url(r'^(?P<some_key>[a-zA-Z]+)/$', views.some_try , name='try'),

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Something
import datetime
from django.db import models


def index(request):
  queryset=Something.objects.all()
  context={'some_index':queryset}
  return render(request,'myapp/index.html',context)

def new(request):
  #detail(request=<HttpRequest object>, something_id='1')
  #one_entery=Something.objects.values()
  #some_list=list(Something.objects.all())
  """
  queryset=Something.objects.all()
  for i in (queryset.values()):
    return HttpResponse(i.values())
  """

  queryset=Something.objects.all()
  context={'some_new':queryset}
  return render(request,'myapp/detail.html',context)
  #return HttpResponse("id is %s"%something_id)
  #return HttpResponse(one_entery)
  #return render(request,'myapp/index.html',{'id':some_obj.some_key})
  #return render(request,'myapp/index.html',a)
def some_post(request):
    if request.method == 'POST':
      some_word=request.POST['yours_name']
      return HttpResponse(some_word)

def some_try(request,some_key):
  some=get_object_or_404(Something,some_key=some_key)
  return render(request,'myapp/choice.html',{'some_value':some})
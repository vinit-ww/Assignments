from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Something
from django.views import generic
from django import forms
from .forms import NameForm ,Norm
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
  template_name='myapp/index.html'

  def get_queryset(self):
    return Something.objects.all()

class DetailView(generic.DetailView):
  model=Something
  template_name='myapp/detail.html'

class PostCreate(CreateView):
  template_name="myapp/new_form.html"
  model=Something
  fields=['some_key','pub_date']


class PostEdit(UpdateView):
  template_name="myapp/new_form.html"
  model=Something
  fields=['some_key','pub_date']

class PostDelete(DeleteView):
  template_name="myapp/new_form.html"
  model=Something
  fields=['some_key','pub_date']
  success_url=reverse_lazy('myapp:index')









'''
def Home(request):
    if request.method == 'POST':
      form=Norm(request.POST)
      if form.is_valid():
        instance=form.save(commit=False)
        print instanceform.save(commit=False)
        print instance.some_key
        print instance.pub_date
        instance.save()
    else:
      form=Norm()
    return render(request,'myapp/data.html',{'form':form})




def index(request):
  queryset=Something.objects.all()
  context={'some_index':queryset}
  return render(request,'myapp/index.html',context)

def new(request):
  #detail(request=<HttpRequest object>, something_id='1')
  #one_entery=Something.objects.values()
  #some_list=list(Something.objects.all())
  queryset=Something.objects.all()
  for i in (queryset.values()):
    return HttpResponse(i.values())

  queryset=Something.objects.all()
  context={'some_new':queryset}
  return render(request,'myapp/detail.html',context)
  return HttpResponse(one_entery)
  return render(request,'myapp/index.html',{'id':some_obj.some_key})
  return render(request,'myapp/index.html',a)
def some_post(request):
    if request.method == 'POST':
      some_word=request.POST['yours_name']
      return HttpResponse(some_word)

def some_try(request,some_key):
  some=get_object_or_404(Something,some_key=some_key)
  return render(request,'myapp/choice.html',{'some_value':some})
'''
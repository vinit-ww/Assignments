from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Post

def posts_create(request):
	queryset=Post.objects.all()
	context={
	"title":"Create",
	"object_list":queryset
	}
	return render(request,"index.html",context)



def posts_detail(request,id):
	#queryset=Post.objects.all()	
	instance=get_object_or_404(Post,id=id)
	context={
	"instance":instance,	
	"title":"details"
	}
	return render(request,"details.html",context)


def posts_list(request):
	return HttpResponse("list")

def posts_update(request):
	return HttpResponse("update")

def posts_delete(request):
	return HttpResponse("delete")


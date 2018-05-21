from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from posts.forms import PostForm
from django.contrib import messages
# Create your views here.
from .models import Post

def post_create(request):
	form=PostForm(request.POST or None) 
	if form.is_valid():
		instance=form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Success")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		messages.error(request, "Not Successfully Created")
	#if request.method=="POST":
		#print (request.POST.get("content"))
		#print (request.POST.get("title"))

	context={"form":form}
	return render(request,"posts/form.html",context)

def post_detail(request, id=None): #retrieve
	#instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "posts/detail.html", context)

def post_list(request): #list items
	queryset = Post.objects.all()
	context = {
		"object_list": queryset, 
		"title": "List"
	}

	return render(request, "posts/index.html", context)


def post_update(request,id=None):
	instance = get_object_or_404(Post, id=id)
	form=PostForm(request.POST or None,instance=instance) 
	if form.is_valid():
		instance=form.save(commit=False)
		#print form.cleaned_data.get("title")
		instance.save()
		messages.success(request,"Success")
		return HttpResponseRedirect(instance.get_absolute_url())
	else :
		messages.error(request,"iunSuccess")

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "posts/form.html", context)


def post_delete(request,id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Deleted")
	return redirect("posts:list")
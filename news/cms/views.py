from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def home(request):
	#context data
	data = {
		"posts":Post.objects.all()
	}
	return render(request,"home.html",data)


def insert(request):
	# p = Post()
	# p.title = request.POST.get('title')
	# p.author = request.POST.get('author')
	# p.content = request.POST.get('content')
	# p.save()
	title = request.POST.get('title')
	author = request.POST.get('author')
	content = request.POST.get('content')
	Post(title=title,author=author,content=content).save()

	return redirect(home)
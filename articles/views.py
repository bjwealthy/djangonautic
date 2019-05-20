from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required	#learn about decorators
from . import forms

#the request for homepage shd henceforth take us to 
#furniture landing page
def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request, slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")	#protects the view below from users that are not logged in. Such user is redirected to login page
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			#save article to db
			instance = form.save(commit=False)	#get the instance of the form to be saved, but don't save it yet
			instance.author = request.user	#attach the author that's logged into this session with that instance
			instance.save()
			return redirect('articles:list')

	else:
		form=forms.CreateArticle()
	return render(request, 'articles/article_create.html', {'form':form })
from django.shortcuts import render, get_object_or_404
from .models import Article, Comment


def home(request):
	return render(request, "news/home.html")

def about(request):
	return render(request, "news/about.html")

def subscription(request):
	return render(request, "news/subscription.html")

def actual_home(request):
	article = Article.objects.all().order_by("-date_posted")

	context = {
		'article': article
	}

	return render(request, "news/actual_home.html", context)

def article_detail(request, pk):
	article = get_object_or_404(Article, id=pk)

	context = {
		'article': article
	}

	return render(request, "news/article_detail.html", context)

def article1(request):
	return render(request, "news/articles/article1.html")

def article2(request):
	return render(request, "news/articles/article2.html")

def article3(request):
	return render(request, "news/articles/article3.html")

def article4(request):
	return render(request, "news/articles/article4.html")

def article5(request):
	return render(request, "news/articles/article5.html")
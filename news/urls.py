from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home/', views.actual_home, name="actual_home"),
	path('<int:pk>/', views.article_detail, name="article_detail"),

	path('about/', views.about, name="about"),
	path('subscription/', views.subscription, name="subscription"),

	
	path('article1/', views.article1, name="article1"),
	path('article2/', views.article2, name="article2"),
	path('article3/', views.article3, name="article3"),
	path('article4/', views.article4, name="article4"),
	path('article5/', views.article5, name="article5"),
]
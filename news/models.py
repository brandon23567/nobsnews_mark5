from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
	title 		= models.CharField(max_length=200)
	article_img = models.ImageField(upload_to="header_imgs/")
	snippet 	= models.TextField()
	body 		= RichTextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	article 	 = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
	comment_body = RichTextField()
	comment_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.comment_body
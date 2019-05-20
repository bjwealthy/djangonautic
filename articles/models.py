from django.db import models
from django.contrib.auth.models import User #we shall later use a foreign key to associate this user with the 'author' field in Article model
'''each table is represented by a model class 
-each record in the db table is created when a new object of the class is created
-each field/column represents the fields
-after making a model, we migrate it to db
'''
# Create your models here.
class Article(models.Model):
#https://docs.djangoproject.com/en/1.11/ref/models/fields
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.png", blank=True)
	author = models.ForeignKey(User, on_delete=models.PROTECT,default=None)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]+"..."
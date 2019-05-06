# models.py
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField(max_length=70)

	def __str__(self):
		return self.name 

class Book(models.Model):
	name = models.CharField(max_length=70)
	category = models.ForeignKey(to="Category", on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	users_like =  models.ManyToManyField(User, related_name='books_lieked')

	def __str__(self):
		return self.name

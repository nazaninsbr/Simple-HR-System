from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	date = models.DateField(null=True, blank=True)
	picture = models.FileField(upload_to='foodImages/', null=True, blank=True)
	description = models.TextField()
	orders = models.ManyToManyField(User)
	order_count = models.IntegerField(default=0)

	def __str__(self):
		return self.name

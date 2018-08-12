from django.db import models
from accounts.models import Employee
# Create your models here.
class Message(models.Model):
	author = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
	text = models.TextField()

	def __str__(self):
		return self.author.user.username+' : '+self.text
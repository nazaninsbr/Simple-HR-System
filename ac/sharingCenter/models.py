from django.db import models
from accounts.models import Employee
# Create your models here.
class Share(models.Model):
	id = models.AutoField(primary_key=True)
	uploader = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
	name = models.CharField(max_length=100)
	file = models.FileField(upload_to='shares', blank=True)

	def __str__(self):
		return self.name+'Uploaded by: '+self.uploader.user.username
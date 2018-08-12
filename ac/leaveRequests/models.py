from django.db import models
from accounts.models import Employee
# Create your models here.
class LeaveRequest(models.Model):
	id = models.AutoField(primary_key=True)
	request_from = models.ForeignKey(Employee, related_name='sender', on_delete= models.CASCADE)
	request_to = models.ForeignKey(Employee, related_name='reciever', on_delete= models.DO_NOTHING)
	explanation = models.TextField()
	leave_date = models.DateField(null=True, blank=True)
	request_date = models.DateField(null=True, blank=True)
	approved = models.IntegerField()

	def __str__(self):
		return "From: "+str(self.request_from.user.username)+" To: "+str(self.request_to.user.username)
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Employee(models.Model):
	STANDARD = 'STD'
	MANAGER = 'MGR'
	SR_MANAGER = 'SRMGR'
	PRESIDENT = 'PRES'

	EMPLOYEE_TYPES = (
		(STANDARD, 'base employee'),
		(MANAGER, 'manager'),
		(SR_MANAGER, 'senior manager'),
		(PRESIDENT, 'president')
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	role = models.CharField(max_length=25, choices=EMPLOYEE_TYPES)
	gender = models.CharField(max_length=50)
	job_description = models.TextField()
	birth_date = models.DateField(null=True, blank=True)
	profile_picture = models.FileField(upload_to='profileImages', blank=True)
	department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
	salary = models.DecimalField(max_digits=20, decimal_places=3)

	manager = models.ForeignKey('self', null=True, blank=True, related_name='employee', on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.user.first_name+' '+self.user.last_name
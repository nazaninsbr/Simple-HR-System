from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from datetime import timedelta, date
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout, login

# Create your views here.
def home(request, slug):
	if not request.user.is_authenticated:
		return redirect('login')
	user = User.objects.filter(username=slug)
	thisEmp = Employee.objects.filter(user=user[0])
	if thisEmp is not None:
		userInfo = {'username': slug, 'first_name': user[0].first_name, 'email':user[0].email, 'role': thisEmp[0].role, 'birth_date': thisEmp[0].birth_date}
		content = {'userInfo': userInfo}
		return render(request, 'accounts/home.html', content)
	else:
		return HttpResponse('<h1>Could not find user</h1>')

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home', str(request.user.username))
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return home(request, str(username))
		else:
			return render(request, 'accounts/login.html', {'error': 'could not find user or user information incorrect'})
	else:
		return render(request, 'accounts/login.html')


def logout_view(request):
	logout(request)
	return render(request, 'accounts/logout.html')

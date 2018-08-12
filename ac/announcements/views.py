from django.shortcuts import render
from .models import Message
from accounts.models import Employee
# Create your views here.
def create(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			thisEmp = Employee.objects.filter(user=request.user)[0]
			author = thisEmp
			text = request.POST["text"]
			message_obj = Message(author = author, text=text)
			message_obj.save()
			return view(request)
		else:
			return render(request, 'announcements/create_announcements.html')
	else:
		return redirect('login')
	

def view(request):
	if request.user.is_authenticated:
		all_announcements = Message.objects.all()
		content = {'messages': all_announcements}
		return render(request, 'announcements/announcements.html', content)
	else:
		return redirect('login')
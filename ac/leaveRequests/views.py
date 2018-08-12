from django.shortcuts import render
from .models import LeaveRequest
from accounts.models import Employee
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.
def view_leave_requests(request):
	if request.user.is_authenticated:
		thisEmp = Employee.objects.filter(user=request.user)[0]
		# if thisEmp.role in ['SRMGR', 'MGR', 'PRES']:
		all_sent = LeaveRequest.objects.filter(request_from=thisEmp)
		all_recieved = LeaveRequest.objects.filter(request_to=thisEmp)
		content = {'recieved' : all_recieved, 'sent': all_sent}
		return render(request, 'leave/leaveReqs.html', content)
	else:
		return redirect('login')

def create(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			reciever_username = request.POST["reqTo"]
			recieverUser = User.objects.get(username=reciever_username)
			recieverEmp = Employee.objects.filter(user=recieverUser)[0]
			senderEmp = Employee.objects.filter(user=request.user)[0]
			leave_date = datetime.strptime(request.POST["reqDate"], '%b %d %Y')
			explanation = request.POST["explanation"]
			approved = 2 #not seen yet
			req_obj = LeaveRequest(request_to=recieverEmp, request_from=senderEmp, explanation=explanation, leave_date=leave_date, request_date=datetime.now().date(), approved=approved)
			req_obj.save()
			return view_leave_requests(request)
		else:
			thisEmp = Employee.objects.filter(user=request.user)[0]
			today = datetime.now().date()
			content = {'sender': thisEmp.user.first_name+' '+thisEmp.user.last_name, 'date': today}
			return render(request, 'leave/create_leave_request.html', content)
	else:
		return redirect('login')

def view_single_request(request, slug):
	if request.user.is_authenticated:
		if request.method=='POST':
			if 'Deny' in request.POST:
				thisReq = LeaveRequest.objects.get(id=slug)
				thisReq.approved = 0
				thisReq.save()
			elif 'Approve' in request.POST:
				thisReq = LeaveRequest.objects.get(id=slug)
				thisReq.approved = 1
				thisReq.save()
			return view_leave_requests(request)
		else:
			thisReq = LeaveRequest.objects.get(id=slug)
			thisEmp = Employee.objects.filter(user=request.user)[0]
			if thisReq.request_to==thisEmp:
				content = {'request' : thisReq}
				return render(request, 'leave/reciever_single_request.html', content)
			else:
				content = {'request' : thisReq}
				return render(request, 'leave/sender_single_request.html', content)
	else:
		return redirect('login')
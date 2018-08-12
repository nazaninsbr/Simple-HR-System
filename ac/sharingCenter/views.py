from django.shortcuts import render
from .models import Share
from accounts.models import Employee
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.
def all(request):
	if request.user.is_authenticated:
		all_items = Share.objects.all()
		content = {'all': all_items}
		return render(request, 'sharing/view_all.html', content)
	else:
		return redirect('login')

def download(request, slug):
	if request.user.is_authenticated:
		item = Share.objects.get(id=slug)
		if 'pdf' in str(item.file):
			return HttpResponse(item.file, content_type='application/pdf')
	else:
		return redirect('login')

def upload(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			thisEmp = Employee.objects.filter(user=request.user)[0]
			myfile = request.FILES['myfile']
			fileName = request.POST['filename']
			share = Share(uploader=thisEmp, name=fileName, file=myfile)
			share.save()
			return redirect('view_shares')
		else:
			return render(request, 'sharing/upload.html')
	else:
		return redirect('login')
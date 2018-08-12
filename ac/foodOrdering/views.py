from django.shortcuts import render
from .models import Food
from accounts.models import Employee
from datetime import datetime, timedelta, time
from django.shortcuts import redirect

# Create your views here.
def menu(request):
	if request.user.is_authenticated:
		today = datetime.now().date()
		tomorrow = today + timedelta(1)
		allFoods = Food.objects.filter(date__range=[tomorrow, "2100-01-31"])
		content = {'foods': allFoods, 'user': request.user}
		return render(request, 'food/menu.html', content)
	else:
		return redirect('login')

def order_food(request, slug):
	if request.user.is_authenticated:
		food_item = Food.objects.get(id=slug)
		food_item.orders.add(request.user)
		food_item.order_count = food_item.order_count+1
		food_item.save()
		return redirect('menu')
	else:
		return redirect('login')

def remove_food_order(request, slug):
	if request.user.is_authenticated:
		food_item = Food.objects.get(id=slug)
		food_item.orders.remove(request.user)
		food_item.order_count = food_item.order_count-1
		food_item.save()
		return redirect('menu')
	else:
		return redirect('login')

def all_orders_view(request, slug):
	if request.user.is_authenticated:
		food_item = Food.objects.get(id=slug)
		all_orders = [x for x in food_item.orders.all()[1:]]
		content = {'orders': all_orders, 'name': food_item.name}
		return render(request, 'food/all_orders.html', content)
	else:
		return redirect('login')



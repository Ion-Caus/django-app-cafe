from django.shortcuts import render

from .models import Order
from .forms import OrderForm, DrinkForm

from .price_calculator import order_price

def index(request):
    submitted = False

    if request.method == 'POST':
        drinkForm = DrinkForm(request.POST)
        orderForm = OrderForm(request.POST)

        if drinkForm.is_valid():
            drinkForm.save()

            if orderForm.is_valid():
                orderForm.instance.drink = drinkForm.instance
                orderForm.save()

                total = order_price(orderForm.instance)

            return render(request, 'index.html', {'orderForm' : orderForm, 'drinkForm' : drinkForm, 'submitted' : True, 'total' : total})
    else:
        orderForm = OrderForm
        drinkForm = DrinkForm
    
    return render(request, 'index.html', {'orderForm' : orderForm, 'drinkForm' : drinkForm})

def orders(request):
    orders = Order.objects.order_by('-created_at')
    return render(request, 'orders.html', { 'orders': orders})

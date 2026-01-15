from django.shortcuts import render,redirect
from Pages.models import *
from Pages.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from Pages.utils import *
import datetime
import json

# Create your views here.
#...........HomePage-View............#
def homepage_view(request):
      data = cartData(request)
      cartItems = data['cartItems']
      context = {'cartItems':cartItems}
      return render(request, 'homepage.html', context)
    


#...........HomePage2-View............#
@login_required(login_url= 'login')
def homepage2_view(request):
      data = cartData(request)
      cartItems = data['cartItems']
      context = {'cartItems':cartItems}
      return render(request, 'homepage2.html', context)




#...........AboutPage-View............#
@login_required(login_url= 'login')
def aboutpage_view(request):
      data = cartData(request)
      cartItems = data['cartItems']
      context = {'cartItems':cartItems}
      return render(request, 'about.html', context)




#...........ContactusPage-View.........#
@login_required(login_url= 'login')
def contactuspage_view(request):
    data = cartData(request)
    cartItems = data['cartItems']
    form1 = contactusform()
    if request.method == 'POST':
        form1 = contactusform(request.POST)
        if form1.is_valid():
            form1.save()
        data = form1.cleaned_data.get('name')
        messages.success(request, 'Your message has been submitted!'+ data)
        return redirect('contact')
    context ={'form1': form1, 'cartItems':cartItems}
    return render(request, 'contact.html', context)






#...............SignupPage-View..............#
def signuppage_view(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else:
        form2 = signupform()
        if request.method == 'POST':
            form2 = signupform(request.POST)
            if form2.is_valid():
             user =  form2.save()
             useraccount = form2.cleaned_data.get('username')
             messages.success(request, 'You have signedup successfully!'+ useraccount)
             Customer.objects.create(user=user, name=user.username, email=user.email)
             return redirect('login')
    context = {'form2': form2}
    return render(request, 'signup.html', context)







#...............LoginPage-View................#
def loginpage_view(request):
    if request.user.is_authenticated:
        return redirect('home2')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home2')
            else:
                messages.info(request, 'Username or Password is incorrect!')
    context = {}
    return render(request, 'login.html', context)






#...................Logout..................#
def logoutpage(request):
    logout(request)
    return redirect('login')






#.................StorePage-View....................#
@login_required(login_url= 'login')
def storepage_view(request):
	data = cartData(request)
	cartItems = data['cartItems']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)


#.................CartPage-View....................#
@login_required(login_url= 'login')
def cartpage_view(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)




#.................CheckoutPage-View.....................#
@login_required(login_url= 'login')
def checkoutpage_view(request):

	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)



#.................UpdateItemPage-View.....................#
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)






#..................ProcessOrderPage-View....................#
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)


#................Finally! Has Finished!...................#
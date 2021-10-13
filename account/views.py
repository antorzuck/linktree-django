from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from mains.views import *


# Create your views here.

def login(request):
	if request.method == 'POST':
		usrn = request.POST['lu']
		pas = request.POST['lp']
		user = auth.authenticate(username=usrn, password=pas)
		if user is not None:
			auth.login(request, user)
			return redirect(dashboard)
		else:
			messages.error(request, "Incorrect password, try give another shot!")
			return render(request, 'login.html')
	return render(request, 'login.html')


def signup(request):
	if request.method == 'POST':
		username = request.POST['su']
		password = request.POST['sp']
		conpass = request.POST['spc']
		if password != conpass:
			messages.error(request, "Password not mathed. try give another shot!")
			return render(request, 'signup.html')
		if len(username) < 4:
			messages.error(request, "Username must be 5 characters long.")
			return render(request, 'signup.html')
		try:
			usr = User.objects.get(username=username)
			messages.error(request, "Username already exist, try another!")
			return render (request, 'signup.html')
		except User.DoesNotExist:
			usr = User.objects.create_user(username=username, password=password)
			usr.save()
			auth.login(request, usr)
			messages.info(request, "Congratulations, account successfully created!")
			return redirect(dashboard)
	else:
		return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


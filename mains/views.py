from django.shortcuts import render, redirect
from django.contrib import messages
from mains.models import *
from django.contrib.auth.models import User


def home(request):
	return render(request, 'base.html')
	
	
def dashboard(request):
	loguser = request.user
	link = Links.objects.filter(user=loguser)
	
	context={
				'links':link
	}
	return render(request, 'dashboard.html', context)


def addlink(request):
	if request.method == "POST":
		user = request.user
		title =request.POST['ttl']
		url = request.POST['lnk']
		sav = Links(user=user, title=title, url=url)
		sav.save()
		return redirect(dashboard)


def showlink(request, username):
	user = User.objects.get(username=username)
	link = Links.objects.filter(user=user)
    
	context={
	'user':user,
	'link':link
	}
	return render(request, 'profile.html', context)

def delete(request, id):
	get = Links.objects.get(pk=id)
	get.delete()
	return redirect(dashboard)
	
def editprofile(request):
	info = Profile.objects.get(user=request.user)
	if request.method == 'POST':
		info.user = request.user
		info.img = request.FILES.get('profilepic')
		info.bio = request.POST['biodata']
		info.save()
		return render(request, 'editprofile.html')
		
	context={'info':info}
	return render(request, 'editprofile.html', context)
	

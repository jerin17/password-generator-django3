from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def password(request):
	password = 123
	return render(request, 'password.html',{'password':password})
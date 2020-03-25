from django.shortcuts import render
import random

def home(request):
	return render(request, 'home.html')

def password(request):
	password = ""
	char = list('qwertyuiopasdfghjklzxcvbnm')
	len = int(request.GET.get('length',12))

	if request.GET.get('uppercase'):
		char.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
	if request.GET.get('numbers'):
		char.extend(list('1234567890'))
	if request.GET.get('special'):
		char.extend(list('!@#$%^&*()_+?>:~'))

	for x in range(len):
		password += random.choice(char)

	return render(request, 'password.html',{'password':password, 'len':len})
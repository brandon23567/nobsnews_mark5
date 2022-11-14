from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		myuser = User.objects.create_user(username, email, password)
		myuser.save()

		return redirect('actual_home')

	return render(request, "user_auth/signup.html")

def signin(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)

			return redirect('actual_home')

	return render(request, "user_auth/signin.html")
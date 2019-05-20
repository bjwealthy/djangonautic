from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST) #passing the dta supplied by user into a new instance of UserCreationForm for validation. form(the instance returned is either valid or invalid)
		if form.is_valid():	#validity test(returns True or False)
			user = form.save()
			login(request, user)
			return redirect('articles:list')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):	#don.t use 'login' cos it's already defined in django (ln 3)
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#log in user
			user = form.get_user()
			login(request, user)
			#if the next property exists in the post data, we can send user to that value
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			else:	
				return redirect('articles:list')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('articles:list')
	
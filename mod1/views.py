from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm,userloginform
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
        return render(request, 'mod1/index.html')
'''def register(request):
	return render(request,'mod1/register.html')'''

#def login(request):
	#return render(request,'mod1/login.html')

def home(request):
	return render(request,'mod1/home.html')
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return render(request,'mod1/home.html')
    else:
        form = SignUpForm()
    c={'form':form}
    return render(request, 'mod1/register.html',c)

def user_login(request):
	if request.method== 'POST':
		form=userloginform(request.POST)
		if form.is_valid():
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username,password=password)
			if user:
				if user.is_active:
					auth_login(request,user)
					return redirect('mod1:home')
	else:
		form = userloginform()
	context={
	'form':form,
	}
	return render(request,'mod1/login.html',context)

def user_logout(request):
	logout(request)
	return redirect('index')
def oracle(request):
	return render(request,'mod1/oracle.html')

def mysql(request):
	return render(request,'mod1/mysql.html')

def mariadb(request):
	return render(request,'mod1/mariadb.html')

def postgres(request):
	return render(request,'mod1/postgres.html')

def mysqllambda(request):
	return render(request,'mod1/mysqllambda.html')


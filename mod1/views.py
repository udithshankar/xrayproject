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
					request.session['username'] = username
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

def myaccount(request):
	username = None
	if not request.user.is_authenticated:
		return render(request, 'mod1/login.html')
	else:
		username = request.user.username
		email=request.user.email
		return render(request, 'mod1/myaccount.html', {'username': username, 'email': email})

def about(request):
	return render(request, 'mod1/about.html')


def aurora(request):
	return render(request, 'mod1/aurora.html')


def redshift(request):
	return render(request, 'mod1/redshift.html')


def sqlserver(request):
	return render(request, 'mod1/sqlserver.html')

def mysqlsup(request):
	return render(request, 'mod1/mysqlsup.html')	

def rdssup(request):
	return render(request, 'mod1/rdssup.html')	

def rds(request):
	return render(request, 'mod1/rds.html')	

def rdsadvan(request):
	return render(request, 'mod1/rdsadvan.html')	


def database(request):
	return render(request, 'mod1/database.html')	
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import login as auth_login
from admin.homepage.models import Homepage
from django.db import connection
import re

# Create your views here.

def index(request):
	
	data = Homepage.objects.all()

	return render(request, 'frontendTemplates/home/index.html', {'data':data})



def signup(request):
	return render(request, 'frontendTemplates/signup/index.html')


def signup_post(request):
	if request.method == 'POST':
		new_user = {}
		new_user['fname'] = request.POST['fname']
		new_user['lname'] = request.POST['lname']
		new_user['email_Id'] = request.POST['email_id']
		new_user['password'] = request.POST['password']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',new_user['fname']):

			messages.error(request, 'Enter a valid Name')
			return redirect('home-signup')
		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',new_user['lname']):

			messages.error(request, 'Enter a valid Name')
			return redirect('home-signup')

		if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$',new_user['email_Id']):

			messages.error(request, 'Enter a valid Email')
			return redirect('home-signup')


		print (new_user)
		# usr = CustomUser(name=name, email=email, password=make_password(password), usr_phone=number, usr_gender=gender)

		# usr.save()
		with connection.cursor() as cursor:
			cursor.execute("Insert Into User_Accounts(email_Id, password, fname, lname) Values (%s, %s, %s, %s)",
            [new_user["email_Id"], new_user["password"], new_user["fname"], new_user["lname"]])

		messages.success(request, 'Successfully Registered!')

		return redirect('home-signup')

'''
def add_user_account(data):
    with connection.cursor() as cursor:

        if DEBUG:
            print(data)

        cursor.execute("Select * from User_Accounts where emailid = %s", [data["emailid"]])

        row = cursor.fetchone()
        # User Account already present
        if row != None:
            return False

        cursor.execute("Insert Into User_Accounts Values (%s, %s, %s)",
            [data["emailid"], data["passwd"], data["type_of_acc"]]
        )

        return True
'''

def login(request):
	return render(request, 'frontendTemplates/login/index.html')


def login_post(request):
	username = request.POST['email']
	password = request.POST['password']

	if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
		messages.error(request, 'Enter a valid Email')
		return redirect('home-login')

	if len(password) < 3:
		messages.error(request, 'Provide a Valid Password')
		return redirect('home-login')

	UserModel = get_user_model()


	try:
		user = UserModel.objects.get(email=username)

		if user.check_password(password):
			auth_login(request, user)
			return redirect('home-index')
		else:
			messages.error(request, 'Invalid Password!')
			return redirect('home-login')

	except UserModel.DoesNotExist:
		messages.error(request, 'Invalid Email!')
		return redirect('home-login')

@login_required(login_url='home-login')
def logout_post(request):
    logout(request)
    return redirect('home-index')
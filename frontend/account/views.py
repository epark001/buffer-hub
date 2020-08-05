from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from admin.user.models import CustomUser
from admin.gen_ed.models import GenEd
from django.db import connection
from operator import itemgetter

import re
import json
# Create your views here.



@login_required(login_url='home-login')
def index(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/index.html', {'usr':usr})
@login_required(login_url='home-login')
def about_page(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/about.html', {'usr':usr})


@login_required(login_url='home-login')
def edit(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/edit.html', {'usr':usr})


@login_required(login_url='home-login')
def sqlsearch(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/sqlsearch.html', {'usr':usr})

@login_required(login_url='home-login')
def course_insert(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/course_insert.html', {'usr':usr})
@login_required(login_url='home-login')
def course_search(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/course-search.html', {'usr':usr})


def search_course(request):
	output = {}
	output['status'] = "Failure"
	output['data'] = None
	if request.method == 'POST':
		input = {}
		# print(request.POST)
		input['Subject'] = request.POST['subject']
		input['range_Sel'] = request.POST['one']
		input['GPA_GTE'] = request.POST['gpa_wanted']
		input['Sort_By'] = request.POST['order_by_selection']
		input['num_lower'] = request.POST['first_number']
		input['num_upper'] = request.POST['Single']
		
		#print(input['Sort_By'])
		
		#print(input['Order_By'])
		with connection.cursor() as cursor:
			if input['range_Sel'] == 'Single':
				cursor.execute('''
				SELECT Course_Comb, Average_Grade, Primary_Instructor, Number
				FROM GPA_TABLE
				Where Subject = %s and 
				number = %s and
				Average_Grade >= %s;
				''',[input['Subject'], input['num_lower'], input['GPA_GTE']])
			else:
				cursor.execute('''
				SELECT Course_Comb, Average_Grade, Primary_Instructor, Number
				FROM GPA_TABLE
				Where Subject = %s and 
				number >= %s and
				number <= %s and
				Average_Grade >= %s;
				''',[input['Subject'], input['num_lower'], input['num_upper'], input['GPA_GTE']])
			temp = cursor.fetchall()
			if temp:
				temp = list(temp)
				output['data'] = []
				for x in temp:
					result = {}
					result['course_comb'] = x[0]
					result['Average_Grade'] = x[1]
					result['Primary_Instructor'] = x[2]
					#print(result)
					output['data'].append(result)
					output['status'] = "Success"
				if input['Sort_By'] == 'AVG_GPA_DESC':
					output['data'] = sorted(output['data'], key=itemgetter('Average_Grade'),reverse=True)
				elif input['Sort_By'] == 'AVG_GPA_ASC':
					output['data'] = sorted(output['data'], key=itemgetter('Average_Grade'))
				elif input['Sort_By'] == 'NUMBER_DESC':
					output['data'] = sorted(output['data'], key=itemgetter('course_comb'),reverse=True)
				elif input['Sort_By'] == 'NUMBER_ASC':
					output['data'] = sorted(output['data'], key=itemgetter('course_comb'))
		
			else:
				output['status'] = "Failure: Course Not Found"
			#print(output['data'])
		return render(request, 'frontendTemplates/account/course-search-complete.html', {'data':output['data']})
	return JsonResponse(output)

@login_required(login_url='home-login')
def searchRequest(request):
	if request.method == 'POST':
		gen_ed = request.POST['gened'].upper()
		#data = GenEd.objects.raw('''SELECT * FROM Gen_ED Natural Join WHERE ''' + gen_ed + ''' <> "" ''')
		results = None
		with connection.cursor() as cursor:
			cursor.execute('''SELECT gen.Course, gen.Course_Title, avg(gpa.Average_Grade) as avg_grade FROM Gen_ED gen Inner Join GPA_TABLE gpa ON (gen.Course_Comb = gpa.Course_Comb) Where '''+gen_ed +'''<> "" Group By gen.Course_Comb Order By avg_grade DESC''')
			result = list(cursor.fetchall())
		output = []
		for row in result:
			temp = {}
			print(row)
			temp['course_comb'] = row[0]
			temp['course_title'] = row[1]
			temp['average_grade'] = round(row[2],2)
			output.append(temp)
		#print(output)
		return render(request, 'frontendTemplates/account/sqlsearchcomplete.html', {'data':output})
	return redirect('home-login')

@login_required(login_url='home-login')
def update(request):

	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		gender = request.POST['gender']
		mobile = request.POST['mobile']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?\s?]+$',gender):

			messages.error(request, 'Enter a valid Gender')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$',email):

			messages.error(request, 'Enter a valid Email')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[\d]{10,15}$',mobile):

			messages.error(request, 'Enter a valid Number')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		usr = CustomUser.objects.filter(pk=request.user.id)

		if not usr:
			messages.error(request, 'Log In First!')
			return redirect('home-login')
		else:
			usr = usr.get()

			usr.name = name
			usr.email = email
			usr.usr_gender = gender
			usr.usr_phone = mobile

			usr.save()

			messages.success(request, 'Profile Updated!')
			
			return redirect('account-index')

@login_required(login_url='home-login')
def edit_pass(request):
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()
	return render(request, 'frontendTemplates/account/edit-pass.html', {'usr':usr})


@login_required(login_url='home-login')
def update_pass(request):
	
	if request.method == 'POST':

		cpass = request.POST['cur-pass']
		npass = request.POST['new-pass']
		conpass = request.POST['con-pass']

		if (len(cpass) < 3) or (len(npass) < 3) or (len(conpass) < 3):
			messages.error(request, 'Password Length should be more than 3 characters!')
			return redirect('account-edit-pass')

		UserModel = get_user_model()

		try:
			user = UserModel.objects.get(pk=request.user.id)

			if user.check_password(cpass):

				if npass != conpass:
					messages.error(request, 'New Password does not match with Confirm Password!')
					return redirect('account-edit-pass')

				user.password = make_password(npass)
				user.save()

				auth_login(request, user)

				messages.success(request, 'Password Changed Successfully!')
				return redirect('account-index')

			else:
				messages.error(request, 'Current Password does not match!')
				return redirect('account-edit-pass')

		except UserModel.DoesNotExist:
			messages.error(request, 'Log In First!')
			return redirect('home-login')

@login_required(login_url='home-login')
def profile_pic(request):
	if request.is_ajax():
		if 'file' in request.FILES.keys():

			if not request.FILES['file'].name.split('.')[-1] in ['jpg','png','jpeg']:

				return HttpResponse(json.dumps({'key':'0', 'msg':'Invalid File Type!'}))

			usr = CustomUser.objects.filter(pk=request.user.id)

			if not usr:
				messages.error(request, 'Log In First!')
				return redirect('home-login')
			else:
				usr = usr.get()

			if "team.jpg" in str(usr.profile_pic):

				usr.profile_pic = request.FILES['file']

				usr.save()

			else:
				usr.profile_pic.delete()

				usr.profile_pic = request.FILES['file']

				usr.save()


			return HttpResponse(json.dumps({'key':'1', 'msg':'Success!'}))
			
		else:
			return HttpResponse(json.dumps({'key':'0', 'msg':'No File Selected!'}))


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
from django.http import JsonResponse
import uuid


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

def grad_req_calc(request):
	output = {}
	output['status'] = "Failure"
	output['data'] = None
	input = {}
	input['email_Id'] = request.user.get_username()
	with connection.cursor() as cursor:
		cursor.execute("Select * From Grad_Reqs Where email_Id = %s",[input['email_Id']])
		temp = cursor.fetchall()
		if temp:
			temp = list(temp)
			output['data'] = []
			for x in temp:
				result = {}
				result['Subject'] = x[2]
				result['Course_Type'] = x[3]
				result['Hours_Needed'] = x[4]
				result['Range_Sel'] = x[5]
				result['Lower_Num'] = x[6]
				result['Upper_Num'] = x[7]
				output['data'].append(result)
			#print(output['data'])
			output['result'] = []
			for req in output['data']:
				# if req['Subject'] != "major" or req['Subject'] != "other":
				#query for gened until hours fufiled
				print(type(req['Subject']))
				print(req['Subject'])
				# if req['Range_Sel'] == "Single":
				# 	#single class search
				cursor.execute("SELECT gen.Course_Comb, avg(gpa.Average_Grade) as avg_grade, gpa.Primary_Instructor From Gen_ED gen Inner Join GPA_TABLE gpa ON (gen.Course_Comb = gpa.Course_Comb) Where gen."+req['Subject']+" <> \"\" and gpa.Number = "+req['Lower_Num']+" Group By gen.Course_Comb Order By avg_grade DESC")
				# 	else:
				# 		#do range search
				# 		cursor.execute('''
				# 		SELECT gen.Course_Comb, avg(gpa.Average_Grade) as avg_grade, gpa.Primary_Instructor
				# 		From Gen_ED gen Inner Join GPA_TABLE gpa ON (gen.Course_Comb = gpa.Course_Comb)
				# 		Where gen.%s <> "" and gpa.Number >= %s and gpa.Number <= %s
				# 		Group By gen.Course_Comb 
				# 		Order By avg_grade DESC
				# 		''',[req['Subject'],req['Lower_Num'], req['Upper_Num']])
				# else:
				# 	#find courses within subject and range specified
				# 	if req['Range_Sel'] == "Single":
				# 		#single class search
				# 		cursor.execute('''
				# 		SELECT gpa.Course_Comb, avg(gpa.Average_Grade) as avg_grade, gpa.Primary_Instructor
				# 		From GPA_TABLE gpa
				# 		Where gen.%s <> "" and gpa.Number = %s
				# 		Group By gen.Course_Comb 
				# 		Order By avg_grade DESC
				# 		''',[req['Subject'],req['Lower_Num']])
				# 	else:
				# 		#do range search
				# 		cursor.execute('''
				# 		SELECT gpa.Course_Comb, avg(gpa.Average_Grade) as avg_grade, gpa.Primary_Instructor
				# 		From GPA_TABLE gpa
				# 		Where gen.%s <> "" and gpa.Number >= %s and gpa.Numver <= %s
				# 		Group By gen.Course_Comb 
				# 		Order By avg_grade DESC
				# 		''',[req['Subject'],req['Lower_Num'], req['Upper_Num']])
				temp = None
				temp = cursor.fetchone()
				if fetch:
					temp1 = {}
					temp1['Course_Comb'] = temp[0]
					temp1['Average_Grade'] = temp[1]
					temp1['Primary_Instructor'] = temp[2]
					output['result'].append(temp1)
			output['status'] = "Success"
		else:
			output['status'] = "Failure: Email not found"
	return render(request, 'frontendTemplates/account/grad-req-calc.html', {'data':output['data']})

def grad_req_show(request):
	output = {}
	output['status'] = "Failure"
	output['data'] = None
	input = {}
	input['email_Id'] = request.user.get_username()
	
	
	with connection.cursor() as cursor:
		cursor.execute("Select * From Grad_Reqs Where email_Id = %s",[input['email_Id']])
		temp = cursor.fetchall()
		if temp:
			temp = list(temp)
			output['data'] = []
			for x in temp:
				result = {}
				result['Subject'] = x[2]
				result['Course_Type'] = x[3]
				result['Hours_Needed'] = x[4]
				result['Range_Sel'] = x[5]
				result['Lower_Num'] = x[6]
				result['Upper_Num'] = x[7]
				output['data'].append(result)
			#print(output['data'])
			output['status'] = "Success"
		else:
			output['status'] = "Failure: Email not found"
	return render(request, 'frontendTemplates/account/grad-req-complete.html', {'data':output['data']})

def grad_req_insert(request):
	output = {}
	output['status'] = "Failure"
	output['data'] = None
	if request.method == 'POST':
		input = {}
		#print(request.POST)
		input['_id'] = str(uuid.uuid1())
		input['email_Id'] = request.user.get_username()
		input['Subject'] = request.POST['subject']
		input['type'] = request.POST['type']
		input['Hours_Needed'] =  request.POST['hours_needed']
		input['Range_Sel'] = request.POST['one']
		input['Lower_Num'] = request.POST['first_number']
		input['Upper_Num'] = request.POST['Single']
		#print(input)
		
		result = {}
		with connection.cursor() as cursor:
			cursor.execute('''
			Insert Into Grad_Reqs(_id, email_Id, Subject, Course_Type, Hours_Needed, Range_Sel, Lower_Num, Upper_Num)
			Values (%s, %s, %s, %s, %s, %s, %s, %s)
			''',[input['_id'],input['email_Id'], input['Subject'], input['type'], input['Hours_Needed'], input['Range_Sel'], input['Lower_Num'], input['Upper_Num']])
			temp = cursor.fetchone()
			#temp = list(temp)
			#print(temp)
			#output['data'] = temp
			output['status'] = "Success"
		return redirect('/account/grad-req-show')
	return JsonResponse(output)

@login_required(login_url='home-login')
def edit(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/edit.html', {'usr':usr})

def prof_modal(request):
	output = {}
	output['status'] = "Failure"
	output['data'] = None
	if request.method == 'POST':
		input = {}
		input['email_Id'] = request.user.get_username()
		input['name'] = request.POST['name']
		splitname = input['name'].split(", ")
		result = {}
		result['dept'] = None
		result['firstname'] = splitname[1]
		result['lastname'] = splitname[0]
		result['numratings'] = None
		result['rating'] = None
		result['overallrating'] = None
		output['data'] = result
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM uiucprofs WHERE tFname =%s OR tLname=%s", (splitname[1], splitname[0]))
			temp = cursor.fetchone()
			if temp:
				temp = list(temp)
				result['dept'] = temp[0]
				result['firstname'] = temp[3]
				result['lastname'] = temp[5]
				result['numratings'] = temp[7]
				result['rating'] = temp[8]
				result['overallrating'] = temp[11]
				output['data'] = result
				output['status'] = "Success"
			else:
				output['status'] = "Failure: Teacher Not Found"
	return JsonResponse(output)


@login_required(login_url='home-login')
def sqlsearch(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/sqlsearch.html', {'usr':usr})

def profsearch(request):
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()


	return render(request, 'frontendTemplates/account/profsearch.html')

def course_insert(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()
	return render(request, 'frontendTemplates/account/course_insert.html', {'usr':usr})


@login_required(login_url='home-login')
def sqlsearchProf(request):
	if request.method == 'POST':
		fname = request.POST['firstname']
		lname = request.POST['lastname']
		#data = GenEd.objects.raw('''SELECT * FROM uiucprofs WHERE tFname EQUALS''' + firstname + ''' + ''' OR ''' + ''' + tLname EQUALS ''' + lastname + ''' + ''' )
		results = None
		with connection.cursor() as cursor:
			cursor.execute("SELECT * FROM uiucprofs WHERE tFname =%s OR tLname=%s", (fname, lname))
			result = list(cursor.fetchall())
		output = []
		for row in result:
			temp = {}
			print(row)
			temp['dept'] = row[0]
			temp['firstname'] = row[3]
			temp['lastname'] = row[5]
			temp['numratings'] = row[7]
			temp['rating'] = row[8]
			temp['overallrating'] = row[11]
			  	
			output.append(temp)
		#print(output)
		return render(request, 'frontendTemplates/account/profsqlsearchcomplete.html', {'data':output})
	return redirect('home-login')

@login_required(login_url='home-login')
def course_search(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/course-search.html', {'usr':usr})
@login_required(login_url='home-login')
def grad_reqs(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/graduation-requirements.html', {'usr':usr})

def grad_course(request):
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


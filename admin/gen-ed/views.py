from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.gen-ed.models import gen-ed
import re
# Create your views here.

@login_required(login_url='login')
def add(request):
	return render(request, 'adminTemplates/gen-ed/add.html')

@login_required(login_url='login')
def save(request):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid gen-ed Name')
			return redirect('gen-ed-add')

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid gen-ed Description')
			return redirect('gen-ed-add')


		genr = gen-ed(gen-ed_name=name, gen-ed_des=desc)

		genr.save()

		messages.success(request, 'gen-ed Added Successfully!')

		return redirect('gen-ed-index')

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = GenEd.objects.all()

		return render(request, 'adminTemplates/gen-ed/index.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):

	if request.method == 'GET':

		genr = GenEd.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('gen-ed-index')
		else:
			genr = genr.delete()
			messages.success(request, 'Record Deleted!')

		return redirect('gen-ed-index')


@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		genr = GenEd.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('gen-ed-index')
		else:
			genr = genr.get()

			return render(request, 'adminTemplates/gen-ed/edit.html', {'genr':genr})



@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid gen-ed Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid gen-ed Description')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		genr = gen-ed.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('gen-ed-index')
		else:
			genr = genr.get()

			genr.gen-ed_name = name
			genr.gen-ed_des = desc

			genr.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('gen-ed-index')











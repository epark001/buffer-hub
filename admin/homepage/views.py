from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from admin.homepage.models import Homepage
import re
# Create your views here.

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Homepage.objects.all()

		return render(request, 'adminTemplates/homepage/index.html', {'data':data})



@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		homepage = Homepage.objects.filter(pk=id)

		if not homepage:
			messages.error(request, 'No such records found!')
			return redirect('homepage-index')
		else:
			homepage = homepage.get()
			return None; #render(request, 'adminTemplates/homepage/edit.html', {'homepage':homepage})


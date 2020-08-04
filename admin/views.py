from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.gpa_table.models import Gpa_table
import re
# Create your views here.

@login_required(login_url='login')
def add(request):
	return render(request, 'adminTemplates/gpa_table/add.html')
# Create your views here.

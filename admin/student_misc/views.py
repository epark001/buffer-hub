from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.student_misc.models import StudentMisc
import re
import uuid
# Create your views here.
@login_required(login_url='login')
def add(request):
    return render(request, 'adminTemplates/student_misc/add.html')


@login_required(login_url='login')
def save(request):

    if request.method == 'POST':

        email_val = request.user
        major_taken_val = request.POST['major_taken']
        major_percentile_val = request.POST['major_percentile']
        gened_percentile_val = request.POST['gened_percentile']
        current_gpa_val = request.POST['current_gpa']
        hours_completed_val = request.POST['hours_completed']
        target_gpa_val = request.POST['target_gpa']


        student_misc_val = StudentMisc(email=email_val, major_taken=major_taken_val, major_percentile=major_percentile_val,  gened_percentile=gened_percentile_val,current_gpa=current_gpa_val, hours_completed=hours_completed_val,target_gpa=target_gpa_val)

        student_misc_val.save()

        messages.success(request, 'Gen_Ed values Added Successfully!')

        return redirect('gen_ed-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = StudentMisc.objects.all()

        return render(request, 'adminTemplates/student_misc/index.html', {'data':data})

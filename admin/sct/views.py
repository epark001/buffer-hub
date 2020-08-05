from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.sct.models import StudentCourseTable
import re
import uuid
# Create your views here.
@login_required(login_url='login')
def add(request):
    return render(request, 'adminTemplates/gen_ed/add.html')


@login_required(login_url='login')
def save(request):

    if request.method == 'POST':
        email_val = request.user
        field_id_val = str(uuid.uuid1())
        course_comb_val = request.POST['course_comb']
        letter_grade_val = request.POST['letter_grade']
        gpa_hours_val = request.POST['gpa_hours']
        gpa_quality_points_val=request.POST['gpa_quality_points']


        gen_ed_val = StudentCourseTable(email=email_val,field_id=field_id_val, course_comb=course_comb_val,letter_grade=letter_grade_val,gpa_hours=gpa_hours_val,gpa_quality_points=gpa_quality_points_val)

        gen_ed_val.save()

        messages.success(request, 'Grade values Added Successfully!')

        return redirect('sct-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = StudentCourseTable.objects.get(email="test@gmail.com")
        return render(request, 'adminTemplates/sct/index.html', {'data':data})

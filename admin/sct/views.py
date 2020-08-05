from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.sct.models import StudentCourseTable
from admin.user.models import CustomUser

import re
import uuid

dict_grade = {
    "A+" : "4.0",
    "A" : "4.0",
    "A-" : "3.67",
    "B+" : "3.33",
    "B" : "3.0",
    "B-" : "2.67",
    "C+" : "2.33",
    "C" : "2.00",
    "C-" : "1.67",
    "D+" : "1.33",
    "D" : "1.00",
    "D-" : "0.67",
    "F" : "0"
}
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
        primary_instructor_val=request.POST['primary_instructor']


        gen_ed_val = StudentCourseTable(email=email_val,field_id=field_id_val, course_comb=course_comb_val,letter_grade=letter_grade_val,gpa_hours=gpa_hours_val,gpa_quality_points=gpa_quality_points_val, primary_instructor=primary_instructor_val)

        gen_ed_val.save()

        messages.success(request, 'Grade values Added Successfully!')

        return redirect('sct-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = StudentCourseTable.objects.get(email="test@gmail.com")
        return render(request, 'adminTemplates/sct/index.html', {'data':data})
@login_required(login_url='login')
def index_user(request):
    
    if request.method == 'GET':
        
        data = StudentCourseTable.objects.filter(email_id=request.user.username)
        print (data)
        return render(request, 'frontendTemplates/sct/index.html', {'data':data})
@login_required(login_url='login')
def save_user(request):

    if request.method == 'POST':
        email_val = request.user.username
        field_id_val = str(uuid.uuid1())
        course_comb_val = request.POST['class_selection']
        letter_grade_val = request.POST['letter_grade']
        gpa_hours_val = request.POST['gpa_hours']
        gpa_quality_points_val = int(gpa_hours_val) * dict_grade[letter_grade_val]
        primary_instructor_val = request.POST['primary_instructor']

        sct = StudentCourseTable(email_id=email_val, field_id=field_id_val,course_comb=course_comb_val, letter_grade=letter_grade_val, gpa_hours =gpa_hours_val, gpa_quality_points=gpa_quality_points_val,primary_instructor=primary_instructor_val)

        sct.save()

        messages.success(request, 'Courses Added Successfully!')

        return redirect('sct-index-user')
@login_required(login_url='login')
def delete(request, id):

    if request.method == 'GET':
        print(id)
        sct = StudentCourseTable.objects.get(field_id=id)
        print(sct)
        if not sct:
            messages.error(request, 'No such records found!')
            return redirect('sct-index-user')
        else:
            sct = sct.delete()
            messages.success(request, 'Record Deleted!')

        return redirect('sct-index-user')
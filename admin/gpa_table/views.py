from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.gpa_table.models import GpaTable
import re
import uuid
# Create your views here.

@login_required(login_url='login')
def add(request):
    return render(request, 'adminTemplates/gpa_table/add.html')


@login_required(login_url='login')
def save(request):

    if request.method == 'POST':
        print ('here')
        field_id_val = str(uuid.uuid1())
        course_comb_val = 'course_comb' in request.POST
        subject_val = 'subject' in request.POST
        number_val = 'number' in request.POST
        course_title_val = 'course_title' in request.POST

        a_plus_val = 'a_plus' in request.POST
        a_standard_val = 'a_standard' in request.POST
        a_minus_val = 'a_minus' in request.POST
        b_plus_val = 'b_plus' in request.POST
        b_standard_val = 'b_standard' in request.POST
        b_minus_val = 'b_minus' in request.POST
        c_plus_val = 'c_plus' in request.POST
        c_standard_val = 'c_standard' in request.POST
        c_minus_val = 'c_minus' in request.POST
        d_plus_val = 'd_plus' in request.POST
        d_standard_val = 'd_standard' in request.POST
        d_minus_val = 'd_minus' in request.POST
        f_val = 'f' in request.POST
        average_grade_val = 'average_grade' in request.POST
        primary_instructor_val = 'primary_instructor' in request.POST


        gpa_table_val = GpaTable(field_id=field_id_val, course_comb =course_comb_val,subject =subject_val, number = number_val, course_title =course_title_val, a_plus = a_plus_val, a_standard=a_standard_val,a_minus=a_minus_val,b_plus=b_plus_val, b_standard = b_standard_val, b_minus=b_minus_val, c_plus= c_plus_val,c_standard=c_standard_val,c_minus=c_minus_val,d_plus=d_plus_val,d_standard=d_standard_val, d_minus=d_minus_val, f=f_val, average_grade=average_grade_val, primary_instructor = primary_instructor_val)

        gpa_table_val.save()

        messages.success(request, 'Gpa values Added Successfully!')

        return redirect('gpa_table-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = GpaTable.objects.all()

        return render(request, 'adminTemplates/gpa_table/index.html', {'data':data})

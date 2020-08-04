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

        field_id_val = str(uuid.uuid1())
        course_comb_val = request.POST['course_comb']
        subject_val = request.POST['subject']
        number_val =  request.POST['number']
        course_title_val =  request.POST['course_title']

        a_plus_val = request.POST['a_plus']
        a_standard_val =  request.POST['a_standard']
        a_minus_val =  request.POST['a_minus']
        b_plus_val =  request.POST['b_plus']
        b_standard_val =  request.POST['b_standard']
        b_minus_val =  request.POST['b_minus']
        c_plus_val =  request.POST['c_plus']
        c_standard_val =  request.POST['c_standard']
        c_minus_val =  request.POST['c_minus']
        d_plus_val =  request.POST['d_plus']
        d_standard_val =  request.POST['d_standard']
        d_minus_val =  request.POST['d_minus']
        f_val =  request.POST['f']
        average_grade_val =  request.POST['average_grade']
        primary_instructor_val =  request.POST['primary_instructor']

        gpa_table_val = GpaTable(field_id=field_id_val, course_comb =course_comb_val,subject =subject_val, number = number_val, course_title =course_title_val, a_plus = a_plus_val, a_standard=a_standard_val,a_minus=a_minus_val,b_plus=b_plus_val, b_standard = b_standard_val, b_minus=b_minus_val, c_plus= c_plus_val,c_standard=c_standard_val,c_minus=c_minus_val,d_plus=d_plus_val,d_standard=d_standard_val, d_minus=d_minus_val, f=f_val, average_grade=average_grade_val, primary_instructor = primary_instructor_val)

        gpa_table_val.save()

        messages.success(request, 'Gpa values Added Successfully!')

        return redirect('gpa_table-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = GpaTable.objects.all()

        return render(request, 'adminTemplates/gpa_table/index.html', {'data':data})

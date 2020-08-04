from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.gen_ed.models import GenEd
import re
import uuid
# Create your views here.

@login_required(login_url='login')
def add(request):
    return render(request, 'adminTemplates/gen_ed/add.html')


@login_required(login_url='login')
def save(request):

    if request.method == 'POST':

        field_id_val = str(uuid.uuid1())
        course_comb_val = request.POST['course_comb']
        course_val =  request.POST['course']
        course_title_val =  request.POST['course_title']
        acp_val =  request.POST['acp']
        cs_val =  request.POST['cs']
        hum_val =  request.POST['hum']
        nat_val =  request.POST['nat']
        qr_val =  request.POST['qr']
        sbs_val =  request.POST['sbs']


        gen_ed_val = GenEd(field_id=field_id_val, course_comb =course_comb_val, course=course_val, course_title = course_title_val,acp=acp_val,cs=cs_val,hum=hum_val,nat=nat_val,qr=qr_val,sbs=sbs_val)

        gen_ed_val.save()

        messages.success(request, 'Gen_Ed values Added Successfully!')

        return redirect('gen_ed-index')
@login_required(login_url='login')
def index(request):
    
    if request.method == 'GET':
        
        data = GenEd.objects.all()

        return render(request, 'adminTemplates/gen_ed/index.html', {'data':data})

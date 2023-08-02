from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def loginmain(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def studentreg(request):
    registrations = Registration.objects.values('fname').distinct()

    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        pword=request.POST.get("pword")
        sem=request.POST.get("sem")

        data = Registration.objects.create(fname=fname, lname=lname, email=email, phno=phno, uname=uname, pword=pword,sem=sem)
        data.save()

    return render(request, 'studentreg.html', {'registrations': registrations})
    
def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        
        try:
            user = Registration.objects.get(uname=uname, pword=pword)
            print(user.id)
            print(user.fname,'fname')
        except Registration.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'student.html')
            # User authenticated successfully
        context = {
            'fname': user.fname,
            'lname': user.lname,
            'email': user.email,
            'phno': user.phno,
            'uname': user.uname,
            'sem':user.sem,
        }
        return render(request, 'studentprof.html', context)
    
    return render(request, 'student.html')

def studentprof(request):
    return render(request,'studentprof.html')

def staffprof(request):
    return render(request,'staffprof.html')
#logout
def logout(request):
    return render(request,'home.html',{})


def staffavail(request):
    users = StaffRegistration.objects.all() 
    id = request.session.get('id')
    # Retrieve all users from the StaffRegistration table
    if request.method == 'POST':
        # username = request.user.username  # Get the username of the logged-in user
        print(id,"iddd")
        # print(username,'username')
        
        if 'first' in request.POST:
            subject_first=int(request.POST.get('first', ''))
            if subject_first==1:
                subject_first=id
            else:
                subject_first=0    
        else:
            subject_first=0    
        if 'second' in request.POST:
           subject_second = int(request.POST.get('second', ''))
           if subject_second==1:
               subject_second=id
           else:
               subject_second=0
        else:
            subject_second=0        
        if 'third' in request.POST:
            subject_third=int(request.POST.get('third', ''))
            if subject_third==1:
                subject_third=id
            else:
                subject_third=0    
        else:
            subject_third=0        
        if 'fourth' in request.POST:
            subject_fourth=int(request.POST.get('fourth', ''))
            if subject_fourth==1:
                subject_fourth=id
            else:
                subject_fourth=0    
        else:
            subject_fourth=0    
        subcode = ''
        fname = ''
        today=date.today()
        print(subject_first,subject_second,subject_third,subject_fourth)
        # Retrieve the subcode and fname for the logged-in user from the StaffRegistration table
        try:
            # print(username)
            staff_registration = StaffRegistration.objects.get(id=id)
            print(staff_registration.id)
            subcode = staff_registration.subcode
            fname = staff_registration.fname
        except StaffRegistration.DoesNotExist:
            pass
        try:
            timetable = TimeTable.objects.get(date=today)
            if timetable.first_hour==0:
                timetable.first_hour = subject_first
            elif timetable.first_hour==id:
                timetable.first_hour=subject_first
            elif subject_first==0:
                pass    
            else:
                messages.success(request,("First hour is already taken"))
            if timetable.second_hour==0:     
                timetable.second_hour = subject_second
            elif timetable.second_hour==id:
                timetable.second_hour=subject_second
            elif subject_second==0:
                pass    
            else:
                messages.success(request,("First hour is already taken"))
                
            if timetable.third_hour==0:    
               timetable.third_hour = subject_third
            elif timetable.third_hour==id:
                timetable.third_hour=subject_third
            elif subject_third==0:
                pass    
            else:
                messages.success(request,("First hour is already taken"))
                
            if timetable.fourth_hour==0:   
               timetable.fourth_hour = subject_fourth
            elif timetable.fourth_hour==id:
                timetable.fourth_hour=subject_fourth
            elif subject_fourth==0:
                pass    
            else:
                messages.success(request,("First hour is already taken"))
                
            timetable.save()
            messages.success(request,("Updated Successfully."))
        except TimeTable.DoesNotExist:
            timetable, created = TimeTable.objects.get_or_create(
                date=today,
                defaults={
                    'first_hour': subject_first,
                    'second_hour': subject_second,
                    'third_hour': subject_third,
                    'fourth_hour': subject_fourth,
                }
            )
            return HttpResponse("Created succsfully")

            


    context = {
        'users': users,
        'id':id,
        'timetable':timetable,
    }

    return render(request, 'staffavail.html', context)


def staffavailin(request):
        id = request.session.get('id')
        try:
            today=date.today()
            timetable = TimeTable.objects.get(date=today)
            return render(request,'staffavail.html',{'id':id,'timetable':timetable})
            
        except:
            
            return render(request,'staffavail.html',{'id':id})







def studentnewtt(request):
    return render(request,'studentnewtt.html')

def studenttopic(request):
    return render(request,'studenttopic.html')

def studentassign(request):
    assignments = Assignments.objects.all()
    return render(request, 'studentassign.html', {'assignments': assignments})

def studentabs(request):
    return render(request,'studentabs.html')


def staffnewtt(request):
    return render(request,'staffnewtt.html')

def stafftopic(request):
    return render(request,'stafftopic.html')

def staffassign(request):
    if request.method == 'POST':
        assignments = request.POST.get('assignments')
        print(assignments)
        Assignments.objects.create(assignments=assignments)
        return redirect('/staffassign')
    return render(request,'staffassign.html')

def sample(request):
    if request.method == 'POST':
        selected_persons = request.POST.getlist('persons')
        print(selected_persons)
        for person_name in selected_persons:
            Assignments.objects.create(absentees=person_name)

        # Redirect to success page after submission
        return redirect('/sample')
    return render(request, 'sample.html')
   

def adminlogin(request):
    return render(request,'admin.html')


def stafflogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        
        try:
            user = StaffRegistration.objects.get(uname=uname, pword=pword)
            print(user.id)
            request.session['id'] = user.id
            id = request.session.get('id')
            print(id)
        except StaffRegistration.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'staff.html')
        
        # User authenticated successfully
        context = {
            'fname': user.fname,
            'lname': user.lname,
            'email': user.email,
            'phno': user.phno,
            'uname': user.uname,
            'dep':user.dep,
            'id':user.id,
            
        }
        return render(request, 'staffprof.html', context)
    
    return render(request, 'staff.html')


def staffreg(request):
    registrations = StaffRegistration.objects.values('fname').distinct()

    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        phno=request.POST.get("phno")
        uname=request.POST.get("uname")
        pword=request.POST.get("pword")
        dept=request.POST.get("dept")

        data = Registration.objects.create(fname=fname, lname=lname, email=email, phno=phno, uname=uname, pword=pword,dept=dept)
        data.save()

    return render(request, 'staffreg.html', {'registrations': registrations})







    

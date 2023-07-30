from django.shortcuts import render,HttpResponse,HttpResponsePermanentRedirect,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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



def staffavail(request):
    users = StaffRegistration.objects.all()  # Retrieve all users from the StaffRegistration table

    if request.method == 'POST':
        username = request.user.username  # Get the username of the logged-in user
        subject_first = request.POST.get('first', '')
        subject_second = request.POST.get('second', '')
        subject_third = request.POST.get('third', '')
        subject_fourth = request.POST.get('fourth', '')
        subcode = ''
        fname = ''

        # Retrieve the subcode and fname for the logged-in user from the StaffRegistration table
        try:
            staff_registration = StaffRegistration.objects.get(uname=username)
            subcode = staff_registration.subcode
            fname = staff_registration.fname
        except StaffRegistration.DoesNotExist:
            pass

        # Check if any of the selected hours are already occupied by another user
        if (
            TimeTable.objects.filter(first_hour=subject_first).exists() or
            TimeTable.objects.filter(second_hour=subject_second).exists() or
            TimeTable.objects.filter(third_hour=subject_third).exists() or
            TimeTable.objects.filter(fourth_hour=subject_fourth).exists()
        ):
            return HttpResponse('One or more of the selected hours are already occupied.')

        # Create a new TimeTable object with the user, subject hours, subcode, and fname
        timetable = TimeTable.objects.create(
            user=request.user,
            first_hour=subject_first,
            second_hour=subject_second,
            third_hour=subject_third,
            fourth_hour=subject_fourth,
            subcode=subcode,
            fname=fname
        )

        return HttpResponse('Availability submitted successfully!')

    context = {
        'users': users
    }

    return render(request, 'staffavail.html', context)










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







    

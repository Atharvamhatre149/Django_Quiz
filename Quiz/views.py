from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from multiprocessing import context
from Quiz.models import Score

# Create your views here.
def home(request):

    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/Quizselect")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')

    return render(request,'login.html')



def signup(request):
    if request.method=="POST":
        username=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirmpswd=request.POST['confirmPassword']
        if User.objects.filter(username=username).exists():
            messages.warning(request,"user already exist")
            return redirect("signin")
        if(confirmpswd!=password):
            messages.warning(request,"password mismatch")
            return redirect("signup")
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        messages.success(request,"Your Account has been successfully created.")
        return redirect('signin')
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('home')

def python(request):
    if request.user.is_authenticated:
        current_use = request.user.username
        print(current_use)
        context = {"current_u": current_use}
        return render(request, 'python.html', context)

    return render(request,'python.html')

def Quizselect(request):
    print("hello")
    if request.user.is_authenticated:
        current_use = request.user.username
        print(current_use)
        context = {"current_u": current_use}
        return render(request, 'Quizselect.html', context)

    return render(request,'Quizselect.html')

def aoa(request):
    if request.user.is_authenticated:
        current_use = request.user.username
        print(current_use)
        context = {"current_u": current_use}
        return render(request, 'aoa.html', context)
    return render(request,'aoa.html')

def dbms(request):
    if request.user.is_authenticated:
        current_use = request.user.username
        print(current_use)
        context = {"current_u": current_use}
        return render(request, 'dbms.html', context)
    return render(request,'dbms.html')

def os(request):
    if request.user.is_authenticated:
        current_use = request.user.username
        print(current_use)
        context = {"current_u": current_use}
        return render(request, 'os.html', context)
    return render(request,'os.html')
def score(request):
    if request.method=="POST":
        username=request.user.username

        score=int(request.POST['score'])

        subjectName=request.POST['subjectname']
        myscore=Score(username=username,score=score,subjectName=subjectName)
        myscore.save()
        if(subjectName=="PYTHON"):
            return redirect('python')
        elif subjectName=="OPERATING SYSTEM":
            return redirect('os')
        elif subjectName=="DBMS":
            return redirect('dbms')
        elif subjectName=="AOA":
            return redirect('aoa')

def showScore(request):
    user_name = request.user.username
    context={
        "all_score" : Score.objects.filter(username=user_name),
    }
    return render(request,"showScore.html",context=context)

# def login(request):
#     m = Member.objects.get(username=request.POST['username'])
#     if m.check_password(request.POST['password']):
#         request.session['member_id'] = m.id
#         return HttpResponse("You're logged in.")
#     else:
#         return HttpResponse("Your username and password didn't match.")
#
# def logout(request):
#     try:
#         del request.session['member_id']
#     except KeyError:
#         pass
#     return HttpResponse("You're logged out.")
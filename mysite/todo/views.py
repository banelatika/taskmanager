from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, LoginForm, TaskForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import Group
from .models import profile, TaskUser
from django.contrib.auth.decorators import login_required


# signup
def sign_in(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            user = fm.save()
            name = email.split('@')[-1]
            domain = name.split('.')[0]
            gruop = Group.objects.filter()
            if domain not in gruop:
                group, created = Group.objects.get_or_create(name=domain)
                Profile = profile.objects.create(user=user, gruop=group)
                if created:
                    Profile.is_admin = True
                    # if is_active is False, user can not login without admin approval
                    Profile.is_active = True
                    Profile.save()

            else:
                group = Group.objects.get(name=domain)
                user.groups.add(group)
                Profile = profile.objects.create(user=user, gruop=group)
                Profile.is_admin = False
                # if is_active is False, user can not login without admin approval
                Profile.is_active = False
                Profile.save()
            return HttpResponseRedirect('/logied/')
    else:
        fm = RegistrationForm()
    return render(request, 'todo/signup.html', {'fm': fm, })


def profile_userlog(request):
    return render(request, 'todo/logined.html', {'name': request.user.username})


# login form
def login_form(request):
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.profile.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
                else:
                    return HttpResponse("Hi, Your Login Request is pending for Approval")
    else:
        fm = AuthenticationForm()
        return render(request, 'todo/loginform.html', {'fm': fm})


def profile_user(request):
    if request.user.is_authenticated:
        if request.user.profile.is_active and request.user.profile.is_admin:
            unactiveuser = profile.objects.filter(is_active=False)
            print(unactiveuser)
            return render(request, 'todo/profile.html', {'name': request.user, 'unactiveuser': unactiveuser})
        else:
            if request.user.profile.is_active:
                return render(request, 'todo/profile.html', {'name': request.user,})
    else:
        return HttpResponseRedirect('/logied/')


def request_accepts(request, my_user):
    accept = profile.objects.get(pk=my_user)
    accept.is_active = True
    accept.save()
    return HttpResponseRedirect('/profile/')


def Task_User(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            tasksall = TaskForm( request.POST)
            if tasksall.is_valid():
                tasksall = tasksall.save(commit=False)
                tasksall.assignor=request.user
                tasksall.save()
                tasksall = TaskForm()
                return HttpResponseRedirect('/profile/')
                
        else:
            tasksall = TaskForm()
            return render(request, 'todo/taskform.html', {'tasksall' :tasksall})
    else:
        return HttpResponseRedirect('/logied/')
    


def task_board(request):
     if request.user.is_authenticated:
        if request.user.profile.is_active and request.user.profile.is_admin:
            tasklist = TaskUser.objects.all()
            return render(request, 'todo/tasksboard.html', {'tasklist' :tasklist})
        else:
            if request.user.profile.is_active:
                tasklist = TaskUser.objects.filter(assignee = request.user)
                print(tasklist)
            return render(request, 'todo/tasksboard.html', {'tasklist' :tasklist})
        

def task_edit(request, id):
    if request.user.is_authenticated:
        if request.user.profile.is_active and request.user.profile.is_admin:
            if request.method == 'POST':
                pi = TaskUser.objects.get(pk=id)
                forms =TaskForm(request.POST,instance=pi) 
                if forms.is_valid():
                    forms.save()
                    return HttpResponseRedirect('/profile/')
            else:
                pi = TaskUser.objects.get(pk=id)
                print(pi)
                print('kya hai ye')
                forms =TaskForm(instance=pi) 
                print(forms)
            return render(request, 'todo/updatetask.html', {'forms' :forms})

    else:
        return HttpResponseRedirect('/login/')

def delete_date(request, id):
    if request.method == "POST":
        # perticula one data they get on data base
        pi = TaskUser.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/tasksboard/')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def task_completed(request, id):
    task = TaskUser.objects.get(id=id, assignee=request.user)
    task.checkbox = True
    task.save()
    return HttpResponseRedirect('/tasksboard/')
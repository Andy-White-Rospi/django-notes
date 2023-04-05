from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Task,Vacation_rescheduling, Commission, Register_assistence, \
    Official_permit_for_hours, Personal_leave_with_pay, Vacation_account_request, Data_user

from .forms import TaskForm, CommissionForm,Register_assistenceForm, Vacation_reschedulingForm,\
            Official_permit_for_hoursForm, Personal_leave_with_payForm, Vacation_account_requestForm,\
            Data_userForm

# Create your views here.


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                form = Data_userForm(request.POST)
                new_task = form.save(commit=False)
                new_task.user = request.user
                new_task.save()
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def tasks(request):
    tasks = Vacation_rescheduling.objects.filter(user=request.user)
    tasks1 = Vacation_account_request.objects.filter(user=request.user)
    tasks2 = Register_assistence.objects.filter(user=request.user)
    tasks3 = Personal_leave_with_pay.objects.filter(user=request.user)
    tasks4 = Official_permit_for_hours.objects.filter(user=request.user)
    return render(request, 'tasks.html', {"tasks": tasks,"tasks1": tasks1,"tasks2": tasks2,"tasks3": tasks3,"tasks4": tasks4})

@login_required
def commission(request):
    if request.method == "GET":
        return render(request,'commission.html',{"form": CommissionForm})
    else:
        try:
            form = CommissionForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'commission.html',
                          {"form": TaskForm, "error": "Error creating task." + new_task + "Hola"})


@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'tasks.html', {"tasks": tasks})


@login_required
def registro_de_asistencia(request):
    if request.method == "GET":
        return render(request, 'register_of_assistence.html', {"form": Register_assistenceForm})
    else:
        try:
            form = Register_assistenceForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'register_of_assistence.html', {"form": Register_assistenceForm, "error": "Error creating task."+ new_task+"Hola"})

@login_required
def vacation_rescheduling(request):
    if request.method == "GET":
        return render(request, 'vacation_rescheduling.html', {"form": Vacation_reschedulingForm})
    else:
        try:
            form = Vacation_reschedulingForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'vacation_rescheduling.html', {"form": Vacation_reschedulingForm, "error": "Error creating task."+ new_task+"Hola"})

@login_required
def official_permit_for_hours(request):
    if request.method == "GET":
        return render(request, 'official_permit_for_hours.html', {"form": Official_permit_for_hoursForm})
    else:
        try:
            form = Official_permit_for_hoursForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'official_permit_for_hours.html', {"form": Official_permit_for_hoursForm, "error": "Error creating task."+ new_task+"Hola"})

@login_required
def personal_leave_with_pay(request):
    if request.method == "GET":
        return render(request, 'personal_leave_with_pay.html', {"form": Personal_leave_with_payForm})
    else:
        try:
            form = Personal_leave_with_payForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'personal_leave_with_pay.html', {"form": Personal_leave_with_payForm, "error": "Error creating task."+ new_task+"Hola"})

@login_required
def vacation_account_request(request):
    if request.method == "GET":
        return render(request, 'vacation_account_request.html', {"form": Vacation_account_requestForm})
    else:
        try:
            form = Vacation_account_requestForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'vacation_account_request.html', {"form": Vacation_account_requestForm, "error": "Error creating task."+ new_task+"Hola"})

def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('tasks')

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form, 'error': 'Error updating task.'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
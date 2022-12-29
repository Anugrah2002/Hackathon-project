import random
import string

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader

from .forms import BranchForm
from .models import *


def password_generator():
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))
    return res


def home_page(request):
    branches = Branch.objects.values_list("branch_name", flat=True).distinct()
    return render(request, 'home_page.html', {'branches': branches})


# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/administrator/')
        else:
            messages.error(request, "Wrong Username and Password ")
            return render(request, 'login_page.html')
    return render(request, 'login_page.html')


def administrator(request):
    return render(request, 'administrator.html')


def add_branch(request):
    form = BranchForm()
    if request.method == "POST":
        my_form = BranchForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            messages.success(request, "Branch Created successfully")
            return redirect(administrator)
        else:
            return render(request, 'add_branch.html', {'form': my_form})
    return render(request, 'add_branch.html', {'form': form})


def add_branch_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        emp_id = request.POST.get('emp_id')
        contact_number = request.POST.get('contact_no')
        branch_name = request.POST.get('branch')
        branch = Branch.objects.get(branch_name=branch_name)
        password = password_generator()
        request.session['new_password'] = password
        html_message = loader.render_to_string('emails/branch_created_email.html', {'password': password})
        mail = send_mail('Password', '', settings.EMAIL_HOST_USER, [email], html_message=html_message, fail_silently=False)
        if mail:
            my_user = User.objects.create(email=email, password=make_password(password), is_branch_user=True)
            Branch_user(user=my_user, branch_name=branch, name=name, emp_id=emp_id, contact_number=contact_number).save()
            messages.success(request, "Branch Created successfully")
            return redirect(administrator)
        else:
            messages.error(request, "Branch not created")
            return render(request, 'add_branch_user.html')
    branches = Branch.objects.values_list("branch_name", flat=True).distinct()
    return render(request, 'add_branch_user.html',{'branches': branches})

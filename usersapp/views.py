from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.decorators import login_required
import json
from  .forms import UserLoginForm, UserRegisterForm
# Create your views here.
# Create your views here.
def home_page(request):
    context = {}
    return render(request, 'guestapp/home-page.html', context)

def user_page(request):
    context = {}
    return render(request, 'usersapp/user-page.html', context)

def login_user(request):
    form= UserLoginForm()
    next = request.GET.get('next')
    if request.user.is_authenticated:
        return redirect('usersapp:user-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)
                messages.success(request, 'Welcome')
                return redirect('usersapp:home-page')
            else:
                messages.info(request, 'Username OR password is incorrect')
        

        context = {'form':form}
        return render(request, 'usersapp/login-user.html', context)


def register_user(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        messages.success(request, 'welcome')
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('usersapp:home-page')

    context = {
        'form': form,
    }
    return render(request, "usersapp/register-user.html", context)

def logout_user(request):
    logout(request)
    return redirect('guestapp:home-page')

def usernameValidation(request):
    username = request.GET.get('username', None)
    data ={
        'is_taken': UserRegisterForm.objects.filter(username=username).exist()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exist.'
    return JsonResponse(data)

def passwordValidation(request):
    return JsonResponse({ 'password_mismatch':'Password mismatch'})
def emailValidation(request):
    return JsonResponse({ 'email_exist':'email not available'})




from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout
from django.shortcuts import redirect

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            user = User.create_user(email=email, password=password, username=username, name=name, phone=phone)
            user.save()

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('main:index')
    else:
        form = ProfileForm()
    return render(request, 'accounts/authentication.html', {'form_register': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                return HttpResponse('Invalid login')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/authentication.html', {'form_login': form})

def user_logout(request):
    logout(request)
    return redirect('main:index')

        

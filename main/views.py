from django.shortcuts import render, redirect
from django.http import HttpResponse
from .  import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.

def homepage(request):
    return render(request = request,    
                  template_name = 'main/home.html',
                  context= {'articles' : models.Article.objects.all})


def signup(request):
    
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"New account made for {username}")
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            print(ValidationError)
            return render(request = request,
                            template_name = "main/register.html",
                            context={"form" : form})
    form = UserCreationForm

    return render(request=request,
                    template_name = 'main/register.html',
                    context={'form' : form})

def logout_req(request):
    logout(request)
    messages.info(request, 'logged out')
    return redirect('main:homepage')
def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate( username=username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Logged in as {username}')
                return redirect('main:homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}')

    form = AuthenticationForm
    return render(
        request,
        template_name = 'main/login.html',
        context= {'form': form}
    )

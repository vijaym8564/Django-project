from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, f'Hi {user.username} Account created successfully! You can now log in.')
        return redirect('login')

    return render(request, 'accounts/signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'accounts/login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# Simple Home Page
from django.shortcuts import render

def home_view(request):
    devops_tools = [
        "Git & GitHub",
        "Jenkins",
        "Maven",
        "SonarQube",
        "Nexus",
        "Docker",
        "Kubernetes",
        "Helm",
        "ArgoCD",
        "Terraform",
        "Ansible",
        "Prometheus",
        "Grafana",
        "Azure DevOps",
        "AWS",
        "Linux",
        "azure"
    ]
    return render(request, 'accounts/home.html', {'devops_tools': devops_tools})


# Create your views here.

from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'financeapp/main.html')


def home(request):
    return render(request, 'financeapp/home.html')


def dashboard(request):
    return render(request, 'financeapp/dashboard.html')


def register(request):
    return render(request, 'financeapp/register.html')


def login(request):
    return render(request, 'financeapp/login.html')

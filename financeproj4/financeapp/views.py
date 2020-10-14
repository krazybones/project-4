from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .forms import StockForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Stock
from .yfinanceEx import get_data

# Create your views here.


def main(request):
    return render(request, 'financeapp/main.html')


def home(request):
    return render(request, 'financeapp/home.html')


@login_required(login_url='login')
def dashboard(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']

        # pk_d2c4a815f6d34f34bffd2b1760bd99e5
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_d2c4a815f6d34f34bffd2b1760bd99e5")
        graphic = get_data(ticker)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'financeapp/dashboard.html', {'api': api, 'graphic': graphic})

    else:
        return render(request, 'financeapp/dashboard.html', {'ticker': "Enter a Ticker Symbol Above"})


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user)

                return redirect('login')
        context = {'form': form}
        return render(request, 'financeapp/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'financeapp/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect('add_stock')

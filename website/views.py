from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegistrationForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "There was an error logging in! Please try again.")
            return redirect('home')
    return render(request, 'home.html', {'records':records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    return redirect('home')

def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, "You have registered successfully!")
            return redirect('home')        
    return render(request, 'registration/register.html', {'form':form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else:
        messages.error(request, "You must be logged in to view a record!")
        return redirect('home')
    

def delete(request, pk):
    deleted_record = Record.objects.get(id=pk)
    deleted_record.delete()
    messages.success(request, "Record was deleted successfullt!")
    return redirect('home')
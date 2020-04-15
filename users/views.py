from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def register(request):

    if request.method == 'POST': # This is a POST Request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')  # Grab the username that is submitted for now
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:    # This is not a POST Request. We will just create a form

        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form':form})


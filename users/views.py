from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

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

    return render(request, 'users/register.html', {'form': form})



@login_required
def profile(request):
    if request.method == 'POST':   # This Will Be Run When I Submit My Form. And Possibly Pass New Data.
        u_form = UserUpdateForm(request.POST, instance=request.user)  # request.POST To Pass The POST Data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)  # File Data (images) Users Try To Upload.

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {   # To Pass This Into Template We Used context.
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
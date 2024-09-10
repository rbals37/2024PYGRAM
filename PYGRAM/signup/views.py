from django.shortcuts import render, redirect
from .forms import CustomSignupForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

# Create your views here.



def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('main')
        else:
            messages.error(request, error)
            
    else:
         form = CustomSignupForm()

    return render(request, 'signup.html', {'form': form})
         
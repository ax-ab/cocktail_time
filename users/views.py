from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from .decorators import student_required

def register(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save(commit=False)
            
            #new_user.is_student = True
            new_user.save()

            messages.success(request, 'User account created successfully')
            # new_user = authenticate(username=form.cleaned_data['email'],
            #                         password=form.cleaned_data['password'],
            #                         )
            login(request, new_user)
        
            return redirect('/profile')

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
#@student_required
def profile(request):
    return render(request, 'users/profile.html')
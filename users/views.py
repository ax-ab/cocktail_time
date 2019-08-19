from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from core.models import Cocktail

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            
            new_user.save()
            
            messages.success(request, 'Welcome! You are now logged in')                   )
            login(request, new_user)
        
            return redirect('/profile')

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    
    user = request.user
    fav_cocktails = Cocktail.objects.filter(customuser=user)
    
    context = {
        'number_of_cocktails':len(fav_cocktails)
    }
    
    return render(request, 'users/profile.html', context)
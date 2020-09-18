from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        creation_form = UserRegisterForm(request.POST)
        if creation_form.is_valid():
            creation_form.save()
            username = creation_form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login_user')
    else:
        creation_form = UserRegisterForm ()
    return render(request, 'users/register.html', {'form': creation_form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        creation_form = UserCreationForm(request.POST)
        if creation_form.is_valid():
            username = creation_form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('blog_home')
    else:
        creation_form = UserCreationForm()
    return render(request, 'users/register.html', {'form': creation_form})
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.core.paginator import Paginator


def edit_profile(request):
    return render(request, 'users/edit_profile.html')


def register(request):
    if request.method == 'POST':
        creation_form = UserRegisterForm(request.POST)
        if creation_form.is_valid():
            creation_form.save()
            username = creation_form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login_user')
    else:
        creation_form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': creation_form})


@login_required
def profile(request):
    # Profile create post view
    context = {
        'posts': Post.objects.filter(author=request.user)
    }

    return render(request, 'users/profile.html', context)


@login_required
def ext_profile(request, username):
    post_author = User.objects.get(username=username)
    users_posts = Post.objects.filter(author=post_author).order_by('-date_posted')
    paginator = Paginator(users_posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': users_posts,
        'user': post_author,
        'page_obj': page_obj
    }
    return render(request, 'users/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_edit_form = UserEditForm(request.POST, instance=request.user)
        profile_edit_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            profile_edit_form.save()
            user_edit_form.save()
            messages.success(request, "User's data successfully updated")
            return redirect('user_profile')
    else:
        user_edit_form = UserEditForm(instance=request.user)
        profile_edit_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_edit_form': user_edit_form,
        'profile_edit_form': profile_edit_form
    }
    return render(request, 'users/edit_profile.html', context)
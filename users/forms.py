from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from blog.models import Post


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio_desc']


class UserCreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
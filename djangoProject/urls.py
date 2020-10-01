"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_login'),
    path('', include('blog.urls')),
    path('register/', user_views.register, name='register_user'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login_user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_user'),
    path('profile/', user_views.profile, name='user_profile'),
    path('edit-profile/', user_views.edit_profile, name='user_edit_profile'),
    path('user/<username>', user_views.ext_profile, name='user_view_ext_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

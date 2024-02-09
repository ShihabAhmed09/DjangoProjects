"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

admin.site.site_header = "Log in to Shihab's Portfolio"
admin.site.site_title = "Shihab's Portfolio Admin Panel"
admin.site.index_title = "Welcome to Shihab's Portfolio Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('projects/', include('projects.urls')),
    path('blog/', include('blog.urls')),

    path('profile/', user_views.profile, name='profile'),

    path('signup/', user_views.registration, name='registration'),
    path('login/', user_views.login_user, name='login'),
    path('logout/', user_views.logout_user, name='logout'),

    path('password-change/', user_views.password_change, name='password_change'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
    #      name='change_password'),
    # path('password-change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
    #      name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""she_codes_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from . import settings


urlpatterns = [
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    #path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),  
]


if settings.DEBUG:
    # enable local preview of error pages if in Debug mode
    urlpatterns.append(path('403', TemplateView.as_view(template_name="403.html"),name='403'))
    urlpatterns.append(path('404', TemplateView.as_view(template_name="404.html")))
    urlpatterns.append(path('500', TemplateView.as_view(template_name="500.html")))

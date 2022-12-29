"""help_desk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from . import views, ajax

urlpatterns = [
    path("", views.home_page),
    path("login_page/", views.login_page),
    path("administrator/", views.administrator),
    path("administrator/add_branch_user/", views.add_branch_user),
    path("administrator/add_branch/", views.add_branch),

    # Ajax
    path('send_OTP/', ajax.send_OTP),
    path('verify_OTP/', ajax.verify_OTP),
]

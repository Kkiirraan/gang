"""
URL configuration for GWE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('studentreg',views.studentreg),
    path('student/',views.login),
    path('about/',views.about),
    path('login/',views.loginmain),
    path('register/',views.register),
    path('studentprof/',views.studentprof),
    path('studentnewtt/',views.studentnewtt),
    path('studenttopic/',views.studenttopic),
    path('studentassign/',views.studentassign),
    path('studentabs/',views.studentabs),
    path('admin1/',views.adminlogin),
    path('staff/',views.stafflogin),
    path('staffreg/',views.staffreg),
    path('staffprof/',views.staffprof),
    path('staffnewtt/',views.staffnewtt),
    path('stafftopic/',views.stafftopic),
    path('staffassign/',views.staffassign),
    path('sample/',views.sample),
    path('staffavail/',views.staffavail),
    

]

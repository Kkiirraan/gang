from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginmain, name="loginmain"),
    path('studentassign/', views.studentassign, name="studentassign"),
    path('logout/', views.logout, name="logout"),
    path('studentnewtt/', views.studentnewtt, name="studentnewtt"),
    path('staffnewtt/', views.staffnewtt, name="staffnewtt"),
    path('studentreg/', views.studentreg, name="studentreg"),
    path('student/', views.login, name="studentlogin"),
    path('about/', views.about, name="about"),
    path('register/', views.register, name="register"),
    path('studentprof/', views.studentprof, name="studentprof"),
    path('studenttopic/', views.studenttopic, name="studenttopic"),
    path('studentabs/', views.studentabs, name="studentabs"),
    path('admin1/', views.adminlogin, name="admin1"),
    path('staff/', views.stafflogin, name="staff"),
    path('staffreg/', views.staffreg, name="staffreg"),
    path('staffprof/', views.staffprof, name="staffprof"),
    path('stafftopic/', views.stafftopic, name="stafftopic"),
    path('staffassign/', views.staffassign, name="staffassign"),
    path('sample/', views.sample, name="sample"),
    path('staffavail/', views.staffavail, name='staffavail'),
    path('staffavailin', views.staffavailin, name='staffavailin'),
    
]

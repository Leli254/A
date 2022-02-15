from django.urls import path,reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views 

app_name= 'accounts'

urlpatterns = [
    #user accounts paths
    
    path('signup',TemplateView.as_view(template_name='accounts/signup.html'),name='signup'),
    path('student-signup/',views.StudentSignUp.as_view(), name='StudentSignUp'),
    path('teacher-signup/',views.TeacherSignUp.as_view(), name='TeacherSignUp'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='accounts/password_reset.html',
             subject_template_name='accounts/password_reset_subject.txt',
             email_template_name='accounts/password_reset_email.html',
             success_url = reverse_lazy('accounts:password_reset_done'),
         ),name='password_reset'),    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_confirm.html",
             success_url = reverse_lazy('accounts:password_reset_complete'),
         ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_completed.html'), name='password_reset_complete'),      
    path('change-password/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/change_password.html',
             success_url = '/'
         ),name='change_password'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
]    
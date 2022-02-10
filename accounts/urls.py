from django.urls import path 
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .import views 

app_name= 'accounts'

urlpatterns = [
    #user accounts paths
    path('signup',TemplateView.as_view(template_name='accounts/signup.html'),name='signup'),
    path('student-signup/',views.StudentSignUp.as_view(), name='StudentSignUp'),
    path('teacher-signup/',views.TeacherSignUp.as_view(), name='TeacherSignUp'),
    path('login/',views.LoginView.as_view(), name='login'),
    path('password_reset/',views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),      
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html',success_url = '/'),name='change_password'),
]    
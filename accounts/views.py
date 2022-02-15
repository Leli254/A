from django.contrib.auth import login
from django.shortcuts import redirect
#from django.core.mail import send_mail, BadHeaderError
#from django.contrib.auth.forms import  AuthenticationForm 
from django.views.generic import CreateView,FormView

from .forms import StudentSignUpForm,TeacherSignUpForm,ContactForm
from .models import Student,Teacher


class StudentSignUp(CreateView):
    model = Student
    form_class = StudentSignUpForm
    template_name = 'accounts/student_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
class TeacherSignUp(CreateView):
    model = Teacher
    form_class = TeacherSignUpForm
    template_name = 'accounts/teacher_signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



      
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = "/"
    
    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(ContactView, self).form_valid(form)
    
    def send_mail(self, valid_data):
        # Send mail logic
        print(valid_data)
        pass
    
    
    
    
    

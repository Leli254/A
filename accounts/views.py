from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect,render
#from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import  AuthenticationForm 
from django.views.generic import View
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


class LoginView(View):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})


      
class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    success_url = "/"

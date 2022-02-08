from django import forms
from .models import Student,Teacher
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction



        
class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Student
        fields = ('first_name','last_name','gender' ,'phone_number', 'email', 'password1' ,'password2' )
        
    
    

class TeacherSignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = Teacher
        fields = ('first_name','last_name','gender','tech_stack' ,'phone_number', 'email', 'password1' ,'password2')
        
        
        
        
        
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label="Email")
    subject =forms.CharField(required=False)
    category = forms.ChoiceField(choices=[('Courses', 'Courses'), ('Other', 'Other'),
                                          ])
    message = forms.CharField(widget=forms.Textarea)
        
        

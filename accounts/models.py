from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


from .managers import UserManager


GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    """custom User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_number=models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='Male')
    
    def __str__(self):
        return self.email 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
    
  
  
class Student(User):
    joindate=models.DateField(auto_now_add=True)
    is_student = models.BooleanField('student status',default=True)
   
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'


class Teacher(User):
    APPROVAL_CHOICES = (
        ('n', 'Not Requested For Approval'),
        ('p', 'Approval Application on Pending'),
        ('d', 'Approval Request Declined'),
        ('a', 'Approved')
    )
    
    
    joindate=models.DateField(auto_now_add=True)
    tech_stack = models.TextField(_('programming languanges you are good at'))
    approval_status = models.CharField(
        max_length=2,
        choices=APPROVAL_CHOICES,
        default='n',
    )
    is_teacher = models.BooleanField('teacher status', default=True)
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


"""
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    bio = models.TextField()
    profile_pic= models.ImageField(default='default.jpg', upload_to='profile_pics')
    verified= models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.email} Profile' #show how we want it to be displayed in admin section
"""
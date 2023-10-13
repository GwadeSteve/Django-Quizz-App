from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    LEVELS = [
        ('1', 'Level 1'),
        ('2', 'Level 2'),
        ('3', 'Level 3'), 
        ('4', 'Level 4'), 
        ('5', 'Level 5')
    ]
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    COURSES = [
        ('Ing', 'Engineering'),
        ('Sng', 'Engineering Sciences'),
    ]
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, choices=GENDER, default=None)
    level = models.CharField(max_length=1, choices=LEVELS, default=None)
    course_program = models.CharField(max_length=3, choices=COURSES, default=None)
    major = models.CharField(max_length=100, default=None)
    points = models.PositiveIntegerField(default=0)
    time_taken = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # Define the field to use for authentication
    USERNAME_FIELD = 'username'

    #R equired fields
    REQUIRED_FIELDS = ['email', 'sex', 'level', 'course_program', 'major']

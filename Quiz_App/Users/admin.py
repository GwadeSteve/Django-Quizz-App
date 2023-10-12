from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('name', 'email', 'sex', 'level', 'course_program', 'major', 'points', 'time_taken')
    list_filter = ('sex', 'level', 'course_program')
    search_fields = ('name', 'email', 'major')
    ordering = ('name',)

    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Personal Info', {'fields': ('sex', 'level', 'course_program', 'major')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
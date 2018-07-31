from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User, CustomUser
from .forms import CustomUserCreationForm,CustomChangeForm

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'profession', 'institution', 'email' ,'purpose']

admin.site.register(CustomUser,CustomUserAdmin)

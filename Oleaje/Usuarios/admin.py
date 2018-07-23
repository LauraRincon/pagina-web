from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import User, CustomUser
from .forms import CustomUserCreationForm,CustomChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomChangeForm
    model = CustomUser
    list_display = ['username', 'institution', 'email']

admin.site.register(CustomUser,CustomUserAdmin)

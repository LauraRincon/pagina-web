from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import User

def home(request):
 if request.method == "POST":
     form = CustomUserCreationForm(request.POST)
     print(form)
     if form.is_valid:
         form.save()
         return redirect('Usuarios_login')
 else:
     form = CustomUserCreationForm()
 return render(request, "Usuarios/signup.html", {'form': form})

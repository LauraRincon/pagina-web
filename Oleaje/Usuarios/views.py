from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import User



from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('Usuarios_login')
    template_name = 'Usuarios/home.html'
# Create your views here.

def home(request):
 if request.method == "POST":
     form = CustomUserCreationForm(request.POST)
     if form.is_valid:
         form.save()
         return redirect('Usuarios_login')
 else:
     form = CustomUserCreationForm()
 return render(request, "Usuarios/home.html", {'form': form})

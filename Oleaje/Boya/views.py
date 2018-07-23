from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def register(request):
    return render(request, "Boya/register.html")

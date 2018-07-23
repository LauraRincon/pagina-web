from django.http import HttpResponse
from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('Boya_register')
    else:
        return  render(request, 'Oleaje/welcome.html')

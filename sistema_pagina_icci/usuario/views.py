
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

# Create your views here.

class register_usuario(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registrar.html", {"form":form})

    def post(self, request):
        pass    

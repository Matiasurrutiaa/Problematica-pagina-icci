
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm




# Create your views here.

class register_usuario(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registrar.html", {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario=form.save()

            login(request, usuario)

            return redirect("aplication:subir_archivos")

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])    

            return render(request, "registro/registrar.html", {"form":form})

def log_out(request):
    logout(request)

    return redirect("login")


def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user__name=form.cleaned_data.get("username")
            password_=form.cleaned_data.get("password")
            user=authenticate(username=user__name, password=password_)
            if user is not None:
                login(request, user)
                return redirect("aplication:subir_archivos")
            else:
                messages.error(request, "usuario no valido")    
        else:
            messages.error(request, "información incorrecta")



    form=AuthenticationForm()
    return render(request, "login/login.html", {"form":form})   


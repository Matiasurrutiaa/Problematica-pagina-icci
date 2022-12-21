from django.urls import path
from .views import register_usuario

#app_name="aplication"

urlpatterns = [
   path("", register_usuario.as_view(), name= "usuario"),
   
]
from django.urls import path
from .views import register_usuario, log_out, logear

#app_name="aplication"

urlpatterns = [
   path("", register_usuario.as_view(), name= "usuario"),
   path("cerrar_sesion", log_out, name= "cerrar_sesion"),
   
   

   
]
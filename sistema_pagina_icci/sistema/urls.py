
from django.urls import path
from sistema import views

app_name="aplication"

urlpatterns = [
   path("", views.subir_archivos, name= "subir archivos"),
   path("detail_<int:id>/", views.detail, name= "detail"),
   path("create/", views.create_documents, name="create"),
   
]
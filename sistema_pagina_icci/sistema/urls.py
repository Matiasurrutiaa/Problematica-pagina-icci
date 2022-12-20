
from django.urls import path
from sistema import views

app_name="aplication"

urlpatterns = [
   path("", views.subir_archivos, name= "subir_archivos"),
   path("detail_<int:id>/", views.detail, name= "detail"),
   path("create/", views.create_documents, name="create"),
   path("update_<int:id>/", views.update_documents, name="update"),
   path("delete_<int:id>/", views.delete_documents, name="delete"),
   
]
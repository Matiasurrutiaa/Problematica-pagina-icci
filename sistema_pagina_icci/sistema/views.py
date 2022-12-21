from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import  Documents
from .forms import DocumentForm
from django.db.models import Q 

# Create your views here.

def subir_archivos(request):
    queryset= request.GET.get("buscar")
    documentos = Documents.objects.all()
    context= {
        'documentos' : documentos
    }
    if queryset:
        documentos=Documents.objects.filter(
            Q(title__icontains = queryset) |
            Q(author__icontains = queryset)    
        ).distinct()

    
   
    return render(request, 'sistema/subir_archivos.html', context)

def detail(request, id):
    detail_documents= get_object_or_404(Documents, pk = id)
    context={
        "detail_documents" : detail_documents
    }
    return render(request, 'sistema/detail.html', context)

def create_documents(request):
    if request.method == "POST":
        document_form = DocumentForm(request.POST)
        if document_form.is_valid():
            document_form.save()
            return redirect("aplication:subir_archivos")
    else:
        document_form=DocumentForm()
    return render(request, "sistema/create.html", {'document_form':document_form})


def update_documents(request, id):
    document = get_object_or_404(Documents, id = id)
    if request.method == "POST":
       document_form=document_form(request.POST, instance= document)
       if document_form.is_valid():
            document_form.save() 
            return redirect("aplication:subir_archivos")
    else:
        document_form=DocumentForm()
        return render(request, "sistema/editar.html", {'document_form':document_form})

def delete_documents(request, id):
    document = get_object_or_404(Documents, id = id)

    if document:
        document.delete()
        return redirect("aplication:subir_archivos")

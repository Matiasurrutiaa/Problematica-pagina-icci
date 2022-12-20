from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Users, Documents
from .forms import DocumentForm 

# Create your views here.

def subir_archivos(request):
    documentos = Documents.objects.all()
    context= {
        'documentos' : documentos
    }
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
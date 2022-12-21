from django.forms import ModelForm
from .models import Documents

class DocumentForm(ModelForm):
    class Meta:
        model=Documents
        fields= "__all__"



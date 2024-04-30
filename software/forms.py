from django import forms
from .models import Software


class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['name', 'version', 'license']


"""class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_name', 'file']
"""
from django import forms

from project.upload.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name','description', 'document',)

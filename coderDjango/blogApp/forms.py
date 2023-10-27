from django import forms

from blogApp.models import Articulo
from ckeditor.widgets import CKEditorWidget


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['title', 'subtitle', 'text', 'image']  # Include 'image' field
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'text': 'Write your thoughts here:',
            'image': 'Upload an image',
        }

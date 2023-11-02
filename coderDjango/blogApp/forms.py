from django import forms

from blogApp.models import Articulo
from ckeditor.widgets import CKEditorWidget


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['title', 'subtitle', 'text', 'image']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
        }


class CardSearchForm(forms.Form):
    search_text = forms.CharField(
        label='Search Text',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter search text'}),  
    )

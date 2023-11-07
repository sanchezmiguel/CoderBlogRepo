from ckeditor.widgets import CKEditorWidget
from django import forms

from blogApp.models import Articulo
from .models import Resena, Guia, Noticia, Entrevista, Tutorial


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


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['title', 'subtitle', 'text', 'image', 'score', 'review_date']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'step': '0.01'}),
            'review_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
            'score': 'Puntuación de la reseña',
            'review_date': 'Fecha de la reseña',
        }


class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['title', 'subtitle', 'text', 'image', 'topic', 'duration']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(),
            'duration': forms.NumberInput(attrs={'step': '1'}),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
            'topic': 'Tema de la guía',
            'duration': 'Duración estimada (minutos)',
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['title', 'subtitle', 'text', 'image', 'source', 'publication_date']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'source': forms.TextInput(),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
            'source': 'Fuente de la noticia',
            'publication_date': 'Fecha de publicación',
        }


class EntrevistaForm(forms.ModelForm):
    class Meta:
        model = Entrevista
        fields = ['title', 'subtitle', 'text', 'image', 'interviewed_person', 'interviewed_person_position',
                  'interview_date', 'interviewer']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'interviewed_person': forms.TextInput(),
            'interviewed_person_position': forms.TextInput(),
            'interview_date': forms.DateInput(attrs={'type': 'date'}),
            'interviewer': forms.TextInput(),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
            'interviewed_person': 'Nombre del entrevistado',
            'interviewed_person_position': 'Cargo del entrevistado',
            'interview_date': 'Fecha de la entrevista',
            'interviewer': 'Nombre del entrevistador',
        }


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'subtitle', 'text', 'image', 'category', 'level']
        widgets = {
            'title': forms.TextInput(),
            'subtitle': forms.TextInput(),
            'text': CKEditorWidget(config_name='default'),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(),
            'level': forms.TextInput(),
        }
        labels = {
            'title': 'Título',
            'subtitle': 'Subtítulo',
            'text': 'Texto del artículo',
            'image': 'Imagen',
            'category': 'Categoría del tutorial',
            'level': 'Nivel del tutorial',
        }

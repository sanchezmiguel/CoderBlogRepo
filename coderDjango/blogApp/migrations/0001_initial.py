# Generated by Django 4.2.6 on 2023-11-02 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Título del artículo.', max_length=200)),
                ('subtitle', models.CharField(help_text='Subtítulo del artículo.', max_length=200)),
                ('text', models.TextField(blank=True, help_text='Texto del artículo. Puede estar en blanco si es necesario.')),
                ('image', models.ImageField(blank=True, help_text='Imagen asociada al artículo.', null=True, upload_to='articulo_images/')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de creación del artículo.')),
                ('author', models.ForeignKey(help_text='Autor del artículo. Enlazado a un usuario.', on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-02 11:34

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
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats1', to=settings.AUTH_USER_MODEL)),
                ('usuario_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chats2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mensajeriaApp.chat')),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfilesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creatorprofile',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='creatorprofile',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
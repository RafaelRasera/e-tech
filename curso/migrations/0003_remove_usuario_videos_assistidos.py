# Generated by Django 5.0.4 on 2024-05-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_usuario_playlists_acessadas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='videos_assistidos',
        ),
    ]

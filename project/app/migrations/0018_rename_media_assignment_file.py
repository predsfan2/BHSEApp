# Generated by Django 3.2.19 on 2023-06-22 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_assignment_media'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='media',
            new_name='file',
        ),
    ]

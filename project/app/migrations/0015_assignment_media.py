# Generated by Django 3.2.19 on 2023-06-22 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_message_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='media',
            field=models.FileField(null=True, upload_to='assignments/media'),
        ),
    ]

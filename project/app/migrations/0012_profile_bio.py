# Generated by Django 3.2.19 on 2023-06-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]

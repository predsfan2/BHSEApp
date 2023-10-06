# Generated by Django 3.2.19 on 2023-06-22 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='classAssignedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.classsites'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='received_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2021-09-09 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('floppas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='active_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
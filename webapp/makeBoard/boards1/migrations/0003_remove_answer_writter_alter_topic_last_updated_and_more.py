# Generated by Django 5.0.1 on 2024-01-23 08:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards1', '0002_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='writter',
        ),
        migrations.AlterField(
            model_name='topic',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='message',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='topic',
            name='writter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-01 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='TodoApp.user'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-18 00:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0003_tasklist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
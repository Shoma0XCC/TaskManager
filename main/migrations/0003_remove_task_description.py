# Generated by Django 5.1.4 on 2025-01-01 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_options_remove_task_name_task_task_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-19 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_task_start_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-start_time']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='end_time',
        ),
    ]

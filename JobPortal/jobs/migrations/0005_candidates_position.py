# Generated by Django 3.2.5 on 2021-08-31 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_rename_location_jobpost_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='position',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

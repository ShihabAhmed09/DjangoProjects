# Generated by Django 3.2.5 on 2021-08-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20210805_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, default='projects/thumbnails/thumbnail.png', null=True, upload_to='projects/thumbnails'),
        ),
    ]
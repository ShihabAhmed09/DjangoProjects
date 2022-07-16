# Generated by Django 3.2.4 on 2021-06-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('title_desc', models.CharField(max_length=5000)),
                ('heading', models.CharField(default='', max_length=200)),
                ('heading_desc', models.CharField(default='', max_length=5000)),
                ('sub_heading', models.CharField(default='', max_length=200)),
                ('sub_heading_desc', models.CharField(default='', max_length=5000)),
                ('publish_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='blog/thumbnails')),
            ],
        ),
    ]
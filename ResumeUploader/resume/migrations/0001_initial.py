# Generated by Django 3.2.5 on 2021-07-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('division', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Sylhet', 'Sylhet'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur'), ('Mymenshing', 'Mymenshing')], max_length=100)),
                ('zip_code', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('preferred_job_location', models.CharField(max_length=100)),
                ('profile_pic', models.ImageField(upload_to='resume/profile_pics')),
                ('resume_file', models.FileField(upload_to='resume/profile_pics')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

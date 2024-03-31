# Generated by Django 5.0.3 on 2024-03-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('federation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athletes', models.TextField()),
                ('trainer', models.TextField()),
                ('doctors', models.TextField()),
            ],
        ),
    ]
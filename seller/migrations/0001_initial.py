# Generated by Django 5.0.1 on 2024-01-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=20)),
                ('Addresss', models.CharField(max_length=20)),
                ('Place', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
    ]

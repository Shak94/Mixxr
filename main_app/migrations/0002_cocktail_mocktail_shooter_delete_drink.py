# Generated by Django 4.2.3 on 2023-07-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=600)),
                ('recipe', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MockTail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=600)),
                ('recipe', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=600)),
                ('recipe', models.TextField(max_length=700)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
           
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
    ]

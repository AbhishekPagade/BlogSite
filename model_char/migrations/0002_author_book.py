# Generated by Django 4.2.2 on 2023-07-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_char', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('authors', models.ManyToManyField(to='model_char.author')),
            ],
        ),
    ]

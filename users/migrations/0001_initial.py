# Generated by Django 4.2 on 2023-04-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]

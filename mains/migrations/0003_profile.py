# Generated by Django 3.2.7 on 2021-10-10 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0002_auto_20211008_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(null=True, upload_to='photos')),
                ('bio', models.TextField()),
            ],
        ),
    ]

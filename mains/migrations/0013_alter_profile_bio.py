# Generated by Django 3.2.7 on 2021-10-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0012_auto_20211010_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hi'),
        ),
    ]
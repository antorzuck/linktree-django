# Generated by Django 3.2.7 on 2021-10-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0013_alter_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default=''),
        ),
    ]

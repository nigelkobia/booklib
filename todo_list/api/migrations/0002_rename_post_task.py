# Generated by Django 5.1.7 on 2025-03-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Task',
        ),
    ]

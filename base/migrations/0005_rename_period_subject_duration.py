# Generated by Django 3.2.9 on 2021-12-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20211207_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='period',
            new_name='duration',
        ),
    ]
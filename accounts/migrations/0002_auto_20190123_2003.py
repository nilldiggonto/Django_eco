# Generated by Django 2.1.4 on 2019-01-23 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GuestEmain',
            new_name='GuestEmail',
        ),
    ]

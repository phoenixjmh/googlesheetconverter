# Generated by Django 2.0.4 on 2018-04-23 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SheetApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyers',
            old_name='Address',
            new_name='address',
        ),
    ]

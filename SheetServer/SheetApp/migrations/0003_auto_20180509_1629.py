# Generated by Django 2.0.4 on 2018-05-09 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SheetApp', '0002_auto_20180423_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyers',
            name='address',
        ),
        migrations.RemoveField(
            model_name='buyers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='buyers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='buyers',
            name='phone',
        ),
    ]

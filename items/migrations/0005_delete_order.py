# Generated by Django 4.0.6 on 2022-08-06 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]

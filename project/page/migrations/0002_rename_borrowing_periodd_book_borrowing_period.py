# Generated by Django 3.2.4 on 2021-07-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='borrowing_periodd',
            new_name='borrowing_period',
        ),
    ]

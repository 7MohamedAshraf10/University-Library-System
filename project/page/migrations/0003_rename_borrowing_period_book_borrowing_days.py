# Generated by Django 3.2.4 on 2021-07-15 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_rename_borrowing_periodd_book_borrowing_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='borrowing_period',
            new_name='borrowing_days',
        ),
    ]

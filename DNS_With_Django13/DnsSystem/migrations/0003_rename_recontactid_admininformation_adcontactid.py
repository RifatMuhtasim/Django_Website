# Generated by Django 3.2.8 on 2021-10-23 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DnsSystem', '0002_auto_20211023_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admininformation',
            old_name='ReContactId',
            new_name='AdContactId',
        ),
    ]

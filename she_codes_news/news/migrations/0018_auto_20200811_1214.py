# Generated by Django 3.0.8 on 2020-08-11 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_auto_20200811_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsstory',
            old_name='edited',
            new_name='edit_date',
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-03 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200803_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, default='https://i.imgur.com/odto5AG.jpg'),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-09 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_auto_20200809_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='category',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='cat_stories', to='news.Category'),
        ),
    ]

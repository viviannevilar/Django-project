# Generated by Django 3.0.8 on 2020-08-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20200808_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.Category'),
        ),
    ]

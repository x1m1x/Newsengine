# Generated by Django 3.0.5 on 2020-05-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20200525_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

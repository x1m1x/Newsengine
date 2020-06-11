# Generated by Django 3.0.5 on 2020-05-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200524_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

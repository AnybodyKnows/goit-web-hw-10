# Generated by Django 5.0.6 on 2024-06-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

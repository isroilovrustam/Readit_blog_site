# Generated by Django 4.1.4 on 2022-12-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
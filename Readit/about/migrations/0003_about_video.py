# Generated by Django 4.1.4 on 2022-12-22 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

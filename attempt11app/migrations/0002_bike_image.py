# Generated by Django 5.1.2 on 2024-11-20 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attempt11app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.ImageField(default=3, upload_to='images/'),
            preserve_default=False,
        ),
    ]

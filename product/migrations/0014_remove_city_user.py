# Generated by Django 5.0.1 on 2024-01-24 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
    ]

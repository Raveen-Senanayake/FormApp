# Generated by Django 3.0.5 on 2021-05-31 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_formentry_is_deployed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formentry',
            name='is_deployed',
        ),
    ]

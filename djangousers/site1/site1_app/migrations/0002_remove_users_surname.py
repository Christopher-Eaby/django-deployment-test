# Generated by Django 3.1.5 on 2021-03-24 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site1_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='surname',
        ),
    ]

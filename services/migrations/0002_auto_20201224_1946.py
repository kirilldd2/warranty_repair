# Generated by Django 3.1.4 on 2020-12-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consultant',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='expert',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'managed': True},
        ),
    ]
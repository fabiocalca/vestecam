# Generated by Django 3.2.16 on 2022-11-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

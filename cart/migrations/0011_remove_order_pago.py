# Generated by Django 3.2.16 on 2022-12-04 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_order_payment_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pago',
        ),
    ]

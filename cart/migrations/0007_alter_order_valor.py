# Generated by Django 3.2.16 on 2022-12-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_order_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
